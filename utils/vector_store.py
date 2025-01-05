# utils/vector_store.py
import logging
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Configure logging
logger = logging.getLogger(__name__)

def get_vectorstore(text_chunks, persist_directory):
    try:
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_texts(
            texts=text_chunks,
            embedding=embeddings,
            persist_directory=persist_directory
        )
        vectorstore.persist()
        logger.info("Vector store created and persisted successfully")
        return vectorstore
    except Exception as e:
        logger.error(f"Error in get_vectorstore: {str(e)}")
        return None