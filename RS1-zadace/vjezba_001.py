prvi_broj = float(input("Unesite prvi broj: "))
operator = input("Unesi operator +, -, *, /: ")
drugi_broj = float(input("Unesite drugi broj: "))

if operator == "+":
  zbroj = prvi_broj + drugi_broj
  print(f"Rezultat operacije {prvi_broj} + {drugi_broj} je {zbroj}")

elif operator == '-':
  razlika = prvi_broj - drugi_broj
  print(f"Rezultat operacije {prvi_broj} - {drugi_broj} je {razlika}")

elif operator == '*':
  umnozak = prvi_broj * drugi_broj
  print(f"Rezultat operacije {prvi_broj} * {drugi_broj} je {umnozak}")

elif operator == '/':
  if drugi_broj == 0:
    print("Dijeljenje s nulom nije dozvoljeno.")
  else:
    kolicnik = prvi_broj / drugi_broj
    print(f"Rezultat operacije {prvi_broj} / {drugi_broj} je {kolicnik}")

else:
  print("Nepodržan operator.")