import os
import google.auth
import google.auth.transport.requests
import google.oauth2.credentials
import googleapiclient.discovery
import googleapiclient.errors

# Define the credentials file
CLIENT_SECRETS_FILE = 'client_secrets.json'

# Define the video file
VIDEO_FILE = 'video.mp4'

# Define the metadata for the video
video_title = 'My Video Title'
video_description = 'This is a description of my video'
video_tags = ['tag1', 'tag2', 'tag3']
video_category_id = '22'  # See https://developers.google.com/youtube/v3/docs/videoCategories/list for a list of category IDs

# Authenticate with the YouTube API using the client secrets file
scopes = ['https://www.googleapis.com/auth/youtube.upload']

flow = google.auth.flow.InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes)
creds = flow.run_local_server(port=0)

# Create a YouTube API client
youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=creds)

# Upload the video file
request_body = {
    'snippet': {
        'title': video_title,
        'description': video_description,
        'tags': video_tags,
        'categoryId': video_category_id
    },
    'status': {
        'privacyStatus': 'public'
    }
}
media_file = googleapiclient.http.MediaFileUpload(VIDEO_FILE)
response = youtube.videos().insert(part='snippet,status', body=request_body, media_body=media_file).execute()

# Print the video ID
print(f'Video uploaded successfully! Video ID: {response["id"]}')
