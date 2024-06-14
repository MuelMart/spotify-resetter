import argparse

import spotipy
from spotipy.oauth2 import SpotifyOAuth

if __name__ == '__main__':
    msg = "This program will remove all songs from a playlist"
    parser = argparse.ArgumentParser(msg)
    parser.add_argument("-cid","--client_id")
    parser.add_argument("-cs","--client_secret")
    parser.add_argument("-ruri","--redirect_uri")
    parser.add_argument("-pid","--playlist_id")
    parser.add_argument("-rt","--refresh_token")

    args = parser.parse_args()

    #Authenticate
    auth = SpotifyOAuth(client_id=args.client_id,
                        client_secret=args.client_secret,
                        redirect_uri=args.redirect_uri,
                        scope='playlist-modify-public')
    
    auth.refresh_access_token(args.refresh_token)
    sp = spotipy.Spotify(auth_manager=auth)

    #Get all songs in playlist
    items = sp.playlist_items(args.playlist_id)['items']
    ids = [a['track']['id'] for a in items]

    #Delete occurences of items
    sp.playlist_remove_all_occurrences_of_items(args.playlist_id,items=ids)