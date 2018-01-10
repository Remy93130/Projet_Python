#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fonctions pour gerer les scores."""
# Imports --------------------------------------------------------------------------------------------------------
from upemtk import *

ENTREE = "meilleur_score"

# Fonctions ------------------------------------------------------------------------------------------------------
def lecture_score():
	"""Récupere les score dans le fichier score, les trie et les renvoie"""
	fichier = open(ENTREE, 'r')
	score = list()
	for ligne in fichier.readlines():
		ligne = ligne.strip()
		score.append(ligne.split(':'))
	fichier.close()

	for element in score:
		element[0] = int(element[0])
	score = sorted(score, key=lambda x: x[0], reverse=True)
	return score

def affichage_score(score):
	"""Affiche les meilleur score sur le panneau de jeu"""
	decal = 180
	texte(320, 150, "Meilleur Score", taille=14)
	for element in score:
		texte(320, decal, element[1] + ' ' + str(element[0]), taille=10)
		decal += 15

def meilleur_score(Nscore, highscore):
	"""Demande le nom du joueur et inscrit son score dans le fichier"""
	print("Félicitation c'est un nouveau record")
	nom = input("Entrez votre nom : ")
	nom = nom[0:3]
	print("Bravo {} vous avez fait un score de {}. Il a bien ete enregistre !".format(nom, Nscore))
	highscore.append([Nscore, nom])
	highscore = sorted(highscore, key=lambda x: x[0], reverse=True)
	fichier = open(ENTREE, 'w')
	for i in range(10):
		fichier.write("{}:{}\n".format(highscore[i][0], highscore[i][1]))