import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
response.raise_for_status()
print(response.encoding)
data = response.text

soup = BeautifulSoup(data, "html.parser")

movie_titles = [h3.getText() for h3 in soup.select(selector=".listicleItem_listicle-item__title__hW_Kn")]
# print(movie_titles)

movie_titles_inverted = movie_titles[::-1]
# movie_titles_inverted = movie_titles.reverse()
# print(movie_titles_inverted)

with open("movies.txt", mode="w", encoding="utf-8") as f:
    for item in movie_titles_inverted:
        f.write(f"{item}\n")
