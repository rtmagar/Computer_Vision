# import the necessary packages
import numpy as np
import argparse
import cv2
import imutils

# constructs the argument parser and parse the aguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True,
                help='path to the input image')
args = vars(ap.parse_args())

# load the image from disk, convert it to grayscale, blur it,
# and apply edge detection to reveal the outline of the pill
image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)
edge = cv2.Canny(blur, 20, 100)
cv2.imshow('Edged', edge)
cv2.waitKey(0)

# find contours in the edge map
cnts = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# ensure at least one one contour was found
if len(cnts) > 0:
    # grab the largest contour, then draw a mask for the pill
    c = max(cnts, key=cv2.contourArea)
    mask = np.zeros(gray.shape, dtype='uint8')
    cv2.drawContours(mask, [c], -1, 255, -1)

    # compute its bounding box of pill, then extracts the ROI,
    # and apply the mask
    (x, y, w, h) = cv2.boundingRect(c)
    imageROI = image[y:y + h, x:x + w]
    maskROI = mask[y:y + h, x:x + w]
    imageROI = cv2.bitwise_and(imageROI, imageROI,
                               mask=maskROI)
    cv2.imshow("Mask", imageROI)
    cv2.waitKey(0)
