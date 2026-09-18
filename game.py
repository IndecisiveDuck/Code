story_nodes = {
    "start": {
        "text":"Around you is the bustling of the market square, vendors shouting about their wares. The sun is high overhead, making the spices from the market even more potent in the air. Proceed further? \n Y/N",
        "choices": {"y": "yes", "n": "no"}
    },
    "yes":{
        "text": 'By the fontian is the town crier, a dichevled looking man who looks like he hasn\'t eaten in days. "The end times are here! The mountain will rain fire upon us all!" He wails, looking up to you with pleading eyes. "Everyone must leave the city! Now before the mointain claims us all!"'
    },
    "no":{
        "text": ''
    }
}

current_node  = "start"

while True:
    #node is equal to story nods and it prints the story with an indent. It prints the te
    node = story_nodes[current_node]
    print("\n" + node['text'])

    choice = input("What do you do? ").strip()
    #If the choice is in the current node 
    if choice in node["choices"][choice]:
        current_node = node["choices"][choice]
    else:
        print("invalid choice option")