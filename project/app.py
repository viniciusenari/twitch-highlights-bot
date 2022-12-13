from project.clips import ClipsExtractor, ClipsDownloader
from project.video_edit import VideoEditor
from project.video_content import VideoContentGenerator, VideoContent
from project.youtube import YoutubeUploader
from project.twitch_ids_box_art import games_id


class App:
    def __init__(self):
        self.clips_extractor = ClipsExtractor()
        self.clips_downloader = ClipsDownloader()
        self.video_editor = VideoEditor()
        self.youtube_uploader = YoutubeUploader()

    def run(self, game, amount, languages = []):
        print(f"Creating video compilation with game: {game}, amount: {amount}, languages: {languages}")
        game_id = games_id[game]

        # Get clips from Twitch
        self.clips_extractor.get_clips(quantity = amount, game_id = game_id, languages=languages)
        clips = self.clips_extractor.clips_content
            

        # Download clips
        self.clips_downloader.download_top_clips(clips)

        # Create video compilation
        self.video_editor.create_video_compilation(clips, amount)

        # Upload video to Youtube
        self.video_content_generator = VideoContentGenerator(self.clips_extractor)

        # Create video content
        video_content = VideoContent(
            title = self.video_content_generator.generate_title(),
            description = self.video_content_generator.generate_description(),
            tags = self.video_content_generator.generate_tags(),
            category_id = '20', # Gaming
            privacy_status= 'public'
        )

        # Create thumbnail
        self.video_content_generator.generate_thumbnail()

        # Upload video to Youtube
        self.youtube_uploader.get_authenticated_service()
        self.youtube_uploader.upload_video('files/youtube/video.mp4', video_content)