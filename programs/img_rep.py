import cv2

image = cv2.imread('assets/bottle.jpg', -1)

print(image) # Reads blue green red (BGR) not red green blue (RGB)
print(f'Type: {type(image)}')
print(f'Shape: {image.shape}') # 256, 256, 3

print(f'First pixel: {image[0][0]}')