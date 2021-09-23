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
    print("O/X \n*/# \n!/?")
    BackButton()

def aboutUs():
    DestroyFrame()
    print("Foroogh L \npython._.group")
    BackButton()

main = Tk()
main.title("Tic Tac Toe")
main.geometry("400x480")
main.resizable(width = False, height = False)

app = Frame(main)
app.pack()

menu()
main.mainloop()
