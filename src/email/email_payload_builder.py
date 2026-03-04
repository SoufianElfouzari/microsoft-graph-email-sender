
from config.email_config import email
def email_payload_builder():
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