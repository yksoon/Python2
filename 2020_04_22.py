import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

con = sqlite3.connect("C:/Users/USER/Desktop/YKS/Python2/디지털_가전.db")
cursor = con.cursor()

readed_df = pd.read_sql("SELECT * FROM digital", con)
print(readed_df)

print(readed_df.가격)


# 평균
mean_price = sum(readed_df.가격) / len(readed_df.가격)
print(mean_price)

# 최대
max_price = max(readed_df.가격)
print(max_price)

# 최소
min_price = min(readed_df.가격)
print(min_price)

# 중앙
mid_price = np.median(readed_df.가격)
print(mid_price)

# 4분위
readed_df.가격.describe()

# 선형 차트 출력
x = readed_df.제품명
y = readed_df.가격

plt.xlabel('titlt')
plt.xticks(rotation=90)
plt.ylabel('price')

plt.title('linechart')

plt.plot(x, y)

plt.legend('price')

plt.show()

#################################################





