import language_tool_python
from typing import Tuple, List, Dict

def check_and_correct(text: str) -> Tuple[str, List[Dict]]:
    """
    Check grammar of English text with LanguageTool.
    Returns: corrected text and list of issues.
    """
    try:
        tool = language_tool_python.LanguageTool('en-US')
        matches = tool.check(text)
        corrected = tool.correct(text)

        issues = [
            {"message": m.message, "suggestions": m.replacements}
            for m in matches
        ]
        return corrected, issues
    except Exception as e:
        return text, [{"message": f"Grammar check failed: {str(e)}", "suggestions": []}]