from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
data = response.text

soup = BeautifulSoup(data, "html.parser")
# print(soap.prettify())

# in the webpage there are span elements with the class 'titleline' that contain article titles and links
articles_text = [span.find("a").getText() for span in soup.select(selector=".titleline")]
articles_links = [span.find("a").get("href") for span in soup.select(selector=".titleline")]

# there are also span elements with the class 'subtext' and inside them other spans with the class 'score' showing the
# number of upvotes the article has, but there may be articles without upvotes at the moment. For that reason we must
# check if this value is present or append a value of 0 so to make the number of articles scores equal to the number of
# articles. If an article does indeed contain a score element, we strip the first segment of the string to get ahold of
# only the number and get rid of the 'points' word that it is next to it
articles_subtexts = soup.select(selector=".subtext")
article_points = []
for element in articles_subtexts:
    score = element.find(name="span", class_="score")
    if score is None:
        article_points.append(0)
    else:
        article_points.append(int(score.string.split(" ")[0]))

# debug only
# print(len(articles_text))
# print(len(articles_links))
# print(len(article_points))

# we get ahold of the max value (and its position) in the article_points list
max_points = max(article_points)
max_points_index = article_points.index(max_points)

# using the max_points_index we get the corresponding article title and link
max_points_article_text = articles_text[max_points_index]
max_points_article_link = articles_links[max_points_index]

print(f"The article with more point is '{max_points_article_text}' (link {max_points_article_link}) with a total of "
      f"{max_points} points.")
