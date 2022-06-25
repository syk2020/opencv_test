import numpy as np
import cv2

img = cv2.imread('images/penguins.png', cv2.IMREAD_COLOR)

x = 200
y = 100
channel = 0

# 座標 x, y の画素値を参照 ...[(B)lue, (G)reen, (R)ed]
bgr_val = img[y, x]
print(f'bgr_val ({x}, {y}) = {bgr_val}')

# 座標 x, y の画素のうち channel(=0)の数値
b_val = img[y, x, channel]
print (f'b_val({x}, {y}) = {b_val}')