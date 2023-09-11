from flask import Flask
import json

# # 테스트용 json 파일 생성
# data = {
#     "id" : 1,
#     "age": 27,
#     "gender" : 1,
#     "job" : 7,
#     "turtle_neck" : 0.2,
#     "sleepiness" : 0.5,
#     "tooped_position" : 0.7
# }

# # JSON 파일로 데이터 저장
# with open("data/tmp_user.json", "w") as json_file:
#     json.dump(data, json_file, indent=7)

def create_app():
    app = Flask(__name__)

    from .views import main_views,chat_views,rs_views,board_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(chat_views.bp)
    app.register_blueprint(rs_views.bp)
    app.register_blueprint(board_views.bp)

    return app