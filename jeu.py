#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fonctions d'un jeu de Casse brique."""
# Imports --------------------------------------------------------------------------------------------------------
from upemtk import *
from time import time, sleep
from random import randint
from sys import argv
from score import *


# Variables globales ---------------------------------------------------------------------------------------------
deplacementBalle = [0,0]
deplacementBalle[0] = randint(0,8)
if deplacementBalle[0] != 0:
	deplacementBalle[0] = deplacementBalle[0] / 10
deplacementBalle[1] = 1-deplacementBalle[0]
positionRaquette = [110, 420, 190, 430]
v_vitesse = 1
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------Fonctions d'interface-----------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


def creation_interface(score, vie):
	"""Cree l interface du jeu."""
	efface('score')
	efface('vie')
	texte(320,50, "Score : " + str(score), taille=14, tag='score')
	texte(320,85, "Vie : " + str(vie), taille=14, tag='vie')


def timer(minute, tempsDebut):
	"""Permet de faire le chronometre du jeu renvoie le tuple
	avec les minutes et le temps du debut"""
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
	
	
def fin_jeu(vie, positionBalle):
	"""Permet de verifier si la balle n est pas renvoyer
	Sinon la balle est repositionner renvoie le vie et la 
	position de la balle si la balle est perdue sinon rien
	>>> fin_jeu(3, [150, 455])
	(2, [150, 400])
	>>> fin_jeu(3, [150, 150])
	"""
	if positionBalle[1] > 453:
		vie -= 1
		positionBalle = [150, 400]
		return (vie, positionBalle)
	return None
	
def pause():
	global temps
	while True:
		temps = timer(temps[0], temps[1])
		retour = donne_evenement()
		type_retour = type_evenement(retour)
		if type_retour == "Touche":
			go = touche(retour)
			if go == 'p':
				break
		mise_a_jour()
				
	
	
	
	
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------Fonctions de collision----------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


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
			
			
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------Fonctions d'animation-----------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def animation_balle(balle):
	"""Permet de deplacer la balle."""
	global positionBalle
	positionBalle = (positionBalle[0] + v_vitesse*deplacementBalle[0], positionBalle[1] - v_vitesse*deplacementBalle[1])
	balle = cercle(positionBalle[0], positionBalle[1], 4, remplissage="black")
	mise_a_jour()
	return(balle)



def animation_raquette(raquette):
	"""Permet de deplacer la raquette"""
	global positionRaquette
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
			
		if deplace =='p':
			pause()
	efface(raquette)
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


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------Fonctions des briques-----------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def creation_brique():
	"""Creer les briques qui devront etre detruites"""
	brique = [
	1, 1, 1, 1, 1, 1, 1,
	2, 2, 0, 0, 0, 2, 2,
	1, 1, 3, 3, 3, 1, 1,
	0, 2, 1, 1, 1, 2, 0,
	3, 0, 0, 2, 0, 0, 3,
	3, 3, 0, 2, 0, 3, 3,
	2, 2, 2, 2, 2, 2, 2,
	0, 0, 2, 2, 2, 0, 0,
	1, 1, 1, 1, 1, 1, 1,
	1, 1, 1, 1, 1, 1, 1,
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
						couleur='black', remplissage='yellow', epaisseur=1, tag='tbrique')
				elif brique[briqueTester] == 2:
					#image(j,i,'brique2.gif',
						#ancrage='nw',
							#tag= 't')
					rectangle(j, i, j+40, i+15,
						couleur='black', remplissage='orange', epaisseur=1, tag='tbrique')
				else:
					#image(j,i,'brique3.gif',
						#ancrage='nw',
							#tag= 't')
					rectangle(j, i, j+40, i+15,
						couleur='black', remplissage='red', epaisseur=1, tag='tbrique')
			briqueTester += 1

def collision_brique(brique, positionBalle, score, vie):
	"""Permet de gérer la collision entre la balle et les briques et calcule le score
	si une brique a ete detruite."""
	briqueTester = 0 #Parametre de la premiere brique
	for i in range(10,150,15):
		for j in range(10,280,40):
			if brique[briqueTester] <= 0:
				briqueTester += 1
				continue
			else:
				if (positionBalle[1] > i and positionBalle[1] < i+15) and (positionBalle[0] + v_vitesse*deplacementBalle[0] > j and positionBalle[0] + v_vitesse*deplacementBalle[0] < j+19.8): # gauche 
						score = effet_de_collision(briqueTester, 0, brique, score, vie)
						#print('gauche')
				if (positionBalle[1] > i and positionBalle[1] < i+15) and (positionBalle[0] + v_vitesse*deplacementBalle[0] < j+40 and positionBalle[0] + v_vitesse*deplacementBalle[0] > j+19.9): # droite
						score = effet_de_collision(briqueTester, 0, brique, score, vie)
						#print('droite')
				if (positionBalle[0] > j and positionBalle[0] < j+40) and (positionBalle[1] - v_vitesse*deplacementBalle[1] > i and positionBalle[1] - v_vitesse*deplacementBalle[1] < i+15) and deplacementBalle[1] > 0: #bas
						score = effet_de_collision(briqueTester, 1, brique, score, vie)
						#print('bas')
				if (positionBalle[0] > j and positionBalle[0] < j+40) and (positionBalle[1] - v_vitesse*deplacementBalle[1] > i and positionBalle[1] - v_vitesse*deplacementBalle[1] < i+15) and deplacementBalle[1] < 0:#haut 
						score = effet_de_collision(briqueTester, 1, brique, score, vie)
						#print('haut')

			briqueTester += 1
	return score

