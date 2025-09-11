import language_tool_python
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize LanguageTool
tool = None

def initialize_tool():
    global tool
    if tool is None:
        try:
            logger.info("Initializing LanguageTool...")
            tool = language_tool_python.LanguageTool('en-US')
            logger.info("LanguageTool initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing LanguageTool: {str(e)}")
            raise Exception(f"Grammar tool initialization failed: {str(e)}")
    return tool

def check_and_correct(text: str):
    """
    Check and correct grammar in the input text.
    Returns a tuple of (corrected_text, issues).
    """
    logger.info(f"Checking grammar for text: {text}")
    try:
        tool = initialize_tool()
        matches = tool.check(text)
        corrected_text = tool.correct(text)
        issues = [match.message for match in matches]
        logger.info(f"Corrected text: {corrected_text}, Issues: {issues}")
        return corrected_text, issues
    except Exception as e:
        logger.error(f"Error checking grammar: {str(e)}")
        raise Exception(f"Grammar check failed: {str(e)}")