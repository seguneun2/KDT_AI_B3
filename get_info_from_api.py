import os
import time
import json
import base64
import requests
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader

API_CALL_COUNT = 0
TOTAL_INFO_DICT = {}

# .env 파일 로드
load_dotenv()

def api_call(api_link):
    global API_CALL_COUNT
    API_CALL_COUNT += 1
    
    response = requests.get(
        api_link, 
        auth=(os.getenv("GITHUB_NAME") , os.getenv("GITHUB_TOKEN"))
    )
    
    if response.status_code == 200:
        content = response.content.decode('utf-8')
        return json.loads(content)
    else:
        print(response.status_code)
        return None


def get_dir_info(api_link, file_name="Git_Repository"):
    file_info_list = api_call(api_link) 
    for file_info in file_info_list:
        file_name = file_info["name"]
        
        if file_name.endswith('.pdf'):
            file_pdf_link = file_info["download_url"]
            loader = PyPDFLoader(file_pdf_link)
            pages = loader.load()
            total_pdf_string = ""
            
            for page in pages:
                total_pdf_string += page.page_content
            TOTAL_INFO_DICT[file_name] = total_pdf_string
            continue 
        else:
            file_api_link = file_info["_links"]["self"]
        
        if file_info["type"] == "file":
            file_info = api_call(file_api_link)
            content = base64.b64decode(file_info['content']).decode('utf-8')
            TOTAL_INFO_DICT[file_name] = content
        else:
            get_dir_info(file_api_link, file_name)


def github_api_call(web_link, make_txt_file=False):
    start_time = time.time() 
    user_name,repo_name = web_link.split('/')[-2:] 
    get_dir_info(f"https://api.github.com/repos/{user_name}/{repo_name}/contents/")
    print("Get DIR information.")

    end_time = time.time()  # 실행 종료 시간 기록
    execution_time = end_time - start_time  # 실행 시간 계산
    print(f"프로그램 실행 시간: {execution_time:.2f}초")
    print(f"API call 횟수 : {API_CALL_COUNT}")
    
    if make_txt_file is True:
        with open('myfile_2.txt', 'w', encoding='utf-8') as f:
            print(TOTAL_INFO_DICT, file=f)
    
    return TOTAL_INFO_DICT
# https://github.com/SamLynnEvans/Transformer