from tkinter import *
 
def deplacement():
    global dx, dy
    if (canvas.coords(balle1)[3]>400) or (canvas.coords(balle1)[1]<0):
        dy=-1*dy
    if (canvas.coords(balle1)[0]<0) or (canvas.coords(balle1)[2]>500):
        dx=-1*dx
 
    #Test de la collision avec la raquette par coordonnees:
    if (canvas.coords(balle1)[3]>canvas.coords(raquette)[1]) and (canvas.coords(balle1)[0]<canvas.coords(raquette)[2]) and (canvas.coords(balle1)[2]>canvas.coords(raquette)[0]):
        dy=-1*dy
 
    #On deplace la balle :
    canvas.move(1,dx,dy)
 
    #On repete cette fonction
    tk.after(20,deplacement)
 
#Une fonction pour le deplacement vers la droite :
def droite(event):
    canvas.move(raquette,10,0)
 
#Une fonction pour le deplacement vers la gauche :
def gauche(event):
    canvas.move(raquette,-10,0)
 
#Vitesse de deplacement de la balle:
dx=5
dy=5
 
#On cree une fenetre et un canevas:
tk = Tk()
canvas = Canvas(tk,width = 500, height = 400 , bd=0, bg="white")
canvas.pack(padx=10,pady=10)
 

#On cree une balle:
balle1 = canvas.create_oval(20,20,40,40,fill='red')
 
#On cree une raquette:
raquette = canvas.create_rectangle(200,380,300,390,fill='red')
 
#On associe les fleches du clavier aux fonctions droite() et gauche():
canvas.bind_all('<Right>', droite)
canvas.bind_all('<Left>', gauche)
 
#On lance le mouvement:
deplacement()
 
#On lance la boucle principale:
tk.mainloop()