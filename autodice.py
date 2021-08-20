from consolemenu import *
from consolemenu.items import *
import os, random

def rollDice(diceString):
    try:
        stringParts = diceString.lower().split('d')
        stringParts = ([int(s) if s != '' else 1 for s in stringParts])
        print(f"Your {diceString.upper()} roll resulted in these numbers:")
        numArray = [str(random.randint(1,stringParts[1])) for i in range(stringParts[0])]
        print("-------------------------------")
        print(*numArray,sep=", ")
        print("-------------------------------")
        os.system("pause")
    except:
        print("something went wrong processing your dice roll.")
        os.system("pause")

def diceInput():
    rollDice(input("enter a dice roll (formatted #D# or D#)\n"))

menu = ConsoleMenu("D&D Style Dice Roller","Make your selection and press [enter]")

d20Button = FunctionItem("Roll a D20",rollDice,["d20"])
d12Button = FunctionItem("Roll a D12",rollDice,["d12"])
d210Button = FunctionItem("Roll a 2D10",rollDice,["2d10"])
d8Button = FunctionItem("Roll a D8",rollDice,["d8"])
d6Button = FunctionItem("Roll a D6",rollDice,["d6"])
d4Button = FunctionItem("Roll a D4",rollDice,["d4"])
dCustomButton = FunctionItem("Make a custom dice roll",diceInput)
menu.append_item(d20Button)
menu.append_item(d12Button)
menu.append_item(d210Button)
menu.append_item(d8Button)
menu.append_item(d6Button)
menu.append_item(d4Button)
menu.append_item(dCustomButton)
menu.show()