import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
load_dotenv(os.path.join(BASE_DIR, ".env"))

APP_NAME = os.getenv("APP_NAME", "Student Information System")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
MAX_STUDENTS = int(os.getenv("MAX_STUDENTS", "50"))
