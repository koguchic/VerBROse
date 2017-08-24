import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials('65caa2e15c2147d59ba48af9741319f3',
                                                      '50ac0c5f189d4ce1bd1b5f6b2f3330e3')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

results = sp.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])


# export SPOTIPY_CLIENT_ID='65caa2e15c2147d59ba48af9741319f3'
# export SPOTIPY_CLIENT_SECRET='50ac0c5f189d4ce1bd1b5f6b2f3330e3'
# export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

"""
Client ID
65caa2e15c2147d59ba48af9741319f3
Client Secret
50ac0c5f189d4ce1bd1b5f6b2f3330e3
"""
