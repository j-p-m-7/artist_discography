import os
import json
import importlib
#from dotenv import load_dotenv


def asciiify(image_path="image.png"):
    # # open artist_albums_0.json
    # with open('jsons/artist_albums_0.json') as f:
    #     artist_albums = json.load(f)
    
    # image_urls = []
    # for i in range(len(artist_albums['items'])):
    #     image_urls.append(artist_albums['items'][i]['images'][0]['url'])  

    # image_urls = image_urls[:15]

    # # pick a random image from the list using random library
    # import random
    # image_url = random.choice(image_urls)
    # print(image_url)

    # # download the image to image.png
    # import requests
    # from PIL import Image
    # from io import BytesIO

    # response = requests.get(image_url)
    # image = Image.open(BytesIO(response.content))
    # image.save('image.png')

    # Convert image to ASCII art
    asc = importlib.import_module("ascii_test")

    # Convert image to ASCII art and print it
    ascii_art = asc.print_ascii("image.png")
    print(ascii_art)

# Main Function
# Filter this function to only run the functions you want to test
# IE if you only want to run the Setlist API functions, comment out the Spotify API functions using the '#' symbol
if __name__ == '__main__':
    pass
    # # open artist_albums_0.json
    # with open('jsons/artist_albums_0.json') as f:
    #     artist_albums = json.load(f)
    
    # image_urls = []
    # for i in range(len(artist_albums['items'])):
    #     image_urls.append(artist_albums['items'][i]['images'][0]['url'])  

    # image_urls = image_urls[:15]

    # # pick a random image from the list using random library
    # import random
    # image_url = random.choice(image_urls)
    # print(image_url)

    # # download the image to image.png
    # import requests
    # from PIL import Image
    # from io import BytesIO

    # response = requests.get(image_url)
    # image = Image.open(BytesIO(response.content))
    # image.save('image.png')

    # Convert image to ASCII art
    #asc = importlib.import_module("ascii_test")

    # # Convert image to ASCII art and print it
    # ascii_art = asc.image_to_ascii("image.png")
    # print(ascii_art)

     