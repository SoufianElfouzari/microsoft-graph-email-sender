from src.models.email_model import EmailModel
from src.utils.template_loader import load_template

html_body = load_template("base_email.html")

email = EmailModel(
    subject="Test Email from Microsoft Graph API", # TODO: Update with your Subject
    
    # Here you can add as many recipients as you want, simply by adding their email addresses to the list
    recipient=["elfouzari.soufian@gmail.com", "another recipient@gmail.com"], # TODO: Update with your Recipients
    
    body=html_body
)