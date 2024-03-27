from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import requests
import urllib.parse
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "https://example.com/"

date = input("Which year do you want to travel to?: Type the date in this format YYYY-MM-DD: ")
# date = "1989-03-22"

# -------------------------------- SCRAPPING BILLBOARD HOT 100 USING DATE -------------------------------- #

url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")

songs_list = []
list_row = soup.find_all(name="ul", class_="o-chart-results-list-row")
for element in list_row:
    title = element.find(name="h3", class_="c-title")
    artist = title.next_sibling.next_sibling
    if title is not None and artist is not None:
        song_obj = {
            "title": title.text.strip().strip('\n'),
            "artist": artist.text.strip().strip('\n')
        }
        songs_list.append(song_obj)

# print(songs_list)

# -------------------------------- SPOTIPY API AUTHENTICATION -------------------------------- #

# scope = "user-library-read"
scope = "playlist-modify-private playlist-read-private user-read-recently-played"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI, scope=scope, show_dialog=True,
                                               cache_path="token.txt",))

# -------------------------------- SPOTIPY API PLAYLIST CREATION -------------------------------- #

# user_id = "pipipo89"
# user_id = sp.user()
user_id = sp.me()['id']

playlist_name = f"{date} Billboard Hot 100"
playlist_description = f"The Billboard Hot 100 songs that were playing on this date {date}."
create_list_result = sp.user_playlist_create(user=user_id, name=playlist_name, public=False,
                                             description=playlist_description)
playlist_id = create_list_result['id']  # id of the created playlist

tracks_list = []
for item in songs_list:
    search_query = f"track:{item['title']} artist:{item['artist']}"
    ascii_query = urllib.parse.quote(search_query)
    track = sp.search(q=ascii_query, limit=1, type="track", market="CL")
    try:
        track_uri = track["tracks"]["items"][0]["uri"]
        tracks_list.append(track_uri)
    except IndexError:
        print(f"{item['title']} doesn't exist in Spotify. Skipped.")

# print(tracks_list)
add_track_results = sp.playlist_add_items(playlist_id=playlist_id, items=tracks_list)

# some additional useful methods
user_playlists = sp.current_user_playlists()
user_recently_played_songs = sp.current_user_recently_played()