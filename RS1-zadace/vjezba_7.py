def provjera_lozinke(lozinka):
    # 1. Provjera duljine
    if len(lozinka) < 8 or len(lozinka) > 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova.")
        return

    # 2. Provjera barem jednog velikog slova i jednog broja
    ima_veliko = any(z.isupper() for z in lozinka)
    ima_broj = any(z.isdigit() for z in lozinka)

    if not (ima_veliko and ima_broj):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj.")
        return

    # 3. Provjera zabranjenih riječi ('password', 'lozinka')
    mala_lozinka = lozinka.lower()
    if "password" in mala_lozinka or "lozinka" in mala_lozinka:
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'.")
        return

    # 4. Ako sve uvjete zadovoljava:
    print("Lozinka je jaka!")


unos = input("Unesi lozinku: ")
provjera_lozinke(unos)