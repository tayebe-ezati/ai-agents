from transformers import pipeline

# Initialize the question-answering pipeline
qa_pipeline = None

def initialize_pipeline():
    global qa_pipeline
    if qa_pipeline is None:
        try:
            qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad", revision="main")
        except Exception as e:
            print(f"Error initializing pipeline: {str(e)}")
    return qa_pipeline

def general_agent(question: str, context: str = None) -> str:
    """
    Answer a question using the QA pipeline, with optional context.
    If no context is provided, use a default context.
    """
    if not question:
        return "Please provide a question."
    
    if context is None:
        context = "This is a default context for answering questions when no specific context is provided."
    
    try:
        pipeline = initialize_pipeline()
        if pipeline is None:
            return "Pipeline initialization failed."
        
        result = pipeline(question=question, context=context)
        return result['answer']
    except Exception as e:
        return f"Error answering question: {str(e)}"