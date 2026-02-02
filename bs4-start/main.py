from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
response_html = response.text

soup = BeautifulSoup(response_html, 'html.parser')

titles = soup.select('.athing')

scores = soup.select('.score')

score_max = 0
id_score_max = 0
for score in scores:
    current_score = int(score.text.split(' ')[0])
    if current_score > score_max:
        score_max = current_score
        id_score_max = score.get("id")

print(score_max)
print(id_score_max)

score_max_id_number = id_score_max.split('_')[1]
print(score_max_id_number)

max_title = soup.find('tr', id=score_max_id_number)
title = max_title.text

print(title)