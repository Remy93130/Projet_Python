#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fonctions d'un jeu de Casse brique."""
# Imports --------------------------------------------------------------------------------------------------------
from upemtk import *
from time import *
from random import randint
from sys import argv

# Variables globales ---------------------------------------------------------------------------------------------
deplacementBalle = [randint(0,6),10]
positionRaquette = [110, 420, 190, 430]

# Fonctions ------------------------------------------------------------------------------------------------------
def creation_interface():
	"""Cree l interface du jeu."""
	ligne(300,0,300,450, epaisseur="2")
	texte(320,15, "Casse Brique", taille=14)


def animation_balle(balle):
	"""Permet de deplacer la balle."""
	global positionBalle
	efface(balle)
	positionBalle = (positionBalle[0] + deplacementBalle[0], positionBalle[1] - deplacementBalle[1])
	balle = cercle(positionBalle[0], positionBalle[1], 4, remplissage="black")
	mise_a_jour()
	return(balle)


def collision(positionBalle):
	"""Permet de verifier si la balle entre en contact avec un element."""
	global deplacementBalle, positionRaquette

	#On verifie si elle touche le haut de la fenetre
	if (positionBalle[1]+4 <= 0):
		#On inverse le deplacement verticale de la balle
		deplacementBalle[1] *= -1

	#On verifie si elle touche un cote de la fenetre
	if (positionBalle[0]+4 <= 0 or positionBalle[0]+4 >= 300):
		deplacementBalle[0] *= -1

	#On verifie si elle touche la raquette:
	collision_raquette(positionBalle)
	


def collision_raquette(positionBalle):
	"""Complement de la fonction collision, permet de vérifier 
	si la balle touche la raquette et modifie l'orientation de
	la balle."""
	global deplacementBalle, positionRaquette

	if (positionBalle[0] >= positionRaquette[0] and positionBalle[0] <= positionRaquette[2]) and (positionBalle[1] == 420):

		deplacementBalle[1] *= -1 #On renvoie la balle vers le haut

		#On choisi l inclinaison de la balle selon ou elle touche la raquette
		if ((positionRaquette[0] <= positionBalle[0] and positionBalle[0] <= positionRaquette[0]+10) or 
			(positionRaquette[0]+70 <= positionBalle[0] and positionBalle[0] <= positionRaquette[0]+80)):

			deplacementBalle = [8,8]
		elif ((positionRaquette[0]+10 <= positionBalle[0] and positionBalle[0] <= positionRaquette[0]+20) or 
			(positionRaquette[0]+60 <= positionBalle[0] and positionBalle[0] <= positionRaquette[0]+70)):

			deplacementBalle = [6,8]
		elif ((positionRaquette[0]+20 <= positionBalle[0] and positionBalle[0] <= positionRaquette[0]+30) or 
			(positionRaquette[0]+50 <= positionBalle[0] and positionBalle[0] <= positionRaquette[0]+60)):
			
			deplacementBalle = [4,8]

		else:
			deplacementBalle = [2,10]

		#Verifie si la balle doit changer de direction selon le positionnement
		#De la raquette
		if (positionBalle[0] < ((positionRaquette[0]+positionRaquette[2])/2) and deplacementBalle[0] > 0):
			deplacementBalle[0] *= -1
		if (positionBalle[0] > ((positionRaquette[0]+positionRaquette[2])/2) and deplacementBalle[0] < 0):
			deplacementBalle[0] *= -1


def animation_raquette(raquette):
	"""Permet de deplacer la raquette"""
	global positionRaquette
	efface(raquette)
	appuie = donne_evenement()
	type_appuie = type_evenement(appuie)
	if type_appuie == "Touche":
		deplace = touche(appuie)
		if deplace == 'Right' and positionRaquette[2] < 290:

			positionRaquette[0] += 20
			positionRaquette[2] += 20
			
		if deplace == 'Left' and positionRaquette[0] > 0:
			
			positionRaquette[0] -= 20
			positionRaquette[2] -= 20

	raquette = rectangle(positionRaquette[0], positionRaquette[1], 
		positionRaquette[2], positionRaquette[3],
		couleur='black', remplissage='blue', epaisseur=1,)
	mise_a_jour()
	return raquette 


def mode_auto(raquette):
	"""Permet si l'option est selectionnee que 
	l ordinateur joue a notre place."""
	global positionBalle, positionRaquette
	efface(raquette)
		
	positionRaquette = (positionBalle[0]-40, positionRaquette[1],
			 positionBalle[0]+40, positionRaquette[3])
	
	if positionRaquette[0] < 0:
		positionRaquette = (0, positionRaquette[1],
			 80, positionRaquette[3])
	
	if positionRaquette[2] > 300:
		positionRaquette = (220, positionRaquette[1],
			 300, positionRaquette[3])
	raquette = rectangle(positionRaquette[0], positionRaquette[1], 
		positionRaquette[2], positionRaquette[3],
		couleur='black', remplissage='blue', epaisseur=1,)
	mise_a_jour()
	return raquette 

def fin_jeu(vie, positionBalle):
	"""Permet de verifier si la balle n est pas renvoyer
	fonction incomplete creer pour une update futur."""
	if positionBalle[1] > 453:
		vie -= 1
	return(vie)


