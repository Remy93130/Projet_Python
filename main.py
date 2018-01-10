#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fonctions du menu principale du casse brique."""
# Imports --------------------------------------------------------------------------------------------------------
from upemtk import *
import sys
import jeu

# Fonctions ------------------------------------------------------------------------------------------------------
def interface_start():
	"""Creation de l interface de depart"""
	cree_fenetre(450, 450)
	texte(225, 35, "Bienvenue sur Relobrik\n Choisissez un mode", ancrage='center')
	rectangle(10, 100, 440, 250, couleur='red', remplissage='red')
	texte(225, 175, "Mode challenge", ancrage='center', taille=18)
	rectangle(10, 270, 440, 420, couleur='blue', remplissage='blue')
	texte(225, 345, "Mode personnalisé", ancrage='center', taille=18)

def lecture():
	brique = list()
	fichier = open("brique_perso.txt", 'r')
	for ligne in fichier.readlines():
		if ligne[0] == '#':
			continue
		else:
			briqueL = ligne.strip()[0:7]
			for element in ligne.strip():
				brique.append(int(element))
	fichier.close()

	if len(brique) != 7*10:
		print("Il y a un probleme avec le niveau personnalisé")
		sys.exit(0)
	return brique
	

if __name__ == '__main__':
	
	interface_start()
	while 1:
		x = attente_clic()
		if 10 < x[0] < 440:
			if 100 <= x[1] <= 250:
				ferme_fenetre()
				jeu.lancement([False, None])
				break
			if 270 <= x[1] <= 420:
				ferme_fenetre()
				jeu.lancement([True, lecture()])
				break