import requests
from twitch_api import TwitchAPI
from utils import client_id, client_secret, games_id, prev_week_saturday, prev_week_sunday

api = TwitchAPI()
api.auth(client_id, client_secret)

class ClipContent:
    def __init__(self, url, broadcaster_id, creator_name, title, thumbnail_url):
        self.url = url
        self.broadcaster_id = broadcaster_id
        self.creator_name = creator_name
        self.title = title
        self.thumbnail_url = thumbnail_url
    
    def __str__(self):
        return f'url: {self.url}\nbroadcaster_id: {self.broadcaster_id}\ncreator_name: {self.creator_name}\ntitle: {self.title}\nthumbnail_url: {self.thumbnail_url}'

class ClipsExtractor:
    def __init__(self):
        self.clips_content = []

    def get_clips(self, game_id, quantity):
        params = {
            'game_id' : game_id,
            'first' : quantity,
            'started_at' : prev_week_sunday,
            'ended_at' : prev_week_saturday
        }

        response = requests.get('https://api.twitch.tv/helix/clips', params=params, headers=api.headers)

        for clip in response.json()['data']:
            clip_content = ClipContent(url = clip['url'],
                                        broadcaster_id = clip['broadcaster_id'],
                                        creator_name = clip['creator_name'],
                                        title = clip['title'],
                                        thumbnail_url = clip['thumbnail_url'])
            self.clips_content.append(clip_content)


game_id = games_id['Counter-Strike: Global Offensive']

clip_extractor = ClipsExtractor()
clip_extractor.get_clips(game_id, 10)
for clip_content in clip_extractor.clips_content:
    print(clip_content)
    print('-------------------------------------------------------------')


