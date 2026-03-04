
from src.config.email_config import email

def build_email_payload():
    email_data = {
        "message": {
            "subject": email.subject,
            "body": {
                "contentType": "HTML",
                "content": email.body
            },
            "toRecipients": [
                {"emailAddress": {"address": email.recipient}}
            ]
        }
    }

    return email_data