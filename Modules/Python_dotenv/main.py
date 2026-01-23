from dotenv import load_dotenv
import os


# loads variables from .env into environment
load_dotenv(dotenv_path="stagging.env") # define dotenv path

api_key = os.getenv("API_KEY")
print(f'Your API key is: {api_key}')


