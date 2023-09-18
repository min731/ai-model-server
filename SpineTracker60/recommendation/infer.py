import pandas as pd
import pickle

# 저장된 모델을 불러오기
with open('face.pkl', 'rb') as f:
  loaded_model = pickle.load(f)

#추론
# 추론할 정보
user_input = {
    '성별_녀': 1,
    '나이_20대': 1,
    '직업_사무 종사자': 1,
    '거북목': 5,
    '졸음': 3,
    '비대칭': 7,
    '척추후만': 4
}

# 원핫인코딩을 했기 때문에 선택하지 않은 정보에 대해선 0으로 처리
user_df = pd.DataFrame([user_input])
empty_df = pd.DataFrame(columns=['거북목', '졸음', '비대칭', '척추후만', '성별_남', '성별_녀', '나이_10대', '나이_20대',
       '나이_30대', '나이_40대', '나이_50대', '나이_60대이상', '직업_관리자', '직업_군인',
       '직업_기능원 및 관련 기능 종사자', '직업_농림어업 숙련 종사자', '직업_단순노무 종사자', '직업_사무 종사자',
       '직업_서비스 종사자', '직업_장치·기계 조작 및 조립 종사자', '직업_전문가 및 관련 종사자', '직업_판매 종사자'])
final_user_df = pd.concat([empty_df, user_df], ignore_index=True, sort=False).fillna(0)

# 제품 추천 확률 계산
predicted_probabilities = loaded_model.predict_proba(final_user_df)[0]

num_recommendations = 3  # 상위 3개 제품 추천
top_product_indices = predicted_probabilities.argsort()[::-1][:num_recommendations]
# 상위 N개 제품 추천
print(f"회원님의 정보로 저희가 추천 드릴 수 있는 상위 {num_recommendations}개의 제품은:", '번, '.join(map(str,top_product_indices)),'번 입니다.')