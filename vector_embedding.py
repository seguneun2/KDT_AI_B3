from dotenv import load_dotenv
from langchain.vectorstores import DeepLake

load_dotenv()

def upload_document(texts, username, file_name):
    