import cv2
from cv2 import IMREAD_COLOR

img = cv2.imread("images/penguins_copy.png", IMREAD_COLOR)

# [上:下, 左:右]
img_roi = img[100:600, 0:1300]

cv2.imshow("img", img)
cv2.imshow("img_roi", img_roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
