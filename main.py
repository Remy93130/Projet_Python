from upemtk import *


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
	efface(balle)
	global xBalle, yBalle
	xBalle = 150
	yBalle -= 20
	balle = cercle(xBalle, yBalle, 4, remplissage="black")
	mise_a_jour()
	return(balle)


if __name__ == '__main__':
	

	creation_fenetre()
	xBalle, yBalle = 150, 400
	balle = cercle(xBalle, yBalle, 4, remplissage="black")

	attente_clic()
	balle = animation_balle(balle)
	balle = animation_balle(balle)
	balle = animation_balle(balle)
	

	attente_clic()
	ferme_fenetre()