# implementation of card game - Memory - by CDK
# Written on CodeSkulptor.org

import simplegui
import random


# helper function to initialize globals
def new_game():
    global click1, click2, deck, exposed, turns, state 
    click1 = 0
    click2 = 0
    deck = (range(8) + range(8))
    random.shuffle(deck)
    exposed = []
    for i in range(16):
        exposed.insert(i, False)
    turns = 0
    label.set_text("Turns = " + str(turns))
    state = 0
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global click1, click2, deck, exposed, turns, state
    selection = int(pos[0] / 50)
    print "Card Index:", str(selection)
    if state == 0:
        state = 1
        click1 = selection
        exposed[click1] = True
    elif state == 1:
        if not exposed[selection]:
            state = 2
            click2 = selection
            exposed[click2] = True
            turns += 1
            label.set_text("Turns = " + str(turns))
    else:
        if not exposed[selection]:
            if deck[click1] is not deck[click2]:
                exposed[click1] = False
                exposed[click2] = False
            click1 = selection
            exposed[click1] = True
            state = 1
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        if exposed[i]:
            canvas.draw_text(str(deck[i]), (50 * i + 10, 65), 55, "White")
        else:
            canvas.draw_polygon([(50 * i, 0), (50 * i, 100), (50 * i + 50, 100), (50 * i + 50, 0)], 5, "PaleGreen", "Olive")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()