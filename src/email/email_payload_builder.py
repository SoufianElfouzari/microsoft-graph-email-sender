def email_payload_builder(subject, recipient, body):
    email_data = {
        "message": {
            "subject": subject,
            "body": {
                "contentType": "HTML",
                "content": body
            },
            "toRecipients": [
                {"emailAddress": {"address": recipient}}
            ]
        }
    }

    return email_data