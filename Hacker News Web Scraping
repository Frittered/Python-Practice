#This file scrapes the from bs4 import BeautifulSoup
import requests
import json
def hacker_n_scrape(website):
    print('The Hottest Stories from Hacker News')
    news_list=[]
    for i in range(1,4):
        web = website
        if i > 1:
            add = f'news?p={i}'
            web = web + add
        with requests.get(web) as hacker_news:
            html = hacker_news.text
            #print(html)
            soup = BeautifulSoup(hacker_news.text, 'html.parser')
            scores = soup.find_all('span', class_= 'score')
            titles = soup.find_all('a', class_='storylink')
            links = soup.select('a.storylink[href]')

            for index,(title,score) in enumerate(zip(titles,scores)):
                raw_score = score.get_text().replace('points','')
                if int(raw_score)>100:
                    link = title.get('href')
                    news_list.append({'title':title.get_text(), 'score':int(raw_score), 'link':link})
            final_sorted_list = sorted(news_list, key= lambda key:key['score'], reverse=True)
    return print(json.dumps(final_sorted_list, indent= 2, sort_keys=False))

hacker_n_scrape('https://news.ycombinator.com//')
