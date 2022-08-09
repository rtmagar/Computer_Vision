import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args= vars(ap.parse_args())

# load image and print it's dimension
image = cv2.imread(args['image'])
print('width: %d pixels' % (image.shape[1]))
print('height: %d pixels' % (image.shape[0]))
print('channels: %d' % (image.shape[2]))

# display image
cv2.imshow("Image", image)
cv2.waitKey(0)

# save image in different format
cv2.imwrite('grand_canyon_2.jpg', image)