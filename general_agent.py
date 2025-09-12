import streamlit as st
from transformers import pipeline
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

qa_pipeline = None

@st.cache_resource
def initialize_pipeline():
    global qa_pipeline
    if qa_pipeline is None:
        try:
            logger.info("Initializing text generation pipeline...")
            qa_pipeline = pipeline("text-generation", model="facebook/opt-350m")
            logger.info("Text generation pipeline initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing pipeline: {str(e)}")
            qa_pipeline = None
    return qa_pipeline

def general_agent(question: str, context: str = None) -> str:
    """
    Answer a question using a generative model, with optional context.
    Returns the generated answer as a string.
    """
    logger.info(f"Received question: {question}, context: {context}")
    if not question:
        logger.warning("No question provided.")
        return "Please provide a question."
    
    try:
        pipeline = initialize_pipeline()
        if pipeline is None:
            logger.error("Pipeline is None.")
            return "Pipeline initialization failed."
        
        # Construct prompt
        prompt = f"Question: {question}\n"
        if context:
            prompt += f"Context: {context}\n"
        prompt += "Answer:"
        
        logger.info("Running pipeline...")
        result = pipeline(prompt, max_length=100, num_return_sequences=1, truncation=True)
        answer = result[0]['generated_text'].split("Answer:")[-1].strip()
        logger.info(f"Answer: {answer}")
        return answer
    except Exception as e:
        logger.error(f"Error answering question: {str(e)}")
        return f"Error answering question: {str(e)}"