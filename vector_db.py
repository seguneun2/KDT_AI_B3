from langchain.vectorstores import DeepLake
from langchain.embeddings.openai import OpenAIEmbeddings


# deeplake 에 데이터 업로드
def upload_document(texts, username, file_name):
    print("OPEN AI deeplake 에 업로드 시작..",end='')
    # openai embedding
    embeddings = OpenAIEmbeddings()
  
    db = DeepLake.from_documents(
    texts,
    embeddings,
    dataset_path=f"hub://{username}/{file_name}"
    )
    
    db = DeepLake(
        dataset_path=f"hub://{username}/{file_name}",
        read_only=True,
        embedding_function=embeddings
    )
    print("  완료! ")
    return db

def get_retriever(db, distance, fetch, relevance, k):
    retriever = db.as_retriever()
    retriever.search_kwargs["distance_metric"] = distance
    retriever.search_kwargs["fetch_k"] = fetch
    retriever.search_kwargs["maximal_marginal_relevance"] = relevance
    retriever.search_kwargs["k"] = k
    
    return retriever