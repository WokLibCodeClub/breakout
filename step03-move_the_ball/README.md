# Step 3 - Get the ball moving

If you've followed the instructions in Step 2 your code should look like the code in breakout2.py on this page. Note that there are comments added to show which parts of the code do which task. This is a very good thing to do in your Python coding.

1. Add a velocity property to the ball

   We mentioned that ZRect objects can have a property called velocity. This controls how fast the ball moves, and it is another *tuple* type of variable which has two values - how fast the ball moves in the x direction (left to right) and how fast it moves in the y direction (up and down).

   Under the line of code which creates the variable ball add this line:
   ```
   ball.velocity = (2,-2)
   ```

   As you will see we will slowly ramp up the ball's velocity to make the game more difficult!


2. Make a function called update()

   When Pygame Zero is running it looks in the code for a function called **update()** and it runs this function just before running the function **draw()***. So the place to put all the code which changes the position of objects is in function update(). 

   Add this code to create function update(). A good place for function update() is just before function draw().

   ```
   def update():
       vx, vy = ball.velocity
       ball.move_ip(vx, vy)
   ```
   The first line of the function uses two new variables, **vx** and **vy** to hold the two values of the ball.velocity tuple. The second line moves the ball by amount **vx* in the x direction and **vy** in the y direction.

4. Save the code and test it.

5. What to do if the ball goes off the edge?

   You probably saw the ball disappear off the top of the window. How can we stop this happening?

   When the ball gets to the top of the window its y coordinate will be equal to zero (in Pygame Zero y coordinates start at zero at the top of the window and increase downwards). So to stop the ball disappearing we need 
   a) an ```if``` statement to check when the ball's x coordinate becomes less than zero, and
   b) a statement which will reverse the ball y velocity, so that instead of moving upwards it moves downwards.

   Here is the code to *add* to function update() to make these things happen:
   ```
       if ball.top < 0:
           vy = -vy

       ball.velocity = vx, vy
   ```
   The first line tests if the top of the ball rectangle is at a y coordinate less than zero, the second line reverses the value of variable vy and the last line puts the new value of variable vy back into the ball's velocity property ready for the next time when the function is called.

   **Be careful with the indentation!** The if statement needs to be indented because it's part of function update(). The line inside the if statement needs to be indented *twice*, once because it's inside function update() and again because it's inside the if statement.

6. Reverse the x velocity if the ball goes off the sides

   Now add code for two more if statements to function update, one to test if the ball goes off the left edge and one to test if the ball goes off the right edge. In both cases you will want to reverse the x velocity of the ball. Test the values of the ball properties ball.right and ball.left in your if statements.

   Put the two if statements after the first if statement but before the line ball.velocity = vx, vy. Be careful to get the indentation correct.

7. Testing your code

   To check if your code is working make a change to the line of code where you created variable **ball**. Change it to
   ```
   ball = ZRect(WIDTH*0.8, HEIGHT*0.8, 30, 30)
   ```
   This will start the ball off a bit further to the right and lower down so you should be able to see it bounce off both the right and left edges.
   
   Now save your code and run it.

   Remember, we don't need to stop the ball going off the bottom of the window - in Breakout you lose a life if the ball goes off the bottom.

[Go to step 4](../step04-bat_on_ball)