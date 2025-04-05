"""
File: my_drawing.py
Name:Jay
----------------------
try to draw a mario
"""

from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow

window = GWindow(width=240, height=340, title="Pixel Mario")

# Constants
SIZE = 20

def main():
    """
    Title: Marvelous era of nostalgia

    Mario is not just a character;
    he represents an entire generation's childhood,filled with the
    joy and wonder of early console gaming. For many of us, Mario was
    our companion during countless hours of adventure on TV gaming ,
    bringing unforgettable memories and moments of happiness.
    """

    # Hat
    upper_hat = GRect(SIZE * 5, SIZE, x=60, y=0)
    upper_hat.color = 'firebrick'
    upper_hat.filled = True
    upper_hat.fill_color = 'firebrick'
    window.add(upper_hat)

    down_hat = GRect(SIZE * 8.5, SIZE, x=40, y=20)
    down_hat.color = 'firebrick'
    down_hat.filled = True
    down_hat.fill_color = 'firebrick'
    window.add(down_hat)

    # Ears
    ear = GRect(SIZE * 3, SIZE, x=40, y=40)
    ear.color = 'darkgray'
    ear.filled = True
    ear.fill_color = 'darkgray'
    window.add(ear)

    ear_left = GRect(SIZE, SIZE * 2, x=20, y=60)
    ear_left.color = 'darkgray'
    ear_left.filled = True
    ear_left.fill_color = 'darkgray'
    window.add(ear_left)

    ear_right = GRect(SIZE, SIZE * 2, x=60, y=60)
    ear_right.color = 'darkgray'
    ear_right.filled = True
    ear_right.fill_color = 'darkgray'
    window.add(ear_right)

    ear_more = GRect(SIZE, SIZE, x=80, y=80)
    ear_more.color = 'darkgray'
    ear_more.filled = True
    ear_more.fill_color = 'darkgray'
    window.add(ear_more)

    ear_down = GRect(SIZE, SIZE, x=40, y=100)
    ear_down.color = 'darkgray'
    ear_down.filled = True
    ear_down.fill_color = 'darkgray'
    window.add(ear_down)

    # Face
    face_left = GRect(SIZE, SIZE * 2, x=40, y=60)
    face_left.color = 'peru'
    face_left.filled = True
    face_left.fill_color = 'peru'
    window.add(face_left)

    face_middle = GRect(SIZE * 2, SIZE * 3, x=100, y=40)
    face_middle.color = 'peru'
    face_middle.filled = True
    face_middle.fill_color = 'peru'
    window.add(face_middle)

    face_down = GRect(SIZE * 4, SIZE * 2, x=60, y=100)
    face_down.color = 'peru'
    face_down.filled = True
    face_down.fill_color = 'peru'
    window.add(face_down)

    face_point = GRect(SIZE, SIZE, x=80, y=60)
    face_point.color = 'peru'
    face_point.filled = True
    face_point.fill_color = 'peru'
    window.add(face_point)

    face_another_point = GRect(SIZE, SIZE * 2, x=160, y=40)
    face_another_point.color = 'peru'
    face_another_point.filled = True
    face_another_point.fill_color = 'peru'
    window.add(face_another_point)

    face_point_again = GRect(SIZE * 2, SIZE * 2, x=180, y=60)
    face_point_again.color = 'peru'
    face_point_again.filled = True
    face_point_again.fill_color = 'peru'
    window.add(face_point_again)

    face_point_point = GRect(SIZE, SIZE, x=220, y=80)
    face_point_point.color = 'peru'
    face_point_point.filled = True
    face_point_point.fill_color = 'peru'
    window.add(face_point_point)

    face_final_point = GRect(SIZE, SIZE, x=140, y=80)
    face_final_point.color = 'peru'
    face_final_point.filled = True
    face_final_point.fill_color = 'peru'
    window.add(face_final_point)

    # Facial Features
    eye = GRect(SIZE, SIZE * 2, x=140, y=40)
    eye.color = 'black'
    eye.filled = True
    eye.fill_color = 'black'
    window.add(eye)

    nose = GRect(SIZE, SIZE, x=160, y=80)
    nose.color = 'black'
    nose.filled = True
    nose.fill_color = 'black'
    window.add(nose)

    mouse = GRect(SIZE * 4, SIZE, x=140, y=100)
    mouse.color = 'black'
    mouse.filled = True
    mouse.fill_color = 'black'
    window.add(mouse)

    # Chin
    double_chin = GRect(SIZE * 2, SIZE, x=140, y=120)
    double_chin.color = 'peru'
    double_chin.filled = True
    double_chin.fill_color = 'peru'
    window.add(double_chin)

    # Shirt
    left_shirt = GRect(SIZE * 4, SIZE * 3, y=140)
    left_shirt.color = 'firebrick'
    left_shirt.filled = True
    left_shirt.fill_color = 'firebrick'
    window.add(left_shirt)

    space_left = GRect(SIZE, SIZE * 2, y=140)
    space_left.color = 'white'
    space_left.filled = True
    space_left.fill_color = 'white'
    window.add(space_left)

    space_left_again = GRect(SIZE, SIZE, x=20, y=140)
    space_left_again.color = 'white'
    space_left_again.filled = True
    space_left_again.fill_color = 'white'
    window.add(space_left_again)

    shirt_left_more = GRect(SIZE, SIZE, x=40, y=200)
    shirt_left_more.color = 'firebrick'
    shirt_left_more.filled = True
    shirt_left_more.fill_color = 'firebrick'
    window.add(shirt_left_more)

    neckline = GRect(SIZE * 2, SIZE * 2, x=100, y=140)
    neckline.color = 'firebrick'
    neckline.filled = True
    neckline.fill_color = 'firebrick'
    window.add(neckline)

    right_shirt = GRect(SIZE * 4, SIZE * 3, x=160, y=140)
    right_shirt.color = 'firebrick'
    right_shirt.filled = True
    right_shirt.fill_color = 'firebrick'
    window.add(right_shirt)

    space_right = GRect(SIZE * 2, SIZE, x=200, y=140)
    space_right.color = 'white'
    space_right.filled = True
    space_right.fill_color = 'white'
    window.add(space_right)

    space_right_again = GRect(SIZE, SIZE, x=220, y=160)
    space_right_again.color = 'white'
    space_right_again.filled = True
    space_right_again.fill_color = 'white'
    window.add(space_right_again)

    shirt_right_more = GRect(SIZE, SIZE, x=180, y=200)
    shirt_right_more.color = 'firebrick'
    shirt_right_more.filled = True
    shirt_right_more.fill_color = 'firebrick'
    window.add(shirt_right_more)

    # Arms and Hands
    left_hand = GRect(SIZE * 2, SIZE * 3, y=200)
    left_hand.color = 'peru'
    left_hand.filled = True
    left_hand.fill_color = 'peru'
    window.add(left_hand)

    left_hand_finger = GRect(SIZE, SIZE, x=40, y=220)
    left_hand_finger.color = 'peru'
    left_hand_finger.filled = True
    left_hand_finger.fill_color = 'peru'
    window.add(left_hand_finger)

    right_hand = GRect(SIZE * 2, SIZE * 3, x=200, y=200)
    right_hand.color = 'peru'
    right_hand.filled = True
    right_hand.fill_color = 'peru'
    window.add(right_hand)

    right_hand_finger = GRect(SIZE, SIZE, x=180, y=220)
    right_hand_finger.color = 'peru'
    right_hand_finger.filled = True
    right_hand_finger.fill_color = 'peru'
    window.add(right_hand_finger)

    # Pants
    pants = GRect(SIZE * 6, SIZE * 5, x=60, y=200)
    pants.color = 'royalblue'
    pants.filled = True
    pants.fill_color = 'royalblue'
    window.add(pants)

    left_pants = GRect(SIZE, SIZE * 3, x=40, y=240)
    left_pants.color = 'royalblue'
    left_pants.filled = True
    left_pants.fill_color = 'royalblue'
    window.add(left_pants)

    right_pants = GRect(SIZE, SIZE * 3, x=180, y=240)
    right_pants.color = 'royalblue'
    right_pants.filled = True
    right_pants.fill_color = 'royalblue'
    window.add(right_pants)

    pants_upper = GRect(SIZE * 4, SIZE, x=80, y=180)
    pants_upper.color = 'royalblue'
    pants_upper.filled = True
    pants_upper.fill_color = 'royalblue'
    window.add(pants_upper)

    pants_left_upper = GRect(SIZE, SIZE * 2, x=80, y=140)
    pants_left_upper.color = 'royalblue'
    pants_left_upper.filled = True
    pants_left_upper.fill_color = 'royalblue'
    window.add(pants_left_upper)

    pants_right_upper = GRect(SIZE, SIZE * 2, x=140, y=140)
    pants_right_upper.color = 'royalblue'
    pants_right_upper.filled = True
    pants_right_upper.fill_color = 'royalblue'
    window.add(pants_right_upper)

    # Shoes
    left_shoes_upper = GRect(SIZE * 3, SIZE, x=20, y=300)
    left_shoes_upper.color = 'saddlebrown'
    left_shoes_upper.filled = True
    left_shoes_upper.fill_color = 'saddlebrown'
    window.add(left_shoes_upper)

    left_shoes_lower = GRect(SIZE * 4, SIZE, y=320)
    left_shoes_lower.color = 'saddlebrown'
    left_shoes_lower.filled = True
    left_shoes_lower.fill_color = 'saddlebrown'
    window.add(left_shoes_lower)

    right_shoes_upper = GRect(SIZE * 3, SIZE, x=160, y=300)
    right_shoes_upper.color = 'saddlebrown'
    right_shoes_upper.filled = True
    right_shoes_upper.fill_color = 'saddlebrown'
    window.add(right_shoes_upper)

    right_shoes_lower = GRect(SIZE * 4, SIZE, x=160, y=320)
    right_shoes_lower.color = 'saddlebrown'
    right_shoes_lower.filled = True
    right_shoes_lower.fill_color = 'saddlebrown'
    window.add(right_shoes_lower)

if __name__ == '__main__':
    main()
