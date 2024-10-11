import os
import json
#from dotenv import load_dotenv

def add_tracks_to_playlist(sp):
        # read all spotify track uris from track_uris/track_uris.txt
        track_uris = []
        with open('track_uris/track_uris.txt', 'r') as f:
            for line in f:
                track_uris.append(line.strip())

        playlist_name = os.getenv('ARTIST') + ' Discography'

        # # create a new playlist called os.getenv('ARTIST') and add all track uris to the playlist
        playlist = sp.user_playlist_create(user=sp.current_user()['id'], name=playlist_name, public=True)

        # # add all track uris to the playlist
        for i in range(0, len(track_uris), 100):
            sp.user_playlist_add_tracks(user=sp.current_user()['id'], playlist_id=playlist['id'], tracks=track_uris[i:i+100])
            if len(track_uris) - i > 99:
                print(f'Processed tracks {i} to {i+100}...')
            else:
                print(f'Processed tracks {i} to {len(track_uris)}...')
                print('\nAll tracks added to playlist')



# Main Function
# Filter this function to only run the functions you want to test
# IE if you only want to run the Setlist API functions, comment out the Spotify API functions using the '#' symbol
if __name__ == '__main__':
    #load_dotenv()

    # Sets up API keys
    # TODO - update this function to be more dynamic
    # check if .env file exists
    # if it doesn't exist, run the setup_api_keys() function
    if not os.path.exists('.env'):
        setup_api_keys()
    
    # Initializes the SpotiPy Object
    sp = load_and_initialize_spotify()

    # # read all spotify track uris from track_uris/track_uris.txt
    # track_uris = []
    # with open('track_uris/track_uris.txt', 'r') as f:
    #     for line in f:
    #         track_uris.append(line.strip())

    # playlist_name = os.getenv('ARTIST') + ' Discography'

    # # # create a new playlist called os.getenv('ARTIST') and add all track uris to the playlist
    # playlist = sp.user_playlist_create(user=sp.current_user()['id'], name=playlist_name, public=True)

    # print()
    # # # add all track uris to the playlist
    # for i in range(0, len(track_uris), 100):
    #     sp.user_playlist_add_tracks(user=sp.current_user()['id'], playlist_id=playlist['id'], tracks=track_uris[i:i+100])
    #     if len(track_uris) - i > 99:
    #         print(f'Processed tracks {i} to {i+100}...')
    #     else:
    #         print(f'Processed tracks {i} to {len(track_uris)}...')
    #         print('\nAll tracks added to playlist\n')

    
    
