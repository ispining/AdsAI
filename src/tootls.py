def api_key() -> str:
    """
    Returns the Gemini API key from the file.
    """
    with open("/rkeys/gemini", "r", encoding="utf-8") as f:
        return f.read()
    
