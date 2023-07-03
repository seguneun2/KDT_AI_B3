from langchain.schema import Document
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter

# 도큐먼트 리스트들을 chunking 하기
def document_chunking(docs, size, overlap=0):
    text_splitter = CharacterTextSplitter(chunk_size=size, chunk_overlap=overlap)
    texts = text_splitter.split_documents(docs)
    return texts 

# dictionary 를 도큐먼트 리스트 형식으로 바꾸기
def document_processing(github_info_dict):
    docutment_list = []
    
    # langchain 의 Document 로 변환 
    for file_name, file_content in github_info_dict.items():
        tmp_doc = Document(
            page_content=file_name,
            metadata={"content":file_content}
        )
        
        docutment_list.append(tmp_doc)

    return docutment_list
        
    