from slacker import Slacker
from extract_from_arxiv import *
import datetime
import os
from load_config import load_config
config = load_config()

day_before_3 = datetime.datetime.today() - datetime.timedelta(days=config['day_before'])
day_before_3_str = day_before_3.strftime('%Y%m%d')

channel = config['channel_cvpr']


def post_abst_on_slack():
    slack = Slacker(config['slack_token_kaggle'])
    texts = extract_abstract()

    if len(texts) == 0:
        slack.chat.post_message(channel, "No paper published on" + day_before_3_str)
    for text in texts:
        slack.chat.post_message(channel, text)


if __name__ == '__main__':
    post_abst_on_slack()
