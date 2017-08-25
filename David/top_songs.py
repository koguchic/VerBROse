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
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope) #will redirect you to specified page in env variable, copy paste the redirected URL to proceed

if token:
	song_count = 20 #change to get top X songs
	sp = spotipy.Spotify(auth=token)
	top_tracks = sp.current_user_top_tracks(limit=song_count)['items']
	#i = 1
	print("Top {} songs".format(song_count))

	for k,v in enumerate(top_tracks):
		track_name = v['name']
		artist_list = []
		for artist in v['artists']:
			artist_list.append(artist['name'])

		print("{}. Track: {} Artist: {}".format(k+1, track_name,", ".join(str(i) for i in artist_list)))
