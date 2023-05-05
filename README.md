
### TELEGRAM BOT POSTS YOUTUBE VIDEOS

__Description:__  
This Telegram bot posts urls from a list to a Telegram channel. You can trigger the script manually, or with a cron job. 

Repo also includes two YouTube-related scripts; one for harvesting links of a particular channel [get_youtube_links_per_channel.py](https://github.com/whileseated/telegram-bot-posts-youtube-videos/blob/master/get_youtube_links_per_channel.py), the other is a test script [youtube_checker.py](https://github.com/whileseated/telegram-bot-posts-youtube-videos/blob/master/youtube_checker.py) that makes sure all your YouTube links are valid, public videos.

---

##### Step One:
Clone this repository. Create a `config.py` in the same directory with these three credentials:  

Get your bot's token from [@botfather](https://t.me/botfather)  
TOKEN = 'YOUR TOKEN HERE'

Get the channel or group id to which you'd like to add your bot. The ID is a long sequence of digits, sometimes negative. Try forwarding a message from your channel to [@JsonDumpBot](https://t.me/JsonDumpBot) to reveal the channel's ID.  
CHANNEL_NAME = 'YOUR CHANNEL ID HERE'

Optional, for your YouTube API key, if you need to create a list of links.  
DEVELOPER_KEY = 'YOUR KEY HERE'

---

##### Step Two:
After adding your bot to a channel/group, go into that channel/group and make sure the bot has fine-grained admin rights. You can access these from the channel itself, by clicking the bot's username in the list of administrators. I've seen errors when admin rights haven't been __fully__ granted.

If necessary, run the YouTube-related scripts, as explained above, or create, find or scrape a list of YouTube links, a la [videos_to_post.txt](https://github.com/whileseated/telegram-bot-posts-youtube-videos/blob/master/videos_to_post.txt). Links should be one link per line, as in the example.

---

##### Step Three:
Run the script: `python [bot.py](https://github.com/whileseated/telegram-bot-posts-youtube-videos/blob/master/bot.py)`  

Telegram expands YouTube links, creating a card for each video (see [example.jpg](https://github.com/whileseated/telegram-bot-posts-youtube-videos/blob/master/example.jpg)), including a play-in-Telegram preview, the video's title & description, and the original link, which, when clicked, launches the YouTube app (on iOS).
   
Optional: set-up a cron job to run `bot.py` on a schedule.  

---

#### Troubleshooting:
I've had some issues with two libraries for Telegram. There's `pip install telegram` and `pip install python-telegram-bot`. Went through a bunch of installs and de-installs and ultimately had the most success when deinstalling both, and then installing an earlier version of python-telegram-bot: `pip install python-telegram-bot==13.7`

