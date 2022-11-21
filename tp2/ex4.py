from tkinter import *
from tkinter import ttk
from PIL import Image

root = Tk()
root.title("cisco pas ouf tracer")
root.attributes('-fullscreen', True) 
root.configure(bg='black')

largeur = 1700
hauteur =1000
dessin=Canvas(root,bg="white",width=largeur,height=hauteur)
dessin.pack(side='left', padx=30, pady=30)

img1 = PhotoImage(file = 'ordi.png')
img2 = PhotoImage(file = 'switch.png')
img3 = PhotoImage(file = 'routeur.png')

def pose(pos):
	if pos.char== 'c':
		dessin.create_image(pos.x,pos.y,image=img1)
	if pos.char== 's':
		dessin.create_image(pos.x,pos.y,image=img2)
	if pos.char== 'r':
		dessin.create_image(pos.x,pos.y,image=img3)


btn1 = Button(root,text="FERMER", command=root.destroy)
btn1.pack(side = LEFT, fill = X)

root.bind('<KeyPress>',pose)

root.mainloop()
