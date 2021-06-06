from slacker import Slacker
from extract_from_arxiv import *
import datetime
slack_token = "xoxb-1577884876279-2153634736353-Eeo8yNO1ArtPetdZYvkCFOFe"


day_before_3 = datetime.datetime.today() - datetime.timedelta(days=3)
day_before_3_str = day_before_3.strftime('%Y%m%d')

channel = "#cvpr_abstract"


def post_abst_on_slack():
    slack = Slacker(slack_token)
    texts = extract_abstract()

    if len(texts) == 0:
        slack.chat.post_message(channel, "No paper published on" + day_before_3_str)
    for text in texts:
        slack.chat.post_message(channel, text)


if __name__ == '__main__':
    post_abst_on_slack()
