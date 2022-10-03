import requests
from twitch_api import TwitchAPI
from utils import client_id, client_secret

api = TwitchAPI()
api.auth(client_id, client_secret)

class GetTopGames:
    def __init__(self):
        pass

    def get_top_games(self):
        params = {
            'first' : 100
        }

        games_id = {}
        games_name = {}
        games_box_art_url = {}
        response = requests.get('https://api.twitch.tv/helix/games/top', params=params, headers=api.headers)
        for game in response.json()['data']:
            games_id[game['name']] = game['id']
            games_name[game['id']] = game['name']
            games_box_art_url[game['name']] = game['box_art_url'].replace('{width}', '285').replace('{height}', '380')
        
        return games_id, games_name, games_box_art_url


top_games = GetTopGames()
games_id, games_name, games_box_art_url = top_games.get_top_games()