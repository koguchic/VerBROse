import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys

client_credentials_manager = SpotifyClientCredentials('65caa2e15c2147d59ba48af9741319f3',
                                                      '50ac0c5f189d4ce1bd1b5f6b2f3330e3')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


name = 'The Killers'

results = sp.search(q='artist:' + name, type='artist')
LINEBREAK = '\n' + '%' * 80 + '\n'


artists = results['artists']['items']
for artist in artists:

    print(LINEBREAK) # linebreak
    print(artist['name']) # queries artist name

    attributes = sorted(artist.keys())
    for attrib in attributes:
        print('\t~ ', attrib, '\n\t\t', artist[attrib]) # print key and values for each artist

"""

Dictionary Keys and Expected Values
    genres
        list of str
    uri
        str 'spotify:artist:artist ID'
    name
        str
    images
        link to a picture of the band
    popularity
        int
    id
        str artist ID 
    followers
        int

"""


















