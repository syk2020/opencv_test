import cv2

img = cv2.imread('images/penguins_copy.png', cv2.IMREAD_COLOR)
x = 200
y = 100
channel = 0

print(f'before: bgr_val({x}, {y}) = {img[y, x]}')

img[y, x] = [0xff, 0xff, 0xff]
print(f'after: bgr_val({x}, {y}) = {img[y, x]}')

# 同じスコープとみなすのか、上のスクリプト実行後は0になってしまう
print(f'before: b_val({x}, {y}, {channel}) = {img[y, x, channel]}')

img[y, x, channel] = 0
print(f'after: b_val({x}, {y}, {channel}) = {img[y, x, channel]}')
