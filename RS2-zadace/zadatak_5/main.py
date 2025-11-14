from shop.proizvodi import dodaj_proizvod, skladiste, Proizvod
from shop.narudzbe import napravi_narudzbu


proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

# Dodavanje proizvoda u skladište
for p in proizvodi_za_dodavanje:
    dodaj_proizvod(p["naziv"], p["cijena"], p["dostupna_kolicina"])

# Ispis svih proizvoda
print("=== Skladište ===")
for p in skladiste:
    p.ispis()


# Napravi narudžbu
narudzba_lista = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1},
]

narudzba = napravi_narudzbu(narudzba_lista)

if narudzba:
    print("\n=== Narudzba ===")
    narudzba.ispis()
