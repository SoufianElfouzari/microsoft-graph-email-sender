import msal
from src.config.load_env import CLIENT_ID, CLIENT_SECRET, AUTHORITY, SCOPE

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
