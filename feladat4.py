def negyedik():
    szam = int(input("Kérem adjon meg egy pozitív páros számot!"))
    while not(szam > 9 and szam > 0):
        szam = int(input("Kérem adjon meg egy pozitív páros számot!"))
    print(str(szam), "egy pozitív páros szám!")