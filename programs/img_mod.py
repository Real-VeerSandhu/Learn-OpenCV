import cv2

image = cv2.imread('assets/bottle.jpg', -1)

print(image) # Reads blue green red (BGR) not red green blue (RGB)
print(f'Type: {type(image)}')
print(f'Shape: {image.shape}') # 256, 256, 3

print(f'First pixel: {image[0][0]}')

for i in range(100): # Number of rows to change (max 256 for bottle.jpg)
    for j in range(image.shape[1]):
        image[i][j] = [233, 45, 23]

cv2.imshow('Modified Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()