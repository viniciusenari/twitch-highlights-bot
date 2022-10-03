from twitch_ids_box_art import games_name

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
            return f'Top {len(self.clips_extractor.clips_content)} most watched {games_name[self.clips_extractor.clips_content[0].game_id]} Twitch clips this week'
        return f'Top {len(self.clips_extractor.clips_content)} {self.clips_extractor.clips_content[0].broadcaster_id} highlights of the week'

    def generate_description(self):
        description = ''
        
        timestamp = 0
        for clip in self.clips_extractor.clips_content:
            description += f'{timestamp} - {clip.title}({clip.url})\n'
            timestamp += clip.duration

        return description

    def generate_tags(self):
        tags = ['twitch', 'clips', 'highlights', 'livestreaming', 'streaming', 'stream highlights', 'stream clips', 'streaming clips', 'streaming highlights', 'twitch clips', 'twitch highlights', 'twitch streaming', 'twitch stream highlights', 'twitch stream clips', 'twitch streaming clips', 'twitch streaming highlights']
        if self.clips_extractor.by_game:
            tags.append(self.clips_extractor.clips_content[0].broadcaster_name)
        else:
            tags.append(games_name[self.clips_extractor.clips_content[0].game_id])
            
        for clip in self.clips_extractor.clips_content:
            if self.clips_extractor.by_game:
                tags.append(clip.broadcaster_name)
            else:
                tags.append(games_name[clip.game_id])
        return tags