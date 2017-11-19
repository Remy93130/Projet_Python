from time import sleep
from upemtk import *

if __name__ == '__main__':
	
	cree_fenetre(400, 400)
	attente_clic()

	while True:

		ligne(10,10,50,50)
		appuie = donne_evenement()
		type_appuie = type_evenement(appuie)
		print(appuie)
		print(type_appuie)
		print()
		sleep(1)
		efface_tout()
