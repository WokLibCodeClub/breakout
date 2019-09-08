# Step 4 - How to get the bat to hit the ball

The code in breakout3.py on this page shows the project so far, except you will see in function update() that the if statements to check if the ball goes off the left or right edges have been combined into a single if statement by using the connecting word **or**. This makes the code shorter. It is often possible to combine two or more **if** statements into a single statement like this.

1. Detect a collision between bat and ball

   Pygame Zero has a special function to detect when two rectangle objects collide with each other called **colliderect()**.


[Go to step 5](../step04-add_sounds)