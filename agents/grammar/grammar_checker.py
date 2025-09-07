import language_tool_python

def check_and_correct(text: str):
    """
    بررسی گرامر متن انگلیسی با LanguageTool
    خروجی: متن اصلاح‌شده + لیست خطاها
    """
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    corrected = tool.correct(text)

    issues = []
    for m in matches:
        issues.append({
            "message": m.message,
            "suggestions": m.replacements
        })

    return corrected, issues
