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
	global xBalle, yBalle, deplacementX, deplacementY
	efface(balle)
	xBalle += deplacementX
	yBalle -= deplacementY
	balle = cercle(xBalle, yBalle, 4, remplissage="black")
	mise_a_jour()
	sleep(rafraichissement)
	return(balle)


def collision(xBalle, yBalle):
	"""
	Permet de vérifier si la balle entre en contact avec un element
	"""
	global deplacementX, deplacementY
	#On verifie si elle touche le haut ou le bas de la fenetre
	if (yBalle == 450 or yBalle == 0):
		deplacementY *= -1 #On inverse le deplacement verticale de la balle
	#On verifie si elle touche un cote de la fenetre
	if (xBalle == 0 or xBalle == 300):
		deplacementX *= -1 #On inverse le deplacement honrizontale de la balle


if __name__ == '__main__':
	

	creation_fenetre()
	#Vitesse de deplacement de la balle
	deplacementX = 5
	deplacementY = 5
	rafraichissement = 0.05 #(a modifier celon la machine)

	#Position de depart de la balle
	xBalle, yBalle = 150, 400
	balle = cercle(xBalle, yBalle, 4, remplissage="black")
	attente_clic()

	while 1:
		balle = animation_balle(balle)
		collision(xBalle, yBalle)
	

	attente_clic()
	ferme_fenetre()