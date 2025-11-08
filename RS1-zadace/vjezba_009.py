def ukloni_duplikate(lista):
    nova_lista = list(set(lista))
    return nova_lista

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(ukloni_duplikate(lista))