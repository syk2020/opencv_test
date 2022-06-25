import cv2
import numpy as np
import matplotlib.pyplot as plt

img_bgr = cv2.imread("images/chocolates.jpg")
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(img_hsv)

plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.title("Original (RGB)")
plt.imshow(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))

plt.subplot(2, 3, 2)
plt.title("Hue (H)")
plt.imshow(h, cmap="gray")

plt.subplot(2, 3, 3)
plt.title("Saturation (S)")
plt.imshow(s, cmap="gray")

plt.subplot(2, 3, 4)
plt.title("Value, Brightness (V)")
plt.imshow(v, cmap="gray")

# 範囲を指定してマスク部分を特定する
mask = np.zeros(h.shape, dtype=np.uint8)
mask[(h > 80) & (h < 140) & (s > 70)] = 255

# クロージング処理
# よく分からないのでまた確認
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((41, 41), np.uint8))

# maskを３チャンネルに変更
mask_3ch = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)

result_img = cv2.bitwise_and(img_bgr, mask_3ch)

plt.subplot(2, 3, 5)
plt.title("mask")
plt.imshow(mask, cmap="gray")

plt.subplot(2, 3, 6)
plt.title("result")
plt.imshow(cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB))

plt.show()
