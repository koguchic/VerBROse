import sys
import spotipy
import spotipy.util as util
"""
These env. vars must be set to run the code

set SPOTIPY_CLIENT_ID='your-spotify-client-id'
set SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
set SPOTIPY_REDIRECT_URI='http://localhost/' 
"""

scope = 'user-top-read'
if len(sys.argv) > 2:
    username = sys.argv[1]
    song_count = sys.argv[2]
    try:
        count = int(song_count)
        if count < 1 or count > 10:
            print("please enter a value [1-10] for song_count.")
            sys.exit()
    except ValueError:
        print("Please enter an integer for song_count.")

else:
    print("Usage: %s username song_count[1-10] - Returns the [song_count] most popular songs for your top 5 artists" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope) #will redirect you to specified page in env variable, copy paste the redirected URL to proceed

if token:
    artist_count = 5
    sp = spotipy.Spotify(auth=token)
    top_tracks = sp.current_user_top_tracks(limit=artist_count + 15)['items']
    #i = 1
    #print("Top {} songs".format(song_count))
    artist_list = []
    artist_id_list = []
    for k,v in enumerate(top_tracks):
        if len(artist_id_list) < artist_count:
            track_name = v['name']
            artist_name = v['artists'][0]['name']
            artist_id = v['artists'][0]['id']
            if artist_name not in artist_list:
                artist_list.append(artist_name) #we only care about the main artist for now
                artist_id_list.append(artist_id)
        else:
            break
        #print("{}. Track: {} Artist: {}".format(k+1, track_name,", ".join(str(i) for i in artist_list)))

    print("\nPopular songs of favorite artists:\nSong Title : Score")
    for k,v in enumerate(artist_id_list):
        print("")
        top_tracks = sp.artist_top_tracks(v)['tracks']
        top_track_list = []
        popularity_list = []
        for track in top_tracks:
            if track['name'] not in top_track_list:
                if count > len(top_track_list):
                    top_track_list.append(track['name'])
                    popularity_list.append(track['popularity'])
                else:
                    break
        print("{}: {}\n{}".format(k+1, artist_list[k], "\n".join(str(i) + " : " + str(j) for i,j in zip(top_track_list, popularity_list))))