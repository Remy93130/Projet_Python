from upemtk import *

if __name__ == '__main__':
	cree_fenetre(450, 450)
	texte(225, 35, "Bienvenue sur Relobrik\n Choisissez un mode", ancrage='center')
	rectangle(10, 100, 440, 250, couleur='red', remplissage='red')
	texte(225, 175, "Mode challenge", ancrage='center', taille=18)
	rectangle(10, 270, 440, 420, couleur='blue', remplissage='blue')
	texte(225, 345, "Mode personnalisé", ancrage='center', taille=18)
	while 1:
		x = attente_clic()
		if 10 < x[0] < 440:
			if 100 <= x[1] <= 250:
				print("challenge")
			if 270 <= x[1] <= 420:
				print("personnalisé")
	ferme_fenetre()