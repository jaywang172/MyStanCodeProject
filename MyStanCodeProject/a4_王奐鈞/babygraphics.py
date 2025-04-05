"""
File: babygraphics.py
Name: Jay
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # To calculate and return the interval
    return GRAPH_MARGIN_SIZE + year_index * (width - 2 * GRAPH_MARGIN_SIZE) // len(YEARS)


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # Draw the straight and horizon line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    # To draw the all straight line
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=str(YEARS[i]), anchor=tkinter.NW,
                           fill='black')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)
    # ----- Write your code below this line ----- #
    color_index = 0

    # To loop all the names
    for name in lookup_names:
        if name in name_data:
            color = COLORS[color_index % len(COLORS)]
            color_index += 1

            # Create a list to store x and y coordinate
            x_and_y_coordinate = []

            # To loop all the years
            for i in range(len(YEARS)):
                year = str(YEARS[i])
                x = get_x_coordinate(CANVAS_WIDTH, i)

                # Check if the year is in name_data
                if year in name_data[name]:
                    rank = int(name_data[name][year])
                    y = GRAPH_MARGIN_SIZE + (rank / MAX_RANK) * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE)
                    rank_text = f"{name} {rank}"
                else:
                    y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    rank_text = f"{name} *"

                # append x_and_y_coordinate and text
                x_and_y_coordinate.append((x, y))
                canvas.create_text(x + TEXT_DX, y, text=rank_text, anchor=tkinter.SW, fill=color)

            # Connect each year's ranking data points with lines to visualize the trend
            for j in range(len(x_and_y_coordinate) - 1):
                canvas.create_line(x_and_y_coordinate[j][0], x_and_y_coordinate[j][1], x_and_y_coordinate[j + 1][0],
                                   x_and_y_coordinate[j + 1][1], width=LINE_WIDTH,
                                   fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY


def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
