# app.py
import streamlit as st
import os
from dotenv import load_dotenv
import logging
import traceback

# Import utility functions
from utils.pdf_processing import get_pdf_text
from utils.text_processing import get_text_chunks
from utils.vector_store import get_vectorstore
from utils.conversation_chain import get_conversation_chain

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Define persistent directory for ChromaDB
PERSIST_DIRECTORY = "db"
os.makedirs(PERSIST_DIRECTORY, exist_ok=True)

# Initialize session state
if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "processing_complete" not in st.session_state:
    st.session_state.processing_complete = False

def handle_userinput(user_question):
    try:
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chat_history = response['chat_history']
        st.session_state.user_question = ""
    except Exception as e:
        logger.error(f"Error in handle_userinput: {str(e)}")
        st.error(f"Error processing your question: {str(e)}")

def process_pdfs(pdf_docs):
    try:
        with st.spinner("Extracting text from PDFs..."):
            raw_text = get_pdf_text(pdf_docs)
            if raw_text is None:
                return

        with st.spinner("Creating text chunks..."):
            text_chunks = get_text_chunks(raw_text)
            if text_chunks is None:
                return

        with st.spinner("Creating vector store..."):
            vectorstore = get_vectorstore(text_chunks, PERSIST_DIRECTORY)
            if vectorstore is None:
                return

        with st.spinner("Setting up conversation chain..."):
            st.session_state.conversation = get_conversation_chain(vectorstore)
            if st.session_state.conversation is None:
                return

        st.session_state.processing_complete = True
        st.success("Processing complete!")
        logger.info("PDF processing completed successfully")
    except Exception as e:
        logger.error(f"Error in process_pdfs: {str(e)}\n{traceback.format_exc()}")
        st.error(f"Error processing PDFs: {str(e)}")
        st.session_state.processing_complete = False

# Page configuration
st.set_page_config(page_title="Chat with Multiple PDFs", page_icon="📚", layout="wide")

# Main UI
st.header("Chat with Multiple PDFs 📚")

# Sidebar for PDF upload
with st.sidebar:
    st.subheader("Your Documents")
    pdf_docs = st.file_uploader(
        "Upload your PDFs here and click on 'Process'",
        accept_multiple_files=True,
        type="pdf"
    )
    if st.button("Process"):
        if pdf_docs:
            process_pdfs(pdf_docs)
        else:
            st.warning("Please upload at least one PDF file.")

# Main chat interface
if st.session_state.processing_complete:
    user_question = st.text_input(
        "Ask a question about your documents:",
        placeholder="ask question here",
        value=st.session_state.get('user_question', '')
    )
    
    if st.button("Send Query"):
        if user_question:
            handle_userinput(user_question)

    # Display chat history
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(f"You: {message.content}")
        else:
            with st.chat_message("assistant"):
                st.write(f"Bot: {message.content}")
else:
    st.info("Please upload your PDFs and click 'Process' to start chatting.")

# Add custom CSS for better UI
st.markdown("""
<style>
    .stTextInput > div > div > input {
        background-color: #050505;
    }
    .stTextInput > div > div > input:focus {
        box-shadow: 0 0 0 2px #4CAF50;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)