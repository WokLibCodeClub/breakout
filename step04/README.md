# Step 3 - Lets build the blocks - and remove them when hit

1. Create a new array variable (place it after the bat variable)
```
blocks = []
```
2. Now we need to fill this array with blocks, each block will have an x postion, y position, height and width.   
We will have 3 rows of 8. So we have a loop to create the rows and within this a loop to create the actual blocks.
The array object has a function to add entries to it called 'append'
```
for block_y in range(3):
    for block_x in range(8):
        block = Rect(
            block_x * 100 + 2,
            block_y * 25 + 2,
            96,
            23
        )
        blocks.append(block)
```
These blocks only exist in memory at the moment.
3. Now we want to actually draw the blocks array on to the screen.   
At the end of the draw function, add this code:
```
 for block in blocks:
        screen.draw.filled_rect(block, GOLD)
```
This iterate through the array, drawing each block as Gold, you can change the colour if you wish.   
4. Now we need to detect if the ball hits any blocks, and if so remove them for being displayed.   
At the end of the 'update' function but before the setting of the ball.veclocity - check if any blocks have been hit with this code  
```
 to_kill = ball.collidelist(blocks)
 ```
 This returns a list of what blocks have been hit.   
 ```
 if to_kill >= 0:
        sounds.block.play()
        vy = abs(vy)
        blocks.pop(to_kill)
 ```
 If we detect a block has been hit, play a sound and remove that particular block from the array
 5. Now test your code