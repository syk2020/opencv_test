import numpy as np
import cv2

# add
x = np.uint8([250])
y = np.uint8([10])
z = cv2.add(x, y)

# 250+20=260 => uint8 max : 255
print(f"z = {z}")


# subtract
x = np.uint8([10])
# 絶対値なので-20でも変わらない
y = np.uint8([20])
z = cv2.subtract(x, y)

# 10-20=-10 => uint min : 0
print(f"z = {z}")
