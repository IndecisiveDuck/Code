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

class player:
    def __init__(self, attack_name, attack_dmg, min_accuracy, max_health, health, armor):
        self.attack_name = attack_name
        self.attack_dmg = attack_dmg
        self.min_accuracy = min_accuracy
        self.max_health = max_health
        self.health = health
        self.armor = armor

class item:
    def __init__(self, name, type, ability, ):
        pass


def update_healthbar():
    health_display = tk.Label(health_window)
    health_display.destroy()
    #health bar where the player heath is devided by max health and displayed as 20 hashtags
    h_count = (player_mc.health / player_mc.max_health)
    h_text = '#'*int(h_count*20)
    d_text = '-'*(20-int(h_count*20))
    health_display = tk.Label(health_window, text=f"{h_text}{d_text}")
    health_display.pack()

current_enemies = [enemy("Rat", {1: "Bite"}, {1: 10},9, 20, 20, 0), 
                   enemy("Rat", {1: "Bite"}, {1: 10},9, 20, 20, 0)]
player_mc = player({1:"Swat", 2:"Punt"}, {1: 1, 2: 5}, 5, 20, 20, 9)

def being_attacked_window():
    for i, enemy in enumerate(current_enemies):
        roll_to_hit = random.randint(1, 20)
        if roll_to_hit > enemy.accuracy:
            pick_attack = random.randint(1, len(current_enemies[i].attack_name))
            attacked_for = enemy.attack_dmg[pick_attack] - player_mc.armor
            player_mc.health -= attacked_for
            update_healthbar()
            return f"{enemy.type} attacked you for {attacked_for}"

def attack_window(enemy_index):

    def attacking_enemy(attack_index, targeted_enemy, enemy_index):
        #all battle mechs here.  
        roll_to_hit = random.randint(1, 20)
        #player rolls for accuracy, if they roll their minimum accuracy or higher,
        #  the attack lands.
        if roll_to_hit > player_mc.min_accuracy:
            current_enemies[enemy_index].health -= int(player_mc.attack_dmg[attack_index]) - targeted_enemy.armor
            tk.Label(fighting_window, text=f"You attacked for {player_mc.attack_dmg[attack_index]}").pack()
            tk.Label(fighting_window, text=f"{targeted_enemy.type} has {current_enemies[enemy_index].health} left").pack()
        else:
            tk.Label(fighting_window, text=f"You missed with your {player_mc.attack_name[attack_index]}").pack()

        # for btn in attack_buttons:
        #     btn.config(state='disabled')

        attcked_text = tk.Label(fighting_window, text= being_attacked_window()).pack()
        tk.Button(fighting_window, text="Change target", command=lambda: [fighting_window.destroy(), startFightButton.config(state="active")]).pack()

        
    targeted_enemy = current_enemies[enemy_index]
    #This is the window where the player will attack the enemies
    fighting_window = Toplevel(root)
    fighting_window.title("fighting Window")
    fighting_window.minsize(200, 100)
    #Stores the buttons into an array so that once one of them is pressed, 
    # all the buttons get locked. Might change later.
    attack_buttons = []
    for i, attacks in enumerate(player_mc.attack_name.items()):
        attack_buttons.append(tk.Button(fighting_window, text=attacks[1], 
                          command=lambda val = attacks[0]: attacking_enemy(val, targeted_enemy, enemy_index)))
        attack_buttons[i].pack()


#Main window where the player will choose what enemy they want to fight
root = tk.Tk()
root.geometry("300x200")  # Set window size
root.title("Main Window")
selected_enemy = tk.IntVar(value = 0)
for index, enemies in enumerate(current_enemies):
    #radio buttons to select a enemy to attack 
    display_text = f"{enemies.type}"
    tk.Radiobutton(root, text=display_text, value=index, variable=selected_enemy).pack(anchor=tk.W)
startFightButton = tk.Button(root, text='Fight', command=lambda: 
                             [attack_window(selected_enemy.get()), startFightButton.config(state='disabled')])
startFightButton.pack()

health_window = Toplevel(root)
health_window.title("Health Bar")
tk.Label(health_window, text="Health").pack()
health_display = tk.Label(health_window)
update_healthbar()



root.mainloop()