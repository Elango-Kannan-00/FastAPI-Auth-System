from dotenv import load_dotenv
import os

# Loads the .env file here
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

