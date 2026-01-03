# importing modules
import os
from dotenv import load_dotenv

# loading all the variables from the .env files
load_dotenv()

# storing the API
API_URL = os.getenv("API_URL")