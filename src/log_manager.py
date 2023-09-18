import os
from dotenv import load_dotenv
from genius import genius_auth

# Load environment variables from the .env file in the root directory
dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)

# Retrieve Genius API and Instagram credentials from environment variables
api_key = os.getenv("api_key")  # Genius API key
user_name = os.getenv("user_name")  # Instagram username
password = os.getenv("password")  # Instagram password

# Authenticate with the Genius API using the provided API key
genius = genius_auth(api_key)
