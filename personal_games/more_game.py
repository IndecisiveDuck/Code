import random
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

class enemy:

    def __init__(self, type, attack_name, attack_dmg, health, armor):
        self.type = type
        self.attack_name = attack_name
        self.attack_dmg = attack_dmg
        self.health = health
        self.armor = armor

class player:
    def __init__(self, attack_name, attack_dmg, health, armor):
        self.attack_name = attack_name
        self.attack_dmg = attack_dmg
        self.health = health
        self.armor = armor

class item:
    def __init__(self, name, type, ability, ):
        pass

def attack_window():
    fighting_window = Toplevel(root)
    fighting_window.title("fighting Window")

root = tk.Tk()
root.geometry("300x200")  # Set window size
root.title("Main Window")
startFightButton = tk.Button(root, text='Fight', command=attack_window)
startFightButton.pack()



root.mainloop()