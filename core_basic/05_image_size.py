import cv2

img = cv2.imread("images/penguins_copy.png", cv2.IMREAD_COLOR)

if len(img.shape) == 3:
    height, width, channels = img.shape[:3]
else:
    height, width = img.shape[:2]
    channels = 1

print(f"width = {width}")
print(f"height = {height}")
print(f"channels = {channels}")
