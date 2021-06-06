# coding: utf-8
from translate_by_deepl import *
import arxiv
from load_config import load_config
import datetime


def extract_abstract(config):
    day_before_3 = datetime.datetime.today() - datetime.timedelta(days=config['day_before'])
    day_before_3_str = day_before_3.strftime('%Y%m%d')
    search = arxiv.Search(
        query=config['query'],
        max_results=config['max_results'],
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    texts = []

    for result in search.get():
        title = result.title
        abstract = translate_by_deepl(result.summary.replace('\n', ' '))
        url = result.pdf_url
        date = result.published.strftime('%Y%m%d')
        text = "Title: {} \nURL: {} \nPublished: {}\n```{}```".format(title, url, date, abstract)
        # print(abstract)
        if date == day_before_3_str:
            texts.append(text)
        else:
            break
    return texts


if __name__ == '__main__':
    config_file = 'config_test.yml'
    _config = load_config(config_file)
    extract_abstract(_config)





