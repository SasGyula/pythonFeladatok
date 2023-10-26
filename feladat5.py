def otodik():
        szam = int(input("Kérem adjon meg egy pozitív páratlan számot!"))
        while not (szam % 3 == 0 and szam > 0):
            szam = int(input("Kérem adjon meg egy pozitív páratlan számot!"))
        print(str(szam), "egy pozítív páratlan szám")