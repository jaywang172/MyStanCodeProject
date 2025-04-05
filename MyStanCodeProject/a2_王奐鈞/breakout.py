"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This breakout game use campy to make a ball to break the bricks.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    The main function to run the Breakout game.
    It initializes the game objects, handles the game loop,
    and checks for win/loss conditions.
    """
    global NUM_LIVES

    graphics = BreakoutGraphics()
    ball = graphics.ball
    window = graphics.window
    lives = NUM_LIVES

    while graphics.get_vx() == 0 and graphics.get_vy() == 0:
        pause(FRAME_RATE)

    # Add the animation loop here!
    while True:
        vx = graphics.get_vx()
        vy = graphics.get_vy()

        ball.move(vx, vy)
        pause(FRAME_RATE)

        # Check if the ball falls below the window (lose a life)
        if ball.y + ball.height >= window.height:
            graphics.reset()
            lives -= 1

        # Check for game over conditions
        if lives == 0 or graphics.nums_of_brick == 0:
            break


if __name__ == '__main__':
    main()
