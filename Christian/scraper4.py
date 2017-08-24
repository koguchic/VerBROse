import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import deque

import sys



def BFS(artist_list, queue):
    """!!!: BUG Quits early without error message
       !!!: BUG Doesn't return completed artist list (stops at 21 artists)
                  Suspect memory problems
                  Maybe set max depth"""

    if queue: # is not empty
        artist = queue.popleft()
        artist_id = artist['id']
        print(artist['name'])

        # So we don't get trapped in an infinite loop, check if a node has been visited before
        if artist['name'] not in artist_list: # O(n)
            artist_list.append(artist['name']) # Append new node

            # Get related artists
            related_artists = sp.artist_related_artists(artist_id)['artists'] # Check neighbors

            # Adds related artists to queue
            for rel_artist in related_artists: # ignores already visited neighbors
                print('\t', rel_artist['name'])
                queue.append(rel_artist)

                # if rel_artist['name'] not in artist_list:
                #     queue.append(rel_artist)

            # Recursion Here!!!
            artist_list = BFS(artist_list, queue)

    return artist_list





client_credentials_manager = SpotifyClientCredentials('65caa2e15c2147d59ba48af9741319f3',
                                                      '50ac0c5f189d4ce1bd1b5f6b2f3330e3')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


name = 'The Killers'
results = sp.search(q='artist:' + name, type='artist')


start_query = results['artists']['items']

root = start_query[0]

# Usage: FIFO Queue - append right and pop left
queue = deque()
queue.append(root)

artist_list = []
artist_list = BFS(artist_list, queue)
print(artist_list)




