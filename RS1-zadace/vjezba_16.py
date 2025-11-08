import heapq

def dijkstra(graf, pocetni):
    udaljenosti = {cvor: float('inf') for cvor in graf}
    udaljenosti[pocetni] = 0
    red = [(0, pocetni)]  # (trenutna_udaljenost, čvor)

    while red:
        trenutna_udaljenost, trenutni = heapq.heappop(red)

        if trenutna_udaljenost > udaljenosti[trenutni]:
            continue

        for sljedeci, tezina in graf[trenutni]:
            nova_udaljenost = trenutna_udaljenost + tezina
            if nova_udaljenost < udaljenosti[sljedeci]:
                udaljenosti[sljedeci] = nova_udaljenost
                heapq.heappush(red, (nova_udaljenost, sljedeci))

    return udaljenosti

graf = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print(dijkstra(graf, 'A'))