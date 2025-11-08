# 1. Funkcija koja vraća prvi i zadnji element liste
def prvi_i_zadnji(lista):
    return (lista[0], lista[-1])

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(prvi_i_zadnji(lista))

# 2. Funkcija koja vraća maksimalni i minimalni element liste
def maks_i_min(lista):
    maks = lista[0]
    min_ = lista[0]

    for broj in lista:
        if broj > maks:
            maks = broj
        if broj < min_:
            min_ = broj
    return (maks, min_)

lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print(maks_i_min(lista)) 

# 3. Funkcija koja vraća presjek dvaju skupova
def presjek(skup1, skup2):
    return skup1 & skup2 

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
print(presjek(skup_1, skup_2))