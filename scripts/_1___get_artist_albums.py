import os
import json

def get_artist_id(sp):
    artist = os.getenv('ARTIST')
    artist_json = sp.search(q=artist, type='artist')
    artist_id = artist_json['artists']['items'][0]['id']

    print("\nArtist ID for artist", artist, "is", artist_id, "\n")

    return artist_id

def get_artist_albums(sp, artist_id):
    counter = 0
    offset = 0

    while True:
        artist_albums = sp.artist_albums(artist_id, include_groups='album', limit=50, offset=offset)
        if artist_albums['items'] == []:
            break

        print("Processing", len(artist_albums['items']), "albums...")

        # save json to file
        artist_albums_json = json.dumps(artist_albums, indent=4)
        with open(f'jsons/artist_albums_{offset}.json', 'w') as f:
            f.write(artist_albums_json)

        counter += len(artist_albums['items'])
        offset += 50

    print("All albums acquired")
    print("Total albums acquired:", counter, "\n")
    
def get_artist_singles(sp, artist_id):
    counter = 0
    offset = 0

    while True:
        artist_singles = sp.artist_albums(artist_id, include_groups='single', limit=50, offset=offset)
        if artist_singles['items'] == []:
            break

        print("Processing", len(artist_singles['items']), "singles...")

        # save json to file
        artist_singles_json = json.dumps(artist_singles, indent=4)
        with open(f'jsons/artist_singles_json_{offset}.json', 'w') as f:
            f.write(artist_singles_json)

        counter += len(artist_singles['items'])
        offset += 50

    print("All singles acquired")
    print("Total singles acquired:", counter, "\n")

# Main Function
# Filter this function to only run the functions you want to test
# IE if you only want to run the Setlist API functions, comment out the Spotify API functions using the '#' symbol
if __name__ == '__main__':
    pass

    # # Sets up API keys
    # if not os.path.exists('.env'):
    #     setup_api_keys()
    
    # # Initializes the SpotiPy Object
    # sp = load_and_initialize_spotify()
    # artist = os.getenv('ARTIST')
    # artist_json = sp.search(q=artist, type='artist')
    # artist_id = artist_json['artists']['items'][0]['id']

    # print("Artist ID for artist", artist, "is", artist_id)

    # counter = 0
    # offset = 0

    # while True:
    #     artist_albums = sp.artist_albums(artist_id, include_groups='album', limit=50, offset=offset)
    #     if artist_albums['items'] == []:
    #         break

    #     print("Aquired", len(artist_albums['items']), "albums...")

    #     # save json to file
    #     artist_albums_json = json.dumps(artist_albums, indent=4)
    #     with open(f'jsons/artist_albums_{offset}.json', 'w') as f:
    #         f.write(artist_albums_json)

    #     counter += len(artist_albums['items'])
    #     offset += 50

    # print("\nAll albums acquired")
    # print("Total albums acquired:", counter)

    # counter = 0
    # offset = 0

    # while True:
    #     artist_singles = sp.artist_albums(artist_id, include_groups='single', limit=50, offset=offset)
    #     if artist_singles['items'] == []:
    #         break

    #     print("Aquired", len(artist_singles['items']), "albums...")

    #     # save json to file
    #     artist_singles_json = json.dumps(artist_singles, indent=4)
    #     with open(f'jsons/artist_singles_json_{offset}.json', 'w') as f:
    #         f.write(artist_singles_json)

    #     counter += len(artist_singles['items'])
    #     offset += 50

    # print("\nAll singles acquired")
    # print("Total singles acquired:", counter)