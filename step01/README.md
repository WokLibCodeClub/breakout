# Step 1 - Let's create the screen and display a ball

1. Create a new empty file and save it as breakout.py
2. Create a folder called sounds and download the files from here into it.
3. Set the title, height and width of the screen.
```
TITLE = 'Breakout'
WIDTH = 804
HEIGHT = 600
```
These are variables that will not change, known as constants. Constants always have their name as uppercase.
4. Let's create 3 further constants for colours to use later, these contain the appropriate RGB (Red,Green,Blue) values.
```
RED = 200, 0, 0
WHITE = 200, 200, 200
GOLD = 205, 145, 0
```
5. Now create the ball. This is of a special data type called ZRect, which is requires x and y co-ordinatees to decide where to display it on the screen and height, width parameters to set the size.
```
ball = ZRect(WIDTH / 2, HEIGHT / 2, 30, 30)
```
We then set the velocity of the ball, this is the speed and direction of the ball
```
ball.velocity = 5, -5
```  
6. Now we need to implement the draw function, this is called by the Pygame Zero framework at the start of the program to display the screen.
```  
def draw():
    screen.clear()
    screen.draw.filled_rect(ball, WHITE)
```
This will initially clear the screen and show the ball as white.  
7. Save and test your code

