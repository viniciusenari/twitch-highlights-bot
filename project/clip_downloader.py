import requests
import os

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