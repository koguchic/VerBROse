import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials('65caa2e15c2147d59ba48af9741319f3',
                                                      '50ac0c5f189d4ce1bd1b5f6b2f3330e3')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None


# export SPOTIPY_CLIENT_ID='65caa2e15c2147d59ba48af9741319f3'
# export SPOTIPY_CLIENT_SECRET='50ac0c5f189d4ce1bd1b5f6b2f3330e3'
# export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

"""
Client ID
65caa2e15c2147d59ba48af9741319f3
Client Secret
50ac0c5f189d4ce1bd1b5f6b2f3330e3
"""
