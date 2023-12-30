# 1. 산점도(Scatter Plot)
# 1-1. matplotlib를 이용한 산점도 그리기.

import matplotlib.pyplot as plt # 시각화 패키지 pyplot은 서브패키지이다.
import seaborn as sns

penguin = sns.load_dataset('penguins') # species / island / bill_length_mm / bill_depth_mm / flipper_length_mm / body_mass_g / sex (7개의 변수, 343개의 관측치)
penguin

# 1-1-1. 첫 번째 방법 (명목형으로 그룹화)
# 두 변수간의 관계를 확인하기 위해서 관측치를 그래프에 그려보는 것.



marker = {"Torgersen": 'o', "Biscoe": 's', "Dream": '+'} # marker를 dictionary로 저장.

color = {"Torgersen": 'red', "Biscoe": 'blue', "Dream": 'green'} # 색을 지정.

plt.figure(figsize=(20,5)) # graph의 크기를 width:20, height: 5로 설정.

grouped = penguin.groupby('island') # pandas의 함수 `.groupby()` 입력된 값을 기준으로 분리하고 합하고 다시 commbine 되는 함수이다.

for i, item in grouped:
    plt.scatter('bill_length_mm', 'bill_depth_mm', data=item, s=15, label=i, marker=marker[i], c=color[i]) # s는 사이즈를 의미(여기서는 점의 크기)
    
plt.title('Bill Size by Island', fontsize=14)
plt.xlabel('length', fontsize=12)
plt.ylabel('depth', fontsize=12)
plt.legend()
plt.show()


# 1-1-2. 두 번째 방법 (연속형)

penguin = sns.load_dataset('penguins')

plt.figure(figsize=(20,5))
plt.scatter('bill_length_mm', 'bill_depth_mm', data=penguin, s=15, cmap='Reds', c='body_mass_g')
# cmap 속성은 colormap을 설정하는 속성 / 색을 'body_mass_g'에 따라 지정.
plt.title('Bill Size by Island', fontsize = 14)
plt.xlabel('length', fontsize=12)
plt.ylabel('depth', fontsize=12)
plt.colorbar()
plt.show()

# 첫 번째와 두 번째 방법에 있어서 차이는 첫 번째는 groupby를 이용해서 island로 

# 1-2. seaborn을 이용해서 산점도 그리기.
# 1-2-1. 기본 형식

penguin = sns.load_dataset('penguins')

plt.figure(figsize=(20, 5))
sns.scatterplot(x='bill_length_mm', y='bill_depth_mm', hue = 'island', style='island', s=50, data=penguin)
plt.show()

# 1-2-2. advanced

plt.figure(figsize=(20, 5))
ax = sns.scatterplot(x='bill_length_mm', y='bill_depth_mm', hue='body_mass_g', palette='viridis', s=50, data=penguin)

norm = plt.Normalize(penguin['body_mass_g'].min(), penguin['body_mass_g'].max())
sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm) # 색을 지정?
sm.set_array([])

ax.get_legend().remove()
ax.figure.colorbar(sm)

plt.show()


# 1-3. Plotly를 이용한 산점도
# 1-3-1. 명목형(island)
import plotly.graph_objects as go 

marker = {"Torgersen":1, "Biscoe":2, "Dream":3}
color = {"Torgersen":'red', "Biscoe":'blue', "Dream":'green'}

data = []

for i, items in penguin.groupby('island'):
    trace = go.Scatter(x=items['bill_length_mm'], y=items['bill_depth_mm'], mode='markers',
                       name=i, marker=dict(size=5, color=color[i], symbol=marker[i]))
    
    data = data + [trace]
    
    layout = go.Layout(
        autosize=False,
        width=1000,
        height=400
    )
    
fig = go.Figure(data=data, layout = layout)
fig.show()

# 1-3-2. 연속형(body_mass_g) - 아래 코드 참조

#
#penguin['adj_body_mass_g'] = (penguin['body_mass_g'].mean() - penguin['body_mass_g']) / penguin['body_mass_g'].std()
#
#trace = go.Scatter(x = penguin['bill_length_mm'], y = penguin['bill_depth_mm'], mode = 'markers',
#                   marker = dict(size=5, color = penguin['adj_body_mass_g'], colorscale='inferno'))
#
#fig = go.Figure(data=[trace])
#
#fig.update_traces(opacity = 1, marker=dict(showscale = True, reversescale = True, cmid = 0, size = 5))
#

