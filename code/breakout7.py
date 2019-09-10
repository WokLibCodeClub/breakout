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
ball = Rect(randint(20, WIDTH-50), HEIGHT/2, 30, 30)
# Set initial x and y velocities for the ball
vx = 5
vy = -5

# Create a variable to set how much the game speeds up each bat hit
speed_up = 1.05

# Create boolean variable to check if the game is over
gameover = False

# Define rectangle object variable for the bat
bat = Rect(WIDTH/2, HEIGHT - 50, 100, 15)

# Create an empty list variable called blocks
blocks = []

def makeblocks():
    # use the global variable blocks
    global blocks
    # Generate a list of rectangle objects for the blocks
    # Start with an empty list
    blocks = []
    # Use variable block_row to make four rows of blocks
    for block_row in range(4):
        # Use variable block_col to make 8 blocks in each row
        for block_col in range(8):
            # Create a rectangle object in variable block
            block = Rect(
                block_col * 100 + 2, # x position of left edge of block
                block_row * 25 + 50, # y position of top edge of block
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
    global vx, vy, gameover

    # move the ball by distance vx and vy in x and y directions
    ball.move_ip(vx, vy)

    # reverse x velocity if ball hits left wall
    if ball.left <= 0 and not gameover:
        vx = abs(vx)
        sounds.wall.play()

    # reverse x velocity if ball hits right wall
    if ball.right > WIDTH and not gameover:
        vx = -abs(vx)
        sounds.wall.play()

    # reverse y velocity if ball hits top wall
    if ball.top <= 0 and not gameover:
        vy = -abs(vy)
        sounds.wall.play()

    # play a sound, set gameover to True 
    # if ball goes below bottom wall
    if ball.top > HEIGHT and not gameover:
        sounds.die.play()
        # Stop the ball
        vx = 0
        vy = 0
        gameover = True

    # reverse y velocity and play sound if ball collides with bat
    if ball.colliderect(bat):
        sounds.bat.play()
        vy = -abs(vy)

        # increase x and y velocity if ball hits bat
        vy = vy * speed_up
        vx = vx * speed_up

    # If the ball hits one of the blocks ball.collidelist(blocks)
    # will give the index number of the hit block in the blocks list
    # otherwise it will be set it to -1

    if ball.collidelist(blocks) >= 0: # this means one of the blocks has been hit
        # play a sound
        sounds.block.play()
        # reverse the y velocity
        vy = -vy
        # remove the hit block from the blocks list
        blocks.pop(ball.collidelist(blocks))

    # test if the blocks list is now empty
    # ie all the blocks have been destroyed
    if not blocks and gameover == False:
        # play a sound, set gameover to True
        sounds.win.play()
        # Stop the ball
        vx = 0
        vy = 0
        gameover = True

    # if game over is True test for n pressed on keyboard
    if gameover and keyboard.n:
        exit()
    # if game over is True test for y pressed on keyboard
    elif gameover and keyboard.y:
        # Set initial x and y velocities for the ball
        vx = 5
        vy = -5
        # Set initial position for ball
        ball.topleft =(randint(20, WIDTH-50), HEIGHT/2)
        # Redraw the blocks
        makeblocks()
        # set gameover to False
        gameover = False


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

    if gameover:
        # Ask user whether to play again
        screen.draw.text('Play again (y) or (n)?', (30, HEIGHT - 30))

# Run function makeblocks() to create the blocks
makeblocks()