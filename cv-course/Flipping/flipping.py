import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# flip the image Horizontally
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

# flip the image vertically
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Horizontally", flipped)

# flip the image along both axes
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)



