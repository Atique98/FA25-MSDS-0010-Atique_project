import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Student Information System")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
MAX_STUDENTS = int(os.getenv("MAX_STUDENTS", "50"))
API_KEY = os.getenv("API_KEY")
