# 1. Funkcija koja provjerava je li broj prost
def isPrime(broj):
    if broj <= 1:
        return False
    for i in range(2, int(broj ** 0.5) + 1):
        if broj % i == 0:
            return False
    return True

print(isPrime(7)) 
print(isPrime(10))  

# 2. Funkcija koja vraća sve proste brojeve u zadanom rasponu
def primes_in_range(start, end):
    prosti = []
    for broj in range(start, end):
        if isPrime(broj):
            prosti.append(broj)
    return prosti

print(primes_in_range(1, 10)) 