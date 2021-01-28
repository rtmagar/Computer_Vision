import cv2
import imutils
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to the input')
arg = vars(ap.parse_args())

image = cv2.imread(arg['image'])

(h, w, d) = image.shape
print(f'height {h}, width {w}, depth {d}')

(B, G, R) = image[321, 599]
print(f'B={B}, G={G}, R={R}')

cv2.imshow("Image", image)
cv2.waitKey(0)

roi = image[100:200, 150:200]
cv2.imshow("roi", roi)
cv2.waitKey(0)

resize = cv2.resize(image, (200, 200))
cv2.imshow('resize', resize)
cv2.waitKey(0)

r = 100.0/w
dim = (100, int(h*r))
resize2 = cv2.resize(image, dim)
cv2.imshow("dim", resize2)
cv2.waitKey(0)

resized = imutils.resize(image, width=100)
cv2.imshow('imut', resized)
cv2.waitKey(0)

center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow('OpenCV rotation', rotated)
cv2.waitKey(0)

rotated = imutils.rotate(image, -45)
cv2.imshow('imutils_rotate', rotated)
cv2.waitKey(0)

rotated = imutils.rotate_bound(image, 45)
cv2.imshow('imutils_rotate_bound', rotated)
cv2.waitKey(0)








