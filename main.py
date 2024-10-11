import os

from scripts.envs import *

from scripts._1___get_artist_music import *
from scripts._2___get_artist_albums import *
from scripts._3___get_artist_albums import *
from scripts._4___get_artist_albums import *
from scripts._5___get_artist_albums import *

# Makes parts of the code easier to read
def prints(name, obj=None):
    if not obj:
        print()
        print('-'*50, name, '-'*50)
    else:
        print('-'*50 + '-'*(len(name)+2) + '-'*50)
        print()

if __name__ == '__main__':

    # Sets up API keys
    if not os.path.exists('.env'):
        setup_api_keys()
    
    # Initializes the SpotiPy Object
    sp = load_and_initialize_spotify()

    print('\nStarting the process to collect all tracks for', os.getenv('ARTIST') + '...')



    prints("Step 1")

    artist_id = get_artist_id(sp)
    get_artist_albums(sp, artist_id)
    get_artist_singles(sp, artist_id)
    get_artist_features(sp, artist_id)

    prints("Step 1", '-')

    

    # prints("Step 2")
    # prints("Step 2", '-')

    # prints("Step 3")
    # x3.get_album_tracks(sp)
    # prints("Step 3", '-')

    # prints("Step 4")
    # x4.add_tracks_to_playlist(sp)
    # prints("Step 4", '-')

    # prints("Step 5")
    # x5.asciiify()
    # prints("Step 5", '-')

    # # Step 6 - Clear the jsons folder
    