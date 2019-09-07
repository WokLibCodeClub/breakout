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

# Create a rectangle object in variable ball
ball = ZRect(WIDTH / 2, HEIGHT / 2, 30, 30)
# Create a rectangle object in variable bat
bat = Rect(WIDTH / 2, 0.9 * HEIGHT, 120, 15)

# Define function to detect movement of the mouse pointer
def on_mouse_move(pos):
    x, y = pos
    bat.centerx = x

# Define function draw() to keep refreshing the game window
def draw():
    screen.clear()
    screen.draw.filled_rect(ball, WHITE)
    screen.draw.filled_rect(bat, RED)

