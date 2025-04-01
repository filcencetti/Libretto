from DAO.dbConnect import DBConnect
from voto import Voto

class LibrettoDAO:
    #def __init__(self):
    #    self.dbConnect = DBConnect()

    @staticmethod #questo metodo non vede i parametri dell'istanza
    def getAllVoti(): #tolgo self perché appunto non si riferiscono alle istanze delle classe
        cnx = DBConnect.getConnection()
        cursor = cnx.cursor(dictionary=True)

        query = ("select * from voti ")
        cursor.execute(query)
        res = []
        for row in cursor:
            #materia = row["materia"]
            #punteggio = row["punteggio"]
            #lode = row["lode"]
            #data = row["data"]
            #v = Voto(materia, punteggio, data,lode)
            #res.append(v)
            if row["lode"] == False:
                res.append(Voto(row["materia"],row["punteggio"],row["data"].date(),False))
            else:
                res.append(Voto(row["materia"], row["punteggio"], row["data"].date(), True))
        cnx.close()
        return res

    @staticmethod
    def addVoto(voto: Voto):
        cnx = DBConnect.getConnection()
        cursor = cnx.cursor(dictionary=True)

        query = ("insert into "
        "voti (materia,punteggio,data,lode)"
        "values (%s,%s,%s,%s)")

        cursor.execute(query,
                       (voto.materia,voto.punteggio,voto.data,str(voto.lode)))
        cnx.commit()
        cnx.close()
        return

    @staticmethod
    def hasVoto(voto: Voto):
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor()
        query = ("""select * 
                 from voti v
                 where v.materia = %s""")
        cursor.execute(query,(voto.materia,))
        res = cursor.fetchall()
        cnx.close()
        return len(res) > 0


if __name__ == "__main__":
    mydao = LibrettoDAO()
    mydao.getAllVoti()