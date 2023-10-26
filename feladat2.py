def masodik():
    szam = 0
    eredmeny = 0
    while szam < 10:
        szam1 = int(input("Kérem adjon meg egy számot!"))
        if szam1 % 3 == 0:
            eredmeny += 1
        szam += 1
    print("Összesen", str(eredmeny) , "3-al osztható számot adott meg!")

