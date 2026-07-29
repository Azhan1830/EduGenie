from flask import Flask

from config import Config

from routes import main_bp, upload_bp, chat_bp, export_bp

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(main_bp)

app.register_blueprint(upload_bp)

app.register_blueprint(chat_bp  )

app.register_blueprint(export_bp)

if __name__ == "__main__":
    app.run(debug=True, port=1830)