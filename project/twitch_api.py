import requests

class TwitchAPI():

    def __init__(self):
        self.headers = None

    def auth(self, client_id, client_secret):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = f'client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials'

        response = requests.post('https://id.twitch.tv/oauth2/token', headers=headers, data=data)
        
        bearer = response.json()['access_token']
        self.headers = {
            'Authorization': f'Bearer {bearer}',
            'Client-Id': client_id,
        }