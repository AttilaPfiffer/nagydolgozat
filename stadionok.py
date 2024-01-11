from Stadion import Stadionok

slista = []
fajlom = open("stadionok.txt", "r", encoding = "UTF-8")
fajlom.readline()
lista = fajlom.readlines()
fajlom.close()
for i in range(0, len(lista), 1):
    aktsor: int = lista[i].strip()
    print(aktsor)
    sor_lista = aktsor.strip()
    sor_lista = aktsor.split(";")
    print(sor_lista[0])
    print(sor_lista[1])
    print(sor_lista[2])
    print(sor_lista[3])
    print(sor_lista[4])
    autok = Stadionok(sor_lista[0], sor_lista[1], sor_lista[2], sor_lista[3], sor_lista[4])
    slista.append(autok)

for i in range(0, len(slista), 1):
    print(f"{slista[i].snev}, {slista[i].shelyszin}, {slista[i].shany}, {slista[i].seloszor}, {slista[i].sutoljara}")