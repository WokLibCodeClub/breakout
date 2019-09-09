
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
    # Inner loop runs 8 times, block_col = 0,1,2,3,4,5,6,7
    for block_col in range(8):
        # Create a rectangle object in a variable called block
        block = Rect(
                         , # put your sum for the rectangle's x using block_col before the comma
                         , # put your sum for the rectangle's y using block_row before the comma
            96, # width of each block in pixels
            23  # height of each block in pixels
        )

        # Add new rectangle object block to the end of the blocks list 
        blocks.append(block)


# Define function draw() to refresh the screen
def draw():
    # clear the screen
    screen.clear()
    # draw all the blocks in the list blocks in colour GOLD
    for block in blocks:
        screen.draw.filled_rect(block, GOLD)

