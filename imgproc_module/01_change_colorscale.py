import cv2

img_bgr = cv2.imread("images/veggie.png")
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

cv2.imshow("img_bgr", img_bgr)
cv2.imshow("img_gray", img_gray)
cv2.imshow("img_hsv", img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows
