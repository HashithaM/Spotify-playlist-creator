# Spotify-playlist-creator
This code creates a spotify playlist with most popular songs in the given date
This Python script fetches the Billboard Hot 100 songs for a specific date provided by the user, searches for these songs on Spotify, and creates a private playlist containing those songs if they are found on Spotify.

Here's a breakdown of what the code does:

Imports necessary libraries:

requests for making HTTP requests.
BeautifulSoup from bs4 for parsing HTML.
spotipy for interacting with the Spotify Web API.
SpotifyOAuth for handling Spotify authentication.
Prompts the user to input a date in the format YYYY-MM-DD.

Extracts the year from the input date.

Fetches the Billboard Hot 100 songs for the specified date using BeautifulSoup to parse the HTML response from the Billboard website.

Extracts the names of the songs from the parsed HTML.

Initializes Spotify API authentication using spotipy.Spotify() with OAuth authentication, providing the client ID, client secret, redirect URI, requested scope, cache path, and dialog display preferences.

Retrieves the user's Spotify ID.

Searches for each song on Spotify using the Spotify API's search functionality, appending the URI (Uniform Resource Identifier) of each found track to a list (song_uris). If a song is not found, it prints a message indicating that the song was skipped.

Creates a new private playlist on the user's Spotify account named after the specified date, and adds the found songs to the playlist using sp.user_playlist_create() and sp.playlist_add_items().

Prints the URIs of the found songs and the total number of found songs.

Finally, it comments out some code that is either commented out for testing purposes or not used in the current context.

The script essentially automates the process of creating a Spotify playlist based on the Billboard Hot 100 songs for a specific date provided by the user.






