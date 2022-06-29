import email
from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

Label(root, text="Registration Form", font="ar 20 bold").grid(row=0, column=3)

name = Label(root, text="Name")
surname = Label(root, text="Surname")
gender = Label(root, text="Gender")
phone = Label(root, text="Phone")
email = Label(root, text="E-mail")

name.grid(row=1, column=2)
surname.grid(row=2, column=2)
gender.grid(row=3, column=2)
phone.grid(row=4, column=2)
email.grid(row=5, column=2)

namevalue = StringVar
surnamevalue = StringVar
gendervalue = StringVar
phonevalue = StringVar
emailvalue = StringVar
checkvalue = IntVar

nameentry = Entry(root, textvariable=namevalue)
surnameentry = Entry(root, textvariable=surnamevalue)
genderentry = Entry(root, textvariable=gendervalue)
phoneentry = Entry(root, textvariable=phonevalue)
emailentry = Entry(root, textvariable=emailvalue)

nameentry.grid(row=1, column=3)
surnameentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
phoneentry.grid(row=4, column=3)
emailentry.grid(row=5, column=3)

checkbtn = Checkbutton(text="Remember me?", variable = checkvalue)
checkbtn.grid(row=6, column=3)

Button(text="Submit", command=getvals).grid(row=7, column=3)

root.mainloop()