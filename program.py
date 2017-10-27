""" Scrape the EconTalk website for podcast transcripts."""


import requests

from time import sleep
from bs4 import BeautifulSoup


def main():
    tx_urls = get_urls()
    save_transcript_pages(tx_urls[:])
    print("Finished.")


def save_transcript_pages(tx_urls):
    """ Append each transcript to corpus. """
    for url in tx_urls:
        page = build_page_from_url(url)
        sleep(1)
        save_to_file(page)


def build_page_from_url(url):
    """ Scrape transcripts from EconTalk. """
    print("Downloading {}...".format(url), flush=True)
    resp = requests.get(url)
    html = resp.text
    soup = BeautifulSoup(html, 'lxml')
    transcript = soup.select("#unique")[0].get_text()

    return transcript


def get_urls():
    """ Get the urls from text file. """
    urls = []
    with open('data/urls.txt', 'r') as fin:
        for line in fin:
            urls.append(line.strip())

    return urls


def save_to_file(page):
    with open('data/corpus.txt', 'a') as fout:
        fout.write(page)


# def clean_line(text):
#     text = text.replace('\n', ' ').replace('\t', ' ')
#     size = len(text) + 1
#     while size > len(text):
#         size = len(text)
#         text = text.replace('  ', ' ')
#
#     return text.strip()


if __name__ == '__main__':
    main()
