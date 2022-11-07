from twitch_ids_box_art import games_name
from PIL import Image, ImageDraw, ImageFont
from config import font_thumbnail
from math import floor, sqrt
from utils import prev_week_saturday_dBY, prev_week_sunday_dBY
import os

class VideoContent:

    def __init__(self, title, description, tags, category_id, privacy_status):
        self.title = title
        self.description = description
        self.tags = tags
        self.category_id = category_id
        self.privacy_status = privacy_status

class VideoContentGenerator:

    def __init__(self, clips_extractor):
        self.clips_extractor = clips_extractor

    def generate_title(self):
        if self.clips_extractor.by_game:
            return f'Top {len(self.clips_extractor.clips_content)} Most Watched {games_name[self.clips_extractor.clips_content[0].game_id]} Twitch Clips of The Week'
        return f'Top {len(self.clips_extractor.clips_content)} {self.clips_extractor.clips_content[0].broadcaster_id}\'s highlights of the week'

    def generate_description(self):
        description = f'Top {len(self.clips_extractor.clips_content)} most watched {games_name[self.clips_extractor.clips_content[0].game_id]} Twitch clips \
from {prev_week_sunday_dBY} to {prev_week_saturday_dBY}. \n \nLanguages: {self.clips_extractor.languages if self.clips_extractor.languages else "All"} \n \nClips:\n'
        
        timestamp = 0
        for clip in self.clips_extractor.clips_content:
            description += f'{int(timestamp) // 60}:{int(timestamp) % 60:02d} - {clip.title} ({clip.url})\n'
            timestamp += clip.duration

        description += '\nAll clips in this video were automatically selected based on their popularity. This video was generated and uploaded using a Python script. \
\nCheck out the source code here: https://github.com/viniciusenari/automated-twitch-clips-youtube-channel, leave a star if you liked it!'

        # remove greather than and less than symbols from description to avoid errors
        description = description.replace('<', '').replace('>', '')

        return description

    def generate_tags(self):
        tags = set(['twitch', 'clips', 'highlights', 'livestreaming', 'streaming', 'stream highlights', 'stream clips', 'streaming clips', 'streaming highlights', 'twitch clips', 'twitch highlights', 'twitch streaming', 'twitch stream highlights', 'twitch stream clips', 'twitch streaming clips', 'twitch streaming highlights'])
            
        for clip in self.clips_extractor.clips_content:
            tags.add(games_name[clip.game_id])
            tags.add(clip.broadcaster_name)
        return list(tags)
    
    def generate_thumbnail(self):
        overlay = Image.new('RGBA', (1280, 720), color = (255,255,255,0))
        d = ImageDraw.Draw(overlay)

        # Generate background with thumbnail images
        x = floor(sqrt(len(self.clips_extractor.clips_content)))
        for i in range(x):
            for j in range(x):
                img = Image.open(f'files/thumbnails/{self.clips_extractor.clips_content[i * x + j].title.replace(" ", "_").replace("/","_").lower()}.jpg')
                img = img.resize((1280 // x, 720 // x))
                overlay.paste(img, (i * (1280 // x), j * (720 // x)))

        # Generate text
        line1 = f'Top {len(self.clips_extractor.clips_content)}'
        line2 = f'{games_name[self.clips_extractor.clips_content[0].game_id]}'
        line3 = 'Twitch Clips'

        # rename games with long names to fit in the thumbnail
        rename = {
            'Counter-Strike: Global Offensive': 'CSGO',
            'League of Legends': 'LOL',
        }

        if line2 in rename: line2 = rename[line2]

        _, _, w, h = d.textbbox((0, 0), line1, font = ImageFont.truetype(font_thumbnail, 100))
        d.text(((1280 - w)/ 2, (720 - h) / 2 - 120), line1, font=ImageFont.truetype(font_thumbnail, 100), stroke_width=3, stroke_fill=(0, 0, 0), fill=(255, 255, 255))
        _, _, w, h = d.textbbox((0, 0), line2, font = ImageFont.truetype(font_thumbnail, 130))
        d.text(((1280 - w)/ 2, (720 - h) / 2), line2, font = ImageFont.truetype(font_thumbnail, 130), stroke_width=4, stroke_fill=(0, 0, 0), fill=(255, 255, 255))
        _, _, w, h = d.textbbox((0, 0), line3, font = ImageFont.truetype(font_thumbnail, 100))
        d.text(((1280 - w)/ 2, (720 - h) / 2 + 140), line3, font = ImageFont.truetype(font_thumbnail, 100), stroke_width=3, stroke_fill=(0, 0, 0), fill=(255, 255, 255))

        if not os.path.exists('files/youtube'): os.makedirs('files/youtube')
        overlay.save(f'files/youtube/thumbnail.png')