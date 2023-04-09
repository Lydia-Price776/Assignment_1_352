import requests


def get_dog_uri():
    host = 'dog.ceo'
    path = 'api/breeds/image/random'
    response = requests.get(f'https://{host}/{path}')
    outmap = response.json()
    print(outmap)
    filename = 'user_data/user_dog_image.jpg'
    get_image(outmap['message'], filename)


def get_cat_uri():
    host = 'api.thecatapi.com'
    path = 'v1/images/search'
    response = requests.get(f'https://{host}/{path}')
    [outmap] = response.json()
    filename = 'user_data/user_cat_image.jpg'
    get_image(outmap['url'], filename)


def get_duck_uri():
    host = 'random-d.uk'
    path = 'api/v2/random'
    response = requests.get(f'https://{host}/{path}')
    outmap = response.json()
    filename = 'user_data/user_duck_image.jpg'
    get_image(outmap['url'], filename)


def get_image(uri, filename):
    response = requests.get(uri)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)


def get_movie_():
    host = 'www.omdbapi.com'
    apikey = '?apikey=2820b54'
    path = '&t=alien'
    print(f'https://{host}/{apikey}{path}')
    response = requests.get(f'https://{host}/{apikey}{path}')
    outmap = response.json()
    print(outmap)



