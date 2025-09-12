from transformers import pipeline
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the question-answering pipeline
qa_pipeline = None

def initialize_pipeline():
    global qa_pipeline
    if qa_pipeline is None:
        try:
            logger.info("Initializing QA pipeline...")
            qa_pipeline = pipeline(
                "question-answering",
                model="distilbert-base-uncased-distilled-squad",
                revision="main",
                # model_kwargs={"cache_dir": "/content/model_cache"}  # Comment out or change to {"cache_dir": "./model_cache"}
            )
            logger.info("QA pipeline initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing pipeline: {str(e)}")
            qa_pipeline = None
    return qa_pipeline

def general_agent(question: str, context: str = None) -> str:
    """
    Answer a question using the QA pipeline, with optional context.
    If no context is provided, use a default context.
    """
    logger.info(f"Received question: {question}, context: {context}")
    if not question:
        logger.warning("No question provided.")
        return "Please provide a question."
    
    if context is None:
        context = "Ada Lovelace was a mathematician and writer, known for her work on Charles Babbage's Analytical Engine. She is considered the first computer programmer."
    
    try:
        pipeline = initialize_pipeline()
        if pipeline is None:
            logger.error("Pipeline is None.")
            return "Pipeline initialization failed."
        
        logger.info("Running pipeline...")
        result = pipeline(question=question, context=context)
        answer = result['answer']
        logger.info(f"Answer: {answer}, Score: {result['score']}")
        return f"{answer} (Score: {result['score']:.2f})"
    except Exception as e:
        logger.error(f"Error answering question: {str(e)}")
        return f"Error answering question: {str(e)}"