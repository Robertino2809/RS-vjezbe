import random

broj = random.randint(1, 100)
broj_pokusaja = 0
pogoden_broj = False

while not pogoden_broj:
  pokusaj = int(input("Pogodi broj između 1 i 100: "))
  broj_pokusaja += 1

  if pokusaj < broj:
    print("Previše nisko! Pokušaj ponovno.")
  elif pokusaj > broj:
    print("Previše visoko! Pokušaj ponovno.")
  else:
    pogoden_broj = True
    print(f"Bravo, pogodio si u {broj_pokusaja} pokušaja!")