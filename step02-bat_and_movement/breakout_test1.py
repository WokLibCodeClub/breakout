## Breakout type game to demonstrate Pygame Zero library
## Based originally upon Tim Viner's London Python Dojo demonstration
## Licensed under MIT License - see file COPYING

TITLE = 'Breakout'
WIDTH = 800
HEIGHT = 600

RED = 200, 0, 0
WHITE = 200, 200, 200
GOLD = 205, 145, 0


ball = ZRect(WIDTH*0.8, HEIGHT*0.8, 30, 30)
ball.velocity = (2, -2)

bat = Rect(WIDTH / 2, 0.9 * HEIGHT, 120, 15)

def on_mouse_move(pos):
    x, y = pos
    bat.centerx = x

def draw():
    screen.clear()
    screen.draw.filled_rect(ball, WHITE)
    screen.draw.filled_rect(bat, RED)


def update():
    vx, vy = ball.velocity
    ball.move_ip(vx, vy)

    if ball.top < 0:
        vy = vy * -1

    if ball.left < 0:
        vx = vx * -1

    if ball.right > WIDTH:
        vx = vx * -1

    ball.velocity = vx, vy

