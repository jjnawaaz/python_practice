import os
import httplib2
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_httplib2 import AuthorizedHttp

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def get_gmail_service():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    http = AuthorizedHttp(creds, http=httplib2.Http(timeout=15))
    return build("gmail", "v1", http=http)


def fetch_unread_emails(max_results=10):
    service = get_gmail_service()

    results = service.users().messages().list(
        userId="me",
        labelIds=["INBOX", "UNREAD"],
        maxResults=max_results
    ).execute()

    messages = results.get("messages", [])
    emails = []

    for msg in messages:
        data = service.users().messages().get(
            userId="me",
            id=msg["id"],
            format="metadata",
            metadataHeaders=["Subject", "From"]
        ).execute()

        snippet = data.get("snippet", "")
        email_link = f"https://mail.google.com/mail/u/0/#inbox/{msg['id']}"

        emails.append({
            "id": msg["id"],
            "snippet": snippet,
            "link": email_link
        })

    return emails
