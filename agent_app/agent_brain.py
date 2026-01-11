from llm_brain import analyze_email

def think(email_snippet):
    decision = analyze_email(email_snippet)
    return decision