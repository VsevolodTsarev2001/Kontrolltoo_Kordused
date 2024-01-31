import random
#1
n=int(input("sisenda number vahemikkus 1-9:"))
if 1 <= n <= 9:
    for _ in range(n):
        print("   ~~~~~   ", end="")
    print()  # Liigu järgmisele reale

    for _ in range(n):
        print("  /_____\\  ", end="")
    print()

    for _ in range(n):
        print("  | []  |  ", end="")
    print()

    for _ in range(n):
        print("   -----   ", end="")
    print()
else:
    print("Palun sisestage number määratud vahemikus.")
#3
õpilased = 22
maksimaalne = 1
minimaalne = 5
for i in range(õpilased):
    hinned = random.randint(100, 500)/100
    print(hinned)
    if hinned > maksimaalne:
        maksimaalne = hinned
    if hinned < minimaalne:
        minimaalne = hinned
print("Maksimaalne hind on::", maksimaalne)
print("Minimaalne hind on:", minimaalne)
#4
elanikkond = [120, 80, 150, 90, 110, 70, 130, 100, 140, 95, 120, 85] #tuhendetes inimesi
pindala = [50, 30, 60, 40, 45, 25, 55, 35, 58, 38, 48, 33] # km^2

kogu_tihendus = 0

for i in range(len(elanikkond)):
    tihedus = elanikkond[i] / pindala[i]
    kogu_tihendus += tihedus

keskmine_tihendus = kogu_tihendus / len(elanikkond)

print(f"Piirkonna keskmine rahvastiku tihedus: {keskmine_tihendus} tuhat inimest/km^2")