from transformers import pipeline

# ... (keep initialize_pipeline and logging)

# Change to text-generation pipeline
qa_pipeline = None  # Rename if needed

def initialize_pipeline():
    global qa_pipeline
    if qa_pipeline is None:
        try:
            logger.info("Initializing text generation pipeline...")
            qa_pipeline = pipeline("text-generation", model="distilgpt2")
            logger.info("Text generation pipeline initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing pipeline: {str(e)}")
            qa_pipeline = None
    return qa_pipeline

def general_agent(question: str, context: str = None) -> str:
    # ... (keep logging and checks)
    
    try:
        pipeline = initialize_pipeline()
        if pipeline is None:
            return "Pipeline initialization failed."
        
        prompt = f"Question: {question}\nContext: {context or 'General knowledge.'}\nAnswer:"
        result = pipeline(prompt, max_length=100, num_return_sequences=1)
        answer = result[0]['generated_text'].split("Answer:")[-1].strip()
        return f"{answer}"
    except Exception as e:
        return f"Error answering question: {str(e)}"