# Step 5 - Add the blocks

The object of Breakout is to get the ball to destroy all the blocks at the top of the window while preventing the ball from going off the bottom of the window. This section is about how to draw the blocks and how they get destroyed if the ball hits them.

The blocks will be rectangle objects, and we will put all the blocks in a Python *list*.

1. First, add this in the same part of your code where other variables (like bat, ball) are created, and before all the functions:
   ```
      blocks = []
   ```

   This line makes an empty *list* variable called **blocks**, where the blocks will be stored. 

2. Create the rectangles to put in the list
   The blocks will be rectangles which are 96 pixels wide and 23 pixels high, and we want four rows of blocks, with eight blocks in each row. We want to space them out to leave a narrow gap between each of the blocks. The ideal spacing will be to have the first block with its top left corner at coordinates x = 2, y = 50, then have them spaced them out every 100 pixels going across, and every 25 pixels going down. We could make each block individually:
   ```
   blocks[0] = Rect(2, 50, 96, 23)
   blocks[1] = Rect(102, 50, 96, 23)
   blocks[2] = Rect(202, 50, 96, 23)

   up to ...

   blocks[31] = Rect(702, 150, 96, 23)
   ```

   but that would be a TERRIBLY tedious way of making them and very likely to produce errors. Much better is to use a Python **for** loop where Python automatically calculates the positions and then adds each new block into the list.

   In fact, the best way of doing this is to use *two* **for** loops, with *one inside the other*. This is a common thing to do in coding. When loops are arranged one inside the other they are called *nested* loops.

3. Make nested **for** loops

4. Try out your code to make the blocks

   To test out your coding start a new Python file in your project, open the file test_blocks.py at the top of this page and copy the code into your new file. You now have to complete two lines of code, then run this file with ```pgzrun```. If you get the calculations right the screen should look like this:

![alt text](blocks_in_place.png "How the blocks should look")