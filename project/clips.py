import requests
import os
from twitch_api import TwitchAPI
from utils import client_id, client_secret, games_id, prev_week_saturday, prev_week_sunday

api = TwitchAPI()
api.auth(client_id, client_secret)

class ClipContent:
    def __init__(self, url, broadcaster_id, game_id, creator_name, title, thumbnail_url):
        self.url = url
        self.broadcaster_id = broadcaster_id
        self.game_id = game_id
        self.creator_name = creator_name
        self.title = title
        self.thumbnail_url = thumbnail_url
    
    def __str__(self):
        return f'url: {self.url}\nbroadcaster_id: {self.broadcaster_id}\ncreator_name: {self.creator_name}\ntitle: {self.title}\nthumbnail_url: {self.thumbnail_url}'

class ClipsExtractor:
    def __init__(self):
        self.clips_content = []

    def get_clips(self, quantity = 10, broadcaster_id = None, game_id = None, languages = []):
        params = {
            'broadcaster_id' : broadcaster_id,
            'game_id' : game_id,
            'first' : 100,
            'started_at' : prev_week_sunday,
            'ended_at' : prev_week_saturday
        }

        response = requests.get('https://api.twitch.tv/helix/clips', params=params, headers=api.headers)

        index = 0
        while len(self.clips_content) <= quantity or index < len(response.json()['data']):
            clip = response.json()['data'][index]
            if languages == [] or clip['language'] in languages:
                clip_content = ClipContent(url = clip['url'],
                                            broadcaster_id = clip['broadcaster_id'],
                                            game_id = clip['game_id'],
                                            creator_name = clip['creator_name'],
                                            title = clip['title'],
                                            thumbnail_url = clip['thumbnail_url'])
                self.clips_content.append(clip_content)
            index += 1

class ClipDownloader():
    def __init__(self):
        pass

    def download_clip(self, thumb_url, title):
        index = thumb_url.find('-preview')
        clip_url = thumb_url[:index] + '.mp4'

        r = requests.get(clip_url)
        if r.headers['Content-Type'] == 'binary/octet-stream':
            if not os.path.exists('clips'): os.makedirs('clips')
            with open(f'clips/{title}.mp4', 'wb') as f:
                f.write(r.content)
        else:
            print(f'Failed to download clip from thumb: {thumb_url}')
    
    def download_top_clips(self, quantity, broadcaster_id = None, game_id = None, languages = []):
        clips_extractor = ClipsExtractor()
        clips_extractor.get_clips(quantity, broadcaster_id, game_id, languages)
        for i in range(quantity):
            clip = clips_extractor.clips_content[i]
            self.download_clip(clip.thumbnail_url, clip.title.replace(' ', '_').lower())
