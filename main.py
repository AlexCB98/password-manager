from tkinter import *

def generate_password():
    pass

def add():
    pass

window = Tk()
window.title('Password Manager')
window.config(padx= 20, pady= 20, bg= '#C0E1D2')

canvas = Canvas(width= 400, height= 400, highlightthickness= 0, bg= '#C0E1D2')

logo_img = PhotoImage(file='logo.png')
logo_img = logo_img.subsample(4,4)
canvas.create_image(200, 200, image= logo_img)
canvas.grid(row= 0, column= 1)

label_1 = Label(text= 'Website:', bg= '#C0E1D2')
label_1.grid(row= 1, column= 0)

entry_1 = Entry(width= 50)
entry_1.grid(row= 1, column= 1, columnspan= 2)

label_2 = Label(text=' Email / Username:', bg= '#C0E1D2')
label_2.grid(row= 2, column= 0)

entry_2 = Entry(width= 50)
entry_2.grid(row= 2, column= 1, columnspan= 2)

label_3 = Label(text= 'Password:', bg= '#C0E1D2')
label_3.grid(row= 3, column= 0, sticky="ew")

entry_3 = Entry(width= 25)
entry_3.grid(row= 3, column= 1)

button_1 = Button(text= 'Generate Password', command=generate_password, bg= '#DBE4C9')
button_1.grid(row= 3, column= 3, sticky="ew")

button_2 = Button(text= 'Add', command= add, bg= '#DBE4C9')
button_2.grid(row= 4, column= 1, columnspan= 2)

window.mainloop()
