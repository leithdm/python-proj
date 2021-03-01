from bs4 import BeautifulSoup
import requests
# import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# get hold of single tags

# print(soup.title.string)
# print(soup.li)
# print(soup.p)

# get hold of multiple tags
# 1
all_anchor_tags = soup.find_all(name='a')
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.get('href'))

# 2
all_paragraph_tags = soup.find_all(name='p')
for paragraph in all_paragraph_tags:
    print(paragraph.getText())

# 3 - specific queries, with multiple parameters
heading = soup.find(name='h1', id='name')
# note the use of class_ if you want to find a 'class'
heading = soup.find(name='h3', class_='heading')
print(heading)

# 4 - drilling down using multiple selectors
company_url = soup.select_one(selector='p a')

name = soup.select_one(selector='#name')

headings = soup.select('.heading')

print(company_url)

# 5 - Scrape Hacker News to get the most upvoted story

response = requests.get(url="https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

# get a single article
# article_tag = soup.find(name='a', class_='storylink')
# text = article_tag.getText()
# print(text)
# article_link = article_tag.get('href')
# print(article_link)
# article_upvote = soup.find(name='span', class_='score').getText()
# print(article_upvote)

# get multiple articles

articles = soup.find_all(name='a', class_='storylink')
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

highest_vote = 0
highest_vote_index = 0
for index, vote in enumerate(article_upvote):
    if vote > highest_vote:
        highest_vote = vote
        highest_vote_index = index

# alternative way of doing above
highest_vote = max(article_upvote)
largest_index = article_upvote.index(highest_vote)
highest_vote_article = article_texts[largest_index]
highest_vote_link = article_links[largest_index]

print(highest_vote)
print(highest_vote_article)
print(highest_vote_link)