def kilencedik():
    szoveg = input("Kérem adjon meg egy 4 karakteres kisbetűs szöveget!")
    while not(len(szoveg) > 3 and szoveg.islower()):
        szoveg = input("Kérem adjon meg egy 4 karakteres kisbetűs szöveget!")
    print(szoveg)