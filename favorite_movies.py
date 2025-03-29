import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
a_tags = soup.select(selector="ul li a")
movies = []
for tag in a_tags:
    if tag.get("data-test") is not None:
        movies.append(tag.getText())
movies.reverse()
print(movies)
print(len(movies))

with open("movies.txt", mode="w") as movies_file:
    movie_num = 1
    for movie in movies:
        movies_file.write(f"{movie_num}. {movie} \n")
        movie_num += 1