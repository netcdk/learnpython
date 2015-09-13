# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# Written on CodeSkulptor.org

#import modules
import simplegui
import math
import random

# state global variable(s) for program start
range = 100

# helper functions
## helper function to start and restart the game
def new_game():
    print "You have started a new game with a range of 0 to", range
    # state and generate global variable "secret_number" for a new game
    global secret_number
    secret_number = random.randrange(range)
    print "A secret number has been selected from the current range"
    # state and generate global variable "allotted_guesses" for a new game
    global allotted_guesses
    allotted_guesses = math.ceil(math.log(range, 2))
    # state and reset global variable "guesses_made" for a new game
    global guesses_made
    guesses_made = 0
    # print and return starting number of guesses
    print "You have", int(allotted_guesses - guesses_made), "guesses to determine the secret number"
    return (secret_number, allotted_guesses, guesses_made)

## helper function to increment number of guesses made
def guess_increment():
    global guesses_made
    guesses_made = guesses_made + 1
    return guesses_made

## helper function to limit number of guesses, and restart game if limit is met
def guess_limiter():
    global allotted_guesses, guesses_made
    guesses_left = allotted_guesses - guesses_made
    if not guesses_left:
        print "You have used all of your guesses, the computer wins!"
        print ""
        print ""
        new_game()
    elif 2 <= guesses_left <= 10:
        print "You have", int(guesses_left), "guesses remaining"
    else:
        print "You have only", int(guesses_left), "guess remaining"
    
# define event handlers for control panel
## function for button that starts a new game, changes the range to [0,100],
## and selects a new secret number
def range100():
    print "You gave up, the computer wins!"
    print ""
    print ""
    # set global variable "range" and start new game 
    global range
    range = 100
    new_game()

## function for button that starts a new game, changes the range to [0,1000],
## and selects a new secret number
def range1000():
    print "You gave up, the computer wins!"
    print ""
    print ""
    # set global variable "range" and start new game 
    global range
    range = 1000
    new_game()    
    
## input field for submitting guesses
def input_guess(guess):
    guess = int(guess)
    # range of 100, and guess within selected range
    if range == 100 and 0 <= guess < range:
        if guess == secret_number:
            print ""
            print "You guessed", guess
            print "Correct!"
            print ""
            print ""
            new_game()
        elif guess < secret_number:
            print ""
            print "You guessed", guess
            print "Higher!"
            guess_increment()
            guess_limiter()
        elif guess > secret_number:
            print ""
            print "You guessed", guess
            print "Lower!"
            guess_increment()
            guess_limiter()
    # range of 1000, and guess within selected range
    elif range == 1000 and 0 <= guess < range:
        if guess == secret_number:
            print ""
            print "You guessed", guess
            print "Correct!"
            print ""
            print ""
            new_game()
        elif guess < secret_number:
            print ""
            print "You guessed", guess
            print "Higher!"
            guess_increment()
            guess_limiter() 
        elif guess > secret_number:
            print ""
            print "You guessed", guess
            print "Lower!"
            guess_increment()
            guess_limiter()
    # either range, guess not within selected range
    else:
        print ""
        print "You guessed", guess
        print "With a selected range of 0 to", range, "you should guess between 0 and", range - 1
        guess_increment()
        guess_limiter()
        
# create frame
frame = simplegui.create_frame("Guess the number!", 350, 350, 300)

# register event handlers for control elements and start frame

label1 = frame.add_label("WELCOME TO THE GAME!")
label2 = frame.add_label("")
label3 = frame.add_label("")
inp = frame.add_input('Guess the number!', input_guess, 50)
label4 = frame.add_label("")
label5 = frame.add_label("")
label6 = frame.add_label("Start a new game with a range of 100")
button1 = frame.add_button("Range: 0 - 100", range100)
label7 = frame.add_label("")
label8 = frame.add_label("Start a new game with a range of 1000")
button2 = frame.add_button("Range: 0 - 1000", range1000)
frame.start()

# call new_game 
new_game()