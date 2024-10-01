from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

print(response.text)

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)
article_tag= soup.find(name='span', class_='titleline')
print(article_tag)
article_text = article_tag.getText()
print(article_text)
article_link = article_tag.find(name="a")
print(article_link['href'])
article_upvote=soup.find(name='span', class_="score").getText()
print(article_upvote)


all_article_tags= soup.find_all(name='span', class_ ="titleline")
article_texts = []
article_links = []
for tag in all_article_tags:
    #print(tag.getText())
    text = tag.getText()
    article_texts.append(text)
    link = tag.find(name="a")
    #print(link['href'])
    article_links.append(link['href'])

#article_upvotes=soup.find_all(name='span', class_="score").getText()
#the above gets a list and I can't call .getText() on a list.
#work around and alternative to for loop, we use list comprehension
article_upvotes=[int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

#creating ordered lists
print(article_texts)
print(article_links)
print(article_upvotes)

#print(int(article_upvotes[0].split()[0]))

largest_number=max(article_upvotes)
print(largest_number)
index = article_upvotes.index(largest_number)
print(article_texts[2], article_links[2], article_upvotes[2])
print(article_texts[index], article_links[index], article_upvotes[index])