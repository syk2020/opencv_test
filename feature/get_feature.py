# import glob
import os
import numpy as np
import cv2

"""
# files = glob.glob("playwright_test/ss/*")
# for file in files:
#     if file.find('Hospital') > 0:
#         # print(f'{file} : Hospital')
#         img_read = cv2.imread(file, )
#     elif file.find('Restaurant') > 0:
#         # print(f'{file} : Restaurant')
"""

path = 'playwright_test/ss/'
files = os.listdir(path)
# for file in files:
#     print(file)

# os.path.isfile(fullpath)でファイルのみリスト化
files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
for file in files_file:
    # print(file[:-4])

    # ファイルをCV2で読み込み
    img_read = cv2.imread(path + file, cv2.IMREAD_COLOR)

    # numpyデータ化
    # 保存
    np.save(f'feature/data/{file[:-4]}.npy', img_read)


#     img_read = cv2.imread(file, cv2.IMREAD_COLOR)

#     if len(img_read.shape) == 3:
#         height, width, channels = img_read.shape[:3]
#     else:
#         height, width = img_read.shape[:2]
#         channels = 1

"""
img_read = cv2.imread('playwright_test/ss/Restaurant_10.png', cv2.IMREAD_COLOR)
# if len(img_read.shape) == 3:
#     height, width, channels = img_read.shape[:3]

bgr_val = img_read[333, 555]
print(f'bgr_val (555 333) = {bgr_val}')

np.save('feature/data/Restaurant_10.npy', img_read)

data = np.load('feature/data/Restaurant_10.npy')
print(type(data))
print(data[333][555])
"""
