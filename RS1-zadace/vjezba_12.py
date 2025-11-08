def obrni_rjecnik(rjecnik):
    obrnuti = {vrijednost: kljuc for kljuc, vrijednost in rjecnik.items()}
    return obrnuti

rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
print(obrni_rjecnik(rjecnik))