def effet_de_collision(numbrique, axe, brique, score, vie):
	"""Fonction complémentaire de collision_brique,permet l'actualisation d'une brique touchée
	ainsi que l'inversement du deplacement de la balle."""
	deplacementBalle[axe] *= -1
	brique[numbrique] -= 1
	if not brique[numbrique]: #Si on viens de detruire une brique
		score += 10
	efface('tbrique')
	afficher_brique(brique)
	creation_interface(score, vie)
	mise_a_jour()
	return score
	
def verification_brique(brique):
	"""Verifie si toutes les briques ont ete detruite
	renvoie True si oui sinon False
	>>> verification_brique([0,0,0,0])
	True
	>>> verification_brique([0,1,0,0])
	False
	"""
	for element in brique:
		if element > 0:
			return False
	return True
	
	
	
def lancement(modePerso):
	"""Fonction principale pour lancer le jeu
	"""
	global positionRaquette, positionBalle

	hauteur = 450
	largeur = 450
	fin = False
	a = 0 #Rafraichissement du jeu
	b = 0 #Rafraichissement du timer

	#Definition de variable pour l interface
	score = 0
	vie = 3

	if "jeveuxdesvies" in argv: #Petit easter egg
		vie = 99
	if 'aezakmi' in argv:
			fin = True

	#Vitesse du jeu a modifier selon la machine
	if "auto" in argv: #On augmente la vitesse du jeu si on est en mode auto (debogage)
		rafraichissement = 100
		v_vitesse = 3
	else:	
		rafraichissement = 5000
		
	cree_fenetre(largeur, hauteur)
	ligne(300,0,300,450, epaisseur="2", tag='ligne')
	texte(320,15, "Relobrik", taille=14, tag='nom')
	creation_interface(score, vie)

	if not modePerso[0]:
		highscore = lecture_score()
		affichage_score(highscore)
		

	
	#----------Position initiale de la raquette----------#
	raquette = rectangle(positionRaquette[0], positionRaquette[1], 
		positionRaquette[2], positionRaquette[3],
		couleur='black', remplissage='', epaisseur=1,)

	
	#----------Position de départ de la balle-------------#
	positionBalle = [150, 400]
	balle = cercle(positionBalle[0], positionBalle[1], 4, remplissage="black")
	
	#----------Affichage initiale des briques-------------#
	if not modePerso[0]:
		brique = creation_brique()
	else:
		brique = modePerso[1]
	afficher_brique(brique)
	
	#-----------Jeu en attente du joueur------------------#
	texte(30, 225, '   Appuyez sur une \ntouche pour commencer', couleur='red',
				ancrage='nw', police="Purisa", taille=10, tag='commence')
	attente_touche()
	efface('commence')
	
	#----------affichage initiale du chronometre----------#
	temps = timer(0, time())


	while (vie > 0 and fin == False): #Corps du programmes

		
		if a%rafraichissement == 0:
			if "auto" in argv: #Si on a choisi le mode auto en parametre
				raquette = mode_auto(raquette)
			else:
				raquette = animation_raquette(raquette)
			efface(balle)
			balle = animation_balle(balle)
			collision(positionBalle)
					
			score = collision_brique(brique, positionBalle, score, vie)
			reset = fin_jeu(vie, positionBalle)
			

			#On verifie si le joueur perd une vie et on remet la balle en place si c est le cas
			if reset:
				vie = reset[0]
				if vie == 0:
					break
				positionBalle = reset[1]
				positionRaquette = [110, 420, 190, 430]
				creation_interface(score, vie)
				deplacementBalle[1] *= -1
				texte(30, 225, '   Appuyez sur une \ntouche pour continuer', couleur='red',
					ancrage='nw', police="Purisa", taille=20, tag='texteC')
				attente_touche()
				efface('texteC')


			fin = verification_brique(brique)
			temps = timer(temps[0], temps[1])
			if b%100== 0:
				temps = timer(temps[0], temps[1])
				b = 0
			b += 1
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
		score += int((1500/(0.25*tempsSeconde+1)) + 100*vie)
		creation_interface(score, vie)
		sleep(1)
		if not modePerso[0] and score > highscore[-1][0]: #Verification meilleur score
			meilleur_score(score, highscore)

	attente_touche()
	ferme_fenetre()