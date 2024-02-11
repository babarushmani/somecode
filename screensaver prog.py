import cv2
import numpy as np

def screensaver():
    img = np.zeros((480, 640, 3)) # zeroes will give the background black, if we need white then use ones.
    dx, dy = 1, 1   # speed in pixels(downward), if we put negative value circle will move upward.
    x, y = 150, 250 # pixel value of point where to start circle
    while True:
        # Display the image
        cv2.imshow('screensaver', img) # name of screensaver window
        k = cv2.waitKey(1)
        img = np.zeros((480, 640, 3)) # zeros array to play screensaver image
        # Increment the position
        x = x + dx
        y = y + dy
        cv2.circle(img, (x, y), 40, (0, 255, 0), -1)
        if k != -1:
            break
        # Change the sign of increment on collision with the boundary
        if y >= 460:
            dy *= -1
        elif y <= 20:
            dy *= -1
        if x >= 620:
            dx *= -1
        elif x <= 20:
            dx *= -1
    cv2.destroyAllWindows()


while True:

    # Background Image
    img1 = cv2.imread('D:/downloads/original_image.png')
    cv2.imshow('leena', img1)
    k = cv2.waitKey(5000) # wait time for screensaver window
    # If no key is pressed, display the screensaver
    if k == -1:
        screensaver()

    elif k == 27: # escape key will break the program
        break
cv2.destroyAllWindows()
