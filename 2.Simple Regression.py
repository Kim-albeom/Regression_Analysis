# 2. 단순회귀분석(Simple Regression Analysis)

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

## minus를 `-` 표시 제대로 출력
matplotlib.rcParams['axes.unicode_minus'] = False 

from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression

# 데이터 불러오기
df = pd.read_csv('.\\data\\toluca_company_dataset.csv') 

df.head(5)

## 시각화

fig = plt.figure(figsize=(8,8))
fig.set_facecolor('white')

font_size = 15
plt.scatter(df['Lot_size'],df['Work_hours'])

plt.xlabel('Lot Size', fontsize=font_size)
plt.ylabel('Work Hours', fontsize=font_size)
plt.show() 

# 데이터가 우상향하는 것을 확인할 수 있다.

# 2-1. statsmodels로 적합시켜보기.

# 단순선형회귀모형 적합
fit = ols('Work_hours ~ Lot_size', data=df).fit()
fit.summary()
# summary()로 결정계수와 수정결정계수 등을 제공하고 회귀계수의 추정값과 검정통계량, p-value도 제공.
# ols는 기본적으로 절편항을 추정한다. 절편항을 제외하고 싶다면 아래와 같이 모델 표현에 -1읋 추가한다.

# fit = ols('Work_hours ~ Lot_size - 1', data=df).fit()

# 회귀 계수 / 순서대로 절편과 기울기
print(fit.params.Intercept)
print(fit.params.Lot_size)

# 추정값(y_hat)
fit.fittedvalues

# 잔차
fit.resid

# 예측값, Lot_size 값이 80일 때의 예측값
fit.predict(exog=dict(Lot_size=[80]))

## 산점도와 회귀직선 시각화

fig = plt.figure(figsize=(8,8))
fig.set_facecolor('white')

font_size = 15

# 관측치 점 찍기
plt.scatter(df['Lot_size'], df['Work_hours'])

# 회귀직선 추가
plt.plot(df['Lot_size'], fit.fittedvalues, color='red')

plt.xlabel('Lot size', fontsize=font_size)
plt.ylabel('Work hours', fontsize = font_size)
plt.show()

## 잔차 모형
fig = plt.figure(figsize=(8,8))
fig.set_facecolor('white')

font_size = 15

# 잔차 산점도
plt.scatter(df['Lot_size'], fit.resid)

plt.xlabel('Lot Size', fontsize = font_size)
plt.ylabel('Residual', fontsize = font_size)
plt.show()

## 2-2. sklearn을 이용해서 적합시키기
# 차원을 증가. statsmodels와 달리 설명변수의 차원을 하나 증가시켜줘야 합니다.
x = df['Lot_size'].values.reshape(-1,1)
y = df['Work_hours']

# fit으로 모형을 적합시켜줍니다.
fit = LinearRegression().fit(x,y)

# 회귀 계수, 절편과 기울기
print(fit.intercept_)
print(fit.coef_)

# 추정값
fit.predict(x)

# sklearn에서는 잔차를 따로 제공하지 않기 때문에 잔차는 직접 계산해줘야합니다.
residual = y - fit.predict(x)
print(residual)

# 예측값
fit.predict([[80]])

# 회귀모형을 적합할때는 sklearn보다 statsmodel을 사용하는 것이 더 좋은 것 같다.
# summary로 요약할 수도 있고, 잔차와 학습데이터에 대한 반응변수의 추정값을 계산하지 않아도 된다.
# 또 데이터의 차원을 증가시키지 않아도 됩니다. 즉, 전처리가 필요 없이 범주형 데이터를 바로 모형에 적합할 수 있다.
