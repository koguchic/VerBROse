import sys
import spotipy
import spotipy.util as util
import os
"""
These env. vars must be set to run the code

set SPOTIPY_CLIENT_ID='your-spotify-client-id'
set SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
set SPOTIPY_REDIRECT_URI='http://localhost/'
"""

scope = 'user-top-read'
# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print("Usage: %s username" % (sys.argv[0],))
#     sys.exit()


username = 'koguchic'

os.environ['SPOTIPY_CLIENT_ID'] = '65caa2e15c2147d59ba48af9741319f3'
os.environ['SPOTIPY_CLIENT_SECRET'] = '50ac0c5f189d4ce1bd1b5f6b2f3330e3'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost/'


# token = util.prompt_for_user_token(username, scope) #will redirect you to specified page in env variable, copy paste the redirected URL to proceed
token = util.prompt_for_user_token(username, scope, client_id='65caa2e15c2147d59ba48af9741319f3',
								   client_secret='50ac0c5f189d4ce1bd1b5f6b2f3330e3',
								   redirect_uri='http://localhost/')




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
