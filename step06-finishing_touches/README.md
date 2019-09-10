# Step 6 - Last steps to get the game working

#### 1. Speeding up the ball

You may have already increased the initial speed of the game by increasing the value of variables **vx** and **vy** to bigger than 2. If you haven't, try changing the values to 5 and -5. Now we want to add an extra feature where the ball gets faster every time it hits the bat.

First, make a variable called **speed_up** and set this to a value of 1.05. This will be a global variable so put it in the section of your code where other variables are declared. A good place would be just below the declarations for **vx** and **vy**.

Since we want the speed to increase whenever the ball hits the bat we need to add code inside the **if** block which tests for the ball hitting the bat - this begins `if ball.colliderect(bat):`. Inside this block add two lines of code which multiply the variables **vx** and **vy** by **speed_up**. This will make the ball travel faster every time it hits the bat. You can easily change the value of **speed_up** if you want to make this effect bigger or smaller. Experiment!

What do you think would happen if you set **speed_up** to a value less than 1?

#### 2. Winning and Losing

The player wins when all the blocks have been destroyed. When this happens the list of blocks **blocks** will be empty (because every time a block is hit it is removed from the list). When Python finds an empty list it treats the list as something which is `False`. This means we can test for an empty list to determine if the player has won. 

If a list called **blocks** is empty then the Python code

`not blocks:`

will give a value `True`. (It's complicated, but things which are `not False` are automatically `True`.)

Add yet another **if** statement to the function update() to check if the player has won. When the player wins we want the game to print the word "Winner!" on the terminal, and to exit the programme. Here is the code to add to update():
```python
    if not blocks:
        print("Winner!")
        exit()
```
But what about the player losing? If the ball goes off the bottom of the screen then the player has lost. We can easily check for this by testing the y coordinate of the top of the ball. If the player loses we want to print "Loser!" on the terminal and exit the programme.

Add another **if** statement to function update() which will carry out these tasks. (The **if** part will be very similar to the if statements you used to test if the ball went off the edges of the screen in step 3.)

#### 3. Add some sounds

The old arcade games used to make really annoying sounds as you played them, so, to be realistic, our version of Breakout will include some of these sounds.
When you use sounds in a Pygame Zero project you need to create a folder called **sounds** inside the project folder,to store all the sound files you want the programme to use. These should be .wav format files. 

To get the sounds you need for this game:

1. in your project folder make a folder called sounds

2. look at the top of this webpage for a folder icon labelled sounds and click on the icon. It will go to a new webpage where you will see five sound files. *For each file* click on the filename then in the new webpage click on the button at the right hand side labelled Download, and save the file in your new sounds folder. (After you download one file you will need to use the back button on your browser to get back to the list of files to get the next one.)

Now we need to write code to use these sound files.

We will use the sound bat.wav whenever the ball hits the bat.

- Find the line in your code where there is an if block which tests for a collision between the bat and the ball.
- At the end of this if block add
  
  `sounds.bat.play()`
  
  This is the Pygame Zero command to play the file bat.wav. (Make sure you indent this code to line up with the other statement inside the if block.)

We will use the sound wall.wav whenever the ball hits the side or the top walls

- Find the lines in your code where you test if the ball is about to go off the edges or the top of the game window.
- At the end of these three if blocks add
  
  `sounds.wall.play()`
  
We will use the sound block.wav whenever the ball hits one of the blocks

- Find the line in your code where there is an if statement which tests for a collision between the bat and any block.
- At the end of this if block add
  
  `sounds.block.play()`
  
We will use the sound win.wav when the player wins.

- Find the line in your code where you test for the list of blocks being empty.
- At the end of this if block add
  
  `sounds.win.play()`
  
We will use the die.wav sound when the player loses.
- Find the line in your code where you test if the ball goes off the bottom of the window.
- At the end of this if block add
  
  `sounds.die.play()`
  
#### 4. Try out your finished Breakout game

Save your code and run it. Enjoy playing...

[Go to step 7](../step07-ideas_for_improvement)