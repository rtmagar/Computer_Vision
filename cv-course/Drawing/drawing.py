import numpy as np
import cv2

# intialize a canvas/image
canvas = np.zeros((300,300,3), dtype='uint8')

# draw green line (top-left --- bottom-right)
green = (0, 255, 0)
cv2.line(canvas, (0,0), (300,300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw red line (top-right ----- bottom-left), thickness: 3 pix
red = (0, 0, 255)
cv2.line(canvas, (300,0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


# draw a green 50x50 pixel square, starting at 10x10 and ending at 60x60
cv2.rectangle(canvas, (10,10), (60,60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw another rectangle, this time we'll make it red and 5 pixels thick
cv2.rectangle(canvas, (50,200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# let's draw one last rectangle: blue and filled in 
blue = (255, 0, 0)
cv2.rectangle(canvas, (200,50), (225, 125), blue, -1)
cv2.imshow('Canvas', canvas)
cv2.imwrite("output.jpg", canvas)
cv2.waitKey(0)


# reset out canvas and draw a white circle at the center of the canvas with increasing
# sradii - from 25 pixels to 150 pixels
canvas = np.zeros((300, 300, 3), dtype='uint8')
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

# show our work of art
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


# draw some 25 random circles
for i in range(0,25):

    # randomly generate a radius size between 5 and 200, random color and then pick
    # a random point on our canvas where the cirlce will be drawn
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))

    # draw out random circle
    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


# Draw shapes on images
# load the image of Adrian in Florida
image = cv2.imread('florida_trip.jpg')

cv2.circle(image, (168,188), 90,  (0,0,255), 2)
cv2.circle(image, (150,164), 10, (0,0,255), -1)
cv2.circle(image, (192,174), 10, (0,0,255), -1)
cv2.rectangle(image, (134,200), (186, 218), (0,0,255), -1)

cv2.imshow("Output", image)
cv2.waitKey(0)



