
import os
from validation import url_check
from get_info_from_api import github_api_call
from data_processing import (
    document_processing,
    document_chunking,
)
from vector_db import upload_document, get_retriever
from question import get_conversation_chain
from dotenv import load_dotenv

load_dotenv()

def main():
    # 1. 입력받기
    github_link = input("GitHub 링크를 입력해주세요 : ")
    while True:
        if url_check(github_link) is True:
            print("유효성 검사 완료 API 서치 시작")
            break
        else: 
            github_link = input("유효하지 않은 GitHub 링크입니다. 다시 입력해주세요 : ")

    # 2.API Info Dictionary 형식으로 받아오기
    github_info_dict = github_api_call(github_link, make_txt_file=False)
    
    # 3. chunking 후 text processing 하기 
    docs = document_processing(github_info_dict, make_txt_file=False)
    texts = document_chunking(docs, size=1000, overlap=0)
    
    # 4. chunking 된 데이터 vector db 로 임베딩 하기 
    db = upload_document(texts, os.getenv('DEEPLAKE_USERNAME'), 'langchain-code_jhkim')
    retriever =  get_retriever(db, "cos", 100, True, 10)
    
    # 5. 원하는 질문 입력 하기 
    model, qa = get_conversation_chain("gpt-3.5-turbo", retriever)
    
    # 6. QA 시작
    chat_history = []
    while True:
        question = input("질문을 입력해주세요 : ")
        result = qa({"question": question, "chat_history": chat_history})
        chat_history.append((question, result["answer"]))
        
        print(f"**Answer**: {result['answer']} \n")
if __name__ == "__main__":
    main()