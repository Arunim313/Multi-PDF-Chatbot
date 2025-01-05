# Chat with Multiple PDFs

## Overview
"Chat with Multiple PDFs" is a Streamlit application that allows users to upload multiple PDF documents and interactively ask questions about their content. The application processes the PDFs, extracts text, and utilizes a conversational AI model to provide responses based on the uploaded documents.

## Features
- Upload multiple PDF files.
- Extract text from PDFs and create text chunks.
- Store and retrieve information using a vector store.
- Engage in a conversational interface with an AI assistant.
- Customizable user interface with CSS styling.

## Project Structure


### File Descriptions

#### **`app.py`**
- The main entry point for the application. This file integrates the utility modules and executes the application's primary workflow.

#### **`utils/`**
- **`pdf_processing.py`**  
  Contains functions to extract text from PDF files. Supports parsing PDFs for preprocessing.

- **`text_processing.py`**  
  Includes text chunking and processing utilities for managing large text data efficiently.

- **`vector_store.py`**  
  Manages the vector store, including storing and retrieving vector embeddings for efficient querying.

- **`conversation_chain.py`**  
  Sets up the conversational AI logic, connecting the user's inputs with AI responses using pre-defined models.

#### **`requirements.txt`**
- Lists all Python dependencies required to run the project. Install them using the command:  
  ```bash
  pip install -r requirements.txt


## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Arunim313/Multi-PDF-Chatbot
   cd Multi-PDF-Chatbot
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory of the project and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py
   ```

6. **Open your web browser** and navigate to `http://localhost:8501` to access the application.

## Usage Instructions

1. **Upload PDFs**: Use the sidebar to upload one or more PDF files.
2. **Process PDFs**: Click the "Process" button to extract text and prepare the application for interaction.
3. **Ask Questions**: Once processing is complete, enter your questions in the input field and click "Send Query" to receive answers based on the uploaded documents.
4. **View Chat History**: The chat history will display your questions and the AI's responses.

## Additional Documentation
- [Example Queries and Responses](examples.md)
- [Design Explanation and Architectural Overview](architecture.md)

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## Acknowledgments
- [Streamlit](https://streamlit.io/) for the web application framework.
- [LangChain](https://langchain.com/) for the conversational AI framework.
- [PyPDF2](https://pypdf.readthedocs.io/en/stable/) for PDF text extraction.

## Contact
For any questions or feedback, please reach out to [arunim.malviya.13@gmail.com].
