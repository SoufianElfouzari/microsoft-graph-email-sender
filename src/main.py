from src.email.email_service import send_email 

def main(): 
    subject = "Test Email from Microsoft Graph API" 
    recipient = "elfouzari.soufian@gmail.com" 
    body = "<p>Hello, this is a test email sent using Microsoft Graph API!</p>" 
    
    try: 
        send_email(subject, recipient, body) 
        print("Email sent successfully!") 
        print("subject:", subject) 
        print("recipient:", recipient) 
        print("body:", body) 
    except Exception as e: 
        print("Failed to send email:", str(e))    
              
if __name__ == "__main__": 
    main() 