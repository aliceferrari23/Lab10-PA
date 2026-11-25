from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutte le Filiali (i nodi) presenti e filtrando i Collegamenti con
        importo medio per bonifico >= threshold (euro)
        """
        self.G.clear()
        self._nodes = DAO.get_filiali()
        self._edges = DAO.get_collegamenti()

        id_map = {f.id: f for f in self._nodes}
        self.G.add_nodes_from(self._nodes)

        for c in self._edges:
            if c.valore >= threshold and c.id_filiale_1 in id_map and c.id_filiale_2 in id_map:
                self.G.add_edge(id_map[c.id_filiale_1], id_map[c.id_filiale_2], weight=c.valore)

    def get_num_edges(self):
        """
        Restituisce il numero di Collegamenti (edges) del grafo
        :return: numero di edges del grafo
        """
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Filiali (nodi) del grafo
        :return: numero di nodi del grafo
        """
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutti i Collegamenti (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        return self.G.edges(data=True)
