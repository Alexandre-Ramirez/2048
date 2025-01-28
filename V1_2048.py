#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : 2048_project
Author  : Alexandre Ramirez
Date    : 2025.21.01
Version : 0.01
Purpose : Programme jeux 2048.

# ------------------------------------------------------------------------------
# Projet
# ------------------------------------------------------------------------------

# 2025-21-01 01 ARZ
  - Version initiale
"""
from tkinter import *

#labels creation and position (1. Creation 2. position)
def display():
    for line in range(len(gameplate)):
        for col in range(len(gameplate[line])):
            # creation without placement
            labels[line][col].config (text=gameplate[line][col], bg=dico_color[gameplate[line][col]])

# Dico color
dico_color = { " " : "#000000",
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

# 2 dimensions list with data
"""
gameplate = [[2," ",4," "],
             [" "," "," "," "],
             [" ",2," ",8],
             [" "," "," ",16]]
"""

# Gameplay avec toutes les valeurs
gameplate = [[2,4,8,16],
             [32,64,128,256],
             [512,1024,2048,4096],
             [8192," "," "," "]]

# 2 dimensions list (empty, with labels in the future)
labels= [[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None],]

x0=220 # horizontal beginning of labels
y0=100 # vertical beginning of labels
width=90 # horizontal distance between labels
height=80 # vertical distance between labels

# Windows creation
win = Tk()
win.configure(background='#D8C8B1')
win.geometry("840x480")
win.title(' 2048 desert edition ')

# Title
Label(text="2048 Desert Edition",width=25, height=2, font=("Arial", 17, "bold"),fg="white", background="#D8C8B1").place(x=220, y=25)
# Rules
Label(text="Règles :\n\n Comment jouer à ce jeu 2048 :\n "
           "Le but de ce jeu est de glisser les tuiles ensemble\n pour faire le plus grand nombre possible,\n "
           "le but est 2048. Chaque fois que vous glissez,\n vous obtenez une nouvelle tuile,\n "
           "qui peut être un 4 ou un 2,\n et vous devez les relier aux chiffres\n déjà présents sur le terrain de jeu.\n "
           "Le score et le meilleur score\n sont visibles en haut à droite de l'écran.\n "
           "Si vous voulez commencer une nouvelle partie,\n cliquez sur le bouton Nouveau.", width=35, height=16, font=("Arial", 7), background="#D4B483", justify="left").place(x=605, y=88)
#Score
Label(text="Top score\n\n\n\n\n\n\n\n\n Actual score", width=15, height=18, anchor="n", font =("Arial",11) ,background="#D4B483").place(x=45, y=88)
Label(text="15960", width=7, height=1, anchor="n", font =("Arial",8) ,background="#EEEEEE").place(x=90, y=150)
Label(text="6520", width=7, height=1, anchor="n", font =("Arial",8) ,background="#EEEEEE").place(x=90, y=308)

#Game background
Label(width=53, height=22, background="#5A4634").place(x=206, y=88)


for line in range(len(gameplate)):
    for col in range(len(gameplate[line])):
        # creation without placement
        labels[line][col] = Label(win,  width=7, height=3, borderwidth=1, relief="solid",
                                  font=("Arial", 15))
        # label positionning in the windows
        labels[line][col].place(x=x0 + width * col, y=y0 + height * line)

display()

win.mainloop()