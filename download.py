from flickrapi import FlickrAPI 
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys
#API
key = "d58ca6a38740bd677c00f3d5907905d3"
secret = "3f70705f8989a80d"
wait_time = 1

animal_names = ['crow', 'boar', 'monkey']
photo_num = 400


def saveAnimal(animal_name, photo_num):

#    animal_name = sys.argv[1]
    save_dir = "./" + animal_name

    flickr = FlickrAPI(key, secret, format='parsed-json')
    result = flickr.photos.search(
        text = animal_name,
        per_page = photo_num,
        media = 'photos',
        sort = 'relevance',
        safe_search = 1,
        extras = 'url_q, licence'
    )

    photos = result['photos']
    pprint(photos)

    for i, photo in enumerate(photos['photo']):
        url_q = photo['url_q']
        file_path = save_dir + '/' + photo['id'] + '.jpg'
        if os.path.exists(file_path): continue
        urlretrieve(url_q, file_path)
        time.sleep(wait_time)

if __name__ == '__main__':
   for animal_name in animal_names:
#    for