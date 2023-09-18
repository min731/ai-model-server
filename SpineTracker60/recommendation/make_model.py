import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline # 여러가지 모델을 활용하기 위함
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
#모델
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import xgboost as XGB

data = pd.read_csv('데이터.csv', encoding='ANSI')
# 원핫 인코딩
data = pd.get_dummies(data, columns=['성별', '나이', '직업'])

X = data.drop(columns=['제품'])
y = data['제품']
from sklearn.preprocessing import LabelEncoder
# LabelEncoder 객체 생성
label_encoder = LabelEncoder()
# 레이블을 숫자로 변환
y = label_encoder.fit_transform(data['제품'])

# 이제 y는 숫자 형식의 레이블을 갖게 됩니다.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=777)

feature_names = X.columns
pipelines = {
  'lr':make_pipeline(StandardScaler(),LogisticRegression()),
  'rf':make_pipeline(StandardScaler(),RandomForestClassifier()),
  'svd':make_pipeline(StandardScaler(),SVC(probability=True)),
  'knc':make_pipeline(StandardScaler(),KNeighborsClassifier()),
  'xgb':make_pipeline(StandardScaler(),XGB.XGBClassifier()),
 }

# model = RandomForestClassifier(n_estimators=100, random_state=777)
# model.fit(X_train, y_train)

# 학습한 모델 저장
fit_models = {}
for algo,pipelines in pipelines.items():
  #print(algo)
  model = pipelines.fit(X_train,y_train)
  fit_models[algo] = model
fit_models
max = [0,0]
for algo,model in fit_models.items():
  yhat = model.predict(X_test)
  if max[1] < accuracy_score(y_test,yhat):
      max[1] = accuracy_score(y_test,yhat)
      max[0] =algo
  print(algo,accuracy_score(y_test,yhat))
print(f'제일 높은 성능을 보인 모델은, {max[0]} 입니다.')

with open('best_model.pkl','wb') as f:
  pickle.dump(fit_models[max[0]],f)