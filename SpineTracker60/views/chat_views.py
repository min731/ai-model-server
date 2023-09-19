from flask import Blueprint,request,jsonify
import pandas as pd
import pickle
import sys
import os

# 현재 스크립트 파일의 경로를 얻어옵니다.
current_folder = os.path.dirname(os.path.abspath(__file__))
# 프로젝트 루트 디렉토리를 계산합니다.
project_root = os.path.dirname(current_folder)
# 프로젝트 루트 디렉토리를 sys.path에 추가합니다.
sys.path.append(project_root)

from models.chatbot.chatGPT_0919_2 import ChatBot

# 챗봇 bp
bp = Blueprint('chat',__name__,url_prefix='/chat')

chatbot = ChatBot()

# 사용자 질문 종류

# 1) 시스템 안내 -> (chatGPT)
# 2) 스트레칭 질문 -> (chatGPT)
# 3) 상품 추천 -> (chatGPT) *chatGPT 의도 분류 + (ML) 추천 상품 추론
# 4) 기타 -> (chatGPT)

#Recommendaton system
# 저장된 모델을 불러오기
with open('SpineTracker60/recommendation/best_model.pkl', 'rb') as f:
  loaded_model = pickle.load(f)

age = {0: "나이_10대", 1: "나이_20대", 2: "나이_30대", 3: "나이_40대", 4: "나이_50대", 5: "나이_60대이상",}
gender = {0 : "성별_녀", 1 : "성별_남"}
job = {0 : '직업_관리자', 1 : '직업_군인',2 : '직업_기능원 및 관련 기능 종사자', 3 : '직업_농림어업 숙련 종사자', 4 : '직업_단순노무 종사자', 5 : '직업_사무 종사자',
       6 : '직업_서비스 종사자', 7 : '직업_장치·기계 조작 및 조립 종사자', 8 : '직업_전문가 및 관련 종사자', 9 : '직업_판매 종사자'}
def Rec(input_json):
    # 추론할 정보
    user_input = {
        age[input_json['age']] : 1,
        gender[input_json['gender']] : 1,
        job[input_json['job']]: 1,
        '거북목': input_json['turtle_neck'],
        '졸음': input_json['sleepiness'],
        '비대칭': input_json['stooped_position'],
        '척추후만': input_json['sit_back']
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
    answer = f"회원님의 정보로 저희가 추천 드릴 수 있는 상위 {num_recommendations}개의 제품은: "+ '번, '.join(map(str, top_product_indices))+'번 입니다.'
    #print(answer)
    return answer

# 답변 
@bp.route('/answer',methods=['POST'])
def gen_ans():
    
    try:
        input_json = request.json
        question = input_json['question']
        answer = chatbot.get_answer(question)

        if '추천' in answer:
            #print(chatbot.okt.nouns(answer)[-2])
            #answer += " 상품 분류 : " + chatbot.okt.nouns(answer)[-2]
            answer += '\n' + Rec(input_json)
        print("답변 : ",answer)

    except Exception as e:
        print("예외 발생!!! ",str(e))
        answer = str(e)

    input_json['answer'] = answer

    return jsonify(input_json)


# 답변 테스트
@bp.route('/answer_test',methods=['POST'])
def gen_ans_test():
    
    try:
        input_form = request.form
        user_input = input_form['question']
        
        print("질문 : ",user_input)
        answer = chatbot.get_answer(user_input)

        if '추천' in answer:
            answer += (" 상품 분류 : " + chatbot.okt.nouns(answer)[-2])

        print("답변 : ",answer)

    except Exception as e:
        print("예외 발생!!! ",str(e))
        answer = str(e)

    return answer



{
    "id" : 1,

    "age" : 27,
    "gender" : 1,
    "job" : 7,

    "turtle_neck" : 0.5,
    "sleepiness" : 0.2,
    "stooped_position" : 0.9,
    
    "question" : "의자 추천점"

}