# Microsoft Graph Email Sender

A lightweight and easy to use Python service for sending HTML emails through the
Microsoft Graph API using Azure authentication.

------------------------------------------------------------------------

## Features

-   Send emails via **Microsoft Graph API**
-   Secure authentication using **Microsoft Authentication Library
    (MSAL)**
-   Support for **HTML email templates**
-   Modern, maintainable and standart project architecture
-   Environment-based configuration using `.env`
-   Easily extendable for attachments, templates, and automation
-   Clean separation of authentication, services, and utilities

------------------------------------------------------------------------

## Tech Stack

  Technology                                Purpose
  ----------------------------------------- -----------------------------------
  Python                                    Core programming language
  Microsoft Graph API                       Sending emails via Outlook
  MSAL (Microsoft Authentication Library)   Azure AD authentication
  Requests                                  HTTP communication with Graph API
  HTML                                      Email templates
  python-dotenv                             Environment variable management

------------------------------------------------------------------------

## Installation

### 1. Clone the repository

    git clone https://github.com/SoufianElfouzari/microsoft-graph-email-sender.git
    cd microsoft-graph-email-sender

### 2. Create a virtual environment

    python -m venv venv

Activate it:

Linux / macOS

    source venv/bin/activate

Windows

    venv\Scripts\activate

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Configure environment variables

Copy the example environment file:

    cp .env.example .env

Fill in your Microsoft Azure credentials.

### 5. Run the project

After you edited the `templates/base_email.html` & `config/email_config.py` you can run the project.
To get more Info on how what to edit inside those files, refer to the *Usage* section.

    python src/main.py

------------------------------------------------------------------------

## Configuration

Example `.env` file:

    CLIENT_ID=your_client_id
    CLIENT_SECRET=your_client_secret
    TENANT_ID=your_tenant_id
    MAIL_USERNAME=sender_email@domain.com

  Variable        Description
  --------------- ------------------------------
  CLIENT_ID       Azure Application Client ID
  CLIENT_SECRET   Azure Application Secret
  TENANT_ID       Azure Directory Tenant ID
  MAIL_USERNAME   Email address used as sender

------------------------------------------------------------------------

## Usage

Example usage: (`config/email_config.py`)

    from models.email_model import EmailModel
    from email.email_service import send_email

    email = EmailModel(
        subject="Test Email from Microsoft Graph API",
        recipient="example@example.com",
        body="<p>Hello, this email was sent using Microsoft Graph!</p>"
    )

    send_email(email.subject, email.recipient, email.body)

------------------------------------------------------------------------

## Project Structure

    microsoft-graph-email-sender
    │
    ├── src
    │   ├── auth
    │   │   └── graph_auth.py
    │   │
    │   ├── config
    │   │   ├── email_config.py
    │   │   └── load_env.py
    │   │
    │   ├── email
    │   │   ├── email_service.py
    │   │   ├── email_payload_builder.py
    │   │   └── graph_client.py
    │   │
    │   ├── models
    │   │   └── email_model.py
    │   │
    │   ├── templates
    │   │   └── base_email.html
    │   │
    │   ├── utils
    │   │   └── template_loader.py
    │   │
    │   └── main.py
    │
    ├── tests
    ├── examples
    ├── .env.example
    ├── requirements.txt
    ├── pyproject.toml
    ├── LICENSE
    └── README.md

------------------------------------------------------------------------

## Contributing

1.  Fork the repository
2.  Create a branch

```{=html}
<!-- -->
```
    git checkout -b feature/your-feature

3.  Commit your changes

```{=html}
<!-- -->
```
    git commit -m "feat: add new feature"

4.  Push the branch

```{=html}
<!-- -->
```
    git push origin feature/your-feature

5.  Open a Pull Request

------------------------------------------------------------------------

## License

MIT License

------------------------------------------------------------------------

## Author

Soufian Elfouzari

GitHub: https://github.com/SoufianElfouzari
