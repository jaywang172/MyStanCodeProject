"""
File:draw_line.py
Name:Jay
-------------------------
try to make a window that can track user's mouse to draw a line
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked,onmousedragged,onmousemoved

window = GWindow()

# Constants
SIZE = 10

# Global variables
first_point_x = 0
first_point_y = 0
first_point = None
is_first_click = True

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(make_the_initial_place)

def make_the_initial_place(mouse):
    """
    Handles the user's mouse click events. If it is the first click, it marks
    the point with a circle. If it is the second click, it draws a line from
    the first point to the current mouse position and removes the circle.
    """
    global first_point_x, first_point_y, is_first_click,first_point

    if is_first_click:
        # First click: Mark the point with a circle
        first_point = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        first_point_x = mouse.x - SIZE / 2
        first_point_y = mouse.y - SIZE / 2
        window.add(first_point)
        is_first_click = False
    else:
        # Second click: Draw a line from the first point to the current position
        line = GLine(first_point_x, first_point_y, mouse.x, mouse.y)
        window.add(line)

        # Remove the circle from the first click
        if first_point is not None:
            window.remove(first_point)
        is_first_click = True

if __name__ == "__main__":
    main()
