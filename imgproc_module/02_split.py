import cv2

img_bgr = cv2.imread("images/veggie.png")
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(img_hsv)

cv2.imshow("H, S, V", cv2.hconcat([h, s, v]))
cv2.waitKey(0)
cv2.destroyAllWindows

# Sは彩度、Vが明度、Hが色相
