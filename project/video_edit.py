import os
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip
from PIL import Image, ImageDraw, ImageFont
from clips import ClipsExtractor
from games import games_id

clips_extractor = ClipsExtractor()
clips_extractor.get_clips(quantity = 10, game_id = games_id['VALORANT'], languages = ['en', 'en-gb'])
 
class VideoEditor():
    def __init__(self):
        pass

    def create_intro(self):
        pass

    def create_overlay(self, clip_content):
        title = clip_content.title
        broadcaster_name = clip_content.broadcaster_name
        if len(title) > 45: title = title[:45] + '...'

        # Create a 1980x1080 transparent image
        overlay = Image.new('RGBA', (1920, 1080), color = (255,255,255,0))
 
        fnt_clip_name = ImageFont.truetype("usr/share/fonts/truetype/noto/DejaVuSans-Bold.ttf", 62)
        fnt_streamer_name = ImageFont.truetype("usr/share/fonts/truetype/noto/NotoMono-Regular.ttf", 50)
        d = ImageDraw.Draw(overlay)

        d.text((100, 930), title, font=fnt_clip_name, stroke_width=3, stroke_fill=(0, 0, 0), fill=(255, 255, 255))
        d.text((100, 1000), broadcaster_name, font=fnt_streamer_name, stroke_width=3, stroke_fill=(0, 0, 0), fill=(255, 255, 255))
        
        if not os.path.exists('files/overlays'): os.makedirs('files/overlays')
        overlay.save('files/overlays/my_picture.png')
    
    def create_video(self):
        clip = VideoFileClip("files/clips/hasan_tries_to_communicate_with_his_team.mp4")
        img_clip = ImageClip("files/overlays/my_picture.png").set_duration(5)

        # Overlay the text clip on the first video clip
        video = CompositeVideoClip([clip, img_clip])

        video.write_videofile(f'video.mp4', fps = 60, codec = "mpeg4", threads = 1, preset = "ultrafast", bitrate = "16000k")

video_editor = VideoEditor()
video_editor.create_overlay(clips_extractor.clips_content[0])
video_editor.create_video()
