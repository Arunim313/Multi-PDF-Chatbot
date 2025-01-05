# utils/pdf_processing.py
import logging
from PyPDF2 import PdfReader

# Configure logging
logger = logging.getLogger(__name__)

def get_pdf_text(pdf_docs):
    try:
        text = ""
        for pdf in pdf_docs:
            logger.info(f"Processing PDF: {pdf.name}")
            pdf_reader = PdfReader(pdf)
            for page_num, page in enumerate(pdf_reader.pages):
                try:
                    page_text = page.extract_text()
                    text += page_text
                    logger.info(f"Processed page {page_num + 1}")
                except Exception as e:
                    logger.error(f"Error processing page {page_num + 1}: {str(e)}")
        return text
    except Exception as e:
        logger.error(f"Error in get_pdf_text: {str(e)}")
        return None