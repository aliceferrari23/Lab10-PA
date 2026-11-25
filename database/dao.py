from database.DB_connect import DBConnect
from model.filiale import Filiale
from model.collegamento import Collegamento

class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """

    @staticmethod
    def get_filiali():
        cnx = DBConnect.get_connection()
        if cnx is None:
            return []
        result = []
        cursor = cnx.cursor(dictionary=True)
        try:
            cursor.execute("""SELECT id, codice, nome, citta, provincia, latitudine, longitudine
                              FROM filiale""")
            result = [
                Filiale(
                    id=row["id"],
                    codice=row["codice"],
                    nome=row["nome"],
                    citta=row["citta"],
                    provincia=row["provincia"],
                    latitudine=row["latitudine"],
                    longitudine=row["longitudine"],
                )
                for row in cursor
            ]
        finally:
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_collegamenti():
        cnx = DBConnect.get_connection()
        if cnx is None:
            return []
        result = []
        cursor = cnx.cursor(dictionary=True)
        try:
            cursor.execute("""SELECT LEAST(id_filiale_origine, id_filiale_destinazione)    AS f1,
                                     GREATEST(id_filiale_origine, id_filiale_destinazione) AS f2,
                                     SUM(importo)                                          AS somma,
                                     COUNT(*)                                              AS n
                              FROM bonifico
                              WHERE id_filiale_origine <> id_filiale_destinazione
                              GROUP BY f1, f2""")
            for row in cursor:
                result.append(Collegamento(row["f1"], row["f2"], float(row["somma"]), row["n"]))
        finally:
            cursor.close()
            cnx.close()
        return result