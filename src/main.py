import email
from src.email.email_service import send_email

def main(): 
    
    try: 
        send_email() 
        print("Email sent successfully!") 
        print("subject:", email.subject) 
        print("recipient:", email.recipient) 
        print("body:", email.body) 
    except Exception as e: 
        print("Failed to send email:", str(e))    
              
if __name__ == "__main__": 
    main() 