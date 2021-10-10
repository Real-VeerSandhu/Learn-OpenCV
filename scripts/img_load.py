import cv2

image = cv2.imread('assets\can.png', -1)
image = cv2.resize(image, (500, 500))

cv2.imshow('Can Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()