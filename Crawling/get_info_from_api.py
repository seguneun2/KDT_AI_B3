import time
import json
import base64
import requests
import pandas as pd
from anytree import Node, RenderTree 

df = pd.DataFrame(columns=["file_name", "content"])
root = Node("root")


def api_call(api_link):
    headers = {
        "Authorization":"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",
    }
    response = requests.get(api_link, headers=headers)
    
    # time.sleep(0.3)
    if response.status_code == 200:
        content = response.content.decode('utf-8')
        return json.loads(content)
    else:
        print(response.status_code)
        return None


def get_file_info(api_link, file_name, parent_node):
    file_info = api_call(api_link)
    content = base64.b64decode(file_info['content']).decode('utf-8')
    df.loc[len(df)] = [file_name, content]
    Node(file_name, parent=parent_node)
    return


def get_dir_info(api_link, dir_name="GitHub_Reposiory", parent_node=root):
    file_info_list = api_call(api_link)  
    for file_info in file_info_list:
        
        file_name = file_info["name"]
        file_api_link = file_info["_links"]["self"]
        
        if file_info["type"] == "file":
            get_file_info(file_api_link, file_name, parent_node)
        else:
            dir_node = Node(file_name, parent=parent_node)
            get_dir_info(file_api_link, file_name, dir_node)


def main(web_link):
    start_time = time.time() 
    user_name,repo_name = web_link.split('/')[-2:] 
    get_dir_info(f"https://api.github.com/repos/{user_name}/{repo_name}/contents/")

    tree_output = ""
    for pre, _, node in RenderTree(root):
        tree_output += f"{pre}{node.name}\n"

    with open("tree_output.txt", "w",encoding='utf-8') as f:
        f.write(tree_output)
    df.to_excel("data_output.xlsx", index=False)

    end_time = time.time()  # 실행 종료 시간 기록
    execution_time = end_time - start_time  # 실행 시간 계산
    print(f"프로그램 실행 시간: {execution_time:.2f}초")


# 여기다가 링크 입력하고 실행하면 됨
web_link = "https://github.com/SamLynnEvans/Transformer"
main(web_link)


