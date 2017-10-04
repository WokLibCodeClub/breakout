## Breakout type game to demonstrate Pygame Zero library
## Based originally upon Tim Viner's London Python Dojo demonstration
## Licensed under MIT License - see file COPYING

TITLE = 'Breakout'
WIDTH = 804
HEIGHT = 600

RED = 200, 0, 0
WHITE = 200, 200, 200
GOLD = 205, 145, 0


ball = ZRect(WIDTH / 2, HEIGHT / 2, 30, 30)
ball.velocity = 5, -5

bat = Rect(WIDTH / 2, 0.96 * HEIGHT, 120, 15)

blocks = []
for block_y in range(3):
    for block_x in range(8):
        block = Rect(
            block_x * 100 + 2,
            block_y * 25 + 2,
            96,
            23
        )
        blocks.append(block)


def on_mouse_move(pos):
    x, y = pos
    bat.centerx = x

def draw():
    screen.clear()
    screen.draw.filled_rect(ball, WHITE)
    screen.draw.filled_rect(bat, RED)
    for block in blocks:
        screen.draw.filled_rect(block, GOLD)


def update():
    vx, vy = ball.velocity
    ball.move_ip(vx, vy)

    if ball.right > WIDTH or ball.left <= 0:
        vx = -vx

    if ball.top <= 0:
        vy = -vy

    if ball.colliderect(bat):
        sounds.blip.play()
        vy = -abs(vy)

        # Speed up!
        speed_up = 1.05
        vy = vy * speed_up
        vx = vx * speed_up

    to_kill = ball.collidelist(blocks)

    if to_kill >= 0:
        sounds.block.play()
        vy = abs(vy)
        blocks.pop(to_kill)

    if not blocks:
        sounds.win.play()
        print("Winner!")
        exit()

    if ball.top > HEIGHT:
        sounds.die.play()
        print("Loser!")
        exit()

    ball.velocity = vx, vy