import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebScrape.settings")
django.setup()
import bs4
import requests
import time
from Scrape_news.models import NewsBbc
import datefinder

# get urls of MostRead

name = "bbc"


def latest_business_news_bbc():
    urls = []
    url = 'https://www.bbc.com/news'
    resp = requests.get(url)
    sop = bs4.BeautifulSoup(resp.text, 'html.parser')
    for i in sop.find('div', class_='nw-c-most-read__items').find_all('a'):
        urls.append("http://www.bbc.com" + i.get('href'))
    return urls


def article_content__bbc(url):
    resp = requests.get(url)
    sop = bs4.BeautifulSoup(resp.text, 'html.parser')
    title = []
    content = []
    place = []
    country = ["africa", "europe", "australia", "asia" "latin america", "middle", "us&canada"]
    article_date_tem = sop.find('div', class_='date').text
    # convert date format into YYYY-MM-DD
    article_date = time.strftime('%Y-%m-%d', time.localtime(time.mktime(time.strptime(article_date_tem, '%d %B %Y'))))
    title.append(sop.find('h1').text)
    p = sop.find('div', property='articleBody')
    for i in p.find_all('p'):
        content.append(i)
    for ii in country:
        if ii in url:
            place = ii
    return title, place, article_date, content


def latest_business_news_reuters():
    titles = []
    urls = []
    description = []
    date = []
    url_header = "www.reuters.com"
    url = "https://www.reuters.com/news/archive/businessNews?view=page"
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    for i in soup.find_all('div', class_='story-content'):
            titles.append(i.h3.text)
            urls.append(url_header+ i.h3.parent.get('href'))
            description.append(i.p.text)
            date.append(i.time.text)
    return titles, urls, description, date


def article_content_reuters(url):
    contents = []
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    content = soup.find('div', class_='body_1gnLA')
    for i in content.find_all('p'):
        contents.append(i)
    return contents


def latest_business_news_ibt():
    titles = []
    urls = []
    description = []
    url_header = "www.ibtimes.com/"
    url = "http://www.ibtimes.com/business"
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    for i in soup.find_all('article', class_='clearfix'):
         titles.append(i.h3.text)
         urls.append(url_header+ i.h3.a.get('href'))
         description.append(i.find('div',class_='summary').text)
    return titles, urls, description


def article_content_ibt(url):
    contents = []
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    soup_1 = soup.find('div', class_='article-body')
    for content in soup_1.find_all('p'):
        contents.append(content)
    return contents


def save_article_content():
    link_bbc = latest_business_news_bbc()
    for i in link_bbc:
        title, place, article_date, content = article_content__bbc(i)
        NewsBbc.objects.get_or_create(name=name, title=title, place=place, date=article_date, content=content)
# get_or_create() can ensure data is unique