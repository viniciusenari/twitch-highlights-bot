import requests
import os
from twitch_api import TwitchAPI
from utils import client_id, client_secret, prev_week_saturday, prev_week_sunday
from games import games_id

api = TwitchAPI()
api.auth(client_id, client_secret)

class ClipContent:
    def __init__(self, url, broadcaster_id, broadcaster_name, game_id, creator_name, title, thumbnail_url, views, path):
        self.url = url
        self.broadcaster_id = broadcaster_id
        self.broadcaster_name = broadcaster_name
        self.game_id = game_id
        self.creator_name = creator_name
        self.title = title
        self.thumbnail_url = thumbnail_url
        self.views = views
        self.path = path
    
    def __str__(self):
        return f'url: {self.url}\nbroadcaster_id: {self.broadcaster_id}\nbroadcaster_name: {self.broadcaster_name}\ncreator_name: {self.creator_name}\ntitle: {self.title}\nthumbnail_url: {self.thumbnail_url}'

class ClipsExtractor:
    def __init__(self):
        self.clips_content = []

    def get_clips(self, quantity = 10, broadcaster_id = None, game_id = None, languages = []):
        params = {
            'broadcaster_id' : broadcaster_id,
            'game_id' : game_id,
            'first' : quantity,
            'started_at' : prev_week_sunday,
            'ended_at' : prev_week_saturday,
            'after' : None
        }

        while len(self.clips_content) < quantity:
            response = requests.get('https://api.twitch.tv/helix/clips', params=params, headers=api.headers).json()
            for clip in response['data']:
                if clip['language'] in languages:
                    print(clip['language'])
                    self.clips_content.append(ClipContent(
                        clip['url'],
                        clip['broadcaster_id'],
                        clip['broadcaster_name'],
                        clip['game_id'],
                        clip['creator_name'],
                        clip['title'],
                        clip['thumbnail_url'],
                        clip['view_count'],
                        f'files/clips/{clip["title"].replace(" ", "_").lower()}.mp4'
                    ))
            params['after'] = response['pagination']['cursor']

class ClipDownloader():
    def __init__(self):
        pass

    def download_clip(self, clip):
        index = clip.thumbnail_url.find('-preview')
        clip_url = clip.thumbnail_url[:index] + '.mp4'

        r = requests.get(clip_url)
        if r.headers['Content-Type'] == 'binary/octet-stream':
            if not os.path.exists('files/clips'): os.makedirs('files/clips')
            with open(clip.path, 'wb') as f:
                f.write(r.content)
        else:
            print(f'Failed to download clip from thumb: {clip.thumbnail_url}')
    
    def download_top_clips(self, quantity, broadcaster_id = None, game_id = None, languages = []):
        clips_extractor = ClipsExtractor()
        clips_extractor.get_clips(quantity, broadcaster_id, game_id, languages)
        for i in range(quantity):
            print(f'Downloading clip {i+1}/{quantity}')
            clip = clips_extractor.clips_content[i]
            self.download_clip(clip)