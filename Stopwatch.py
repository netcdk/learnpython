# "Stopwatch: The Game" - by CDK
# Written on CodeSkulptor.org

# import modules
import simplegui

# define global variables
t = 0
minutes = 0
sec_tens = 0
sec_ones = 0
mil_sec_tenth = 0
time = "0:00.0"
interval = 100
stop_count = 0
stop_on_sec = 0

# helper function to state wins:attempts for
# each stop on a whole second
def win_count():
    global stop_on_secs, stop_count, stop_wins
    stop_wins = str(stop_on_sec) + "/" + str(stop_count)
    return stop_wins

# helper function that formats time, and stops
# timer at 9:59
def format():
    global t, minutes, sec_tens, sec_ones, mil_sec_tenth, time
    mil_sec_tenth = t % 10
    sec_ones = t % 100 // 10
    sec_tens = t % 600 // 100
    minutes = t // 600
    time = str(minutes) + ":" + str(sec_tens) + str(sec_ones) + "." + str(mil_sec_tenth)
    if time == "9:59:9":
        timer.stop()
    return time
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    timer.start()
    
def stop_timer():
    global stop_count, stop_on_sec, stop_wins
    if timer.is_running() and mil_sec_tenth == 0:
        stop_on_sec = stop_on_sec + 1
    if timer.is_running():
        stop_count = stop_count + 1
    timer.stop()
    return win_count()

def reset():
    timer.stop()
    global t, stop_count, stop_on_sec
    t = 0
    stop_count = 0
    stop_on_sec = 0
    format()
    win_count()
    
# event handler for timer that increments
# milliseconds by one tenth
def increment():
    global t
    t = t + 1
    format()

# draw handler
def draw_handler(canvas):
    canvas.draw_text(time, (92.5, 250), 125, "DimGray")
    canvas.draw_text(win_count(), (385, 50), 45, "DimGray")

    
# create frame
frame = simplegui.create_frame("Timer", 500, 500)
frame.set_canvas_background("DarkSeaGreen")
label1 = frame.add_label("Welcome to Stopwatch!")
label2 = frame.add_label("")
label3 = frame.add_label('Your "win to attempt" ratio is displayed in the upper right.')
label4 = frame.add_label("")
label5 = frame.add_label("")
label6 = frame.add_label("")
label7 = frame.add_label("")
label8 = frame.add_label("Controls:")
label9 = frame.add_label("")
button1 = frame.add_button('START', start_timer, 100)
label10 = frame.add_label("Start the timer.")
label11 = frame.add_label("")
button2 = frame.add_button('STOP', stop_timer, 100)
label12 = frame.add_label("Stop the timer, and test those reflexes!")
label13 = frame.add_label("")
button3 = frame.add_button('RESET', reset, 100)
label14 = frame.add_label('Reset the timer and the "win to attempt" ratio.')

# register event handlers
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, increment)


# start frame
frame.start()