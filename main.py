#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fonctions d'un jeu de Casse brique."""
# Imports --------------------------------------------------------------------------------------------------------
from upemtk import *
from time import *
from random import randint
from sys import argv
from math import *

# Variables globales ---------------------------------------------------------------------------------------------
deplacementBalle = [0,0]
deplacementBalle[0] = randint(0,8)
if deplacementBalle[0] != 0:
	deplacementBalle[0] = deplacementBalle[0] / 10
deplacementBalle[1] = 1-deplacementBalle[0]
positionRaquette = [110, 420, 190, 430]

# Fonctions ------------------------------------------------------------------------------------------------------
def creation_interface(score, vie):
	"""Cree l interface du jeu."""
	efface('score')
	efface('vie')
	texte(320,50, "Score : " + str(score), taille=14, tag='score')
	texte(320,85, "Vie : " + str(vie), taille=14, tag='vie')


def timer(minute, tempsDebut):
	"""Permet de faire un chronometre"""
	efface('timer')
	tempsATM = int(time()-tempsDebut)
	#Si une minute est passe
	if tempsATM >= 60:
		tempsATM = 0
		tempsDebut = time()
		minute += 1
	#On affiche le chrono
	texte(320,120, "Temps : " + str(minute) + ':' + str(tempsATM),
		taille=14, tag='timer')
	return (minute, tempsDebut)


def animation_balle(balle):
	"""Permet de deplacer la balle."""
	global positionBalle
	positionBalle = (positionBalle[0] + deplacementBalle[0], positionBalle[1] - deplacementBalle[1])
	balle = cercle(positionBalle[0], positionBalle[1], 4, remplissage="black")
	mise_a_jour()
	return(balle)


def collision(positionBalle):
	"""Permet de verifier si la balle entre en contact avec un element."""
	global deplacementBalle, positionRaquette

	#On verifie si elle touche le haut de la fenetre
	if (positionBalle[1]+4 < 0):
		#On inverse le deplacement verticale de la balle
		deplacementBalle[1] *= -1

	#On verifie si elle touche un cote de la fenetre
	if (positionBalle[0]+4 < 0 or positionBalle[0]+4 > 300):
		deplacementBalle[0] *= -1

	#On verifie si elle touche la raquette:
	collision_raquette(positionBalle)
	


