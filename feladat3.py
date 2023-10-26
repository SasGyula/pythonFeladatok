def harmadik():
    szam = int(input("Kérem adjon meg egy 10-el osztható számot!"))
    while not(szam % 10 == 0):
        szam = int(input("Kérem adjon meg egy 10-el osztható számot!"))
    print(str(szam), "osztható 10-el!")