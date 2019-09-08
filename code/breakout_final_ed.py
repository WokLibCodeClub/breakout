## Breakout type game to demonstrate Pygame Zero library
## Based originally upon Tim Viner's London Python Dojo demonstration
## Licensed under MIT License - see file COPYING

# import randint to use for random starting position of ball
from random import randint

# Set properties for game window
TITLE = 'Breakout'
WIDTH = 800
HEIGHT = 600

# Define variables for colours to use in game
RED = (200, 0, 0)
WHITE = (200, 200, 200)
GOLD = (205, 145, 0)


# Define a rectangle object variable for the ball
# and set initial x position to a random number between 0 and WIDTH
ball = Rect(randint(0, WIDTH), HEIGHT/2, 30, 30)
# Set initial x and y velocities for the ball
vx = 5
vy = -5

# Define rectangle object variable for the bat
bat = Rect(WIDTH/2, 0.9 * HEIGHT, 120, 15)

# Generate a list of rectangle objects for the blocks
# Create an empty list variable called blocks
blocks = []

# Use variable block_y to make four rows of blocks
for block_y in range(4):
    # Use variable block_x to make 8 blocks in each row
    for block_x in range(8):
        # Create a rectangle object in variable block
        block = Rect(
            block_x * 100 + 2, # x position of left edge of block
            block_y * 25 + 50, # y position of top edge of block
            96, # width of each block in pixels
            23  # height of each block in pixels
        )

        # The lines above from block = to ) are all part of one
        # Python instruction. You could put them all in a single line.
        # Python doesn't mind if you break a long line like this,
        # it makes the code a bit easier to read and to add comments.

        # Add new rectangle object block to the end of the blocks list 
        blocks.append(block)


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

    # play sound, print message and exit game 
    # if ball goes below bottom wall
    if ball.top > HEIGHT:
        sounds.die.play()
        print("Loser!")
        exit()

    # reverse y velocity and play sound if ball collides with bat
    if ball.colliderect(bat):
        sounds.blip.play()
        vy = -vy

        # increase x and y velocity if ball hits bat
        speed_up = 1.05
        vy = vy * speed_up
        vx = vx * speed_up

    # define a local variable called to_kill
    # If the ball hits one of the blocks set to_kill to
    # the index number of the hit block in the blocks list
    # otherwise set it to -1
    to_kill = ball.collidelist(blocks)

    if to_kill >= 0: # this means one of the blocks has been hit
        # play a sound
        sounds.block.play()
        # reverse the y velocity
        vy = -vy
        # remove the hit block from the blocks list
        blocks.pop(to_kill)

    # test if the blocks list is now empty
    # ie all the blocks have been killed
    if not blocks:
        # play a sound, print a message and exit
        sounds.win.play()
        print("Winner!")
        exit()

# Define function draw() to refresh the screen
def draw():
    # clear the screen
    screen.clear()
    # draw the ball using colour WHITE
    screen.draw.filled_rect(ball, WHITE)
    # draw the bat using colour RED
    screen.draw.filled_rect(bat, RED)
    # draw all the blocks in the blocks list in colour GOLD
    for block in blocks:
        screen.draw.filled_rect(block, GOLD)

