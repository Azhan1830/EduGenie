from flask import Flask

from config import Config

from routes import main_bp, upload_bp

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(main_bp)

app.register_blueprint(upload_bp)

if __name__ == "__main__":
    app.run(debug=True)