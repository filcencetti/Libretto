import pathlib

import mysql.connector

class DBConnect:


    # @classmethod
    # def getConnection(cls):
    #     try:
    #         cnx = mysql.connector.connect(
    #             user="root",
    #             password="root",
    #             host="127.0.0.1",
    #             database="Libretto")
    #         return cnx
    #     except mysql.connector.Error as err:
    #         print("Non riesco a collegarmi al database")
    #         print(err)
    #         return None

    def __init__(self):
        RuntimeError("Non crea un'istanza di questa classe per favore!")
    _myPool = None
    @classmethod
    def getConnection(cls):

        if cls._myPool is None:
            try:
            # creao una connessione e restituisco il metodo get_collection
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool(
                    pool_size=3,
                    pool_name="myPool",
                    option_files = "D:/Windows Folders/Documenti/PycharmProjects/Libretto/DAO/connecting.cfg"
                    #option_files=f"{pathlib.Path(__file__).resolve().parent}/connection.cfg"
                )
            except mysql.connector.Error as err:
                    print("Something is wrong in dbconnect")
                    print(err)
            return cls._myPool.get_connection()
        else:
            # se il pool già esiste, restituisco direttamente la connessione
            return cls._myPool.get_connection()

