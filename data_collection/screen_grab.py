"""Keys a gray scale screenshot of a bounded box. The screenshot uses edge detection.
numpy: used to store data about screenshot
Python Image Library: takes screenshot
cv2: proccess the image
"""
from PIL import ImageGrab
import numpy as np
import cv2


def process_img(image):
    """Converts image to gray scale then does edge detection.

    Args:
        image: raw image array.

    Returns:
        processed_img: gray scale + edge dected image (numpy array).
    """
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)

    return processed_img


def screen_record(preview=False):
    """Takes screenshot of image and executes proccessing on it.

    Args:
        preview: boolean of if proccessed image should be shown (big performance hit).

    Returns:
        processed_img: gray scale + edge dected image (numpy array).
    """
    screen = np.array(ImageGrab.grab(bbox=(0, 25, 590, 540)))
    new_screen = process_img(screen)
    if preview is True:
        cv2.imshow("window", new_screen)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        exit()

    return screen

if __name__ == "__main__":
    while True:
        screen_record()
