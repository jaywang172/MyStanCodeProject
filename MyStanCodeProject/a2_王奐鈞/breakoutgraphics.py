"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This file defines the BreakoutGraphics class, which handles
all the game objects, event listeners, and collision detection.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved

import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
DELAY = 700


class BreakoutGraphics:
    """
    This class manages all the graphical components of the Breakout game.
    It includes the game window, paddle, ball, bricks, and event listeners.
    """

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width - paddle_width) // 2,
                            y=window_height - paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = "black"
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(window_width-ball_radius) // 2,
                          y=(window_height-ball_radius) // 2)
        self.ball.filled = True
        self.ball.fill_color = "black"
        self.window.add(self.ball)

        # Store ball radius for later calculations
        self.ball_radius = ball_radius

        # Default initial velocity for the ball
        self.__vx = 0
        self.__vy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.set_game_start)
        onmousemoved(self.set_mouse_drag)

        # Draw bricks
        for i in range(brick_cols):
            for j in range(0, brick_rows):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT, x=j*(brick_width+brick_spacing),
                                   y=i*(brick_height+brick_spacing)+brick_offset)
                self.brick.filled = True
                if i <= 1:
                    self.brick.fill_color = "red"
                elif 3 >= i > 1:
                    self.brick.fill_color = "orange"
                elif 5 >= i > 3:
                    self.brick.fill_color = "yellow"
                elif 7 >= i > 5:
                    self.brick.fill_color = "green"
                elif 9 >= i > 7:
                    self.brick.fill_color = "blue"
                self.window.add(self.brick)

        # Track remaining bricks
        self.nums_of_brick = brick_cols * brick_rows

    def set_game_start(self, mouse):
        """
        Starts the game when the mouse is clicked, setting the ball in motion.
        Ensures that the ball only starts once.
        """
        if self.__vx == 0 and self.__vy == 0:
            self.__vy = INITIAL_Y_SPEED
            self.__vx = random.randrange(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__vx = -self.__vx

    def set_mouse_drag(self, mouse):
        """
        Moves the paddle based on the mouse's x-position.
        Ensures the paddle does not go beyond the window's boundaries.
        """
        self.paddle.x = mouse.x - PADDLE_WIDTH / 2
        if mouse.x - PADDLE_WIDTH / 2 < 0:
            self.paddle.x = 0
        elif mouse.x + PADDLE_WIDTH / 2 > self.window.width:
            self.paddle.x = self.window.width - PADDLE_WIDTH

    def get_vx(self):
        """
        Returns the ball's x velocity. Reverses direction if the ball hits the window boundary.
        """
        if self.ball.x + self.ball.width / 2 > self.window.width or self.ball.x < 0:
            self.__vx = -self.__vx
        return self.__vx

    def get_vy(self):
        """
        Returns the ball's y velocity. Handles collisions with the paddle and bricks.
        """
        if self.ball.y + self.ball.height / 2 > self.window.height or self.ball.y < 0:
            self.__vy = -self.__vy

        # Check the four corners of the ball for collision
        maybe_object_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        maybe_object_2 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y)
        maybe_object_3 = self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball_radius)
        maybe_object_4 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y + 2 *
                                                   self.ball_radius)

        # If the ball hits the paddle
        if maybe_object_1 == self.paddle or maybe_object_2 == self.paddle or maybe_object_3 == self.paddle or \
                maybe_object_4 == self.paddle:
            if self.__vy > 0:
                self.__vy = - self.__vy
                # To prevent the ball stock in paddle
                self.ball.y = self.paddle.y - self.ball.height - 1

        # If the ball hits a brick
        elif maybe_object_1 is not None and maybe_object_1 != self.paddle:
            self.window.remove(maybe_object_1)
            self.__vy = -self.__vy
            self.nums_of_brick -= 1

        elif maybe_object_2 is not None and maybe_object_2 != self.paddle:
            self.window.remove(maybe_object_2)
            self.__vy = -self.__vy
            self.nums_of_brick -= 1

        elif maybe_object_3 is not None and maybe_object_3 != self.paddle:
            self.window.remove(maybe_object_3)
            self.__vy = -self.__vy
            self.nums_of_brick -= 1

        elif maybe_object_4 is not None and maybe_object_4 != self.paddle:
            self.window.remove(maybe_object_4)
            self.__vy = -self.__vy
            self.nums_of_brick -= 1

        return self.__vy

    def reset(self):
        """
        Resets the ball to its original position and stops its movement.
        """
        self.ball.x = (self.window.width - self.ball.width) // 2
        self.ball.y = (self.window.height - self.ball.height) // 2

        self.__vx = 0
        self.__vy = 0

    def set_vx(self, vx):
        """
        Sets the x velocity of the ball.
        """
        self.__vx = -self.__vx
        return self.__vx

    def set_vy(self, vy):
        """
        Sets the  velocity of the ball.
        """
        self.__vy = -self.__vy
        return self.__vy



