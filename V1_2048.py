#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : 2048_project
Author  : Alexandre Ramirez
Date    : 2025.18.03
Version : 1.1
Purpose : Programme jeux 2048.

# ------------------------------------------------------------------------------
# Projet 2048
# ------------------------------------------------------------------------------

# 2025-21-01 01 ARZ
  - Version initiale
"""
import os
import sys
from tkinter import *
import random
from tkinter import messagebox

from PIL.features import check


#labels creation and position (1. Creation 2. position)
def display():
    for line in range(len(gameplate)):
        for col in range(len(gameplate[line])):
            # creation without placement
            labels[line][col].config (text=gameplate[line][col], bg=dico_color[gameplate[line][col]])

# Score initialisation
score = 0

"""----------------------------------------------------------------------------------------------
GAMEPLAY FUNTIONS AND RULES 
-----------------------------------------------------------------------------------------------"""

def pack_4(a,b,c,d):

    global score

    nm = 0
    if c == 0 and d>0:
        c,d = d,0
        nm += 1

    if b == 0 and c>0:
        b,c,d = c,d,0
        nm += 1

    if a == 0 and b>0:
        a,b,c,d = b,c,d,0
        nm += 1

    if a == b and a>0:
        a = 2*a
        nm += 1
        score += a #add the result of the multiplication into score
        b = c
        c = d
        d = 0

    if b == c and b>0:
        b = 2*b
        nm += 1
        score += b
        c = d
        d = 0

    if c == d and c>0:
        c = 2*c
        score += c
        nm += 1
        d = 0

    return a,b,c,d,nm


def key_press(event):
    touche = event.keysym  # récupérer le symbole de la touche
    if touche == "Right" or touche == "d" or touche == "D":
        if move_right() != 0 :
            random_tile()
    if touche == "Left" or touche == "a" or touche == "A":
        if move_left() != 0 :
            random_tile()
    if touche == "Up" or touche == "w" or touche == "W":
        if move_up() != 0 :
            random_tile()
    if touche == "Down" or touche == "s" or touche == "S":
        if move_down() != 0 :
            random_tile()

    display()
    check_win()
    check_defeat()
    score_label.config(text=f"Score: {score}") #update score display after keypress movement

def move_right():
    tot_move = 0
    gameplate[0][3],gameplate[0][2],gameplate[0][1],gameplate[0][0],nm = pack_4(gameplate[0][3],gameplate[0][2],gameplate[0][1],gameplate[0][0])
    tot_move += nm
    gameplate[1][3],gameplate[1][2],gameplate[1][1],gameplate[1][0],nm = pack_4(gameplate[1][3],gameplate[1][2],gameplate[1][1],gameplate[1][0])
    tot_move += nm
    gameplate[2][3],gameplate[2][2],gameplate[2][1],gameplate[2][0],nm = pack_4(gameplate[2][3],gameplate[2][2],gameplate[2][1],gameplate[2][0])
    tot_move += nm
    gameplate[3][3],gameplate[3][2],gameplate[3][1],gameplate[3][0],nm = pack_4(gameplate[3][3],gameplate[3][2],gameplate[3][1],gameplate[3][0])
    tot_move += nm
    return tot_move

def move_left():
    tot_move = 0
    gameplate[0][0],gameplate[0][1],gameplate[0][2],gameplate[0][3],nm = pack_4(gameplate[0][0],gameplate[0][1],gameplate[0][2],gameplate[0][3])
    tot_move += nm
    gameplate[1][0],gameplate[1][1],gameplate[1][2],gameplate[1][3],nm = pack_4(gameplate[1][0],gameplate[1][1],gameplate[1][2],gameplate[1][3])
    tot_move += nm
    gameplate[2][0],gameplate[2][1],gameplate[2][2],gameplate[2][3],nm = pack_4(gameplate[2][0],gameplate[2][1],gameplate[2][2],gameplate[2][3])
    tot_move += nm
    gameplate[3][0],gameplate[3][1],gameplate[3][2],gameplate[3][3],nm = pack_4(gameplate[3][0],gameplate[3][1],gameplate[3][2],gameplate[3][3])
    tot_move += nm
    return tot_move

def move_up():
    tot_move = 0
    gameplate[0][0],gameplate[1][0],gameplate[2][0],gameplate[3][0],nm = pack_4(gameplate[0][0],gameplate[1][0],gameplate[2][0],gameplate[3][0])
    tot_move += nm
    gameplate[0][1], gameplate[1][1], gameplate[2][1], gameplate[3][1],nm = pack_4(gameplate[0][1], gameplate[1][1], gameplate[2][1], gameplate[3][1])
    tot_move += nm
    gameplate[0][2], gameplate[1][2], gameplate[2][2], gameplate[3][2],nm = pack_4(gameplate[0][2], gameplate[1][2], gameplate[2][2], gameplate[3][2])
    tot_move += nm
    gameplate[0][3], gameplate[1][3], gameplate[2][3], gameplate[3][3],nm = pack_4(gameplate[0][3], gameplate[1][3], gameplate[2][3], gameplate[3][3])
    tot_move += nm
    return tot_move

def move_down():
    tot_move = 0
    gameplate[3][0],gameplate[2][0],gameplate[1][0],gameplate[0][0],nm = pack_4(gameplate[3][0],gameplate[2][0],gameplate[1][0],gameplate[0][0])
    tot_move += nm
    gameplate[3][1], gameplate[2][1], gameplate[1][1], gameplate[0][1],nm = pack_4(gameplate[3][1], gameplate[2][1], gameplate[1][1], gameplate[0][1])
    tot_move += nm
    gameplate[3][2], gameplate[2][2], gameplate[1][2], gameplate[0][2],nm = pack_4(gameplate[3][2], gameplate[2][2], gameplate[1][2], gameplate[0][2])
    tot_move += nm
    gameplate[3][3], gameplate[2][3], gameplate[1][3], gameplate[0][3],nm = pack_4(gameplate[3][3], gameplate[2][3], gameplate[1][3], gameplate[0][3])
    tot_move += nm
    return tot_move

#function to add a random 2 or for in an empty case in gameplate
def random_tile():
    global gameplate
    empty_list = []
    for line in range(len(gameplate)) :
        for col in range(len(gameplate[line])) :
            if gameplate[line][col] == 0 :
                empty_list.append([line,col])   #creating a list with all the empty cases in gameplate

    tile_spawn = [2,2,2,2,4]
    n = random.choice(tile_spawn)
    if len(empty_list) > 0 :
            empty_tile = random.choice(empty_list)
            gameplate[empty_tile[0]][empty_tile[1]] = n  #adding a 2 or 4 in an empty case


#fun function to gamble the score
def check_result(i,root) :
    global score
    piece = random.randint(1, 2)
    if i == piece :
        score *= 2
        messagebox.showinfo("Lucky !", f"Your new score is {score}")
    else :
        score /= 2
        messagebox.showinfo("Ouch !", f"Your new score is {score}")

    root.destroy()




"""----------------------------------------------------------------------------------------------
CONDITIONS IF VICTORY OR DEFEAT 
-----------------------------------------------------------------------------------------------"""

def check_defeat(found = False) :
    if 0 not in [element for ligne in gameplate for element in ligne] :
        if check_merge() == False :
            loose_window()

def check_merge() :
    for ligne in range(4) :
        for col in range(3) :
            if gameplate[ligne][col] == gameplate[ligne][col+1]: #verifying column by column if 2 same numbers are adjoined
                return True

    for col in range(4) :
        for ligne in range(3) :
            if gameplate[ligne][col] == gameplate[ligne+1][col] : #verifying line by line if 2 same numbers are adjoined
                return True
    return False

def check_win() :
    if 2048 in [element for ligne in gameplate for element in ligne] :
        global status
        status += 1
        if status == 1 :
            win_window()

"""----------------------------------------------------------------------------------------------
WINDOWS
-----------------------------------------------------------------------------------------------"""

def loose_window() :
    messagebox.showinfo("LOOSE WINDOW", "YOU LOST")
    gambling_score()

def win_window() :
    messagebox.showinfo("WIN WINDOW", "YOU WON !")
    option_window()

def restart_program() :
    root = Tk()
    root.destroy
    python = sys.executable # Get the path to the Python executable that started the program
    os.execl(python, python, *sys.argv) # Restart the program by executing the Python executable with the same arguments (sys.argv = origin parameters when starting a game)

def option_window() :
    # Creating the tkinter window
    root = Tk()
    label = Label(root, text="OPTION")
    label.pack()
    root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

    # Creating and configuring the "stop" or "quit game" button
    button_stop = Button(root, text="Quit game", command=quit)
    button_stop.pack(pady=25)

    # Creating and configuring the "continue" button
    button_continue = Button(root, text="Continue game", command= root.destroy)
    button_continue.pack(pady=25)

    # Creating and configuring the "begin a new game" button
    button_redo = Button(root, text="Restart a new game", command= restart_program )
    button_redo.pack(pady=25)

    root.mainloop()


# Fonction principale pour afficher l'interface
def gambling_score():
    root = Tk()
    label = Label(root, text="GAMBLING SCORE")
    label.pack(pady=20)
    root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

    # Bouton pour HEAD
    button_stop = Button(root, text="HEAD", command=lambda : check_result(1, root) )
    button_stop.pack(pady=25)

    # Bouton pour TAIL
    button_continue = Button(root, text="TAIL", command=lambda : check_result(2, root) )
    button_continue.pack(pady=25)

    Label(text=f"{score}", width=25, height=2, font=("Arial", 17, "bold"), fg="white", background="#D8C8B1").place(x=220, y=25)

    root.mainloop()

"""----------------------------------------------------------------------------------------------
GAME VISUAL 
-----------------------------------------------------------------------------------------------"""

# Dico color
dico_color = { " " : "#000000",
               0 : "#000000",
               2 : "#FFFFFF",
               4 : "#F9F5F0",
               8 : "#F2EBE1",
               16 : "#EDE0D3",
               32 : "#E4D3C2",
               64 : "#DAC2AB",
               128 : "#CBAF95",
               256 : "#BDA387",
               512 : "#AD9274",
               1024 : "#9C8162",
               2048 : "#8A6F50",
               4096 : "#765E42",
               8192 : "#604C33",
               }

"""
# 2 dimensions list with data to win
gameplate = [[1024,1024,4,0],
             [1024,0,0,0],
             [1024,2,0,8],
             [0,0,0,16]]
