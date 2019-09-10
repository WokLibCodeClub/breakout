## Breakout type game to demonstrate Pygame Zero library
## Based originally upon Tim Viner's London Python Dojo demonstration
## Licensed under MIT License - see file COPYING

# Set properties for game window
TITLE = 'Breakout'
WIDTH = 800
HEIGHT = 600

# Define variables for colours to use in game
RED = (200, 0, 0)
WHITE = (200, 200, 200)
GOLD = (205, 145, 0)


# Define a rectangle object variable for the ball
ball = Rect(WIDTH * 0.8, HEIGHT * 0.8, 30, 30)
# Set initial x and y velocities for the ball
vx = 2
vy = -2

# Define rectangle object variable for the bat
bat = Rect(WIDTH/2, HEIGHT - 50, 100, 15)


# Detect movement of mouse pointer and  set the centre of the 
# bat rectangle to the mouse pointer's x coordinate
def on_mouse_move(pos):
    x, y = pos
    bat.centerx = x


# Define function update() to vary object position
def update():
    # Use global variables in the function
    global vx, vy

    # move the ball by distance vx and vy in x and y directions
    ball.move_ip(vx, vy)

    # reverse x velocity if ball hits left or right wall
    if ball.right > WIDTH or ball.left <= 0:
        vx = -vx

    # reverse y velocity if ball hits top wall
    if ball.top <= 0:
        vy = -vy

# Define function draw() to refresh the screen
def draw():
    # clear the screen
    screen.clear()
    # draw the ball using colour WHITE
    screen.draw.filled_rect(ball, WHITE)
    # draw the bat using colour RED
    screen.draw.filled_rect(bat, RED)
