import cv2
import numpy as np
import matplotlib.pyplot as plt

flg, ax = plt.subplots(figsize=(10, 10))

img_hrv = np.zeros((180, 256, 3), np.uint8)

for y, h in enumerate(range(0, 180)):
    for x, s in enumerate(range(0, 256)):
        img_hrv[y, x, :] = (h, s, 20)

cv2.imshow("img_hrv", img_hrv)
cv2.waitKey(0)
cv2.destroyAllWindows()
# HSV だけでみると100-255は桃色っぽい色ばかりになる
# 20は青と緑、RGBだと真っ暗 -> 数値のみを変換している

img_rgb = cv2.cvtColor(img_hrv, cv2.COLOR_HSV2RGB)
ax.set_title("HSV Color Space (V=255)", size="x-large")
ax.set_xlabel("Saturation", size="x-large")
ax.set_ylabel("Hue", size="x-large")

plt.imshow(img_rgb)
plt.show()
