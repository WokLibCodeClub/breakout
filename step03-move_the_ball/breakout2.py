## Breakout type game to demonstrate Pygame Zero library
## Based originally upon Tim Viner's London Python Dojo demonstration
## Licensed under MIT License - see file COPYING

TITLE = 'Breakout'
WIDTH = 800
HEIGHT = 600

RED = 200, 0, 0
WHITE = 200, 200, 200
GOLD = 205, 145, 0


ball = ZRect(WIDTH / 2, HEIGHT / 2, 30, 30)

bat = Rect(WIDTH / 2, 0.9 * HEIGHT, 120, 15)

def on_mouse_move(pos):
    x, y = pos
    bat.centerx = x

def draw():
    screen.clear()
    screen.draw.filled_rect(ball, WHITE)
    screen.draw.filled_rect(bat, RED)

