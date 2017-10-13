# Step 2 - Add a bat and get the bat and ball moving

1. Add a bat variable of type Rect
```
bat = Rect(WIDTH / 2, 0.96 * HEIGHT, 120, 15)
```
Intially positioned to be halfway across the screen, near the bottom.
2. Modify the draw function to also draw the bat
```
 screen.draw.filled_rect(bat, RED)
```
3. Test the code to prove that the bat is now displayed
4. Now add some code, before the draw function,  to move the bat in response to the mouse
```
def on_mouse_move(pos):
    x, y = pos
    bat.centerx = x
```
The Pygame Zero framework will invoke this function everytime the mouse moves, passing the position of the mouse.
The bat's position is now set to this position.
5. Now test the code
6. Let's get the ball moving.
Create a new function called Update, this will be invoked by the framework every second. Move the ball, based on the setting of the ball's velocity.
```
def update():
    vx, vy = ball.velocity
    ball.move_ip(vx, vy)
```
7. Test the code, you will see that the ball immediately disappears off the screen. We need to add code to 'bounce' it off the edges.
```
    if ball.right > WIDTH or ball.left <= 0:
        vx = -vx
```
If the ball is at the edge of the screen left or right, then change the vx variable to be the opposite (if 5, now it will be -5), this will control the horizontal direction of the ball.
```
    if ball.top <= 0:
        vy = -vy
```
If the ball is at the top of the screen, the make the vertical direction negative (it will travel down the screen).   
Now use the new vx and vy settings to change the ball's direction.
```
 ball.velocity = vx, vy
```
8. Test the code.
9. Now we need the ball to bounce of the bat when its hit. Add the following code to just before we setting the ball.velocity variable.
```
 if ball.colliderect(bat):
        sounds.blip.play()
        vy = -abs(vy)

        # Speed up!
        speed_up = 1.05
        vy = vy * speed_up
        vx = vx * speed_up
```
If the ball hits the bat then play a sound and reverse the vy value (travel upwards). Also increase the speed of the ball
10. Now test your code.
