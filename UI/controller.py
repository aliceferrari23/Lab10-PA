import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_collegamenti(self, e):
        """
        Funzione che controlla prima se il valore dell'importo inserito sia valido (es. non deve essere una stringa) e
        poi popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Filiali presenti
        * Numero di Collegamenti
        * Lista di Collegamenti che superano l'importo indicato come soglia
        """
        testo = self._view.importo_medio_minimo.value
        self._view.lista_visualizzazione.controls.clear()

        if testo is None or testo.strip() == "":
            self._view.show_alert("Inserire un importo medio minimo.")
            return
        try:
            soglia = float(testo.strip())
        except ValueError:
            self._view.show_alert("Inserire un valore numerico valido.")
            return

        self._model.costruisci_grafo(soglia)

        lv = self._view.lista_visualizzazione
        lv.controls.append(ft.Text(f"Numero di Filiali: {self._model.get_num_nodes()}"))
        lv.controls.append(ft.Text(f"Numero di Collegamenti: {self._model.get_num_edges()}"))
        for u, v, data in self._model.get_all_edges():
            lv.controls.append(ft.Text(f"[{u}] - [{v}] - importo medio: {data['weight']:.2f} €"))
        self._view.update()