"""

# 2 dimension list with data to lose
gameplate = [[16,8,4,2],
             [2,4,8,16],
             [16,8,512,64],
             [64,0,0,0]]


"""
# Gameplay with all initial values
gameplate = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]
"""
# 2 dimensions list (empty, with labels in the future)
labels= [[None,None,None,None],
         [None,None,None,None],
         [None,None,None,None],
         [None,None,None,None],]

x0=220 # horizontal beginning of labels
y0=100 # vertical beginning of labels
width=90 # horizontal distance between labels
height=80 # vertical distance between labels

# Windows creation
win = Tk()
win.configure(background='#D8C8B1')
win.geometry("840x480")
win.title(' 2048 desert edition ')

# Center the game Window
screen_width = win.winfo_screenwidth() # collect screen size informations    --|
screen_height = win.winfo_screenheight()                               #    <--|

window_width = 840
window_height = 480

x_position = (screen_width - window_width) // 2 # horizontal start point position of the window
y_position = (screen_height - window_height) // 2 # vertical start point position of the window

win.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')


# Title
Label(text="2048 Desert Edition",width=25, height=2, font=("Arial", 17, "bold"),fg="white", background="#D8C8B1").place(x=220, y=25)
# Rules
Label(text="Règles :\n\n Comment jouer à ce jeu 2048 :\n "
           "Le but de ce jeu est de glisser les tuiles ensemble\n pour faire le plus grand nombre possible,\n "
           "le but est 2048. Chaque fois que vous glissez,\n vous obtenez une nouvelle tuile,\n "
           "qui peut être un 4 ou un 2,\n et vous devez les relier aux chiffres\n déjà présents sur le terrain de jeu.\n "
           "Le score et le meilleur score\n sont visibles en haut à droite de l'écran.\n "
           "Si vous voulez commencer une nouvelle partie,\n cliquez sur le bouton Nouveau.", width=35, height=16, font=("Arial", 7), background="#D4B483", justify="left").place(x=605, y=88)

#Score display
score_label = Label(win, text="Score: 0", font=("Arial", 14), bg="#D4B483")
score_label.place(x=90, y=88)

#Option button
option_button = Button(win, text="Option", font=("Arial", 14), fg="grey", background="#D4B483", command=option_window)
option_button.place(x=90, y=250)

#Game background
Label(width=53, height=22, background="#5A4634").place(x=206, y=88)


for line in range(len(gameplate)):
    for col in range(len(gameplate[line])):
        # creation without placement
        labels[line][col] = Label(win,  width=7, height=3, borderwidth=1, relief="solid",
                                  font=("Arial", 15))
        # label positionning in the windows
        labels[line][col].place(x=x0 + width * col, y=y0 + height * line)


"""----------------------------------------------------------------------------------------------
GAME RUN
-----------------------------------------------------------------------------------------------"""

random_tile()
random_tile()
display()
status = 0
win.bind('<Key>', key_press) #on traite les touches clavier
win.mainloop()