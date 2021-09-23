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
    backButton = Button(app , text = "Back" , command = Back)
    # backButton['bg'] = "#FF9AA2"
    backButton.pack()
    backButton.place(x = 5 , y = 450)

#game menu
def menu():
    start = Button(app , text = "start" , command = playGame)
    start.pack()

    icon = Button(app , text = "icon" , command = playerIcon)
    icon.pack()
    
    about = Button(app , text = "about" , command = aboutUs)
    about.pack()

def playGame():
    global XOButton1 , XOButton2 , XOButton3 
    global XOButton4 , XOButton5 , XOButton6 
    global XOButton7 , XOButton8 , XOButton9
    DestroyFrame()
    XOButton1 = Button(app , width = 12 , height = 5 , command = lambda choice = 1 : Game(choice))
    XOButton1.pack()
    XOButton1.place(x = 22 , y = 5)

    XOButton2 = Button(app , width = 12 , height = 5 , command = lambda choice = 2 : Game(choice))
    XOButton2.pack()
    XOButton2.place(x = 142 , y = 5)

    XOButton3 = Button(app , width = 12 , height = 5 , command = lambda choice = 3 : Game(choice))
    XOButton3.pack()
    XOButton3.place(x = 262 , y = 5)

    XOButton4 = Button(app , width = 12 , height = 5 , command = lambda choice = 4 : Game(choice))
    XOButton4.pack()
    XOButton4.place(x = 22 , y = 100)

    XOButton5 = Button(app , width = 12 , height = 5 , command = lambda choice = 5 : Game(choice))
    XOButton5.pack()
    XOButton5.place(x = 142 , y = 100)

    XOButton6 = Button(app , width = 12 , height = 5 , command = lambda choice = 6 : Game(choice))
    XOButton6.pack()
    XOButton6.place(x = 262 , y = 100)

    XOButton7 = Button(app , width = 12 , height = 5 , command = lambda choice = 7 : Game(choice))
    XOButton7.pack()
    XOButton7.place(x = 22 , y = 195)

    XOButton8 = Button(app , width = 12 , height = 5 , command = lambda choice = 8 : Game(choice))
    XOButton8.pack()
    XOButton8.place(x = 142 , y = 195)

    XOButton9 = Button(app , width = 12 , height = 5 , command = lambda choice = 9 : Game(choice)) 
    XOButton9.pack()
    XOButton9.place(x = 262 , y = 195)

    BackButton()

def Game(choice):
    global XOButton1 , XOButton2 , XOButton3 
    global XOButton4 , XOButton5 , XOButton6 
    global XOButton7 , XOButton8 , XOButton9
    global turn

    if turn == 1 :
        Xlist.append(choice)
    elif turn == -1 :
        Olist.append(choice)
    
    if turn == 1 and choice == 1:
        XOButton1.config(text = player1)
        XOButton1['state'] = DISABLED
    elif turn == 1 and choice == 2:
        XOButton2.config(text = player1)
        XOButton2['state'] = DISABLED
    elif turn == 1 and choice == 3:
        XOButton3.config(text = player1)
        XOButton3['state'] = DISABLED 
    elif turn == 1 and choice == 4:
        XOButton4.config(text = player1)
        XOButton4['state'] = DISABLED
    elif turn == 1 and choice == 5:
        XOButton5.config(text = player1)
        XOButton5['state'] = DISABLED
    elif turn == 1 and choice == 6:
        XOButton6.config(text = player1) 
        XOButton6['state'] = DISABLED
    elif turn == 1 and choice == 7:
        XOButton7.config(text = player1) 
        XOButton7['state'] = DISABLED
    elif turn == 1 and choice == 8:
        XOButton8.config(text = player1)
        XOButton8['state'] = DISABLED
    elif turn == 1 and choice == 9:
        XOButton9.config(text = player1)
        XOButton9['state'] = DISABLED
    
    elif turn == -1 and choice == 1:
        XOButton1.config(text = player2)
        XOButton1['state'] = DISABLED
    elif turn == -1 and choice == 2:
        XOButton2.config(text = player2) 
        XOButton2['state'] = DISABLED
    elif turn == -1 and choice == 3:
        XOButton3.config(text = player2)
        XOButton3['state'] = DISABLED 
    elif turn == -1 and choice == 4:
        XOButton4.config(text = player2)
        XOButton4['state'] = DISABLED
    elif turn == -1 and choice == 5:
        XOButton5.config(text = player2)
        XOButton5['state'] = DISABLED
    elif turn == -1 and choice == 6:
        XOButton6.config(text = player2)
        XOButton6['state'] = DISABLED 
    elif turn == -1 and choice == 7:
        XOButton7.config(text = player2)
        XOButton7['state'] = DISABLED 
    elif turn == -1 and choice == 8:
        XOButton8.config(text = player2)
        XOButton8['state'] = DISABLED
    elif turn == -1 and choice == 9:
        XOButton9.config(text = player2)
        XOButton9['state'] = DISABLED
    turn *= -1
    WhoWin()

def WhoWin():
    if 1 in Xlist and 2 in Xlist and 3 in Xlist:
        print("X win")
    elif 4 in Xlist and 5 in Xlist and 6 in Xlist:
        print("X win")
    elif 7 in Xlist and 8 in Xlist and 9 in Xlist:
        print("X win")
    elif 1 in Xlist and 4 in Xlist and 7 in Xlist:
        print("X win")
    elif 2 in Xlist and 5 in Xlist and 8 in Xlist:
        print("X win")
    elif 3 in Xlist and 6 in Xlist and 9 in Xlist:
        print("X win")
    elif 1 in Xlist and 5 in Xlist and 9 in Xlist:
        print("X win")
    elif 3 in Xlist and 5 in Xlist and 7 in Xlist:
        print("X win")

    elif 1 in Olist and 2 in Olist and 3 in Olist:
        print("O win")
    elif 4 in Olist and 5 in Olist and 6 in Olist:
        print("O win")
    elif 7 in Olist and 8 in Olist and 9 in Olist:
        print("O win")
    elif 1 in Olist and 4 in Olist and 7 in Olist:
        print("O win")
    elif 2 in Olist and 5 in Olist and 8 in Olist:
        print("O win")
    elif 3 in Olist and 6 in Olist and 9 in Olist:
        print("O win")
    elif 1 in Olist and 5 in Olist and 9 in Olist:
        print("O win")
    elif 3 in Olist and 5 in Olist and 7 in Olist:
        print("O win")
        
# def gameTableSize():
#     DestroyFrame()
#     print("3x3 \n4x4 \n5x5")
#     BackButton()


# def setSize(choice):
#     global Tablesize
#     if choice == "3x3":
#         Tablesize = 3
#     elif choice == "4x4":
#         Tablesize = 4
#     elif choice == "5x5":
#         Tablesize = 5
        
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

app = Frame(main , )
app.pack()
app.place(relx = 0 , relheight = 1, relwidth = 1)
app['bg'] = "pink"

player1 = "X"
player2 = "O"
turn = 1

Xlist = list()
Olist = list()

menu()
main.mainloop()
