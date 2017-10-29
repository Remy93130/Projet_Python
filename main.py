from upemtk import *
from time import *


def creation_fenetre():
	"""
	Cree la fenetre du jeu
	"""
	hauteur = 450
	largeur = 300
	cree_fenetre(largeur, hauteur)


def animation_balle(balle):
	"""
	Permet de deplacer la balle
	"""
	global positionBalle
	efface(balle)
	positionBalle = (positionBalle[0]+ deplacementX, positionBalle[1] - deplacementY)
	balle = cercle(positionBalle[0], positionBalle[1], 4, remplissage="black")
	mise_a_jour()
	return(balle)


def collision(positionBalle):
	"""
	Permet de verifier si la balle entre en contact avec un element
	"""
	global deplacementX, deplacementY
	global positionRaquette

	#On verifie si elle touche le haut de la fenetre
	if (positionBalle[1] <= 0):
		deplacementY *= -1 #On inverse le deplacement verticale de la balle

	#On verifie si elle touche un cote de la fenetre
	if (positionBalle[0] <= 0 or positionBalle[0] >= 300):
		deplacementX *= -1 #On inverse le deplacement honrizontale de la balle

	#On verifie si elle touche la raquette:
	if (positionBalle[0] >= positionRaquette[0] and positionBalle[0] <= positionRaquette[2]) and (positionBalle[1] == 420):
		deplacementY *= -1 #On renvoie la balle vers le haut

		#On choisi l inclinaison de la balle selon ou elle touche la raquette
		if ((positionRaquette[0] <= positionBalle[0] and positionBalle[0] <= positionRaquette[0]+16) or 
			(positionRaquette[0]+64 <= positionBalle[0] and positionBalle[0] <= positionRaquette[0]+80)):

			deplacementX = 8
			deplacementY = 2
		elif ((positionRaquette[0]+16 <= positionBalle[0] and positionBalle[0] <= positionRaquette[0]+32) or 
			(positionRaquette[0]+48 <= positionBalle[0] and positionBalle[0] <= positionRaquette[0]+64)):

			deplacementX = 6
			deplacementY = 4
		elif (positionRaquette[0]+32 <= positionBalle[0] and positionBalle[0] <= positionRaquette[0]+48):
			deplacementX = 0
			deplacementY = 10
		#Verifie si la balle doit changer de direction selon le positionnement
		#De la raquette
		if (positionBalle[0] < ((positionRaquette[0]+positionRaquette[2])/2) and deplacementX > 0):
			deplacementX *= -1
		if (positionBalle[0] > ((positionRaquette[0]+positionRaquette[2])/2) and deplacementX < 0):
			deplacementX *= -1



def animation_raquette(raquette):
	"""
	Permet de deplacer la raquette
	"""
	global positionRaquette
	efface(raquette)
	appuie = donne_evenement()
	type_appuie = type_evenement(appuie)
	if type_appuie == "Touche":
		deplace = touche(appuie)
		if deplace == 'Right' and positionRaquette[2] < 300:

			positionRaquette = (positionRaquette[0]+20, positionRaquette[1],
			 positionRaquette[2]+20, positionRaquette[3])
			
		if deplace == 'Left' and positionRaquette[0] > 0:
			
			positionRaquette = (positionRaquette[0]-20, positionRaquette[1],
			 positionRaquette[2]-20, positionRaquette[3])
			
	raquette = rectangle(positionRaquette[0], positionRaquette[1], 
		positionRaquette[2], positionRaquette[3],
		couleur='black', remplissage='blue', epaisseur=1,)
	mise_a_jour()
	return raquette 


def fin_jeu(vie):
	"""
	Permet de verifier si la balle n est pas renvoyer
	fonction incomplete creer pour une update futur
	"""
	if positionBalle[1] > 453:
		vie -= 1
	return(vie)


def creation_brique():
	"""
	creer les briques qui devront etre detruite
	"""
	brique = [
	1,2,2,2,2,2,1,
	1,1,1,1,1,1,1,
	1,1,1,1,1,1,1,
	1,1,1,1,1,1,1,
	1,1,1,1,1,1,1,
	1,1,1,1,1,1,1,
	1,1,1,1,1,1,1,
	1,1,1,1,1,1,1,
	1,1,1,1,1,1,1,
	1,1,1,1,1,1,1
	]


def afficher_brique(brique):
	"""
	Permet d'afficher les briques dans la fenetre
	"""
	for element in brique:
		#On verifie si il y a une brique
		if element != 0:
			#On verifie la durabilite de la brique et donc sa couleur
			if element == 1:
				couleur = 'green'
			elif element == 2:
				couleur = 'yellow'
			else:
				couleur = 'red'
			#On obtient la position des briques
			



if __name__ == '__main__':
	

	creation_fenetre()

	#Vitesse de deplacement de la balle
	deplacementX = 0
	deplacementY = 10
	rafraichissement = 0.035 #(a modifier selon la machine)

	#Position de depart de la raquette
	positionRaquette = (110, 420, 190, 430)
	raquette = rectangle(positionRaquette[0], positionRaquette[1], 
		positionRaquette[2], positionRaquette[3],
		couleur='black', remplissage='', epaisseur=1,)

	#Position de depart de la balle
	positionBalle = (150, 400)
	balle = cercle(positionBalle[0], positionBalle[1], 4, remplissage="black")
	vie = 1
	attente_touche()

	while (vie > 0): #A modifier lorqu il y aura plusieur vie !

		raquette = animation_raquette(raquette)
		balle = animation_balle(balle)
		collision(positionBalle)
		vie = fin_jeu(vie)
		sleep(rafraichissement)
	

	texte(30, 225, 'Vous avez perdu', couleur='red',
		ancrage='nw', police="Purisa", taille=24)
	attente_touche()
	ferme_fenetre()