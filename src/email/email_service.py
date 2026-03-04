from auth.graph_auth import get_access_token
from config.load_env import MAIL_USERNAME

from email.email_payload_builder import build_email_payload
from email.graph_client import send_graph_request


def send_email(subject, recipient, body):

    access_token = get_access_token()

    payload = build_email_payload(subject, recipient, body)

    url = f"https://graph.microsoft.com/v1.0/users/{MAIL_USERNAME}/sendMail"

    response = send_graph_request(url, access_token, payload)

    print("Email accepted by Microsoft Graph API")

    return response