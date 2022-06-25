import numpy as np
import cv2

width = 200
height = 100
value = 0x80 # = 128

"""
# height * width の０で埋めた画像（＝黒）生成
img1 = np.zeros((height, width), np.uint8)
# height * width をvalueで埋めた画像
img2 = np.full((height, width), value, np.uint8)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

channels = 3
values = (0,0,0xff)
# channels の色の情報を持たせる（B=0, G=0, R=256）
# np.uint8 にすることを忘れない -> int にするとグレーになってしまう
img3 = np.full((height, width, channels), values, np.uint8)

cv2.imshow('img4', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()