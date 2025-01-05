# utils/text_processing.py
import logging
from langchain.text_splitter import CharacterTextSplitter

# Configure logging
logger = logging.getLogger(__name__)

def get_text_chunks(text):
    try:
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)
        logger.info(f"Created {len(chunks)} text chunks")
        return chunks
    except Exception as e:
        logger.error(f"Error in get_text_chunks: {str(e)}")
        return None