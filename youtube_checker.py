import googleapiclient.discovery
import googleapiclient.errors
from config import DEVELOPER_KEY

# Set up the YouTube Data API client with your API key
api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

# Read the list of video URLs from a text file
with open('videos_to_post.txt') as f:
    urls = f.read().splitlines()

# Check each video for availability
for url in urls:
    video_id = url.split('=')[-1]  # extract the video ID from the URL
    try:
        # Call the YouTube Data API to get information about the video
        request = youtube.videos().list(
            part="status",
            id=video_id
        )
        response = request.execute()
        items = response.get('items', [])
        if items and items[0].get('status', {}).get('uploadStatus') in ['deleted', 'failed']:
            print(f"Video {video_id} is not available.")
        else:
            print(f"Video {video_id} is available.")
    except googleapiclient.errors.HttpError as e:
        print(f"Error checking video {video_id}: {e}")

