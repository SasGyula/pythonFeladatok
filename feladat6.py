import math


def hatodik():
    szam = int(input("Kérem adjon meg 3-al osztható vagy négyzetszámot!"))
    while not((szam % 3 == 0) or (int(szam**0.5) == szam** 0.5)):
        szam = int(input("Kérem adjon meg 3-al osztható vagy négyzetszámot!"))
    print(str(szam), "egy hárommal osztható vagy négyzetszám!")