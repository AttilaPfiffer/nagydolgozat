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
        lista.append(int(szam))
        print(szam)
    return lista

def ketjegyuek_szama(lista):
    darabszam: int = 0
    for i in range(0, len(lista), 1):
        if 100 > lista[i]> 9 or lista[i] < (-9):
            darabszam += 1
    return darabszam

def paros_osszege(lista):
    parosok = []
    for i in range(0, len(lista), 1):
        if lista[i] % 2 == 0:
            parosok.append(lista[i])
            x = sum(parosok)
    return x

def paratlan_osszege(lista):
    paratlanok = []
    for i in range(0, len(lista), 1):
        if not(lista[i] % 2 == 0):
            paratlanok.append(lista[i])
            x = sum(paratlanok)
    return x

