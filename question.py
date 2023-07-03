from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
import asyncio



def get_conversation_chain(model_name, retriever):
    model = ChatOpenAI(model_name=model_name)
    qa = ConversationalRetrievalChain.from_llm(model, retriever=retriever)
    return model, qa

async def get_qu():
    try:
        await asyncio.wait_for(get_conversation_chain(), timeout=2.0)
    
    except asyncio.TimeoutError:
        print("Time out. ")

