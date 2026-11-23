print("1.feladat")
for i in range(40,65,5):
    print(i)
print("2.feladat")
for i in range(200, -1, -40):
    print(i)

print("3.feladat")
import random

k=[]
for i in range(30):
    szam=random.randint(-10,10)
    k.append(szam)
    print(szam,end=" ")
h=int(input("\nHányasával írjuk ki a számokat: "))
for i in range(0,len(k),h):
    print(k[i:i+h],end=" ")

print("\n4. feladat")
db=0
db2=0
for i in range(30):
    if k[i]<0:
        db+=1
    if k[i]==0:
        db2+=1
print(f"Negatív szamok:{db}")
print(f"Nullák száma:{db2}")


print("5.feladat")
#Két kockával dobunk 50-szer! Szimuláljuk ezt a ’d’ listában! Írjuk ki a dobásokat 5 sorban!

d = []
for i in range(50):
    kocka1 = random.randint(1, 6)
    kocka2 = random.randint(1, 6)
    d.append(kocka1 + kocka2)

for i in range(0, len(d), 10):
    print(d[i:i+10])

print("6. feladat")
#Kérjük be a két kockával történő dobás egy lehetséges értékét! 
# Ha olyan értéket adunk meg, ami nem lehetséges, akkor írja ki, hogy ilyen nem lehetséges és kérje újból!

dobas=int(input("Mennyit dobjunk (2-12 között): "))
while dobas<2 or dobas>12:
    print("Ilyen dobás nem lehetséges")
    dobas=int(input("Adj meg egy új számot (2-12 között): "))
print(f"A dobás lehetséges, {dobas}")


print("7. feladat")
#Írjuk ki, hogy hány db olyan értékű dobás volt!
count = d.count(dobas)
print(f"A {dobas} dobásból {count} db volt.")