# Step 1 - Let's create the screen and display a ball

1. Create a new folder called breakout to hold your code.

2. Navigate the terminal window to this new folder.
(If you are using VS Code as your editor the easiest way to do this is to go to
File>Open Folder, and select your new folder. By doing that you will ensure the 
Terminal opens in the right folder.)

3. Using your Python editor create a new empty file and save it as breakout.py

4. Set up the game window

The first steps are to specify the size of the game window. You can also give it a title. When run with Pygame Zero this code will control properties of the game window:

```
TITLE = 'Breakout'
WIDTH = 800
HEIGHT = 600
```
You can test your code so far by typing ```pgzrun breakout.py``` in the terminal. It will create the window for you although it won't do anything else, yet.

**To stop the code executing click on the red cross at the top right corner of the game window.**

5. Add some variables to the project

We are going to make some variables for the project. The first three are variables of a type called *tuples* which have a sequence of values, with the values separated by commas.

```
RED = (200, 0, 0)
WHITE = (200, 200, 200)
GOLD = (205, 145, 0)
```
We have given these variables the names of colours, but to Python they are simply sequences of numbers. Later on we will use these variables in Python instructions where the numbers will become the amounts of the colours red, green and blue which can be mixed together to form any colour.

The next variable is of a type called an *object*, in fact it is a Rectangle object. The function to make this rectangle object is ```ZRect()```. We will call the variable **ball**. When we create the rectangle object we have to specify the coordinates of the position of the rectangle, measured in pixels, and how big the rectangle is, also measured in pixels.
```
ball = ZRect(WIDTH/2, HEIGHT/2, 30, 30)
```
**Note** ```ZRect``` is *not* a standard Python function, so some Python editors (especially VS Code) might show an error at the word ```ZRect```. Don't worry about this. The code is correct.

The first two items in the brackets after ZRect give the x and y coordinates where the ball will be located, the next two items give the width and height of the ball.

The x coordinate of the ball is WIDTH/2, and the y coordinate is HEIGHT/2. Where on the screen do you think the ball will be placed with these values?

If you save your code and run it now you won't see a ball. That's because we need to write the code to *draw* the ball on the screen.

6. Write function **draw()**

Pygame Zero looks for a function called draw() when it runs code. It runs this function over and over again, 60 times a second. To write the draw function add this
```  
def draw():
    screen.clear()
    screen.draw.filled_rect(ball, WHITE)
```
**Note** ```screen``` is *not* a standard Python function, so some Python editors (especially VS Code) might show an error at the word ```screen```. Don't worry about this. The code is correct.

Inside the draw function are two other functions: the first will clear the screen, and the second will draw on the screen.

The second function tells Pygame Zero to draw a rectangle and fill it with colour. The items in the brackets specify where to get the details about the rectangle to draw (we get these details from our variable **ball** which is a rectangle object) and what colour to fill the rectangle with (WHITE is one of our variables created earlier - here it will be taken to mean add 200 units of red, 200 units of blue and 200 units of green together, which will make a very, very light grey). 

7. Save your code and test it with ```pgzrun breakout.py``` in the terminal window.

Did the code do what you expected?

Challenge:
==========

Change the size of the ball.

Change the position of the ball so it appears in the top left quarter of the window.

[Go to step 2](../step02-bat_and_movement)

Explanation of ```ZRect()```: Pygame Zero also has a function called ```Rect()``` for creating rectangle objects. The difference between this and ```ZRect()``` is that the coordinates of a ```Rect()``` object can only be whole numbers. A ```ZRect()``` object allows coordinates which are decimal numbers. In the code above the x coordinate of **ball** is specified as WIDTH/2, so if WIDTH happens to be an odd number this will generate a decimal number, so we have to make **ball** using ```ZRect()``` to avoid an error. The next step uses a ```Rect()``` object.