import json
import requests
from typing import Optional
from django.conf import settings

class FortressClient:
    settings:any = None
    auth_file: Optional[dict] = None
    access_token: Optional[str] = None
    expires_in: Optional[str] = None
    token_type: Optional[str] = None
    logged_in: Optional[str] = None

    @staticmethod
    def login():
        if FortressClient.logged_in is True:
            return FortressClient
        if FortressClient.settings is None:
            FortressClient.settings = settings
        FortressClient.auth_file = {
            "grant_type": "password",
            "username": settings.FORTRESS_USERNAME,
            "password": settings.FORTRESS_PASSWORD,
            "audience": settings.FORTRESS_AUDIENCE,
            "client_id": settings.FORTRESS_CLIENT_ID
        }
        FortressClient.access_token = None
        FortressClient.expires_in = None
        FortressClient.token_type = None
        FortressClient.logged_in = False

        return FortressClient._authenticate()
    @staticmethod
    def _authenticate():
        url = "https://fortress-sandbox.us.auth0.com/oauth/token"

        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=json.dumps(FortressClient.auth_file))
        if response.status_code not in [200, 201]:
            print("Auth endpoint returned " + str(response.status_code))
            return None

        auth_token = response.json()
        FortressClient.access_token = auth_token['access_token']
        FortressClient.expires_in = auth_token['expires_in']
        FortressClient.token_type = auth_token['token_type']
        FortressClient.logged_in = True
        FortressClient.get_headers = {
            'Authorization': 'Bearer ' + FortressClient.access_token,
            'accept': 'application/json',
            }
        FortressClient.post_headers = {
            'accept': 'application/json',
            'content-type': 'application/*+json',
            'Authorization':'Bearer ' + FortressClient.access_token
        }
        return FortressClient
