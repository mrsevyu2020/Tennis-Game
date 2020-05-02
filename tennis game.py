# Modules import
from random import randint, choice
import array as arr
import time

# Colors and format text
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Functions
def tiebreak(psround2):
    while True:
        if randint(1, 2) == 1:
            tbp1[psround2] = tbp1[psround2] + 1
        else:
            tbp2[psround2] = tbp2[psround2] + 1
        if tbp1[psround2] >= 7 and (tbp1[psround2] - tbp2[psround2]) >= 2:
            asp1[psround2] = asp1[psround2] + 1
            return 1
        if tbp2[psround2] >= 7 and (tbp2[psround2] - tbp1[psround2]) >= 2:
            asp2[psround2] = asp2[psround2] + 1
            return 2


def set(psround):
    while True:
        if randint(1, 2) == 1:
            asp1[psround] = asp1[psround] + 1
        else:
            asp2[psround] = asp2[psround] + 1
        if asp1[psround] == 6 and asp2[psround] == 6:
            if tiebreak(psround) == 1:
                return 1
            else:
                return 2
        else:
            if (asp1[psround] == 6 or asp1[psround] == 7) and asp1[psround] - asp2[psround] >= 2:
                return 1
            if (asp2[psround] == 6 or asp2[psround] == 7) and asp2[psround] - asp1[psround] >= 2:
                return 2

def match(setw):
    wsp1 = 0
    wsp2 = 0
    sround = 1
    while wsp1 < setw and wsp2 < setw:
        if set(sround - 1) == 1:
            wsp1 = wsp1 + 1
        else:
            wsp2 = wsp2 + 1
        if wsp1 == setw:
            return 1
        elif wsp2 == setw:
            return 2
        sround = sround + 1
        asp1.append(0)
        asp2.append(0)
        tbp1.append(0)
        tbp2.append(0)

# ****************************************************
# *********************** MAIN ***********************
# ****************************************************

# Variable definitions.
ntorneo = "Us Open"
players = 4
#np1 = "Player1"
#np2 = "Player2"
sets_win = 3

# Ask interactivly.
#while ntorneo == "":
#    ntorneo = "Us Open"

while (players < 2 or players > 8) or (players % 2 != 0):
    players = input("Type number of players (from 2 to 8 and even): ")
    if players == "":
         players = 0
    else:
        players = int(players)

global asp1, asp2, tbp1, tbp2
asp1 = arr.array('i', [0])
asp2 = arr.array('i', [0])
tbp1 = arr.array('i', [0])
tbp2 = arr.array('i', [0])

names = ["Player1", "Player2"]

ganador = match(sets_win)

# Match text lengths.
resul1 = names[0] + " "
resul2 = names[1] + " "
if len(names[0]) > len(names[1]):
    for i in range(0, (len(names[0]) - len(names[1]))):
        resul2 = resul2 + " "
else:
    for i in range(0, (len(names[1]) - len(names[0]))):
        resul1 = resul1 + " "

# Add set results.
for i in range(0, len(asp1)):
    if asp1[i] == 7 or (asp1[i] == 6 and asp2[i] != 7):
        resul1 = resul1 + color.BOLD + str(asp1[i]) + color.END
        resul2 = resul2 + str(asp2[i])
    else:
        resul2 = resul2 + color.BOLD + str(asp2[i]) + color.END
        resul1 = resul1 + str(asp1[i])

    if tbp1[i] != 0 and tbp2[i] != 0:
        resul1 = resul1 + "(" + str(tbp1[i]) + ") "
        resul2 = resul2 + "(" + str(tbp2[i]) + ") "
    else:
        resul1 = resul1 + " "
        resul2 = resul2 + " "

print(resul1)
print(resul2 + "\n")

if ganador == 1:
   print("And the winner of the " + color.BOLD + color.BLUE + ntorneo + color.END + " tournament is: " + color.BOLD + color.RED + names[0] + color.END)
else:
   print("And the winner of the " + color.BOLD + color.BLUE + ntorneo + color.END + " tournament is: " + color.BOLD + color.RED + names[1] + color.END)

