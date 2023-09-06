import requests
from bs4 import BeautifulSoup

def get_news(keyword):
  headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
  data = requests.get(f'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={keyword}',headers=headers)

  soup = BeautifulSoup(data.text, 'html.parser')

  lis = soup.select('#main_pack > section > div > div.group_news > ul > li')

  for li in lis:
    a = li.select_one('a.news_tit')

get_news('한국전자인증')
