from random import choice
import tkinter
from tkinter import *
from tkinter import Button, Tk

#clean the frame
def DestroyFrame():
    for widget in app.winfo_children():
       widget.destroy()

    app.pack_forget

#Back button function
def Back():
    DestroyFrame()
    menu()

#insert Back Button
def BackButton():
    backButton = Button(app , text = "Menu" , command = Back)
    # backButton['bg'] = "#FF9AA2"
    backButton.pack()

#game menu
def menu():
    start = Button(app , text = "start" , command = playGame)
    start.pack()

    size = Button(app , text = "Game table size" , command = gameTableSize)
    size.pack()

    icon = Button(app , text = "icon" , command = playerIcon)
    icon.pack()
    
    about = Button(app , text = "about" , command = aboutUs)
    about.pack()

def playGame():
    DestroyFrame()
    print("yoho you start the game")
    BackButton()

def gameTableSize():
    DestroyFrame()
    print("3x3 \n4x4 \n5x5")
    BackButton()

def playerIcon():
    DestroyFrame()
    XO1 = Button(app , text = "X / O" , command = lambda choice = "X/O" : setIcon(choice))
    XO1.pack()
    XO2 = Button(app , text = "* / #" , command = lambda choice = "*/#" : setIcon(choice))
    XO2.pack()
    XO3 = Button(app , text = "! / ?" , command = lambda choice = "!/?" : setIcon(choice))
    XO3.pack()
    BackButton()

def setIcon(choice):
    global player1 , player2
    if choice == "X/O":
        player1 = "X"
        player2 = "O"
    elif choice == "*/#":
        player1 = "*"
        player2 = "#"
    elif choice == "!/?":
        player1 = "!"
        player2 = "?"

def aboutUs():
    DestroyFrame()
    text = Text(app)
    text.insert(INSERT ,"Foroogh L \ninstagram: python._.group")
    text.pack()
    BackButton()

main = Tk()
main.title("Tic Tac Toe")
main.geometry("400x480")
main.resizable(width = False, height = False)

app = Frame(main)
app.pack()

player1 = "X"
player2 = "Y"

menu()
main.mainloop()
