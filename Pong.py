# Implementation of classic arcade game Pong by CDK
# Written on CodeSkulptor.org

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

direction = " "
score1 = 0
score2 = 0
paddle1_pos = [HALF_PAD_WIDTH, (HEIGHT / 2)]
paddle2_pos = [(WIDTH - HALF_PAD_WIDTH), (HEIGHT / 2)]
paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    # initialize ball_pos
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    # initialize ball_vel
    ball_vel = [0, 0]
    ball_vel[0] = (random.randrange(120, 240)) / 60
    ball_vel[1] = (random.randrange(60, 180)) / 60
    if direction == RIGHT:
        ball_vel[1] = - ball_vel[1]
    elif direction == LEFT:
        ball_vel[0] = - ball_vel[0]
        ball_vel[1] = - ball_vel[1]
    else:
        first_vel = random.randrange(0, 2)
        if first_vel:
            ball_vel[1] = - ball_vel[1]
        else:
            ball_vel[0] = - ball_vel[0]
            ball_vel[1] = - ball_vel[1]
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2
    if score1 > score2:
        print "Player 1 wins!"
    elif score2 > score1:
        print "Player 2 wins!"
    elif score2 == score1 and score2 > 0:
        print "You tied! Lame."
    paddle1_pos = [HALF_PAD_WIDTH, (HEIGHT / 2)]
    paddle2_pos = [(WIDTH - HALF_PAD_WIDTH), (HEIGHT / 2)]
    score1 = 0
    score2 = 0
    spawn_ball(direction)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    
    # determine whether ball collides with top and bottom walls
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 3, "Yellow", "Aqua")
    
    # update paddle's vertical position, keep paddle on the screen
    if (HALF_PAD_HEIGHT <= paddle1_pos[1] + paddle1_vel <= (HEIGHT - HALF_PAD_HEIGHT)):
        paddle1_pos[1] += paddle1_vel
    if (HALF_PAD_HEIGHT <= paddle2_pos[1] + paddle2_vel <= (HEIGHT - HALF_PAD_HEIGHT)):
        paddle2_pos[1] += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[0, (paddle1_pos[1] - HALF_PAD_HEIGHT)], [PAD_WIDTH, (paddle1_pos[1] - HALF_PAD_HEIGHT)], [PAD_WIDTH, (paddle1_pos[1] + HALF_PAD_HEIGHT)], [0, (paddle1_pos[1] + HALF_PAD_HEIGHT)]], 3, "White", "White")
    canvas.draw_polygon([[(WIDTH - PAD_WIDTH), (paddle2_pos[1] - HALF_PAD_HEIGHT)], [WIDTH, (paddle2_pos[1] - HALF_PAD_HEIGHT)], [WIDTH, (paddle2_pos[1] + HALF_PAD_HEIGHT)], [(WIDTH - PAD_WIDTH), (paddle2_pos[1] + HALF_PAD_HEIGHT)]], 3, "White", "White")

    # determine whether paddle and ball collide    
    if (ball_pos[0] + ball_vel[0]) < (PAD_WIDTH + BALL_RADIUS):
        if ((paddle1_pos[1] - HALF_PAD_HEIGHT) <= ball_pos[1] <= (paddle1_pos[1] + HALF_PAD_HEIGHT)):
            ball_vel[0] *= -1.1
        else:
            spawn_ball(RIGHT)
            score2 += 1
    if (ball_pos[0] + ball_vel[0]) > (WIDTH - PAD_WIDTH - BALL_RADIUS):
        if ((paddle2_pos[1] - HALF_PAD_HEIGHT) <= ball_pos[1] <= (paddle2_pos[1] + HALF_PAD_HEIGHT)):
            ball_vel[0] *= - 1.1
        else:
            spawn_ball(LEFT)
            score1 += 1
   
    # draw scores
    canvas.draw_text(str(score1), ((WIDTH * .25), 75), 30, 'White')
    canvas.draw_text(str(score2), ((WIDTH * .75), 75), 30, 'White')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel += -4
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 4
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel += -4
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 4

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
button1 = frame.add_button("Restart", new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
