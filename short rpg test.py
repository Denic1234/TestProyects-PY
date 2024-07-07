import random
# Small adventure story

# User´s input
user_name = input("What's your name? ")
user_class = "none"
available_classes = ["warrior", "mage", "archer", "thief"]
common_enemy = ["boar", "goblin", "skeleton", "zombie","spider"]

#Welcome Message
print(f"""Welcome {user_name} you can choose between
            Warrior, Mage, Archer, Thief""")

#Checks the Class selected
while True:
    class_selected = input(" Select you'r class: ")
    #if the class is in the list of available classes, it will work
    if class_selected.lower() in available_classes:
        user_class = class_selected
        break
    else:
        print(f"Looks like {class_selected} Choose again!")

print(f"Great Choice! you are a {user_class}! {user_name}! , its time to go for an adventure!")
""

#select random common enemy
firstenemy = random.choice(common_enemy)
print(f"You'r first enemy will be a {firstenemy}")

user_choice = input("""Select a option:
                    attk = Attack
                    talk = Talk to it
                    run = Run away
                    
                    """)

if user_choice.lower() == "attk":
    print(f"{user_name} you have ,\033[31m attacked \033[0m, and defeated {firstenemy}")
if user_choice.lower() == "talk":
    print(f"{firstenemy} did not understand and \033[31m attacked you! \033[0m You Lost!")
if user_choice.lower() == "run":
    print(f"{user_name} \033[33m ran away! \033[0m, maybe next time... ")


print("""That was all for Now!
      it was short practice of coding
      Thanks for Playing""")

