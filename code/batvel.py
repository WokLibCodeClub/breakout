
# Set properties for game window
TITLE = 'Breakout'
WIDTH = 800
HEIGHT = 600

# Define variables for colours to use in game
RED = (200, 0, 0)
WHITE = (200, 200, 200)
GOLD = (205, 145, 0)


# Define a rectangle object variable for velocity bar graph
barht = 1 # height of bar graph
batvelbar = Rect(WIDTH * 0.8, HEIGHT * 0.5 - barht, 50, barht)
oldbatx = 0

# Define rectangle object variable for the bat
bat = Rect(WIDTH / 2, 0.9 * HEIGHT, 120, 15)


# Detect movement of mouse pointer and  set the centre of the 
# bat rectangle to the mouse pointer's x coordinate
def on_mouse_move(pos):
    x, y = pos
    bat.centerx = x


# Define function update() to measure batvel
def update():
    global oldbatx, barht
    batvel = bat.centerx - oldbatx
    barht = batvel 
    batvelbar.height = barht
    batvelbar.top = HEIGHT * 0.5 - barht
    oldbatx = bat.centerx

# Define function draw() to refresh the screen
def draw():
    # clear the screen
    screen.clear()
    # draw the bar graph using colour GOLD
    screen.draw.filled_rect(batvelbar, GOLD)
    # draw the bat using colour RED
    screen.draw.filled_rect(bat, RED)
