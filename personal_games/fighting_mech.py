import random

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

#declaring enemies and the player for testing
player_mc = player({"1":"Swat", "2":"Punt"}, {"1": 1, "2":5}, 20, 9)
enemy_1 = enemy("Rat", {'1': 'Bite'}, {'1': 2}, 20, 5)
current_enemies = [enemy_1]

def attack(enemy_index):
    attack_options = player_mc.attack_name
    choice = str(validate_input_range(attack_options, 1, len(attack_options)))
    #rolls a d20 and if higher than the armor, attack will land.
    roll_to_attack = random.randint(1, 20)
    if roll_to_attack > current_enemies[enemy_index].armor:
        #if attack lands then do the damage that matches the attack number
        current_enemies[0].health -= int(player_mc.attack_dmg[choice])
        print(f"You attacked for {player_mc.attack_dmg[choice]}")
        print(current_enemies[enemy_index].health)

        #Is enemy dead?
        if current_enemies[enemy_index].health <= 0:
            del current_enemies[enemy_index]

    else:
        #If the attack misses
        print("You suck")

    #Are enemies left?
    if len(current_enemies) > 0:
        get_attacked()

def options_bar():
    print("Fight the ")
    for i, v in enumerate(current_enemies):
        print(i+1, v.type)
    if len(current_enemies) > 1:
        target = validate_input_range("Who do you target? ",1, len(current_enemies)+1)
    else:
        target = 1

    move = int(validate_input_range("1.)Attack 2)Items", 1, 2))
    if move == 1:
        #Subtract the input to get the correct index
        attack(target-1)
    elif move == 2:
        #going to add an item funtion
        pass

def validate_input_range(prompt, min_value, max_value):
    while True:
        value = int(input(prompt))
        if value >= min_value and value <= max_value:
            return value
        else:
            print("Invalid input.")

def get_attacked():
    for i, enemy in enumerate(current_enemies):
        roll_to_attack = random.randint(1, 20)
        if roll_to_attack > player_mc.armor:
            pick_attack = str(random.randint(1, len(current_enemies[i].attack_name)))
            player_mc.health -= enemy.attack_dmg[pick_attack]
            print(f"{enemy.type} attacked you for {enemy.attack_dmg[pick_attack]}")
            print(player_mc.health)

        #Check if player is dead
        if player_mc.health <= 0:
            print("Ded")
        else:
            options_bar()

        


get_attacked()