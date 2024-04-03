import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to ? Type the date in this format YYYY-MM-DD :")
year = date.split("-")[0]

response = requests.get(url="https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, "html.parser")

song_names_spans = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)

Client_ID = ""
Client_Secret = ""

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=Client_ID,
        client_secret=Client_Secret,
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        cache_path="token.txt",
        show_dialog=True
    )
)

user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exits in Spotify.Skipped.")

print(song_uris)
print(len(song_uris))

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print("\n")

# song_names_spans = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
#
# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])
#
# for song in song_names_spans:
#     print(song.getText().strip())))
