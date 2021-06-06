# coding: utf-8
from slacker import Slacker
from extract_from_arxiv import *
import datetime
from load_config import load_config
import sys
print(sys.getdefaultencoding())


def post_abst_on_slack(config):
    day_before_3 = datetime.datetime.today() - datetime.timedelta(days=config['day_before'])
    day_before_3_str = day_before_3.strftime('%Y%m%d')
    slack = Slacker(config['slack_token'])
    texts = extract_abstract(config)

    if len(texts) == 0:
        slack.chat.post_message(config['channel'], "No paper published on" + day_before_3_str)
    for text in texts:
        slack.chat.post_message(config['channel'], text)


if __name__ == '__main__':
    arg = sys.argv
    if len(arg) != 2:
        print("configファイルを指定してください")
        exit()
    _config = load_config(arg[1])
    post_abst_on_slack(_config)
