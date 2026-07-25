import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = "edugenie-secret-key"

    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

    VECTOR_DB_FOLDER = os.path.join(BASE_DIR, "vector_db")

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    ALLOWED_EXTENSIONS = {"pdf"}