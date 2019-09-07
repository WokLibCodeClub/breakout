## Breakout type game to demonstrate Pygame Zero library
## Based originally upon Tim Viner's London Python Dojo demonstration
## Licensed under MIT License - see file COPYING

# Specify the properties of the game window
TITLE = 'Breakout'
WIDTH = 800
HEIGHT = 600

# Create variables to use for colours in the game
RED = 200, 0, 0
WHITE = 200, 200, 200
GOLD = 205, 145, 0

# Create a rectangle object in variable ball and set its velocity
ball = ZRect(WIDTH*0.8, HEIGHT*0.8, 30, 30)
ball.velocity = (2, -2)

# Create a rectangle object in variable bat
bat = Rect(WIDTH/2, 0.9 * HEIGHT, 120, 15)

# Define function to detect movement of the mouse pointer
def on_mouse_move(pos):
    x, y = pos
    bat.centerx = x

# Define function update() to update ball velocity
def update():
    vx, vy = ball.velocity
    ball.move_ip(vx, vy)

    if ball.top < 0:
        vy = -vy

    if ball.left < 0 or ball.right > WIDTH:
        vx = -vx

    ball.velocity = vx, vy

# Define function draw() to keep refreshing the game window
def draw():
    screen.clear()
    screen.draw.filled_rect(ball, WHITE)
    screen.draw.filled_rect(bat, RED)

