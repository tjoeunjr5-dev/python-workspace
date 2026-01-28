'''
깃허브에는
본인이 만든 모델을 올리지 않는다.
모델의 경우 중요한 자산이기 때문에 개발자나 회사가만든 모델 파일을 
제공하는 것은 회사의 재산을 유출하는 것과 같을 정도로 심각하다.
'''


import FinanceDataReader as fdr
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df = fdr.DataReader('005930', '2026-01-01')

df['MA5'] = df['Close'].rolling(window=5).mean()
df['MA20'] = df['Close'].rolling(window=20).mean()
df['Target'] = df['Close'].shift(-1)
df.dropna(inplace=True)

X = df[['Close', 'MA5', 'MA20']]
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)
# 성능 평가
score = model.score(X_test, y_test)
print(f"모델 정확도 : {score:.4f}")

# 모델 저장 
joblib.dump(model, "samsung_linear_model.pkl")
print(f"모델 저장 완료")