# Ova petlja će se izvrsiti samo jednom jer range (1, 2) generira samo broj 1.
# Nema smisla jer se izvršava samo jednom.
for i in range(1, 2):
  print(i)

# Ovdje je početak 10, kraj 1, korak +2.
# Pošto korak povećava vrijednost (pozitivan je), petlja nikada neće doći do 1 jer ide prema većim brojevima.
# Dakle, ova petlja se uopće NEĆE izvršiti.
for i in range(10, 1, 2):
    print(i)

# Ovdje je početak 10, kraj 1, korak -1.
# To znači da će ići unazad: 10, 9, 8, ..., 2.
# Ova petlja ima smisla jer broji unatrag.
for i in range(10, 1, -1):
    print(i)