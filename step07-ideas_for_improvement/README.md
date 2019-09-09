# Step 7 - Ideas for a better game

Of course, no game is ever finished. There are always things we can do to improve them. Here are some suggestions for making Breakout even better:

#### 1. Randomise the ball starting position or velocities

You might notice that since the ball always starts from the same position it always follows the same route during the game. One way to change this is to make the ball start from a random position. 

To do this we have to import the Python function to generate random integers from the **random** library. At the top of your code (before the variable declarations) add:

`from random import randint`

One way to use this is by changing the declaration of the ball variable to something like

`ball = Rect(randint(0, WIDTH), HEIGHT/2, 30, 30)`

In this example the ball's initial x coordinate is set to a random integer between 0 and the width of the window, while the initial y coordinate is fixed at half way up the window. This will ensure the ball starts from a different position when you play the game again.

There are lots of possible variations - having another `randint` function for the y coordinate, or introducing a random element into **vx** and **vy** so the ball's initial direction of travel can vary.

#### 2. Play again?

If you fancy playing the game more than once it's a bit annoying to have to restart it with pgzrun every time.

Luckily it is not too difficult to add code to ask the player whether or not they want to play again. There are several stages to doing this.
1. Make a global variable called **gameover** and set it to False

   `gameover = False`

   Place this with the other global variables near the top of the code.

   We are going to use this global variable inside function update(). So at the beginning of this function add the variable `gameover` to the list of global variables which currently has `vx` and `vy`.
 
2. The variable gameover will only be True when the player either wins or loses.
   Inside the if statement which checks for winning add

   `gameover = True`

   Delete the line which prints "Winner!" at the terminal, and delete the line which exits the programme.

   Add the same code inside the if statement which checks for losing. Delete the line which prints "Loser!" at the terminal, and delete the line which exits the programme.
   

3. At the end of function draw() add this code:

```python
    if gameover:
        # Ask user whether to play again
        screen.draw.text('Play again (y) or (n)?', (30, HEIGHT - 30))
```
   This will be ignored if gameover is False (game in progress) but if the game has stopped (won or lost) this will cause the text "Play again (y) or (n)?" to be written on the screen at the bottom left corner.
   The text will stay there until gameover is reset to False.

4. Make all the code for creating the blocks into a function

   Before we start the game we need to create and draw the blocks. If we lose or win and want to play again we need to draw all the blocks again. To avoid writing exactly the same code twice we will turn this code into a function, then whenever we want to redraw the blocks we simply call the function.

   Above the line `for block_row in range(4):`

   `def makeblocks():`

   then select all the lines down to and including the line `blocks.append(block)`, then press the TAB key. This should indent all this code which will make it part of the function.

   When we run this function we should start again with an empty blocks list, so copy the code `blocks = []` and paste this as the first line of function makeblocks().

   However, we now have a global variable called **blocks** which was created outside any function, and another variable called **blocks** created inside the function. To avoid confusion we need to ensure that we use the global variable inside the function, so as the very first line of the function add the code `global blocks`.

   We now need to call this function before the game starts for the first time. At the bottom of the code, after all the functions, and not indented at all, add the code

   `makeblocks()`

   This will create the list of blocks ready for the game to start.

5. 

#### 3. Let the bat give the ball some spin

