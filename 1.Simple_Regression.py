# 1. 산점도(Scatter Plot)
# 두 변수간의 관계를 확인하기 위해서 관측치를 그래프에 그려보는 것.

import matplotlib.pyplot as plt # 시각화 패키지 pyplot은 서브패키지이다.
import seaborn as sns

penguin = sns.load_dataset('penguins') # species / island / bill_length_mm / bill_depth_mm / flipper_length_mm / body_mass_g / sex (7개의 변수, 343개의 관측치)
penguin


marker = {"Torgersen": 'o', "Biscoe": 's', "Dream": '+'}

color = {"Torgersen": 'red', "Biscoe": 'blue', "Dream": 'green'}

plt.figure(figsize=(20,5))

grouped = penguin.groupby('island')

for i, item in grouped:
    plt.scatter('bill_length_mm', 'bill_depth_mm', data=item, s=9, label=i, marker=marker[i], c=color[i])
    
plt.title('Bill Size by Island', fontsize=14)
plt.xlabel('length', fontsize=12)
plt.ylabel('depth', fontsize=12)
plt.legend()
plt.show()