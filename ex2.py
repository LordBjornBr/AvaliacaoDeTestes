n = int(input("Escolha uma tabuada: "))
mult = 1
while mult <=10:
    res = n * mult
    print(f"{n} x {mult} = {res}")
    mult += 1
    if mult >10:
        print(f"Essa é a tabuada do {n}")