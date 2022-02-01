from random import choice
import tkinter
from tkinter import *
from tkinter import Button, Tk

#clean the frame
def DestroyFrame():
    for widget in app.winfo_children():
       widget.destroy()

    app.pack_forget

#diable all button
def ButtDis():
    global XOButton1 , XOButton2 , XOButton3 
    global XOButton4 , XOButton5 , XOButton6 
    global XOButton7 , XOButton8 , XOButton9
    XOButton1['state'] = DISABLED
    XOButton2['state'] = DISABLED
    XOButton3['state'] = DISABLED
    XOButton4['state'] = DISABLED
    XOButton5['state'] = DISABLED
    XOButton6['state'] = DISABLED
    XOButton7['state'] = DISABLED
    XOButton8['state'] = DISABLED
    XOButton9['state'] = DISABLED

#Back button function
def Back():
    DestroyFrame()
    menu()

def PlayAgainButt():
    againButton = Button(app , text = "Play again" , command = playGame)
    againButton['bg'] = "#ECE7EB"
    againButton.pack()
    againButton.place(x = 310 , y = 450)

#insert Back Button
def BackButton():
    backButton = Button(app , text = "Back" , command = Back)
    backButton['bg'] = "#ECE7EB"
    backButton.pack()
    backButton.place(x = 5 , y = 450)

#game menu
def menu():
    start = Button(app , text = "start" , width = 30 , font = "arial" , command = playGame)
    start.pack()
    start['bg'] = "#ECE7EB"
    start.place(x = 20 , y = 140)

    icon = Button(app , text = "icon" , width = 30 , font = "arial" , command = playerIcon)
    icon.pack()
    icon['bg'] = "#ECE7EB"
    icon.place(x = 20 , y = 185)

    about = Button(app , text = "about" , width = 30 , font = "arial" , command = aboutUs)
    about.pack()
    about['bg'] = "#ECE7EB"
    about.place(x = 20 , y = 230)

