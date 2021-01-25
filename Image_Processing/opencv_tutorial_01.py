# import the necessary packages
import imutils
import cv2

# load the input image and show its dimension, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread('jp.png')
(h, w, d) = image.shape
print(f'width={w}, height={h}, depth={d}')

# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
cv2.imshow("Image", image)
cv2.waitKey(0)

# access the RGB pixel located at x=50, y=100, keep in  mind that
# opencv stores images in BGR order rather than RGB
(B, G, R) = image[100,50]
print(f'R={R}, G={G}, B={B}')

# extract a 100*100 pixel square ROI (Region of interest) form the
# input image starting at x=320, y=60 at ending at x=420, y=160
roi = image[60:160, 320:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# resize the image to 200x200px, ignoring aspect ratio
resized = cv2.resize(image, (200, 200))
cv2.imshow('Image', resized)
cv2.waitKey(0)

# fixed resizing and distort aspect ration so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
r = 300.0 / w
dim = (300, int(h*r))
resized = cv2.resize(image, dim)
cv2.imshow('Image', resized)
cv2.waitKey(0)

# manually computing the aspect ratio can be a pain so let's use the
# imutils library instead
resized = imutils.resize(image, width=300)
cv2.imshow("Image", resized)
cv2.waitKey(0)