def creation_brique():
	"""Creer les briques qui devront etre detruitees"""
	brique = [
	3,2,2,2,2,2,3,
	3,1,1,1,1,1,3,
	3,2,2,2,2,2,3,
	0,3,1,1,1,3,0,
	0,3,0,0,0,3,0,
	0,3,0,0,0,3,0,
	1,1,1,1,1,1,1,
	1,1,1,1,1,1,1,
	1,1,1,1,1,1,1,
	1,3,3,3,2,2,1
	]
	return(brique)


def afficher_brique(brique):
	"""Permet d'afficher les briques dans la fenetre"""
	briqueTester = 0 #Parametre de la premiere brique
	for i in range(10,150,15):
		for j in range(10,280,40):
			if brique[briqueTester] <= 0:
				rectangle(j,i,
					j+40,i+15,
					remplissage='white',
					couleur='white')
				briqueTester += 1
				continue
			else:
				if brique[briqueTester] == 1:
					fichier = 'brique1.gif'
				elif brique[briqueTester] == 2:
					fichier = 'brique2.gif'
				else:
					fichier = 'brique3.gif'
			image(j,i,fichier,
				ancrage='nw',
				tag=briqueTester)

			briqueTester += 1


def detection_briques(positionBalle, brique):
	"""Permet de savoir si la balle rentre en collision avec
	une brique et permet de connaitre quelle brique"""
	global deplacementBalle
	# if positionBalle[0] < 160:
	# 	return None
	briqueT = 63
	for i in range(160,10,-15):
		for j in range(10,290,40):
			if positionBalle[1]+4 <= i and positionBalle[1]+4 > i-15:
				if positionBalle[0]+4 >= j and positionBalle[0]+4 <= j+40:
					if brique[briqueT] > 0: # Si il y a une brique
						return briqueT
			briqueT += 1
		briqueT -= 14
	return None


def collision_brique(positionBalle, brique, briqueTest):
	"""Complement de detection_briques, si la balle touche
	une brique alors cette fonction va gerer la collision
	avec la destruction ou non de la brique et le changement
	de direction de la balle"""
	global deplacementBalle
	#On simule un deplacement de la balle pour savoir ou elle touche la brique
	positionBallePrecedente1 = (positionBalle[0] + deplacementBalle[0], positionBalle[1] - deplacementBalle[1]) #Gauche
	positionBallePrecedente2 = (positionBalle[0] - deplacementBalle[0], positionBalle[1] - deplacementBalle[1]) #Droite
	#positionBallePrecedente3 = (positionBalle[0], positionBalle[1] - deplacementBalle[1]) #Haut
	#positionBallePrecedente4 = (positionBalle[0], positionBalle[1] + deplacementBalle[1]) #Bas
	#On verifie si il y avais une brique sur ces positions
	briquePrecedente1 = detection_briques(positionBallePrecedente1, brique)
	briquePrecedente2 = detection_briques(positionBallePrecedente2, brique)
	
	deplacementBalle[1] *= -1
	brique[briqueTest] -= 1
	efface_tout()
	creation_interface()
	afficher_brique(brique)
	
	

def verification_brique(brique):
	"""Verifie si toutes les briques ont ete detruite
	renvoie True si oui sinon False"""
	for element in brique:
		if element >0:
			return False
	return True


if __name__ == '__main__':
	#import.doctest
	#doctest.testmod()	

	hauteur = 450
	largeur = 450
	cree_fenetre(largeur, hauteur)
	creation_interface()

	#Vitesse de deplacement de la balle a modifier selon la machine
	if "auto" in argv: #On augmente la vitesse du jeu si on est en mode auto (debogage)
		rafraichissement = 0.0075
	else:
		rafraichissement = 0.035

	raquette = rectangle(positionRaquette[0], positionRaquette[1], 
		positionRaquette[2], positionRaquette[3],
		couleur='black', remplissage='', epaisseur=1,)

	#Position de depart de la balle
	positionBalle = [150, 400]
	balle = cercle(positionBalle[0], positionBalle[1], 4, remplissage="black")
	vie = 1
	fin = False
	brique = creation_brique()
	afficher_brique(brique)
	attente_touche()


	while (vie > 0 and fin == False): #A modifier lorqu il y aura plusieur vie et casser toute les briques!

		if "auto" in argv: #Si on a choisi le mode auto
			raquette = mode_auto(raquette)
		else:
			raquette = animation_raquette(raquette)
		balle = animation_balle(balle)
		collision(positionBalle)
		
		briqueToucher = detection_briques(positionBalle, brique) #Si on est en contact avec une brique
		if briqueToucher is not None:
			collision_brique(positionBalle, brique, briqueToucher)
		creation_interface()
		vie = fin_jeu(vie, positionBalle)
		fin = verification_brique(brique)
		sleep(rafraichissement)

	
	if vie == 0:
		texte(30, 225, 'Vous avez perdu', couleur='red',
			ancrage='nw', police="Purisa", taille=24)
	
	else:
		texte(30, 225, 'Vous avez gagné', couleur='red',
			ancrage='nw', police="Purisa", taille=24)
	attente_touche()
	ferme_fenetre()