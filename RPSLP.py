#rock-paper-scissors-lizard-Spock game!
#written on CodeSkulptor.org

#import Random Module

import random

#helper functions

def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print "Error - this is not a valid choice for play"
    return number

def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print "Error - this number does not correspond with any name"
    return name

#main function

def rpsls(player_choice):
#seperate consecutive games
    print ""
#player's play
    print "The player chooses" + " " + player_choice
    player_number = name_to_number(player_choice)
#computer's play    
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "The computer chooses" + " " + comp_choice
#determine winner
    battle_value = (player_number - comp_number) % 5
    if (battle_value == 1) or (battle_value == 2):
        print "Player wins!"
    elif (battle_value == 3):
        print "Computer wins!"
    elif (battle_value == 4):
        print "Computer wins!"
    elif (battle_value == 0):
        print "Player and computer tie!"
    else:
        print "Error - a winner could not be determined."

#test calls
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")