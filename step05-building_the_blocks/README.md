# Step 5 - Add the blocks

The object of Breakout is to get the ball to destroy all the blocks at the top of the window while preventing the ball from going off the bottom of the window. This section is about how to draw the blocks and how they get destroyed if the ball hits them.

The blocks will be rectangle objects, and we will put all the blocks in a Python *list*.

1. Make an empty list variable

   First, add this in the same part of your code where other variables (like bat, ball) are created, and before all the functions:
   ```
      blocks = []
   ```

   This line makes an empty *list* variable called **blocks**, where the blocks will be stored. 

2. Create the rectangles to put in the list

   The blocks will be rectangles which are 96 pixels wide and 23 pixels high, and we want four rows of blocks, with eight blocks in each row. We want to space them out to leave a narrow gap between each of the blocks. The ideal spacing will be to have the first block with its top left corner at coordinates x = 2, y = 50, then have them spaced them out every 100 pixels going across, and every 25 pixels going down. 

   We could make each block individually:
   ```
   blocks[0] = Rect(2, 50, 96, 23)
   blocks[1] = Rect(102, 50, 96, 23)
   blocks[2] = Rect(202, 50, 96, 23)

   up to ...

   blocks[31] = Rect(702, 150, 96, 23)
   ```
   but that would be a TERRIBLY tedious way of making them and very likely to produce errors. Much better is to use a Python **for** loop where Python automatically calculates the positions, creates the block and then adds the new block into the list.

   In fact, the best way of doing this is to use *two* **for** loops, with *one inside the other*. This is a common thing to do in coding. When loops are arranged one inside the other they are called *nested* loops.

3. Make nested **for** loops

   

4. Add the new block to the list of blocks (and how to remove a block from the list)

   The Python method for adding an item on to the end of a list is **append()**. If we type this Python code:
   ```
   my_list.append(new_item)
   ```
   this will add the object called new_item onto the end of the list called my_list. Think how you would adjust this code if you had a rectangle object called **block** which you wanted to add to the end of a list called **blocks**.

   There is also a Python method for removing an item from a list, called **pop()**. If we type:
   ```
   my_list.pop(unwanted_item)
   ```
   it does two things - it removes unwanted_item from the list and it shuffles all the other items in the list along so that there are no gaps in the list. 

   Sometimes we only know the index number of the item we want to remove from the list. So if we wanted to remove the fourth item from a list (which has index 3) we would type:
   ```
   my_list.pop(my_list[3])
   ```
   In the nested for loop for Breakout, as soon as we've made a new block with the Rect() function we need to add it to the list of blocks, so the next line of code should be and append() instruction.

5. Try out your code to make the blocks

   To test out your calculations start a new Python file in your project, open the file test_blocks.py at the top of this page and copy the code into your new file. You now have to complete two lines of code, to compute the values of **block_x** and **block_y** then run this file with ```pgzrun```. If you get the calculations right the screen should look like this:

![alt text](blocks_in_place.png "How the blocks should look")

6. Destroying the blocks

   A block (which is a rectangle object) will get destroyed when it gets hit by the ball (which is another rectangle object).

   In step 4 we saw the Pygame Zero function for checking if two rectangles are colliding. We could use this again to check if the ball was colliding with one of the blocks but we would have to check this for every single block. Luckily Pygame Zero has another function to check if a rectangle is colliding with any one of the rectangles in a list. The function is **collidelist()**.

   We use this code:
   ```
   ball.collidelist(blocks)
   ```
   This checks if the ball is colliding with any rectangle in the list called blocks, and, if it is, it gives us the index number of the block which is in the collision. If the ball isn't colliding with any of the blocks it gives us the value -1. We can use this in an **if** statement. 

   In the function update() there are already several if statements, so add this line under the other if statements (don't forget to indent it):
   ```
   if ball.collidelist(blocks) >= 0:
   ```

   This will be ignored if there is no collision between the ball and a block, but if there is a collision it will give us the index number of the block which has been hit.

   When a block is hit we want these things to happen:
     i) the block disappears - we do this by removing it from the list of blocks
    ii) the sound block.wav gets played
   iii) the y velocity of the ball gets reversed so the ball goes down if it was going up, or goes up if it was going down

   Under the if statement add lines of code (indented) to carry out these three tasks.

