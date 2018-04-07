import sys

print("")
print("..............CONSIGNES.................")
print("  Ce script va calculer votre moyenne pour vous!")
print("Il faudra lui spécifier le nom de la matiere et le nombre de notes que vous avez eu pour cette matière")
print("Ne taper que des nombres")
print("..........................................")
print("")
print("")
print("Voici le choix de la matière :")
print("{1} Maths")
print("{2} Français")
print("{3} Anglais")
print("{4} Espanol")
print("{5} Sport")
print("{6} Technologie")
print("{7} Physique")
print("{8} SVT")
print("{9} Histoire-Géo")
print("{10} Religion")
try:
	choice = int(input("Quel matière choisissez-vous?"))
except ValueError:
	print("Vous n'avez pas taper un nombre!")
	print("Au revoir...")
	input("Taper la touche Entrée pour quitter")
	sys.exit(1)
else:
	if choice == 1:
		choice = "Maths"
	elif choice == 2:
		choice = "Français"
	elif choice == 3:
		choice = "Anglais"
	elif choice == 4:
		choice = "Espagnol"
	elif choice == 5:
		choice = "Sport"
	elif choice == 6:
		choice = "Technologie"
	elif choice == 7:
		choice = "Physique"
	elif choice == 8:
		choice = "SVT"
	elif choice == 9:
		choice = "Histoire-Géo"
	elif choice == 10:
		choice = "Religion"
	else:
		print("Ceci ne correspond pas aux matières proposées!")
		print("Au revoir")
		input("Taper la touche Entrée pour quitter")
		sys.exit(1)
	print("Vous avez choisi de calculer votre moyenne pour:", choice)
	print("")
	print("..........................................")
	print("")
	try:
		nbnot = int(input("Combien avez vous eu de notes ?"))
	except ValueError:
		print("Vous n'avez pas taper un nombre!")
		print("Au revoir...")
		input("Taper la touche Entrée pour quitter")
		sys.exit(1)
	else:
		if nbnot == 1 or nbnot >= 50:
			print("Ce nombre de note est incorrect!")
			input("Appuyer sur la touche Entrée pour quitter")
			sys.exit(1)
		note = []
		coef = []
		print("Appuyer sur la touche Entrée après chaque notes")
		for i in range(nbnot):
			try:
				i =  float(input("Taper une note: "))
				p = float(input("Quel est son coefficient?"))
			except ValueError:
				print("Vous n'avez pas taper un nombre!")
				print("Au revoir...")
				input("Taper la touche Entrée pour quitter")
				sys.exit(1)
			else:
				coef.append(p)
				i = i * p
				note.append(i)
		add = sum(note)#sum() additionne les valeurs de note entre elles
		ad = sum(coef)# addtions des coefficients
		calc = add/ad
# Pour calculer une moyenne:
# additionner les notes
# additionner les coefficients
# diviser le premier résultat avec le deuxième
		if round(calc) == calc:
			calc = int(calc)
		else:
			calc = float(calc)
		print("")
		print("[..........  ...........................]")
		print("Votre moyenne en", choice,"est de", float(round(calc, 2)))
		print("[.......................................]")
		print("")
		print("")
		input("Appuyer sur la touche Entrée pour quitter")
