# Step 2 - Add a bat and get it moving

If you've followed the instructions in Step 1 your code should look like the code in breakout1.py on this page. Note all the comment lines (which begin with #). These are very useful for identifying which part of your code does which task.

#### 1. Add a variable for the bat

The bat is another object of type rectangle. We will put it in a variable called **bat**.

A good Python rule is to place all the variables for your project together, near the top. So a good place to put this code is just after the code which adds the variable **ball**.
```
bat = Rect(WIDTH/2, HEIGHT - 50, 100, 15)
```
The x coordinate is WIDTH/2 and the y coordinate is 50 pixels less than the value of the variable HEIGHT. Where do you think this will place the bat? 

The width of the bat is 100 pixels and the height is only 15 pixels, so this will be a short wide rectangle.

#### 2. Modify the draw function

To show the bat in the window we need to add this line at the end of function draw(). **Don't forget to indent this line otherwise Python won't know it's part of the draw() function!**
```
    screen.draw.filled_rect(bat, RED)
```
This time we have used the variable RED to specify the colour to fill the rectangle. This variable tells Pygame Zero to add 200 units of red and no blue or green, which will produce a red colour.

#### 3. Save your code and run it

Check that the bat is now displayed.

#### 4. Moving the bat

We need a way to control the position of the bat. We will do this by moving the mouse.

In your code before function draw() define a new function called **on_mouse_move()**. This is a special Pygame Zero function which constantly checks the position of the mouse pointer in the game window, and puts the position in a variable called **pos**.

We need *two* coordinates to show the position of the mouse pointer (x coordinate and y coordinate), so the variable **pos** will be a *tuple* type of variable with two values. But in Breakout the bat only moves from side to side, not up and down, so we only actually need the mouse x coordinate to control the bat. 

We need a way to extract the different values from the tuple variable **pos**. Python does this using this code:
```
x, y = pos
```
This creates two new variables called **x** and **y** and puts the first value of **pos** into **x** (this will be the mouse pointer's x coordinate) and the second value of **pos** into **y** (this will be the mouse pointer's y coordinate). We want the x coordinate of the bat rectangle to be the same as the x coordinate of the mouse pointer - this will equal our new variable **x**. 

Pygame Zero has a special command for setting the x coordinate of the middle of the bat to variable **x**:
```
bat.centerx = x
```

It is important to use the American spelling center here (because Pygame Zero was written by an American).

The complete function **on_mouse_move()** is
```
def on_mouse_move(pos):
    x, y = pos
    bat.centerx = x
```

Put this function in your code just before function draw().

Whenever you move the mouse pointer this function updates the variable **pos** and takes the x coordinate of the mouse and sets the x coordinate of the bat to be the same. Try it and see it working!

#### 5. Save and test your code.

Does the bat move as you move the mouse pointer from side to side?

[Go to step 3](../step03-move_the_ball)
