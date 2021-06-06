from translate_by_deepl import *
import pprint
import arxiv
import pandas as pd

from load_config import load_config
config = load_config()


import datetime
day_before_3 = datetime.datetime.today() - datetime.timedelta(days=config['day_before'])
day_before_3_str = day_before_3.strftime('%Y%m%d')


def extract_abstract():
    search = arxiv.Search(
        query=config['query_cvpr'],
        max_results=config['max_resluts'],
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    texts = []

    for result in search.get():
        title = result.title
        abstract = translate_by_deepl(result.summary)
        url = result.pdf_url
        date = result.published.strftime('%Y%m%d')
        text = "TITLE :\n{} \nURL\n{} \nDATE :\n{}\nABSTRACT:{}\n".format(title, url, date, abstract)
        print(text)
        if date == day_before_3_str:
            texts.append(text)
        else:
            break
    return texts


if __name__ == '__main__':
    extract_abstract()





