import os
import googleapiclient.discovery
import googleapiclient.errors
from config import DEVELOPER_KEY

# Set up the YouTube Data API client with your API key
api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

# Define the ID of the channel you want to retrieve videos from
channel_id = "ADD_YOUR_YOUTUBE_CHANNEL_ID_HERE"

# Call the API to retrieve the list of videos uploaded by the channel
next_page_token = None
videos = []
while True:
    request = youtube.search().list(
        part="id",
        channelId=channel_id,
        type="video",
        videoDefinition="high",
        maxResults=50,
        pageToken=next_page_token
    )
    response = request.execute()

    # Append the video IDs to the list
    for item in response["items"]:
        videos.append(item["id"]["videoId"])

    # Check if there are more pages of results
    if "nextPageToken" in response:
        next_page_token = response["nextPageToken"]
    else:
        break

# Print the list of video IDs
print(videos)
