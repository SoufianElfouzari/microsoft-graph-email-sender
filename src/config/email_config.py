from src.models.email_model import EmailModel
from src.utils.template_loader import load_template


html_body = load_template("base_email.html")

email = EmailModel(
    subject="Test Email from Microsoft Graph API",
    recipient="elfouzari.soufian@gmail.com",
    body=html_body
)