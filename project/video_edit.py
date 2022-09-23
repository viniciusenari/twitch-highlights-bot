import os
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip, concatenate_videoclips
from PIL import Image, ImageDraw, ImageFont
from clips import ClipsExtractor
from games import games_id
from config import font_clip_name, font_broadcaster

class VideoEditor():
    def __init__(self):
        self.clips = []

    def create_intro(self):
        pass

    def create_overlay(self, clip_content):
        title = clip_content.title
        broadcaster_name = clip_content.broadcaster_name
        if len(title) > 45: title = title[:45] + '...'

        # Create a 1980x1080 transparent image
        overlay = Image.new('RGBA', (1920, 1080), color = (255,255,255,0))
 
        fnt_clip_name = ImageFont.truetype(font_clip_name, 62)
        fnt_streamer_name = ImageFont.truetype(font_broadcaster, 50)
        d = ImageDraw.Draw(overlay)

        d.text((100, 930), title, font=fnt_clip_name, stroke_width=3, stroke_fill=(0, 0, 0), fill=(255, 255, 255))
        d.text((100, 1000), broadcaster_name, font=fnt_streamer_name, stroke_width=3, stroke_fill=(0, 0, 0), fill=(255, 255, 255))
        
        if not os.path.exists('files/overlays'): os.makedirs('files/overlays')
        overlay.save(f'files/overlays/{clip_content.title}.png')
    
    def create_video(self, clip_content):
        clip = VideoFileClip(clip_content.path)
        img_clip = ImageClip(f'files/overlays/{clip_content.title}.png').set_duration(5)
        video = CompositeVideoClip([clip, img_clip])
        return video

    def create_video_compilation(self, clips, amount):
        for clip in clips[:amount]:
            self.create_overlay(clip)
            self.clips.append(self.create_video(clip))
            
        video = concatenate_videoclips(self.clips, method='compose')
        video.write_videofile(f'videocsgo.mp4', fps = 60, codec = "mpeg4", threads = 8, preset = "ultrafast", logger = 'bar', bitrate = '20000k')