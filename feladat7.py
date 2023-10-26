def hetedik():
    a = int(input("Adja meg a háromszög 'a' oldalát!"))
    b = int(input("Adja meg a háromszög 'b' oldalát!"))
    c = int(input("Adja meg a háromszög 'c' oldalát!"))
    while not(a+b > c and a+c > b and b+c > a):
        print("A háromszög nem szerkezthető")
        a = int(input("Adja meg a háromszög 'a' oldalát!"))
        b = int(input("Adja meg a háromszög 'b' oldalát!"))
        c = int(input("Adja meg a háromszög 'x' oldalát!"))
    print("A háromszög szerkezthető")