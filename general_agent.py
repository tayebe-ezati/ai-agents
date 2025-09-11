from transformers import pipeline
from typing import str

# Initialize the question-answering pipeline
qa_pipeline = None
try:
    qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
except Exception as e:
    print(f"Error initializing QA pipeline: {str(e)}")

def general_agent(question: str, context: str = None) -> str:
    """
    Answer a question using a pre-trained question-answering model.
    If no context is provided, use a default context.
    """
    if qa_pipeline is None:
        return "Error: QA model failed to initialize. Please check dependencies."

    # Default context for general questions (can be expanded)
    default_context = (
        "This is a general knowledge base. It contains information about various topics, "
        "including history, science, and notable figures. For example, Ada Lovelace was a "
        "mathematician and writer, known for her work on Charles Babbage's Analytical Engine, "
        "and is considered the first computer programmer."
    )

    context = context or default_context

    try:
        result = qa_pipeline(question=question, context=context)
        return result["answer"]
    except Exception as e:
        return f"Error answering question: {str(e)}"