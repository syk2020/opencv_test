import cv2

img1 = cv2.imread('images/penguins_copy.png', cv2.IMREAD_COLOR)

print(f'shape = {img1.shape}')
print(f'dtype = {img1.dtype}')

img2 = cv2.imread('images/penguins_copy.png', cv2.IMREAD_GRAYSCALE)

print(f'shape = {img2.shape}')
print(f'dtype = {img2.dtype}')


# for ind, i in enumerate(img.shape):
#     print(f'channel {ind} : {i} / {hex(i)}')