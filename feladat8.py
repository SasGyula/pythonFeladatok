def nyolcadik():
    szoveg = input("Kérem adjon meg egy 3 karakteres szöveget!")
    nagybetu = szoveg.upper()
    while not(len(szoveg) > 2 ):
        szoveg = input("Kérem adjon meg egy 3 karakteres szöveget!")
    print(nagybetu)