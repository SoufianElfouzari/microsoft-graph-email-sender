import msal
from src.config.load_env import CLIENT_ID, CLIENT_SECRET, AUTHORITY, SCOPE

"""
Explanation:
This function uses the MSAL library to get an access token for the Microsoft Graph API. 
It creates a ConfidentialClientApplication instance with the client ID, authority, and client secret. 
Then it calls acquire_token_for_client with the specified scopes to get an access token for them. 

If successful, 
    it returns the access token; 
    otherwise, 
    it raises an exception with the error details.
"""

def get_access_token():
    app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )

    result = app.acquire_token_for_client(scopes=SCOPE)

    if "access_token" in result:
        return result["access_token"]

    raise Exception(
        "Token Fehler",
        result.get("error"),
        result.get("error_description")
    )
