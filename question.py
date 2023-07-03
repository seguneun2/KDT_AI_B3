from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

def get_conversation_chain(model_name, retriever):
    model = ChatOpenAI(model_name=model_name)
    qa = ConversationalRetrievalChain.from_llm(model, retriever=retriever)
    return model, qa