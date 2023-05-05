import os
import argparse
from telegram import Bot
from config import TOKEN, CHANNEL_NAME
import logging

def post_link(bot: Bot) -> None:
    logging.debug('post_link function called')
    with open('videos_to_post.txt', 'r+') as f:
        links = f.readlines()
        if links:
            link_to_post = links.pop(0)
            bot.send_message(chat_id=CHANNEL_NAME, text=link_to_post)
            f.seek(0)
            f.writelines(links)
            f.truncate()

            with open('videos_posted.txt', 'a+') as f:
                f.write(link_to_post)

def main() -> None:
    print(f"TOKEN: {TOKEN}")
    print(f"CHANNEL_NAME: {CHANNEL_NAME}")

    bot = Bot(TOKEN)

    post_link(bot)

if __name__ == '__main__':
    main()
