#1. Feladat
import random
Llist = [random.randint(0, 9) for _ in range(10)]
print("Eredeti lista: ", Llist)

paratlan = sum(1 for szam in Llist if szam % 2 == 1)
print("Paratlanok szama", paratlan)

ismetlodo_szam = list(set(Llist))
print("Ismetlodo elemek: ", ismetlodo_szam)

hianyzo_szam = [szam for szam in range(10) if szam not in Llist]

if hianyzo_szam:
    print("Nem szereplő számok:", hianyzo_szam)
else:
    print("Minden szám szerepel 0 és 9 között.")

#2. Feladat

mondat = "A programozás logikus gondolkodást fejleszt"

hossz = [len(szo) for szo in mondat.split()]

print(hossz)


#3. feladat
szam = input("Szam: ")

osszeg = 0
for szamjegy in szam:
    osszeg += int(szamjegy)

print("Szamjegyek: " , osszeg)

#4. feladat

mondat = input("Mondat: ")

if not mondat:
    print("Nem adtál meg semmit")
else:
    utolso = mondat[-1]

if utolso == ".":
    print("Kijelento mondat")
elif utolso == "?":
    print("Kerdo mondat")
elif utolso == "!":
    print("felszolito vagy ohajto mondat.")
else:
    print("A mondat tipusa nem hatarozhato meg, nem raktal irasjelet a vegere.")

#5. feladat

szamok = []

while (be := input("adj meg egy szamot vagy ird be hogy 'stop': ")) != "stop":
    if be.isdigit() or (be.startswith("-") and be[1:].isdigit()):
        szamok.append(int(be))

print("beolvasott szamok: ", len(szamok))
if szamok:
    print("Legnagyobb - legkisebb (kulombsege):" , max(szamok) - min(szamok))
    print("3-mal oszthatoak:" , [x for x in szamok if x % 3 == 0])