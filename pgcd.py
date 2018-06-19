import sys


nbpremiers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 43, 59, 61, 67, 71]
print("PGCD: Plus Grand Diviseur Commun")

def Euclide(a, b):
	while a%b != 0:
		a, b = b, a%b
		maxi = max(a, b)
		mini = min(a, b)
		reste = maxi%mini
		div = int(maxi/mini)
		print("{0} = {1}*{2} + {3}".format(maxi, mini, div, reste))
		maxi = mini
		mini = reste
	Back()

def Back():
	print("................................................................................")
	print()
	print("1- Revenir au menu principal")
	print("2- Quitter")
	print()
	try:
		re = int(input("Taper le nombre de votre choix => "))
	except ValueError:
		print("Vous n'avez pas taper un nombre valable")
		sys.exit()
	if re == 1:
		Menu()
	elif re == 2:
		print("Au revoir.")
		sys.exit()
	else:
		print("Ce nombre ne correspond pas aux choix disponibles")
		sys.exit()
		
def PGCD(A, B):
	if A <= 0 or B <= 0:
		print("Les nombres ne peuvent pas être égaux ou inférieur à 0")
		sys.exit()
	elif A >= 100000000 or B >= 100000000:
		print("Les nombres ne peuvent pas être au-dessus de 1000")
		sys.exit()
	divA = []
	divB = []
	divcom = []
	for x in range(1, A+1):
		calc = int(A)/x
		if calc == int(round(calc)):
			if x in divA:
				pass
			else:
				divA.append(int(x))
		else:
			pass
	for i in range(1,B+1):
		ca = int(B)/i
		if ca == int(round(ca)):
			if i in divB:
				pass
			else:
				divB.append(i)
		else:
			pass
	for nb in range(max(A, B)+1):
		if nb in divA and nb in divB:
			if nb in divcom:
				pass
			else:
				divcom.append(nb)
		else:
			pass
	print("................................................................................")
	print("Liste des diviseurs de", A)
	print(divA)
	print("")
	print("Liste des diviseurs de", B)
	print(divB)
	print("")
	print("Liste des diviseurs communs")
	print(divcom)
	longueur = max(divcom)
	print("D'où le plus grand diviseur commun de {0} et de {1} est:".format(A, B), longueur)
	Back()

def View(a, b):
	if a != int(a) and b != int(b):
		print("Tape des entiers!")
		sys.exit()
	if a > b:
		grand = a
		g = b
	elif b > a:
		grand = b
		g = a
	print("PGCD({0}, {1})".format(a, b))
	while True:
		petit = max(a, b) - min(a, b)
		print("= PGCD({0}, {1})".format(min(a, b), petit))
		ok = min(a, b)
		encor = max(ok, petit) - min(petit, ok)
		print("= PGCD({0}, {1})".format(petit, encor))
		a = petit
		b = encor
		if petit == encor:
			break
		if max(a, b) <= 0 or min(a, b) <= 0 or petit <= 0:
			break
	Back()

def Menu():
	print()
	print()
	print("......................................MENU......................................")
	print()
	print("1- Methode d'Euclide")
	print("2- Methode par soustractions successives")
	print("3- Methode détaillée")
	print()
	try:
		choix = int(input("Taper le nombre correspondant à votre choix => "))
	except ValueError:
		print("Vous n'avez pas taper un nombre valable")
		sys.exit()
	print("..................................................................................")
	try:
		if choix == 1:
			a = int(input("Taper A: "))
			b = int(input("Taper B: "))
			Euclide(a, b)
		elif choix == 2:
			a = int(input("Taper A: "))
			b = int(input("Taper B: "))
			View(a, b)
		elif choix == 3:
			A = int(input("Taper A: "))
			B = int(input("Taper B: "))
			PGCD(A, B)
		else:
			print("Ce nombre ne correspond pas aux choix disponibles")
	except ValueError:
		print("Vous n'avez pas taper un nombre valable")
		sys.exit()
Menu()
