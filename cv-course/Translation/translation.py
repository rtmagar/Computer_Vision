import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("Original", image)

# NOTE: Translating (shifting) an image is given by a NumPy matrix in
# the form:
#	[[1, 0, shiftX], [0, 1, shiftY]]
# You simply need to specify how many pixels you want to shift the image
# in the X and Y direction -- let's translate the image 25 pixels to the
# right and 50 pixels down

M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)
cv2.imwrite("Down_Right.png", shifted)

# Shifting the image 50 pix left and 90 pix up
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)
cv2.imwrite("Up_Left.png", shifted)

# shifting an image with imutils function
shifted = imutils.translate(image, 0, 100)
cv2.imshow('Shifted Down', shifted)
cv2.imwrite("Down.png", shifted)
cv2.waitKey(0)

