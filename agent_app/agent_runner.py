# this is the orchestrator of our ai agents

from gmail_tool import fetch_unread_emails
from agent_brain import think
from discord_tool import notify_discord_sync
from message_formatter import format_job_alert



def run_agent():
    emails=fetch_unread_emails(10)

    for email in emails:
        decision = think(email["snippet"])
        decision["email_link"] = email["link"]

        if decision.get('action') == 'notify_discord':
            msg = format_job_alert(decision)
            notify_discord_sync(msg)
            print("\n🔔 Discord notified")
        else:
            print('\n Ignored')


if __name__ == '__main__':
    run_agent()
