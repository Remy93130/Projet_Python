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
	global xcote1, xcote2

	#On verifie si elle touche le haut de la fenetre
	if (yBalle <= 0):
		deplacementY *= -1 #On inverse le deplacement verticale de la balle

	#On verifie si elle touche un cote de la fenetre
	if (xBalle <= 0 or xBalle >= 300):
		deplacementX *= -1 #On inverse le deplacement honrizontale de la balle

	#On verifie si elle touche la raquette:
	if (xBalle >= xcote1 and xBalle <= xcote2) and (yBalle == 420):
		deplacementY *= -1 #On renvoie la balle vers le haut
		#On choisi l inclinaison de la balle selon ou elle touche la raquette
		if (xcote1 <= xBalle and xBalle <= xcote1+16):
			deplacementX = 8
			deplacementY = 2
		elif (xcote1+16 <= xBalle and xBalle <= xcote1+32):
			deplacementX = 6
			deplacementY = 4
		elif (xcote1+32 <= xBalle and xBalle <= xcote1+48):
			deplacementX = 0
			deplacementY = 10
		elif (xcote1+48 <= xBalle and xBalle <= xcote1+64):
			deplacementX = 6
			deplacementY = 4
		else:
			deplacementX = 8
			deplacementY = 2
		#Verifie si la balle doit changer de direction selon le positionnement
		#De la raquette
		if (xBalle < ((xcote1+xcote2)/2) and deplacementX > 0):
			deplacementX *= -1
		if (xBalle > ((xcote1+xcote2)/2) and deplacementX < 0):
			deplacementX *= -1



def animation_raquette(raquette):
	"""
	Permet de deplacer la raquette
	"""
	global xcote1, ycote1
	global xcote2, ycote2
	efface(raquette)
	appuie = donne_evenement()
	type_appuie = type_evenement(appuie)
	if type_appuie == "Touche":
		deplace = touche(appuie)
		if deplace == 'Right' and xcote2 < 300:
			xcote1 +=20
			xcote2 +=20
			
		if deplace == 'Left' and xcote1 > 0:
			xcote1 -=20
			xcote2 -=20
			
	raquette = rectangle(xcote1, ycote1, xcote2, ycote2,
		couleur='black', remplissage='blue', epaisseur=1)
	mise_a_jour()
	return raquette 


def fin_jeu(vie):
	"""
	Permet de verifier si la balle n est pas renvoyer
	fonction incomplete creer pour une update futur
	"""
	if yBalle > 450: #Si on a perdu a faire dans une autre fonction
		vie -= 1
	return(vie)


if __name__ == '__main__':
	

	creation_fenetre()
	#Vitesse de deplacement de la balle
	deplacementX = 0
	deplacementY = 10
	rafraichissement = 0.035 #(a modifier selon la machine)
	#Position de depart de la raquette
	xcote1, ycote1 = 110, 420
	xcote2, ycote2 = 190, 430
	raquette = rectangle(xcote1, ycote1, xcote2, ycote2,
		couleur='black', remplissage='', epaisseur=1,)
	#Position de depart de la balle
	xBalle, yBalle = 150, 400
	balle = cercle(xBalle, yBalle, 4, remplissage="black")
	vie = 1
	attente_clic()

	while (vie > 0): #A modifier lorqu il y aura plusieur vie !
		raquette = animation_raquette(raquette)
		balle = animation_balle(balle)
		collision(xBalle, yBalle)
		vie = fin_jeu(vie)
	
	texte(30, 225, 'Vous avez perdu', couleur='red',
		ancrage='nw', police="Purisa", taille=24)
	attente_clic()
	ferme_fenetre()