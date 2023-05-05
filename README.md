
# TELEGRAM BOT THAT POSTS YOUTUBE VIDEOS

__Description:__  
This Telegram bot posts links from a list to a Telegram channel. You can trigger the script manually, or with a cron job. 

Repo also includes two YouTube-related scripts; one for harvesting links of a particular channel "get_youtube_links_per_channel.py", the other is a test script "youtube_checker.py" that makes sure all your YouTube links are valid, public videos.

---

##### Step One:
Create a config.py with these credentials:

Get your bot's token from the telegram bot father @botfather
TOKEN = 'YOUR TOKEN HERE'

Get the channel id that you'd like to add your bot to - a long sequence of digits, sometimes negative. Try forwarding a message from your channel to @JsonDumpBot to reveal its channel id
CHANNEL_NAME = 'YOUR CHANNEL ID HERE'

Your YouTube API key
DEVELOPER_KEY = 'YOUR KEY HERE'

---

##### Step Two:
Run the YouTube-related scripts, as explained above, if necessary.

Create, find or scrape a list of YouTube links, a la "videos_to_post.txt". Links should be one-per line, as in the example.

---

##### Step Three:
Run the script: 'python bot.py'

---

##### Optional:
Set-up a cron job to run bot.py on a schedule. 