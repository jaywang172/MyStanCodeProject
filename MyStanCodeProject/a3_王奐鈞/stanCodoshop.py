"""
File: stanCodoshop.py
Name: Jay
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import math
import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    dist = math.sqrt((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # Create all the useful variable
    total_pixel_red = 0
    total_pixel_green = 0
    total_pixel_blue = 0

    # To calculate the total of the RGB
    for pixel in pixels:
        total_pixel_red += pixel.red
        total_pixel_green += pixel.green
        total_pixel_blue += pixel.blue

    # Get average
    avg_pixel_red = total_pixel_red // len(pixels)
    avg_pixel_green = total_pixel_green // len(pixels)
    avg_pixel_blue = total_pixel_blue // len(pixels)
    return [avg_pixel_red, avg_pixel_green, avg_pixel_blue]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """

    # Create all the useful variable
    best_pixel = None
    min_dist = float("inf")

    [avg_pixel_red, avg_pixel_green, avg_pixel_blue] = get_average(pixels)

    for pixel in pixels:
        dist = get_pixel_dist(pixel, avg_pixel_red, avg_pixel_green, avg_pixel_blue)

        # To reassign the min_dist
        if min_dist > dist:
            min_dist = dist
            best_pixel = pixel

    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    # Double for loop to calculate all the pixel
    for y in range(height):
        for x in range(width):
            pixels = []
            for image in images:
                # Append all the pixel of image to the list
                pixels.append(image.get_pixel(x, y))
            best_pixel = get_best_pixel(pixels)
            result_pixel = result.get_pixel(x, y)

            # put the best pixel on the image
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue

    # ----- YOUR CODE ENDS HERE ----- #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
