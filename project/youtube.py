import os
import random
import time

import google_auth_oauthlib.flow
import googleapiclient.discovery
from googleapiclient.errors import HttpError

from googleapiclient.http import MediaFileUpload

scopes = ["https://www.googleapis.com/auth/youtube.upload"]


class VideoContent:

    def __init__(self, title, description, tags, privacy_status):
        self.title = None
        self.description = None
        self.tags = None
        self.category_id = None
        self.privacy_status = None

class YoutubeUploader:

    def __init__(self):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.client_secrets_file = "client_secret.json"

    def get_authenticated_service(self):
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(self.client_secrets_file, scopes)
        credentials = flow.run_console()
        self.youtube = googleapiclient.discovery.build(self.api_service_name, self.api_version, credentials=credentials)

    def upload_video(self, file_path, video_content):
        body = dict(
            snippet=dict(
                title=video_content.title,
                description=video_content.description,
                tags=video_content.tags,
                categoryId=video_content.category_id
            ),
            status=dict(
                privacyStatus=video_content.privacy_status
            )
        )

        insert_request = self.youtube.videos().insert(
            part=",".join(body.keys()),
            body=body,
            media_body= MediaFileUpload(
                file_path, chunksize=-1, resumable=True)
        )

        self.resumable_upload(insert_request)

    def resumable_upload(self, insert_request):
        response = None
        error = None
        retry = 0
        while response is None:
            try:
                print("Uploading file...")
                status, response = insert_request.next_chunk()
                if response is not None:
                    if 'id' in response:
                        print("Video id '%s' was successfully uploaded." % response['id'])
                    else:
                        exit("The upload failed with an unexpected response: %s" % response)
            except HttpError as e:
                if e.resp.status in self.__RETRIABLE_STATUS_CODES:
                    error = f"A retriable HTTP error {e.resp.status} occurred:\n{e.content}"
                else:
                    raise
            except self.__RETRIABLE_EXCEPTIONS as e:
                error = f"A retriable error occurred: {e}"

            if error is not None:
                print(error)
                retry += 1
                if retry > self.__MAX_RETRIES:
                    exit("No longer attempting to retry.")

                max_sleep = 2 ** retry
                sleep_seconds = random.random() * max_sleep
                print(f"Sleeping {sleep_seconds} seconds and then retrying...")
                time.sleep(sleep_seconds)

if __name__ == "__main__":
    video_content = VideoContent('test video', 'test description', ['test', 'video'], 'private')

    # upload videocsgo.mp4 to youtube
    uploader = YoutubeUploader()
    uploader.get_authenticated_service()
    uploader.upload_video("videocsgo.mp4", video_content)

