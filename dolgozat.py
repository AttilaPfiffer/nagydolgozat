import random
lista = []

def beker():
    print("1. feladat / a")
    szam: int = int(input("Kérek egy páros számot: "))
    while not(szam % 2 == 0):
        szam: int = int(input("Ez nem páros! Páros számot kérek!"))
    print(szam)
        
def bekerb():
    i: int = 0
    for i in range (0, 3, 1):
        szam: int = int(input(f"Kérem az {i + 1}. páros számot!"))
        while szam % 2 == 0:
            szam: int = int(input(f"Kérem az {i + 1}. páros számot!"))
        else:
            szam: int = int(input(f"Ez nem PÁROS! Kérem az {i + 1}. páros számot!"))

def feladat2():
    lista = []
    for i in range(13):
        szam: int = random.randint(-40, 150)
        lista.append(str(szam))
        print(szam)

def ketjegyuek_szama(lista):
    darabszam = []
    for i in range(0, len(lista), 1):
        if lista[i] % 2 == 0:
            darabszam += 1
        i += 1
    return darabszam