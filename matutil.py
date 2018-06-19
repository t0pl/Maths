import sys
from math import sqrt


def main():
    for i in range(1, nb+1):
        if nb/i == round(nb/i):
            print(nb, "est divisible par", i,)
            print(nb, "divisé par", i, "vaut", nb/i)
        else:
            pass
    for x in range(1, 21):
        print(x, "×", nb, "=", x*nb)
    print("Carré:", nb*nb)
    if sqrt(nb) == round(sqrt(nb)):
        print("La racine carrée de", nb, "tombe juste")
    else:
        print("La racine carrée de" , nb, "ne tombe pas juste")
    print("Racine carrée:", round(sqrt(nb)))
    for v in range(1,11):
        print("Exposant",v,":", nb ** v)
        v += 1

try:
    nb = float(input("Taper un nombre =>"))
    print("......................................")
except ValueError:
    print("Vous n'avez pas tapé un nombre")
    sys.exit()
else:
    if nb == int(nb):
        nb = int(nb)
        main()
    else:
        nb = float(nb)
        main()
