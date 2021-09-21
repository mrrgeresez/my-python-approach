import argparse # terminal working
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="specify path to input image, relative or global")
args = vars(ap.parse_args())
# vars transform the args.namespace to a keyword that can be used in a function

# loading the input image via command line
image = cv2.imread(args["image"]) # args["image"] = args.image
cv2.imshow("Image", image)
# cv2.waitKey(0)
# converting to grayscale for edge detection and thresholding
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
# cv2.waitKey(0)

### Edge detecion with Canny algorithm
edged = cv2.Canny(gray, 30, 150)
# min threshold, max threshold, and sobel kernel size (default 3)
# sobel filter: discrete differentiation operator, computing an approximation of the gradient of the image intensity function, enhancing high freq variations
cv2.imshow("Edged", edged)
# cv2.waitKey(0)

### Thresholding
# used to remove dark or light areas and highlight some regions
# binary inverse threshold: in the image all pixel values less than 225
# to 255 (white; foreground) and all pixel values >= 225 to 255
# (black; background), thereby segmenting the image, critical step for finding contours
thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh", thresh)
# cv2.waitKey(0)

# Detecting contours
# using the thresholded image find the outlining
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
# simply finding white px in a copy of thresh
cnts = imutils.grab_contours(cnts)
# compatibility wrapper for previous versions
output = image.copy()
# make copy when drawing over images
for c in cnts:
	# draw each contour on the output image with a 3px thick purple
	# outline, then display the output contours one at a time
	cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
#     cv2.imshow("Contours", output)
# 	cv2.waitKey(0)
    
text = f"{len(cnts)} objects found!"
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	(240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)

### Erosions and dilations
# To reduce noise in thresholded binary images
# we apply erosions to reduce the size of foreground objects (eroding pixels)
# useful for removing some blobs or undesired objects
mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=5)
# 5 iterations for reducing size
cv2.imshow("Eroded", mask)
# cv2.waitKey(0)

# Similarly dilations enlarge the ground and can combine foreground objects (nearby contours) when interested
mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=5)
cv2.imshow("Dilated", mask)
cv2.waitKey(0)

### Masking
# Mask out or hide regions we are not interested in, maybe to enchance some feature or the image.
mask = thresh.copy()
output = cv2.bitwise_and(image, image, mask=mask)
# the bitwise and only keeps the masked regions
cv2.imshow("Output", output)
cv2.waitKey(0)