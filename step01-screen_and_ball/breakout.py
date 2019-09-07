## Breakout type game to demonstrate Pygame Zero library
## Based originally upon Tim Viner's London Python Dojo demonstration
## Licensed under MIT License - see file COPYING

TITLE = 'Breakout'
WIDTH = 800
HEIGHT = 600

RED = 200, 0, 0
WHITE = 200, 200, 200
GOLD = 205, 145, 0


ball = ZRect(WIDTH/2, HEIGHT/2, 30, 30)

def draw():
    screen.clear()
    screen.draw.filled_rect(ball, WHITE)

    

