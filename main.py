from tkinter import *

window = Tk()
window.title('Password Manager')
window.config(padx= 20, pady= 20, bg= '#C0E1D2')

canvas = Canvas(width= 600, height= 600, highlightthickness= 0, bg= '#C0E1D2')

logo_img = PhotoImage(file='logo.png')
logo_img = logo_img.subsample(3,3)
canvas.create_image(300, 300, image= logo_img)

canvas.pack()

window.mainloop()