def collision_raquette(positionBalle):
	"""Complement de la fonction collision, permet de vérifier 
	si la balle touche la raquette et modifie l'orientation de
	la balle."""
	global deplacementBalle, positionRaquette

	if (positionBalle[0] >= positionRaquette[0] and positionBalle[0] <= positionRaquette[2]) and (positionBalle[1] > 420 and positionBalle[1] < 430):

		deplacementBalle[1] *= -1 #On renvoie la balle vers le haut

		#On choisi l inclinaison de la balle selon ou elle touche la raquette
		if ((positionRaquette[0] <= positionBalle[0] and positionBalle[0] <= positionRaquette[0]+10) or 
			(positionRaquette[0]+70 <= positionBalle[0] and positionBalle[0] <= positionRaquette[0]+80)):

			deplacementBalle = [0.8,0.2]
		elif ((positionRaquette[0]+10 < positionBalle[0] and positionBalle[0] <= positionRaquette[0]+20) or 
			(positionRaquette[0]+60 <= positionBalle[0] and positionBalle[0] < positionRaquette[0]+70)):

			deplacementBalle = [0.6,0.4]
		elif ((positionRaquette[0]+20 < positionBalle[0] and positionBalle[0] <= positionRaquette[0]+30) or 
			(positionRaquette[0]+50 <= positionBalle[0] and positionBalle[0] < positionRaquette[0]+60)):
			
			deplacementBalle = [0.4,0.6]

		else:
			deplacementBalle = [0.2,0.8]

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
		if deplace == 'Right' and positionRaquette[2] < 300:

			positionRaquette[0] += 10
			positionRaquette[2] += 10
			
		if deplace == 'Left' and positionRaquette[0] > 0:
			
			positionRaquette[0] -= 10
			positionRaquette[2] -= 10

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
	
	if positionRaquette[0] < -3:
		positionRaquette = (-3, positionRaquette[1],
			 77, positionRaquette[3])
	
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
	Sinon la balle est repositionner"""
	if positionBalle[1] > 453:
		vie -= 1
		positionBalle = [150, 400]
		return (vie, positionBalle)
	return None


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
				briqueTester += 1
				continue
			else:
				if brique[briqueTester] == 1:
					#image(j,i,'brique1.gif',
						#ancrage='nw',
							#tag= 't')
					rectangle(j, i, j+40, i+15,
						couleur='black', remplissage='yellow', epaisseur=1, tag='t')
				elif brique[briqueTester] == 2:
					#image(j,i,'brique2.gif',
						#ancrage='nw',
							#tag= 't')
					rectangle(j, i, j+40, i+15,
						couleur='black', remplissage='orange', epaisseur=1, tag='t')
				else:
					#image(j,i,'brique3.gif',
						#ancrage='nw',
							#tag= 't')
					rectangle(j, i, j+40, i+15,
						couleur='black', remplissage='red', epaisseur=1, tag='t')

			briqueTester += 1

def collision_brique(brique,positionBalle, score):
	"""Permet de gérer la collision entre la balle et les briques"""
	briqueTester = 0 #Parametre de la premiere brique
	for i in range(10,150,15):
		for j in range(10,280,40):
			if brique[briqueTester] <= 0:
				briqueTester += 1
				continue
			else:
				if (positionBalle[1] > i+3 and positionBalle[1] < i+12) and (positionBalle[0] > j and positionBalle[0] < j+10): # gauche 
					deplacementBalle[0] *= -1
					brique[briqueTester] -= 1
					if not brique[briqueTester]: #Si on viens de detruire une brique
						score += 10
					efface('t')
					afficher_brique(brique)
					creation_interface(score, vie)
					mise_a_jour()
					
					
				if (positionBalle[1] > i+3 and positionBalle[1] < i+12) and (positionBalle[0] < j+40 and positionBalle[0] > j+30): # droite
					deplacementBalle[0] *= -1
					brique[briqueTester] -= 1
					if not brique[briqueTester]: #Si on viens de detruire une brique
						score += 10
					efface('t')
					afficher_brique(brique)
					creation_interface(score, vie)
					mise_a_jour()
					
				if (positionBalle[0] > j and positionBalle[0] < j+40) and (positionBalle[1] > i+12 and positionBalle[1] < i+15): # bas
					if deplacementBalle[1] > 0: # si la balle monte 
						deplacementBalle[1] *= -1
						brique[briqueTester] -= 1
						if not brique[briqueTester]: #Si on viens de detruire une brique
							score += 10
						efface('t')
						afficher_brique(brique)
						creation_interface(score, vie)
						mise_a_jour()
					else: # autrement c'est qu'elle descend, donc elle ne doit pas inverser son Y mais son X
						deplacementBalle[0] *= -1
						brique[briqueTester] -= 1
						if not brique[briqueTester]: #Si on viens de detruire une brique
							score += 10
						efface('t')
						afficher_brique(brique)
						creation_interface(score, vie)
						mise_a_jour()
				
				if (positionBalle[0] > j and positionBalle[0] < j+40) and (positionBalle[1] < i+3 and positionBalle[1] > i): # haut 
					if deplacementBalle[1] < 0: #si la balle descend
						deplacementBalle[1] *= -1
						brique[briqueTester] -= 1
						if not brique[briqueTester]: #Si on viens de detruire une brique
							score += 10
						efface('t')
						afficher_brique(brique)
						creation_interface(score, vie)
						mise_a_jour()
					else: #autrement c'est qu'elle monte, donc elle ne doit pas inverser son Y mais son X
						deplacementBalle[0] *= -1
						brique[briqueTester] -= 1
						if not brique[briqueTester]: #Si on viens de detruire une brique
							score += 10
						efface('t')
						afficher_brique(brique)
						creation_interface(score, vie)
						mise_a_jour()															
			briqueTester += 1
	return score

	
	
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
	fin = False
	a = 0

	#Definition de variable pour l interface
	score = 0
	vie = 3
	minute = 0
	
	cree_fenetre(largeur, hauteur)
	ligne(300,0,300,450, epaisseur="2", tag='ligne')
	texte(320,15, "Relobrik", taille=14, tag='nom')
	creation_interface(score, vie)
	
		
	#Vitesse de deplacement de la balle a modifier selon la machine
	if "auto" in argv: #On augmente la vitesse du jeu si on est en mode auto (debogage)
		rafraichissement = 0.00005
	else:
		rafraichissement = 0.00005

	raquette = rectangle(positionRaquette[0], positionRaquette[1], 
		positionRaquette[2], positionRaquette[3],
		couleur='black', remplissage='', epaisseur=1,)

	#Position de depart de la balle
	positionBalle = [150, 400]
	balle = cercle(positionBalle[0], positionBalle[1], 4, remplissage="black")
	brique = creation_brique()
	afficher_brique(brique)
	attente_touche()
	temps = (minute, time())
	temps = timer(temps[0], temps[1])


	while (vie > 0 and fin == False): #A modifier lorqu il y aura plusieur vie et casser toute les briques!

		if "auto" in argv: #Si on a choisi le mode auto
			raquette = mode_auto(raquette)
		else:
			raquette = animation_raquette(raquette)
		efface(balle)
		balle = animation_balle(balle)
		collision(positionBalle)
		
		
		score = collision_brique(brique,positionBalle, score)
		#creation_interface(score, vie)
		reset = fin_jeu(vie, positionBalle)
		if reset: #Si le joueur a perdu une vie
			vie = reset[0]
			if vie == 0:
				break
			positionBalle = reset[1]
			positionRaquette = [110, 420, 190, 430]
			texte(30, 225, '   Appuyez sur une \ntouche pour continuer', couleur='red',
				ancrage='nw', police="Purisa", taille=20, tag='texteC')
			attente_touche()
			efface('texteC')
		sleep(rafraichissement)
		fin = verification_brique(brique)
		#temps = timer(temps[0], temps[1])
		if a%100 == 0:
			temps = timer(temps[0], temps[1])
			a = 0
		a += 1

	efface(balle)
	efface(raquette)
	if vie == 0:
		texte(30, 225, 'Vous avez perdu', couleur='red',
			ancrage='nw', police="Purisa", taille=24)
	
	else: #Le joueur a gagner
		texte(30, 225, 'Vous avez gagné', couleur='red',
			ancrage='nw', police="Purisa", taille=24)
		#On calcule son score final
		tempsATM = int(time()-temps[1])
		tempsSeconde = temps[0]*60 + tempsATM
		score += int((1500/(0.25*tempsSeconde)) + 100*vie)
		creation_interface(score, vie)
		print(score)

	sleep(rafraichissement)
	attente_touche()
	ferme_fenetre()