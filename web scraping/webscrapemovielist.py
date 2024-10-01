import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)

print(response.text)

movies = response.text
soup = BeautifulSoup(movies, "html.parser")
print(soup.title)
movie_tag= soup.find(name='h3', class_='title')
print(movie_tag)
movie_text = movie_tag.getText()
print(movie_text)

all_movie_tags= soup.find_all(name='h3', class_ ="title")
movie_text = []

all_movie_tags=[tag.getText() for tag in soup.find_all(name='h3', class_ ="title")]

all_movie_tags_reversed= all_movie_tags[::-1]
print(all_movie_tags_reversed)

with open('100BestMovies.txt', 'w', encoding='utf-8') as file:
    for i in all_movie_tags_reversed:
        file.write(f'{i}\n')




