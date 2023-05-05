
### TELEGRAM BOT POSTS YOUTUBE VIDEOS

__Description:__  
This Telegram bot posts urls from a list to a Telegram channel. You can trigger the script manually, or with a cron job. 

Repo also includes two YouTube-related scripts; one for harvesting links of a particular channel [get_youtube_links_per_channel.py](https://github.com/whileseated/telegram-bot-posts-youtube-videos/blob/master/get_youtube_links_per_channel.py), the other is a test script [youtube_checker.py](https://github.com/whileseated/telegram-bot-posts-youtube-videos/blob/master/youtube_checker.py) that makes sure all your YouTube links are valid, public videos.

---

##### Step One:
Clone this repository. Create a config.py in the same directory with these three credentials:  

Get your bot's token from the telegram bot father @botfather  
TOKEN = 'YOUR TOKEN HERE'

Get the channel id that you'd like to add your bot to - a long sequence of digits, sometimes negative. Try forwarding a message from your channel to @JsonDumpBot to reveal its channel id  
CHANNEL_NAME = 'YOUR CHANNEL ID HERE'

Your YouTube API key (if necessary for creating a list of links)  
DEVELOPER_KEY = 'YOUR KEY HERE'

---

##### Step Two:
After adding your bot to a channel/group, go into that channel/group and make sure the bot has fine-grained admin rights. You can access these from the channel itself, by clicking the bot's username in the list of administrators. I've seen errors when admin rights haven't been __fully__ granted.

Run the YouTube-related scripts, as explained above, if necessary, or create, find or scrape a list of YouTube links, a la [videos_to_post.txt](https://github.com/whileseated/telegram-bot-posts-youtube-videos/blob/master/). Links should be one-per line, as in the example.

---

##### Step Three:
Run the script: 'python [bot.py](https://github.com/whileseated/telegram-bot-posts-youtube-videos/blob/master/bot.py)'

---

##### Optional:
Set-up a cron job to run [bot.py](https://github.com/whileseated/telegram-bot-posts-youtube-videos/blob/master/bot.py) on a schedule. 