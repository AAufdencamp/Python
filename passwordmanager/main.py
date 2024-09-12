from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#messagebox is a module and not a class
#when we say import *, that means import everything, but it actually imports only classes and constants
# place cursor on messagebox module above -> right click  -> go to -> implementation
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    #list comprehension review
    password_letters = [random.choice(letters) for i in range(nr_letters)] #list comprehension for a range!
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)] #list comprehension for a range!
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)] #list comprehension for a range!

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list= password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list) #using list comprehension and this .join() method we shorten our code dramatically

    pwentry.insert(0,password)
    #print(f"Your password is: {password}")

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # wsentry.insert(0, "")
    # unentry.insert(0, "")
    # pwentry.insert(0, "")

    web = wsentry.get()
    user = unentry.get()
    pswd = pwentry.get()

    #messagebox.showinfo(title="Title", message="message")
    if len(web) == 0 or len(pswd) == 0:
        messagebox.showinfo(title="Oops", message= "Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {user} \nPassword:"
                                              f" {pswd} \n Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data:    #this alternative closes the file automatically
                data.write(f"{web} | {user} | {pswd} \n")
                wsentry.delete(0,END)
                #unentry.delete(0,END)
                pwentry.delete(0,END)

    # data = open("data.txt", "a") #a for append to end of file; whereas "w" overwrites existing content
    # data.write(wsentry.get() + " " + "|" )
    # data.write(unentry.get() + " " + "|" )
    # data.write(pwentry.get() + " " + "|" )
    # data.write(" \n ")
    # data.close()

    # wsentry.delete(0, 'end')
    # unentry.delete(0, 'end')
    # pwentry.delete(0, 'end')



    #data = open("data.txt", "r") #read
    #print(data.read())
#to do: take inputs from website entry, email/username entry and password entry
# to be saved into a file called data.text when the user clicks Add Button
# data.text containts website | email/username | password
#Hints: write to file documentation; tkinter entry widget insert method
#Hint: once you add the info you want the entries to be cleared out expect for email/username (hint: delete function)
# https://www.w3schools.com/python/python_file_write.asp
# https://tkdocs.com/tutorial/widgets.html#entry

# ---------------------------- UI SETUP ------------------------------- #
#https://tkdocs.com/tutorial/canvas.html

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady = 50)

canvas = Canvas(width = 200, height = 200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100,100, image = logo) #xcor, ycor position of center of image
canvas.grid( row=0,column=1 )

website = Label(text="Website:")
website.grid(row=1,column=0 )

user = Label(text="Email/Username:")
user.grid(row=2,column=0 )

password= Label(text="Password:")
password.grid(row=3,column=0)

wsentry = Entry(width=35) #width is a property of Entry class
wsentry.grid(row=1, column=1, columnspan=2 )
wsentry.focus() #upon startup will place the user cursor here

unentry = Entry(width=35)
unentry.grid(row=2,column=1, columnspan= 2 )
unentry.insert(0, "genericemail@gmail.com") #index 0 ->place email starting at 0th character of Entry()
                                                            #input as string the expected email/username as a convenience

pwentry = Entry(width=35)
pwentry.grid(row=3,column=1, columnspan=2)

genpass = Button(text="Generate Password", command= generate_password)
genpass.grid(row=3,column=3)

add = Button(text="Add", width=36, command=save)
add.grid(row=4,column=1, columnspan = 2)

window.mainloop()

#grid layout target is 5 rows x 3 columns
#note that the canvas widget itself is a component of the window object. It is not itself the window object. The canvas
#can be posisitioned using canvas.grid(column=columni, row = rowj) just like we do with labels or any other
#component we add to the window.

#use label, entry, button objects to create the UI for Password Manager:-)
# For Entry class get or change the value of the entry widget. The .get() method returns the current value,
# and the .delete() and .insert() methods associted w/ Entry class let you change the content

#Entry class allos us to mask contents using a symbol, eg passwords
#passwd = ttk.Entry(parent, textvariable=password, show="*")

#Standard Dialogs, ie popups dialog boxes generated by tkinter. e.g. message box module

#Python string join() method used to join elemnts in lists, tuples, or dictionries by a selected string, eg an empty
# string like ''

#Ability to put strings to the clip board in the case of a generated password so we can save it for personal reference
#Use pyperclip. Allow copy and paste to clipboard
# import pyperclip
# pyperclip.copy('The text to be copied to clipboard.')
# pyperclip.paste()