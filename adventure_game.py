import random
import time


def print_pause(message):
    print(message)
    time.sleep(2)


def combat(weapon):
    print_pause(f"The {enemy} attacks you!")
    if weapon == "dagger":
        print_pause(f"You feel a bit under-prepared for this,"
                    "what with onh only having a tiny {weapon}.")
    choice = input("Would you like to (1) fight or (2) run away?")
    if choice == '1':
        if weapon == "dagger":
            print_pause(f"You do your best...")
            print_pause(f"but your {weapon} is no match for the {enemy}.")
            print_pause(f"You have been defeated!""")
        elif weapon == "sword":
            print_pause(f"As the {enemy} moves to attack, "
                        "you unsheath your new sword.")
            print_pause(f"The Sword of Ogoroth shines brightly in your hand "
                        "as you brace yourself for the attack.")
            print_pause(f"But the {enemy} takes one look at "
                        "your shiny new toy and runs away!")
            print_pause(f"You have rid the town of the {enemy}. "
                        "You are victorious!")
    elif choice == '2':
        print_pause("You run back into the field. Luckily,"
                    "you don't seem to have been followed.")
        where_to()


def play_again():
    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Would you like to play again? (y/n)")
        if choice == 'n':
            print_pause("Thanks for playing! See you next time.")
            return 'game_over'
        elif choice == 'y':
            print_pause("Excellent! Restarting the game ...")
            weapon = 'dagger'
            return 'running'


def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(f"In your hand you hold your trusty"
                "(but not very effective) {weapon}.")


def where_to():
    print_pause("")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")
    if choice == '1':
        house()
    elif choice == '2':
        cave()


def house():
        # Things that happen to the player in the house
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door"
                "opens and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    combat(weapon)


def cave():
    # Things that happen to the player goes in the cave
    global cave_visited
    global weapon
    print_pause("You peer cautiously into the cave.")
    if cave_visited:
        print_pause("You've been here before, and gotten all the good stuff."
                    "It's just an empty cave now.")
    elif cave_visited is False:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause(f"You discard your silly old {weapon} "
                    "and take the sword with you.")
        weapon = "sword"
    cave_visited = True
    print_pause("You walk back out to the field.")
    where_to()


game_state = 'running'
while game_state == 'running':

    enemies = ['troll', 'wicked fairie', 'pirate', 'gorgon', 'dragon']
    enemy = random.choice(enemies)
    weapon = 'dagger'
    cave_visited = False

    intro()
    where_to()
    game_state = play_again()
