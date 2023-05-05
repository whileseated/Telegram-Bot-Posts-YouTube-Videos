
TELEGRAM BOT THAT POSTS YOUTUBE VIDEOS

Description:
This Telegram bot posts links from a list (youtube links, in this case) to a Telegram channel. You can trigger the script manually, or with a cron job. 

Repo also includes two YouTube-related scripts; one for harvesting links of a particular channel, the other is a test script that makes sure all your YouTube links are valid, public videos.

---

Step One:
Create a config.py with these credentials:

# Get your bot's token from the telegram bot father @botfather
TOKEN = 'YOUR TOKEN HERE'

# Get the channel name/id that you'd like to add your bot to - a long sequence of digits, sometimes negative. Try forwarding a message from your channel to @JsonDumpBot to reveal its ID
CHANNEL_NAME = 'YOUR CHANNEL ID HERE'

# Your YouTube API key
DEVELOPER_KEY = 'YOUR KEY HERE'

---

Step Two:
Run the YouTube-related scripts, as explained above, if necessary.

Create, find or scrape a list of YouTube links, a la "videos_to_post.txt"

---

Step Three:
