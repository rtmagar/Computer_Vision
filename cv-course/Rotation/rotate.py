import numpy as np
import argparse 
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)

(h, w) = image.shape[:2]
(cX, cY) = (w/2, h/2)

# rotate the image by 45 degrees
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 degrees", rotated)


# rotate the image by -90 degrees
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 degrees", rotated)

# rotate the image around an arbitrary point rather than the center
M = cv2.getRotationMatrix2D((cX-50, cY-50), 45, 1.0)
roated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by Offset and 45 Degrees", rotated)


rotated = imutils.rotate(image, -180)
cv2.imshow("Rotated by 180 degrees", rotated)
cv2.waitKey(0)

