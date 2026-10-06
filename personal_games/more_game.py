import random
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

class enemy:

    def __init__(self, type, attack_name, attack_dmg, max_health, health, armor):
        self.type = type
        self.attack_name = attack_name
        self.attack_dmg = attack_dmg
        self.max_health = max_health
        self.health = health
        self.armor = armor

class player:
    def __init__(self, attack_name, attack_dmg, max_health, health, armor):
        self.attack_name = attack_name
        self.attack_dmg = attack_dmg
        self.max_health = max_health
        self.health = health
        self.armor = armor

class item:
    def __init__(self, name, type, ability, ):
        pass




rat_enemy = enemy("Rat", {1: "Bite"}, {1: 2}, 20, 20, 5)
current_enemies = [rat_enemy, rat_enemy]
player_mc = player({1:"Swat", 2:"Punt"}, {1: 1, 2: 5}, 20, 10, 9)

def attack_window(enemy_index):

    def attacking_enemy(attack_index, targeted_enemy, enemy_index):
        roll_to_hit = random.randint(1, 20)
        if roll_to_hit > targeted_enemy.armor:
            current_enemies[enemy_index].health -= int(player_mc.attack_dmg[attack_index])
            tk.Label(fighting_window, text=f"You attacked for {player_mc.attack_dmg[attack_index]}").pack()
            tk.Label(fighting_window, text=f"{targeted_enemy.type} has {current_enemies[enemy_index].health} left").pack()
        else:
            tk.Label(fighting_window, text=f"You missed with your {player_mc.attack_name[attack_index]}").pack()

        for btn in attack_buttons:
            btn.config(state='disabled')

        tk.Button(fighting_window, text="Exit", command=lambda: [fighting_window.destroy(), startFightButton.config(state="active")]).pack()

        
    targeted_enemy = current_enemies[enemy_index]
    #This is the window where the player will attack the enemies
    fighting_window = Toplevel(root)
    fighting_window.title("fighting Window")
    #buttons list
    attack_buttons = []
    for i, attacks in enumerate(player_mc.attack_name.items()):
        btn = tk.Button(fighting_window, text=attacks, 
                  command=lambda: attacking_enemy(i, targeted_enemy, enemy_index))
        btn.pack() 
        attack_buttons.append(btn)
        
#Main window where the player will choose what enemy they want to fight
root = tk.Tk()
root.geometry("300x200")  # Set window size
root.title("Main Window")
selected_enemy = tk.IntVar(value = 0)
for index, enemies in enumerate(current_enemies):
    display_text = f"{enemies.type}"
    tk.Radiobutton(root, text=display_text, value=index, variable=selected_enemy).pack(anchor=tk.W)
startFightButton = tk.Button(root, text='Fight', command=lambda: 
                             [attack_window(selected_enemy.get()), startFightButton.config(state='disabled')])
startFightButton.pack()

health_window = Toplevel(root)
health_window.title("Health Bar")
tk.Label(health_window, text="Health").pack()
h_count = player_mc.health / player_mc.max_health
h_text = '#'*int(h_count*20)
health_display = tk.Label(health_window, text=h_text).pack()



root.mainloop()