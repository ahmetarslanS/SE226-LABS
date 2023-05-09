import cv2

image = cv2.imread('image.jpg')
#My image is too big so i resize it to fit my screen
resized_img = cv2.resize(image, (600, 400))

#Splitting image to blue, green, and red channels
b,g,r = cv2.split(resized_img)

cv2.imshow('Blue Channel', b)
cv2.imshow('Green channel', g)
cv2.imshow('Red Channel', r)

#Setting the green value to zero so that green does not exist in image
g.fill(0)

#Combining the image back and showing it on the screen
blue_red_image = cv2.merge((b,g,r))
cv2.imshow('Image without green', blue_red_image)

cv2.waitKey(0)
#cv2.destroyAllWindows()
