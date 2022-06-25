import numpy as np
import cv2


# bitwise_and
# マスク処理
src1 = cv2.imread("images/penguins_copy.png", cv2.IMREAD_COLOR)

height, width, channels = src1.shape[:3]
src2 = np.zeros((height, width, channels), np.uint8)
cv2.rectangle(src2, (150, 135), (290, 315), (255, 255, 255), thickness=-1)

dst = cv2.bitwise_and(src1, src2)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


# bitwise_or
# レイヤーで重ねる感じ
src1 = cv2.imread("images/aloeL.png", cv2.IMREAD_COLOR)
src2 = cv2.imread("images/aloeR.png", cv2.IMREAD_COLOR)

# 重み付け数値
alpha = 0.5
beta = 0.5
# これだけよく分からん
gamma = 0.9

dst = cv2.addWeighted(src1, alpha, src2, beta, gamma)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
