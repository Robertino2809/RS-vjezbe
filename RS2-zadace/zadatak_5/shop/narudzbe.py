class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis(self):
        print("Narudženi proizvodi:")
        for p in self.naruceni_proizvodi:
            print(f"{p['naziv']} x {p['narucena_kolicina']}")
        print(f"Ukupna cijena: {self.ukupna_cijena} eur")


narudzbe = []


def napravi_narudzbu(lista_proizvoda):
    if not isinstance(lista_proizvoda, list):
        print("Greška: argument mora biti lista!")
        return None

    if len(lista_proizvoda) == 0:
        print("Greška: lista proizvoda je prazna!")
        return None

    for p in lista_proizvoda:
        if not isinstance(p, dict):
            print("Greška: svaki element mora biti rječnik!")
            return None

        if not all(k in p for k in ("naziv", "cijena", "narucena_kolicina")):
            print("Greška: rječnik mora imati ključeve naziv, cijena, narucena_kolicina")
            return None

    # Provjera dostupnosti
    from .proizvodi import skladiste

    for p in lista_proizvoda:
        naziv = p["naziv"]
        narucena_kolicina = p["narucena_kolicina"]

        # Pronadi proizvod u skladištu
        item = next((x for x in skladiste if x.naziv == naziv), None)

        if item is None:
            print(f"Proizvod {naziv} ne postoji u skladištu!")
            return None

        if item.dostupna_kolicina < narucena_kolicina:
            print(f"Proizvod {naziv} nije dostupan!")
            return None

    ukupno = sum(p["cijena"] * p["narucena_kolicina"] for p in lista_proizvoda)

    nova = Narudzba(lista_proizvoda, ukupno)

    narudzbe.append(nova)

    return nova
