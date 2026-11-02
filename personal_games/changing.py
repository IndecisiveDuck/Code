import random
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

class enemy:

    def __init__(self, type, attack_name, attack_dmg, accuracy, max_health, health, armor):
        self.type = type
        self.attack_name = attack_name
        self.attack_dmg = attack_dmg
        self.accuracy = accuracy
        self.max_health = max_health
        self.health = health
        self.armor = armor

current_enemies = [enemy("Rat", {1: "Bite"}, {1: 10},9, 20, 20, 0), 
                   enemy("Rat", {1: "Bite"}, {1: 10},9, 20, 20, 0)]

class mainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")
        self.root.geometry("300x200+500+0")

        selected_enemy = tk.IntVar(value = 0)
        for index, enemies in enumerate(current_enemies):
            #radio buttons to select a enemy to attack 
            display_text = f"{enemies.type}"
            tk.Radiobutton(root, text=display_text, value=index, variable=selected_enemy).pack(side="left")
        self.root.startFightButton = tk.Button(root, text='Fight', command=lambda: 
                                    [attack_window(selected_enemy.get()), startFightButton.config(state='disabled')])
        self.root.startFightButton.pack()

def main():
    root = tk.Tk()
    window = mainWindow(root)
    root.mainloop()

main()