from flask import Blueprint,request
import sys
import os

# 현재 스크립트 파일의 경로를 얻어옵니다.
current_folder = os.path.dirname(os.path.abspath(__file__))
# 프로젝트 루트 디렉토리를 계산합니다.
project_root = os.path.dirname(current_folder)
# 프로젝트 루트 디렉토리를 sys.path에 추가합니다.
sys.path.append(project_root)

from models.chatbot.chatGPT_0910 import ChatBot

# 챗봇 bp
bp = Blueprint('chat',__name__,url_prefix='/chat')

chatbot = ChatBot()

# 사용자 질문 종류

# 1) 시스템 안내 -> (chatGPT)
# 2) 스트레칭 질문 -> (chatGPT)
# 3) 상품 추천 -> (chatGPT) *chatGPT 의도 분류 + (ML) 추천 상품 추론
# 4) 기타 -> (chatGPT)
@bp.route('/answer',methods=['POST'])
def generate_answer():

    answer = ''
    
    try:
        user_request = request.form
        user_input = user_request['question']
        
        print("질문 : ",user_input)
        answer = chatbot.get_answer(user_input)

        if '추천' in answer:
            answer += (" 상품 분류 : " + chatbot.okt.nouns(answer)[-2])

        print("답변 : ",answer)

    except Exception as e:
        print("예외 발생!!! ",str(e))
        answer = str(e)

    return answer