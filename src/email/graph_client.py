import json
import requests


def send_graph_request(url, access_token, payload):

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(payload)
    )

    if response.status_code != 202:
        raise Exception(
            f"Mail Fehler {response.status_code}: {response.text}"
        )

    return response