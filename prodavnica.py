import random
import math

proizvodi = ["Laptop", "Mis", "Tastatura", "Monitor", "Slusalice", "Kamera", "Tablet", "Telefon"]

cene = {
    "Laptop": 950.99,
    "Mis": 19.99,
    "Tastatura": 49.99,
    "Monitor": 199.99,
    "Slusalice": 89.99,
    "Kamera": 300.00,
    "Tablet": 250.50,
    "Telefon": 799.99
}

for proizvod in proizvodi:
    print(proizvod, "-", cene[proizvod], "€")

budzet = float(input("Unesite vas budzet: "))

print("Mozete kupiti:")
for proizvod in proizvodi:
    if cene[proizvod] <= budzet:
        print(proizvod)

def najskuplji_proizvod(cene):
    return max(cene, key=cene.get)

najskuplji = najskuplji_proizvod(cene)
print("Najskuplji proizvod:", najskuplji, "-", cene[najskuplji], "€")

random_proizvod = random.choice(proizvodi)
print("Korisniku je privukao paznju proizvod:", random_proizvod)

prosek = round(sum(cene.values()) / len(cene), 2)
print("Prosecna cena:", prosek, "€")

kolicine = [5, 20, 10, 7, 12, 3, 6, 8]

ukupan_prihod = 0
for i in range(len(proizvodi)):
    ukupan_prihod += cene[proizvodi[i]] * kolicine[i]

print("Ukupan prihod:", ukupan_prihod, "€")

proizvodi.append("Pametni sat")
cene["Pametni sat"] = 150.00

print("Nova lista:")
for p in proizvodi:
    print(p)

sortirani = sorted(cene.items(), key=lambda x: x[1])

print("Sortirano:")
for proizvod, cena in sortirani:
    print(proizvod, "-", cena, "€")