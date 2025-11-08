# 1. Suma parnih brojeva od 1 do 100
# For petlja
suma = 0
for i in range(1, 101):
    if i % 2 == 0:   
        suma += i
print(f"Suma svih parnih brojeva od 1 do 100 je {suma}.")

# While petlja
suma = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        suma += i
    i += 1
print(f"Suma svih parnih brojeva od 1 do 100 je {suma}.")

# 2. Prvih 10 neparnih brojeva u obrnutom redoslijedu
# For petlja
neparni = []

for i in range(1, 20, 2): 
    neparni.append(i)

neparni.reverse() 
print("Neparni brojevi u obrnutom redoslijedu:", neparni)

# While petlja
neparni = []
i = 1

while len(neparni) < 10: 
    neparni.append(i)
    i += 2

neparni.reverse()
print("Neparni brojevi u obrnutom redoslijedu:", neparni)

# 3. Ispis Fibonaccijevog niza do 1000
# For petlja
fibonacci = [0, 1]

for i in range(2, 1000):
    sljedeci = fibonacci[-1] + fibonacci[-2]
    if sljedeci > 1000:
        break
    fibonacci.append(sljedeci)

print("Fibonacci niz do 1000:", fibonacci)

# While petlja
fibonacci = [0, 1]

while True:
    sljedeci = fibonacci[-1] + fibonacci[-2]
    if sljedeci > 1000:
        break
    fibonacci.append(sljedeci)

print("Fibonacci niz do 1000:", fibonacci)