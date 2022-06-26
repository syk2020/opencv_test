import csv
import numpy as np
import pandas as pd

with open('./playwright_test/restaurantANDhospital.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# numpyはライブラリ名通り、数値ファイルしか読めない
# のでテキストデータを含むCSV読み込みの処理はエラーになる
"""
np_test = np.loadtxt('./playwright_test/restaurantANDhospital.csv', delimiter=',')
print(type(np_test))
print(np_test)
"""

# pandasテスト
# 処理が重いのでいざという時にだけ
pd_test = pd.read_csv('./playwright_test/restaurantANDhospital.csv')
print(type(pd_test))
print(pd_test)