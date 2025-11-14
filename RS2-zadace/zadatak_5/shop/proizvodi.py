class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print(f"{self.naziv} - Cijena: {self.cijena} eur, Dostupno: {self.dostupna_kolicina}")


# Početno skladište sa 2 proizvoda
skladiste = [
    Proizvod("Laptop", 1200, 5),
    Proizvod("Monitor", 300, 10)
]


def dodaj_proizvod(naziv, cijena, dostupna_kolicina):
    """Dodaje novi proizvod u skladište."""
    novi = Proizvod(naziv, cijena, dostupna_kolicina)
    skladiste.append(novi)
