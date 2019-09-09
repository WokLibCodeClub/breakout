# Step 7 - Ideas for a better game

Of course, no game is ever finished. There are always things we can do to improve them. Here are some suggestions for making Breakout even better:

#### 1. Randomise the ball starting position or velocities

You might notice that since the ball always starts from the same position it always follows the same route during the game. One way to change this is to make the ball start from a random position. 

To do this we have to import the Python function to generate random integers from the **random** library. At the top of your code (before the variable declarations) add:

`from random import randint`

One way to use this is by changing the declaration of the ball variable to something like

`ball = Rect(randint(0, WIDTH), HEIGHT/2, 30, 30)`

In this example the ball's initial x coordinate is set to a random integer between 0 and the width of the window, while the initial y coordinate is fixed at half way up the window.

There are lots of variations - having another `randint` function for the y coordinate, or introducing a random element into **vx** and **vy** so the ball's initial direction of travel might vary.

#### 2. Play again?

If you fancy playing the game more than once it's a bit annoying to have to restart it with pgzrun every time.

Luckily it is quite easy to add code to ask the player whether or not they want to play again.

2. Let the bat give the ball some spin

