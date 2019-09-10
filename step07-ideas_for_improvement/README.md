# Step 7 - Ideas for a better game

Of course, no game is ever finished. There are always things we can do to improve them. Here are some suggestions for making Breakout even better:

#### 1. Randomise the ball starting position or velocities

You might notice that since the ball always starts from the same position it always follows the same route during the game. One way to change this is to make the ball start from a random position. 

To do this we have to import the Python function to generate random integers from the **random** library. At the top of your code (before the variable declarations) add:

`from random import randint`

One way to use this is by changing the declaration of the ball variable to something like

`ball = Rect(randint(20, WIDTH - 50), HEIGHT/2, 30, 30)`

In this example the ball's initial x coordinate is set to a random integer between 20 pixels from the left edge and 50 pixels from the right edge of the window, while the initial y coordinate is fixed at half way up the window. This will ensure the ball starts from a different position when you play the game again.

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
   

3. Prevent sounds playing repeatedly when game ends
   We need to put in some extra control to avoid the sounds playing repeatedly at the end of the game. If the player has lost then the y coordinate of the top of the ball is greater than HEIGHT. Even though the game has stopped this will still be true, so every time the update() function tests for this it will play the die.wav sound. To stop this we can change the **if** statement slightly:

   ```if ball.top > HEIGHT and not gameover:```

   With this adjusted if statement we will only trigger the sound once. After the first time the variable **gameover** will be True, so this bit of code will not be executed.

   The same problem could occur if the player wins the game, or when the ball goes off the edges of the game window. Find the three **if** statements that test for the ball going outside the window and the **if** statement that checks for winning the game and for all of them add ```and not gameover``` at the end of the if line.

4. At the end of function draw() add this code:
   ```python
   if gameover:
       # Ask user whether to play again
       screen.draw.text('Play again (y) or (n)?', (30, HEIGHT - 30))
   ```
   This will be ignored if gameover is False (game in progress) but if the game has stopped (won or lost) this will cause the text "Play again (y) or (n)?" to be written on the screen at the bottom left corner.
   The text will stay there until gameover is reset to False.

5. Make all the code for creating the blocks into a function

   Before we start the game we need to create and draw the blocks. If we lose or win and want to play again we need to draw all the blocks again. To avoid writing exactly the same code twice we will turn this code into a function, then whenever we want to redraw the blocks we simply call the function.

   Above the line `for block_row in range(4):` type

   `def makeblocks():`

   then select all the lines down to and including the line `blocks.append(block)`, and press the TAB key. This should indent all this code which will make it part of the function.

   Whenever we run this function we should make sure we start with an empty blocks list, so copy the code `blocks = []` and paste this as the first line of function makeblocks().

   However, we now have a global variable called **blocks** which was created outside any function, and another variable called **blocks** created inside the function. To avoid confusion we need to ensure that we use the global variable inside the function, so as the very first line of the function add the code `global blocks`.

   We now need to call this function before the game starts for the first time. At the bottom of the code, after all the functions, and not indented at all, add the code

   `makeblocks()`

   This will run the function and create the list of blocks ready for the game to start.

6. Add code inside function update() to say what will happen when the player presses y or n

   We need yet another **if** statement in function update() to say what we want to happen when the player decides whether or not to play again. Here is the code for this:

   ```python
   # if game over is True test for n pressed on keyboard
   if gameover and keyboard.n:
       exit()
   # if game over is True test for y pressed on keyboard
   elif gameover and keyboard.y:
       # Set initial x and y velocities for the ball
       vx = 5
       vy = -5
       # Set initial position for ball
       ball.topleft =(randint(0, WIDTH), HEIGHT/2)
       # Redraw the blocks
       makeblocks()
       # set gameover to False
       gameover = False
   ```
   The first part of this tests for two things at the same time - if the game is stopped AND if the player has pressed n. If both of these are true then the game will exit.

   But if the game is not running and the player has pressed y to play again then we need several things to happen:
   - we need to reset the initial x and y velocity for the ball
   - we need to reset the intial position for the ball
   - we need to redraw all the blocks
   - we need to reset gameover to False, as the game is now in progress.
   The lines of code above do all of these things, after which the game is now ready to go again.

   If the game is not running but the player doesn't press y or n then these if conditions are false so they are ignored. If the game is running then these if conditions are false so they are ignored.

#### 3. Let the bat give the ball some spin

The original arcade game allowed the player to put spin on the ball by moving the bat sideways as it hit the ball. This would change the direction of the ball after the hit. We can add this feature as well.

We need to measure how fast the bat is moving, and we can do this inside function update(). Function update() runs repeatedly so if we measure the bat's x position then remeasure it the next time through function update() then the difference should show how fast the bat is moving.

1. First create a new global variable called oldbatx and set it to 0. Put this code with the other global variables:

   `oldbatx = 0`

   Inside function update() add oldbatx to the list of global variables at the top of this function.

2. Add code inside function update() to calculate the bat velocity and put it in a variable called batvel.

   `batvel = bat.centerx - oldbatx`

    Now we need to put the present x position of the bat into the variable oldbatx so that the function can use it to measure the new bat velocity next time through:

   `oldbatx = bat.centerx`

3. Use the value of batvel to change the ball's x direction velocity when the bat hits the ball

   Inside the if statement that checks for a collision between the bat and the ball and just after the variable **vy** is reversed in sign add a line to change the variable **vx**. There are lots of ways of doing it. Here is one suggestion:

   `vx = vx + batvel/5`

Try experimenting with changing the number 5 to make the effect bigger or smaller.

#### 4. Give the player more than one life before losing

#### 5. Add a score for each block destroyed.

#### 6. Make blocks of different colours with a different score for each colour