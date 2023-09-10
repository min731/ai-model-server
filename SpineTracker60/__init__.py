from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import main_views,chat_views,rs_views,board_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(chat_views.bp)
    app.register_blueprint(rs_views.bp)
    app.register_blueprint(board_views.bp)

    return app