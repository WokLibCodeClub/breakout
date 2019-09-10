# Step 4 - How to get the bat to hit the ball

The code in breakout3.py on this page shows the project so far.

#### 1. Detect when the bat hits the ball

   When the ball moves down and hits the bat we want the ball to start going up again, so we need code to detect the hit and then to reverse the ball's y-direction velocity. 

   If two rectangles come together on the screen this creates a collision, and Pygame Zero has a special function to detect when two rectangle objects collide with each other called **colliderect()**. It is used like this:
   ```
   bat.colliderect(ball)
   ```
   This produces the value *True* if the ball rectangle is colliding with the bat rectangle and *False* otherwise. (It would work equally well if we typed ```ball.colliderect(bat)```, as the bat colliding with the ball is the same as the ball colliding with the bat.) This enables us to write another **if** statement in the function update(). Under the **if** statements for stopping the ball go off the edges add this
   ```
   if ball.colliderect(bat):
   ```
   then underneath write code (indented) which will reverse the ball's y velocity.

#### 2. Save and test your code

   You should now have a game where the ball bounces off the top and the sides of the window, and you can use the bat to stop it going off the bottom.


Challenge:
==========
Is the game a bit slow? What would you change to speed it up?

[Go to step 5](../step05-building_the_blocks)