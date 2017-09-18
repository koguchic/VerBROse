import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import deque
import pickle
import pandas as pd
import urllib
import os
import sys

def initialize_artist(artist_name):
    results = sp.search(q='artist:' + artist_name, type='artist')
    start_query = results['artists']['items']
    root = start_query[0]
    return root

def get_fields(artist):
    # Get relevant fields

    # Field 1 - artist name (string)
    artist_name = artist['name']

    # Field 2 - 1st genre in list of genres (string)
    genres = artist['genres']

    # Field 3 - a jpg image with
    curr_dir = os.getcwd()
    new_dir = 'data' # location where data will be stored

    if new_dir not in curr_dir:
        os.mkdir(new_dir)
        os.chdir(new_dir)
    try:

        url = artist['images'][0]['url']
        artist_name_url = '_'.join(artist_name.split(' ')) # artist name separated by underscore instead of spaces
        urllib.request.urlretrieve(url, artist_name_url + ".jpg")

    except:
        pass

    # Field 4 - popularity (int) 0-100
    popularity = artist['popularity']

    # Field 5 - number of followers (int)
    num_followers = artist['followers']['total']

    try:
        print([artist_name, genres[0], popularity, num_followers])
    except IndexError:
        genres = ['none']

    artist_dict[artist_name] = [genres, popularity, num_followers]

    return artist_dict

def BFS(artist_dict, queue, num_artists):


    if num_artists <= 0:
        return artist_dict


    if queue: # not empty  or len(artist_list) > 100
        artist = queue.popleft()

        # Get an artist not yet in the list by iterating through already visited nodes
        while(artist['name'] in artist_dict.keys()): # if artist is already seen
            artist = queue.popleft() # keep popping until a new one appears

        # Extract all fields from artist
        artist_dict = get_fields(artist)

        # Explore neighbors using artist ID
        artist_id = artist['id']
        related_artists = sp.artist_related_artists(artist_id)['artists']  # list of dicts

        # Append all related artists to queue for exploration
        for rel_artist in related_artists:

            if rel_artist['name'] not in artist_dict.keys():
                # print('\t', rel_artist['name'])
                queue.append(rel_artist)

        # Recursion Here!!!
        artist_list = BFS(artist_dict, queue, num_artists-1)

    return artist_dict



# Initialize Spotify Stuff
client_credentials_manager = SpotifyClientCredentials('65caa2e15c2147d59ba48af9741319f3',
                                                      '50ac0c5f189d4ce1bd1b5f6b2f3330e3')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# Create first node as "Saint Motel"
artist_name = 'Saint Motel'
root = initialize_artist(artist_name)

# Usage: FIFO Queue - append right and pop left
queue = deque()
queue.append(root) # root is a dictionary object

# Allow to larger maximum recursion depth
sys.setrecursionlimit(99999999)

artist_dict = {}
artist_dict = BFS(artist_dict, queue, num_artists=10000)

# pickle.dump(artist_dict, open( "artist_dict.pkl", "wb")) # Serialize
# artist_list = pickle.load(open('artist_dict.pkl', 'rb'))

# Unpack dictionary
artist_list = [[artist_name] + artist_dict[artist_name] for artist_name in artist_dict]

# Convert to DataFrame and Export
artist_df = pd.DataFrame(artist_list, columns=['Artist', 'Genres', 'Popularity', 'Followers'])
artist_df.to_csv('artists.csv')



