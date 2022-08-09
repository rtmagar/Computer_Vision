import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
(h,w) = image.shape[:2]
cv2.imshow('Original', image)


# Images are just Numpy arrays. The top-left pixel can be found at (0,0)
(b,g,r) = image[0,0]
print("Pixel at (0,0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

# make the value of pixel at (0,0) and make it red color
image[0,0] = (0, 0, 255)
(b,g,r) = image[0,0]
print("Pixel at (0,0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))


# compute the center of the image
(cX, cY) = (w // 2, h // 2)

# apply silicing technique to grap the some portion of image(top left side)
t1 = image[0:cY, 0:cX]
cv2.imshow("Top-Left Corner", t1)



# In a similar way, grab the top-right, bottom-right, and bottom left and display them
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)

# change the color into green for top-left
image[0:cY, 0:cX] = (0, 255, 0)

cv2.imshow("Updated", image)
cv2.waitKey(0)




