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

rat_enemy = enemy("Rat", {1: "Bite"}, {1: 2}, 20, 5)
current_enemies = [rat_enemy, rat_enemy]

def attack_window():
    fighting_window = Toplevel(root)
    fighting_window.title("fighting Window")
    for index, enemies in enumerate(current_enemies):
        display_text = f"{enemies.type}"
        tk.Radiobutton(fighting_window, text=display_text, value=index).pack(anchor=tk.W)

root = tk.Tk()
root.geometry("300x200")  # Set window size
root.title("Main Window")
startFightButton = tk.Button(root, text='Fight', command=attack_window)
startFightButton.pack()



root.mainloop()