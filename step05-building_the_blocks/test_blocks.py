
# Set properties for game window
TITLE = 'Breakout'
WIDTH = 800
HEIGHT = 600

# Define variables for colours to use in game
RED = (200, 0, 0)
WHITE = (200, 200, 200)
GOLD = (205, 145, 0)

# Create an empty list variable called blocks
blocks = []

# Outer loop runs 4 times, block_row = 0,1,2,3
for block_row in range(4):
    # put your sum here for the y coord of the rectangles in the row using block_row
    block_x = 
    # Inner loop runs 8 times, block_col = 0,1,2,3,4,5,6,7
    for block_col in range(8):
        # put your sum here for the x coord of the rectangles in the column using block_col
        block_y  = 

        # Create a rectangle object in a variable called block
        block = Rect(block_x, block_y, 96, 23)

        # Add new rectangle object block to the end of the blocks list 
        blocks.append(block)

# Define function draw() to refresh the screen
def draw():
    # clear the screen
    screen.clear()
    # draw all the blocks in the list blocks in colour GOLD
    for block in blocks:
        screen.draw.filled_rect(block, GOLD)

