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

def attack_window(enemy_index):
    print(enemy_index)
    fighting_window = Toplevel(root)
    fighting_window.title("fighting Window")


root = tk.Tk()
root.geometry("300x200")  # Set window size
root.title("Main Window")
selected_enemy = tk.IntVar(value = 0)
for index, enemies in enumerate(current_enemies):
    display_text = f"{enemies.type}"
    tk.Radiobutton(root, text=display_text, value=index, variable=selected_enemy).pack(anchor=tk.W)
startFightButton = tk.Button(root, text='Fight', command=lambda: attack_window(selected_enemy.get()))
startFightButton.pack()



root.mainloop()