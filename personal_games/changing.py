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
    def __init__(self, attack_name:dict, attack_dmg:dict, min_accuracy:int, max_health:int, health:int, armor:int):
        self.attack_name = attack_name
        self.attack_dmg = attack_dmg
        self.min_accuracy = min_accuracy
        self.max_health = max_health
        self.health = health
        self.armor = armor

player_mc = player({1:"Swat", 2:"Punt"}, {1: 1, 2: 5}, 5, 20, 20, 9)
current_enemies = [enemy("Rat", {1: "Bite"}, {1: 10},9, 20, 20, 0), 
                   enemy("Rat", {1: "Bite"}, {1: 10},9, 20, 20, 0)]

class heathbarWindow:
    def __init__(self):
        pass

    def create_window(self, window:Tk):
        self.health_window = Toplevel(window)
        self.health_window.title("Health Bar")
        tk.Label(self.health_window, text="Health").pack()
        heathbarWindow.health_display = tk.Label(self.health_window)
        heathbarWindow.health_display.pack()
        self.update_healthbar()

    def update_healthbar(self):
        #health bar where the player heath is devided by max health and displayed as 20 hashtags
        h_count = (player_mc.health / player_mc.max_health)
        h_text = '#'*int(h_count*20)
        d_text = '-'*(20-int(h_count*20))
        heathbarWindow.health_display.config(text=f"{h_text}{d_text}")


class mainWindow:
    def __init__(self, root:Tk):
        self.root = root
        self.root.title("Main Window")
        self.root.geometry("300x200+500+0")

        selected_enemy = tk.IntVar(value = 0)
        for index, enemies in enumerate(current_enemies):
            #radio buttons to select a enemy to attack 
            display_text = f"{enemies.type}"
            tk.Radiobutton(root, text=display_text, value=index, variable=selected_enemy).pack(side="left")
        self.root.startFightButton = tk.Button(root, text='Fight', command=lambda: 
                                    [attackWindow(root, selected_enemy.get()), self.root.startFightButton.config(state='disabled')])
        self.root.startFightButton.pack()
class attackWindow:
    def __init__(self, window, enemy_index):
        targeted_enemy = current_enemies[enemy_index]
        #This is the window where the player will attack the enemies
        self.fighting_window = Toplevel(window)
        self.fighting_window.title("fighting Window")
        self.fighting_window.minsize(200, 100)
        self.fighting_window.geometry("+100+140")

        #Stores the buttons into an array so, if apliable, the buttons can all be locked or unlocked
        attack_buttons = []
        for i, attacks in enumerate(player_mc.attack_name.items()):
            attack_buttons.append(tk.Button(self.fighting_window, text=attacks[1], 
                                command=lambda: self.attacking_enemy(attacks[0], targeted_enemy, enemy_index)))
            attack_buttons[i].pack()
    
        tk.Button(self.fighting_window, text="Change target", command=lambda: 
                    [self.fighting_window.destroy(), window.startFightButton.config(state="active")]).pack()
        
    def attacking_enemy(self, attack_index: int, targeted_enemy: enemy, enemy_index:int):
        """Attacks the targeted enemy and then calls the being attacked function

        Args:
            attack_index (int): Where the attack is in player_mc.attack_names dictionary
            targeted_enemy (enemy): The enemy you are attacking in the instant you press the button. Used to call the armor of the enemy and the enemy type.
            enemy_index (int): Where the enemy is in relationship to the current enemies array. It's used to store the damage the player does to the rat.
        """
        #all battle mechs here.  
        roll_to_hit = random.randint(1, 20)
        #player rolls for accuracy, if they roll their minimum accuracy or higher,
        #  the attack lands.
        if roll_to_hit > player_mc.min_accuracy:
            current_enemies[enemy_index].health -= int(player_mc.attack_dmg[attack_index]) - targeted_enemy.armor
            tk.Label(self.fighting_window, text=f"You attacked for {player_mc.attack_dmg[attack_index]}").pack()
            if(current_enemies[enemy_index].health <= 0):
                tk.Label(self.fighting_window, text=f"{targeted_enemy.type} was defeated")
                current_enemies
            tk.Label(self.fighting_window, text=f"{targeted_enemy.type} has {current_enemies[enemy_index].health} left").pack()
        else:
            tk.Label(self.fighting_window, text=f"You missed with your {player_mc.attack_name[attack_index]}").pack()

        #This calls the being_attacked() function. It's no longer a window because 
        # that was too many windows.
        for enemy in current_enemies:
            tk.Label(self.fighting_window, text= self.being_attacked_window(enemy)).pack()

    def being_attacked_window(self, enemy) -> str:
        """This is where the player takes damage.

        Returns:
            str: _description_
        """
        health_bar = heathbarWindow()

        roll_to_hit = random.randint(1, 20)
        pick_attack = random.randint(1, len(enemy.attack_name))
        if roll_to_hit > enemy.accuracy:
            attacked_for = enemy.attack_dmg[pick_attack] - player_mc.armor
            player_mc.health -= attacked_for
            health_bar.update_healthbar()
            return f"{enemy.type} attacked you for {attacked_for}"
        else:
            return f"{enemy.type} attacked you with {pick_attack} but missed"

        

def main():
    root = tk.Tk()
    window = mainWindow(root)
    heathbar = heathbarWindow()
    health = heathbar.create_window(root)
    root.mainloop()

main()