import random

class Game:
    def __init__(self):
        self.player_name = ""
        self.game_world = {
            "forest_clearing":{
                "description": "You are in a forest clearing. There is a path to the north and east",
                "actions": ["go north","go east"]
            },
            "mysterious_cave":{
                "description": "You are in a dark, mysterious cave. There is a path to the south",
                "actions": ["go south"]
            },
            "sunny_meadow":{
                "description": "You are in a sunny meadow. There is a path to the west",
                "actions": ["go west"]
            }
        }
        self.current_location = "forest_clearing"
        self.events = {
            "forest_clearing":self.event_forest_clearing,
            "mysterious_cave":self.event_mysterious_cave,
            "sunny_meadow":self.event_sunny_meadow,
        }
    
    def start(self):
        print("Welcome Adventurer!")
        self.player_name = input("What is your name adventurer?")
        print(f"Greetings, {self.player_name}. Let the adveture begin!")
        self.play()
    
    def play(self):
        while True:
            location = self.game_world[self.current_location]
            print(location["description"])
            action = input(f"Available actions: {', '.join(location['actions'])}\nWhat do you want to do? ")

            if action in location["actions"]:
                if action == "go north":
                    self.current_location = "mysterious_cave"
                elif action == "go east":
                    self.current_location = "sunny_meadow"
                elif action == "go south":
                    self.current_location = "forest_clearing"
                elif action == "go west":
                    self.current_location = "forest_clearing"
                
                self.events[self.current_location]()
            else:
                print("Invalid action. Please try again.")

    def event_forest_clearing(self):
        if random.random() < 0.3:
            print("A friendly squirrel appears and gives you a magical acorn.")
            self.game_world["forest_clearing"]["description"] = "You are in a forest clearing. A friendly squirrel waves at you. There's a path to the north and east."

    def event_mysterious_cave(self):
        if random.random() < 0.5:
            print("You find a hidden treasure chest!")
            self.game_world["mysterious_cave"]["description"] = "You are in a dark, mysterious cave. A treasure chest lies open. There's a path to the south."

    def event_sunny_meadow(self):
        if random.random() < 0.2:
            print("A wise old man offers you advice.")
            self.game_world["sunny_meadow"]["description"] = "You are in a sunny meadow. A wise old man nods at you. There's a path to the west."

if __name__ == "__main__":
    game = Game()
    game.start()
