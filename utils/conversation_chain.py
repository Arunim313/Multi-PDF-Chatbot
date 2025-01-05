# utils/conversation_chain.py
import logging
from langchain.chat_models import ChatOpenAI
from langchain_google_vertexai import ChatVertexAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

# Configure logging
logger = logging.getLogger(__name__)

def get_conversation_chain(vectorstore):
    try:
        llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
        # llm = ChatVertexAI(model="gemini-pro")
        memory = ConversationBufferMemory(
            memory_key='chat_history',
            return_messages=True
        )
        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(),
            memory=memory
        )
        logger.info("Conversation chain created successfully")
        return conversation_chain
    except Exception as e:
        logger.error(f"Error in get_conversation_chain: {str(e)}")
        return None