def playGame():
    global XOButton1 , XOButton2 , XOButton3 
    global XOButton4 , XOButton5 , XOButton6 
    global XOButton7 , XOButton8 , XOButton9
    global Xlist , Olist
    
    Xlist = []
    Olist = []
    
    DestroyFrame()
    
    XOButton1 = Button(app , width = 12 , height = 5 , command = lambda choice = 1 : Game(choice))
    XOButton1.pack()
    XOButton1.place(x = 22 , y = 30)
    XOButton1['bg'] = "#E8EAEE"

    XOButton2 = Button(app , width = 12 , height = 5 , command = lambda choice = 2 : Game(choice))
    XOButton2.pack()
    XOButton2.place(x = 142 , y = 30)
    XOButton2['bg'] = "#E8EAEE"

    XOButton3 = Button(app , width = 12 , height = 5 , command = lambda choice = 3 : Game(choice))
    XOButton3.pack()
    XOButton3.place(x = 262 , y = 30)
    XOButton3['bg'] = "#E8EAEE"

    XOButton4 = Button(app , width = 12 , height = 5 , command = lambda choice = 4 : Game(choice))
    XOButton4.pack()
    XOButton4.place(x = 22 , y = 130)
    XOButton4['bg'] = "#E8EAEE"

    XOButton5 = Button(app , width = 12 , height = 5 , command = lambda choice = 5 : Game(choice))
    XOButton5.pack()
    XOButton5.place(x = 142 , y = 130)
    XOButton5['bg'] = "#E8EAEE"

    XOButton6 = Button(app , width = 12 , height = 5 , command = lambda choice = 6 : Game(choice))
    XOButton6.pack()
    XOButton6.place(x = 262 , y = 130)
    XOButton6['bg'] = "#E8EAEE"

    XOButton7 = Button(app , width = 12 , height = 5 , command = lambda choice = 7 : Game(choice))
    XOButton7.pack()
    XOButton7.place(x = 22 , y = 230)
    XOButton7['bg'] = "#E8EAEE"

    XOButton8 = Button(app , width = 12 , height = 5 , command = lambda choice = 8 : Game(choice))
    XOButton8.pack()
    XOButton8.place(x = 142 , y = 230)
    XOButton8['bg'] = "#E8EAEE"

    XOButton9 = Button(app , width = 12 , height = 5 , command = lambda choice = 9 : Game(choice)) 
    XOButton9.pack()
    XOButton9.place(x = 262 , y = 230)
    XOButton9['bg'] = "#E8EAEE"
    
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
        win(player1)
    elif 4 in Xlist and 5 in Xlist and 6 in Xlist:
        win(player1)
    elif 7 in Xlist and 8 in Xlist and 9 in Xlist:
        win(player1)
    elif 1 in Xlist and 4 in Xlist and 7 in Xlist:
        win(player1)
    elif 2 in Xlist and 5 in Xlist and 8 in Xlist:
        win(player1)
    elif 3 in Xlist and 6 in Xlist and 9 in Xlist:
        win(player1)
    elif 1 in Xlist and 5 in Xlist and 9 in Xlist:
        win(player1)
    elif 3 in Xlist and 5 in Xlist and 7 in Xlist:
        win(player1)

    elif 1 in Olist and 2 in Olist and 3 in Olist:
        win(player2)
    elif 4 in Olist and 5 in Olist and 6 in Olist:
        win(player2)
    elif 7 in Olist and 8 in Olist and 9 in Olist:
        win(player2)
    elif 1 in Olist and 4 in Olist and 7 in Olist:
        win(player2)
    elif 2 in Olist and 5 in Olist and 8 in Olist:
        win(player2)
    elif 3 in Olist and 6 in Olist and 9 in Olist:
        win(player2)
    elif 1 in Olist and 5 in Olist and 9 in Olist:
        win(player2)
    elif 3 in Olist and 5 in Olist and 7 in Olist:
        win(player2)

    elif len(Olist) == 4 and len(Xlist) == 5 :
        win("No one")
    elif len(Olist) == 5 and len(Xlist) == 4 :
        win("No one")

def win(winner):
    ButtDis()
    PlayAgainButt()
    str = winner + " win"
    result = Label(app , text = str , font = ("arial" , 20) )
    result.pack()
    result['bg'] = "#CDD2DE"
    if winner == "No one":
        result.place(x = 120 , y = 370)
    else:
        result.place(x = 150 , y = 370)
  
def playerIcon():
    DestroyFrame()
    XO1 = Button(app , text = "X / O" , width = 20 , font = "arial" , command = lambda choice = "X/O" : setIcon(choice))
    XO1.pack()
    XO1['bg'] = "#ECE7EB"
    XO1.place(x = 100 , y = 140)

    XO2 = Button(app , text = "* / #" , width = 20 , font = "arial" , command = lambda choice = "*/#" : setIcon(choice))
    XO2.pack()
    XO2['bg'] = "#ECE7EB"
    XO2.place(x = 100 , y = 185)

    XO3 = Button(app , text = "! / ?" , width = 20 , font = "arial" , command = lambda choice = "!/?" : setIcon(choice))
    XO3.pack()
    XO3['bg'] = "#ECE7EB"
    XO3.place(x = 100 , y = 230)

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
    text = Label(app , text = "Foroogh L \n\ninstagram: python._.group" , font = "arial")
    text.pack()
    text.place(x = 100 , y = 185)
    text['bg'] = "#CDD2DE"
    BackButton()

main = Tk()
main.title("Tic Tac Toe")
main.geometry("380x480")
main.resizable(width = False, height = False)

app = Frame(main , )
app.pack()
app.place(relx = 0 , relheight = 1, relwidth = 1)
app['bg'] = "#CDD2DE"

player1 = "X"
player2 = "O"
turn = 1

Xlist = list()
Olist = list()

menu()
main.mainloop()
