from tkinter import *
from tkinter import messagebox
from random  import choice ,randint, shuffle
import pyperclip# module to copy or paste from clipboard
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    #Password Generator day 5
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)#copies to clipboard
  

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or  len(password) == 0 :
        messagebox.showerror(title="Empty Field",message="Please make sure you haven't left any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"This are the details entered: \nwebsite: {website}\nusername/Mail: {username}\nPassword: {password}\nIs it ok to save!")
        
        if is_ok:
            with open("data.text",mode='a') as file:
                file.write(f"\n{website} || {username} || {password}")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
        messagebox.showinfo(title="Info saved", message="Details Saved Sucessfully!")
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image= logo_image)
canvas.grid(row=0,column=1)

# Lables
website_label = Label(text="Website")
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username")
email_label.grid(row=2,column=0)

passwoard_label = Label(text="Password")
passwoard_label.grid(row=3,column=0)


# Text area
website_entry = Entry(width=52)
website_entry.grid(row=1,column=1, columnspan=2,pady=5)
website_entry.focus()

username_entry = Entry(width=52)
username_entry.grid(row=2,column=1, columnspan=2,pady=5)
username_entry.insert(0,"xyz@gmail.com" )

password_entry = Entry(width=33)
password_entry.grid(row=3,column=1,pady=5)


#Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3,column=2,pady=5)

add_button = Button(text="Add",width=44,command=save)
add_button.grid(row=4,column=1,columnspan=2,pady=5)

window.mainloop()