import cv2

image = cv2.imread('assets/bottle.jpg', -1)

section = image[120:140, 120:140]
image[10:30, 200:220] = section

cv2.imshow('Moved Section Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()