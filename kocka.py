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
