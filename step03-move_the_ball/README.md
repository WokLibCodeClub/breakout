# Step 3 - Get the ball moving

If you've followed the instructions in Step 2 your code should look like the code in breakout2.py on this page. Note that there are comments added to show which parts of the code do which task. This is a very good thing to do in your Python coding.

#### 1. Add variables for the initial velocity of the ball

   We need two new variables, which we could call **vx** and **vy** to set the initial velocity of the ball in the x direction and y direction. Underneath the line which creates the ball rectangle object add two lines to set the variable **vx** to a value of 2 and the variable **vy** to a value -2.

   If the x direction velocity is positive the ball will move to the right; if the y direction velocity is positive the ball will move downwards.

   We use variables for vx and vy because, as you will see later, we will slowly ramp up the ball's velocity to make the game more difficult!


#### 2. Make a function called update()

   When Pygame Zero is running it looks in the code for a function called **update()** and it runs this function just before running the function **draw()**. So the place to put all the code which changes the position of objects is in function update(). 

   Add this code to create function update(). A good place for function update() is just before function draw().

   ```
   def update():
       global vx, vy
       ball.move_ip(vx, vy)
   ```
   The second line (which must be indented) tells this function that when we use the variables vx and vy we mean the variables which we already created outside the function. Variables created outside any function are called *global variables*.

   The third line (also indented) moves the ball by amount **vx** in the x direction and **vy** in the y direction.

#### 4. Save the code and test it.

#### 5. What to do if the ball goes off the top edge?

   You probably saw the ball disappear off the top of the window. How can we stop this happening?

   When the ball gets to the top of the window its y coordinate will be equal to zero (in Pygame Zero y coordinates start at zero at the top of the window and increase downwards). 
   
   To see an diagram of the coordinate system in Pygame Zero projects look [here](https://github.com/WokLibCodeClub/LetterA/blob/master/Step1-display_letter/window.png)

   So to stop the ball disappearing off the top we need 

   a) an ```if``` statement to check when the ball's y coordinate becomes less than zero, and

   b) a statement which will reverse the ball's y velocity, so that instead of moving upwards it moves downwards.

   Add the following code to function update():
   ```
       if ball.top < 0:
           vy = -vy
   ```
   The first line tests if the top of the ball rectangle is at a y coordinate less than zero, the second line changes the sign of the value of variable vy.

   **Be careful with the indentation!** The if statement needs to be indented because it's part of function update(). The line inside the if statement needs to be indented *twice*, once because it's inside function update() and again because it's inside the if statement.
   
   Run your code with pgzrun to check that the ball now bounces off the top wall.

#### 6. Reverse the x velocity if the ball goes off the sides

   We've made the ball bounce when it hits the top wall - now to make it bounce when it hits the side walls.
   
   As the ball goes from side to side its x coordinate changes, so when the ball gets to the *left* edge of the window its x coordinate will be equal to zero. What would the ball's x coordinate be when it gets to the *right* edge of the window?

   Now add two more **if** statements to function update(), one to test if the ball goes off the left edge and one to test if the ball goes off the right edge. They will look quite similar to the code above. In both cases you will want to reverse the x velocity of the ball - this is in variable **vx**. Use the properties of the ball called ball.right and ball.left in your if statements.

#### 7. Testing your code

   To check if your code is working make a change to the line of code where you created variable **ball**. Change it to
   ```
   ball = Rect(WIDTH*0.8, HEIGHT*0.8, 30, 30)
   ```
   This will start the ball off a bit further to the right and lower down so you should be able to see it bounce off both the right and left edges if your code is working properly.
   
   Now save your code and run it.

   We don't need to make the ball bounce off the bottom wall - in Breakout the challenge is to stop the ball going off the bottom of the window.

[Go to step 4](../step04-bat_on_ball)
