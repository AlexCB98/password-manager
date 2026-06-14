from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

FONT = ('Calibre', 20)

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    letters_list = [choice(letters) for _ in range(randint(4, 7))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letters_list + numbers_list + symbols_list

    shuffle(password_list)

    password = ''.join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)


def add():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title= ' Oops', message="Please make sure you haven't left any fields empty")
    else:
        try:
            with open("my_accounts.json", 'r') as my_accounts:
                accounts = json.load(my_accounts)

        except FileNotFoundError:
            with open('my_accounts.json', 'w') as my_accounts:
                json.dump(new_data, my_accounts, indent= 4)
        else:
            accounts.update(new_data)
            with open('my_accounts.json', 'w') as my_accounts:
                json.dump(accounts, my_accounts, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search_account():
    website = website_entry.get()
    try:
        with open('my_accounts.json') as my_accounts:
            accounts = json.load(my_accounts)

    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found.')

    else:
        if website in accounts:
            email = accounts[website]['email']
            password = accounts[website]['password']
            messagebox.showinfo(title= website, message=f'Email: {email}\n'
                                                            f'Password: {password}')
        else:
            messagebox.showinfo(title='Error', message=f'No details for {website} exists.')


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
website_entry.grid(row=1, column=1, sticky="ew", ipady=5)



email_label = Label(text='Email / Username:', bg= '#C0E1D2', font= FONT)
email_label.grid(row=2, column=0, sticky="w")

email_entry = Entry(width= 50)
email_entry.insert(0, 'example_email@example.com')
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew", ipady=5)



password_label = Label(text= 'Password:', bg= '#C0E1D2', font= FONT)
password_label.grid(row=3, column=0, sticky="w")

password_entry = Entry(width= 25)
password_entry.grid(row=3, column=1, sticky="ew", ipady=5)



search_button = Button(text= 'Search', command=search_account, width= 20, bg= '#DBE4C9')
search_button.config(padx=2, pady=2)
search_button.grid(row=1, column=2, padx=(6, 0))

generate_password_button = Button(text= 'Generate Password', width= 20, command=generate_password, bg= '#DBE4C9')
generate_password_button.config(padx=2, pady=2)
generate_password_button.grid(row=3, column=2, padx=(6, 0))

add_button = Button(text= 'Add', command= add, width= 42, bg= '#DBE4C9')
add_button.config(padx= 2, pady= 2)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")


window.mainloop()
