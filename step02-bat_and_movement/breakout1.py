## Breakout type game to demonstrate Pygame Zero library
## Based originally upon Tim Viner's London Python Dojo demonstration
## Licensed under MIT License - see file COPYING


# Set properties for game window
TITLE = 'Breakout'
WIDTH = 800
HEIGHT = 600

# Define variables for colours to use in game
RED = 200, 0, 0
WHITE = 200, 200, 200
GOLD = 205, 145, 0

# Define a rectangle object variable for the ball
ball = Rect(WIDTH/2, HEIGHT/2, 30, 30)

# Define function draw() to refresh the screen
def draw():
    # clear the screen
    screen.clear()
    # draw the ball using colour WHITE
    screen.draw.filled_rect(ball, WHITE)
