"""
File: bouncing_ball.py
Name: Jay
-------------------------
This program simulates the motion of a bouncing ball. The ball starts at a defined position
and moves horizontally while bouncing vertically under the influence of gravity. The ball's
vertical speed decreases with each bounce to simulate energy loss. After the ball moves off
the right side of the window three times, it stops responding to user input.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# global variable
bouncing_time = 0
vertical_speed = 0
the_ball_at_the_start = True

window = GWindow(800, 500, title='bouncing_ball.py')

# to add the ball onto the window
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
ball.fill_color = 'black'
ball.color = 'black'
window.add(ball)

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    onmouseclicked(bouncing_ball)


def bouncing_ball(event):
    global bouncing_time
    global the_ball_at_the_start
    global vertical_speed

    # Prevent animation if the ball has already exited the window three times or if it is currently in motion
    if bouncing_time >= 3 or not the_ball_at_the_start:
        return

    # Update state to start animation
    the_ball_at_the_start = False
    bouncing_time += 1

    # Animate the ball's motion until it exits the right side of the window
    while not ball.x + SIZE / 2 > window.width:
        ball.move(VX, vertical_speed)
        vertical_speed += GRAVITY
        pause(DELAY)

        if ball.y + SIZE / 2 > window.height:
            vertical_speed = -vertical_speed * REDUCE

    # Reset the ball to the starting position after it exits the window
    if ball.x + SIZE / 2 > window.width:
        window.remove(ball)
        window.add(ball, x=START_X, y=START_Y)
        the_ball_at_the_start = True
        vertical_speed = 0

if __name__ == "__main__":
    main()
