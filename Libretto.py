from voto import Voto
class Libretto:
    def __init__(self):
        self._voti = []
        self._lode = []

    def addvoto(self,voto):
        self._voti.append(voto)

    def __str__(self):
        return f"Hai superato questi esami {self._voti}"

    def mean(self):
        if len(self._voti) == 0:
            raise ValueError("Elenco voti vuoto")
        punteggi = [v.punteggio for v in self._voti]
        return sum(punteggi) / len(self._voti)

voto_1 = Voto("Analisi Matematica 1", 10, 28,False ,"2022-02-10")
voto_2 = Voto("Basi di dati",8,30,True,"2023-06-15")

mio_libretto = Libretto()
mio_libretto.addvoto(voto_1)
mio_libretto.addvoto(voto_2)
print(mio_libretto.mean())