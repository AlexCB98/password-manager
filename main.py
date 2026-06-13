from tkinter import *

FONT = ('Calibre', 20)

def generate_password():
    pass

def add():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open("my_accounts.txt", 'a') as my_accounts:
        my_accounts.write(f'-> {website} |-| {email} |-| {password}\n')

    website_entry.delete(0, END)
    password_entry.delete(0, END)



window = Tk()
window.title('Password Manager')
window.config(padx= 100, pady= 50, bg= '#C0E1D2')

canvas = Canvas(width= 400, height= 400, highlightthickness= 0, bg= '#C0E1D2')

logo_img = PhotoImage(file='logo.png')
logo_img = logo_img.subsample(4,4)
canvas.create_image(200, 200, image= logo_img)
canvas.grid(row=0, column=0, columnspan=3)

website_label = Label(text='Website:', bg='#C0E1D2', font= FONT)
website_label.grid(row=1, column=0, sticky="w")

website_entry = Entry(width= 50)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew", ipady=5)

email_label = Label(text='Email / Username:', bg= '#C0E1D2', font= FONT)
email_label.grid(row=2, column=0, sticky="w")

email_entry = Entry(width= 50)
email_entry.insert(0, 'example_email@example.com')
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew", ipady=5)

password_label = Label(text= 'Password:', bg= '#C0E1D2', font= FONT)
password_label.grid(row=3, column=0, sticky="w")

password_entry = Entry(width= 25)
password_entry.grid(row=3, column=1, sticky="ew", ipady=5)

generate_password_button = Button(text= 'Generate Password', command=generate_password, bg= '#DBE4C9')
generate_password_button.config(padx=1, pady=0)
generate_password_button.grid(row=3, column=2, padx=(6, 0))

add_button = Button(text= 'Add', command= add, width= 42, bg= '#DBE4C9')
add_button.config(padx= 2, pady= 2)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
