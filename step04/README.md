# breakout - check if the player has won or lost

1. If there are not blocks left then the player has won.   
In the update function, before the final ball.velocity setting, add this code
```
if not blocks:
        sounds.win.play()
        print("Winner!")
        exit()
```

2. If the ball disappears off the bottom of the sceeen then the player has lost.
Just after the code addded above, add this code   
```
  if ball.top > HEIGHT:
        sounds.die.play()
        print("Loser!")
        exit()
```