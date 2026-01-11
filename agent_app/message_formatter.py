def format_job_alert(decision: dict):
    return f"""
🚨 New Job Opportunity Detected

Role: {decision.get("role")}
Company: {decision.get("company")}
Urgency: {decision.get("urgency").upper()}

🔗 Open Email:
{decision.get("email_link")}
"""
