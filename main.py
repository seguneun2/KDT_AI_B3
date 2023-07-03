
from validation import url_check
from get_info_from_api import github_api_call
from data_processing import (
    document_processing,
    document_chunking,
    embedding_into_vectordb,
)
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
    github_info_dict = github_api_call(github_link)
    
    # 3. chunking 후 text processing 하기 
    docs = document_processing(github_info_dict)
    texts = document_chunking(docs, chunking=1000, overlap=0)
    
    # 4. chunking 된 데이터 vector db 로 임베딩 하기 
    
    
    
    # 5. 원하는 질문 입력 하기 
    
    
if __name__ == "__main__":
    main()