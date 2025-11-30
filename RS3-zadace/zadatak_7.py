import asyncio

# Korutina timer:
# - prima ime timera i broj sekundi do isteka
# - odbrojava svaku sekundu pomoću await asyncio.sleep(1)
# - svaki sleep predaje kontrolu event loop-u
async def timer(name, delay):
    # Odbrojavanje od delay do 1
    for i in range(delay, 0, -1):

        # Korutina ispisuje trenutno stanje
        print(f"{name}: {i} sekundi preostalo...")

        # Ovdje se korutina pauzira na 1 sekundu
        # i PREDAJE kontrolu event loop-u.

        # To znači:
        # ovaj task prelazi u stanje WAITING
        # event loop može pokrenuti druge taskove
        await asyncio.sleep(1)

    # Kada petlja završi, timer je gotov
    print(f"{name}: Vrijeme je isteklo!")


# Glavna korutina:
# - kreira tri taska pomoću asyncio.create_task()
# - svaki create_task odmah registrira korutinu u event loop
# - asyncio.gather čeka da SVI taskovi završe
async def main():

    # Kreiramo listu taskova:
    # create_task() NE čeka izvršavanje!
    # On samo registrira korutinu u event loop-u.
    # Sva tri taska se postavljaju u stanje READY.
    timers = [
        asyncio.create_task(timer("Timer 1", 3)),
        asyncio.create_task(timer("Timer 2", 5)),
        asyncio.create_task(timer("Timer 3", 7))
    ]

    # asyncio.gather:
    # - paralelno pokreće sve taskove
    # - pauzira main() dok SVI ne završe
    # - ali event loop ostaje aktivan i raspoređuje taskove
    # gather ne blokira event loop → samo blokira main
    await asyncio.gather(*timers)


# Pokretanje event loop-a:
# asyncio.run():
# - kreira event loop
# - pokreće main() u njemu
# - zatvara loop kada sve korutine završe
asyncio.run(main())
