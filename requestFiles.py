import requests


def get_dog_uri():
    host = 'dog.ceo'
    path = 'api/breeds/image/random'
    response = requests.get(f'https://{host}/{path}')
    outmap = response.json()
    components = outmap['message'].split('/')
    filename = 'user_data/' + components[len(components) - 1]
    get_image(outmap['message'], filename)
    return filename


def get_cat_uri():
    host = 'api.thecatapi.com'
    path = 'v1/images/search'
    response = requests.get(f'https://{host}/{path}')
    [outmap] = response.json()
    components = outmap['url'].split('/')
    filename = 'user_data/' + components[len(components) - 1]
    get_image(outmap['url'], filename)
    return filename


def get_duck_uri():
    host = 'random-d.uk'
    path = 'api/v2/random'
    response = requests.get(f'https://{host}/{path}')
    outmap = response.json()
    components = outmap['url'].split('/')
    filename = 'user_data/' + components[len(components) - 1]
    get_image(outmap['url'], filename)
    return filename


def get_image(uri, filename):
    response = requests.get(uri)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)


def get_movies(title1, title2, title3):
    movie_list = [get_movie(title1), get_movie(title2), get_movie(title3)]
    return movie_list


def get_movie(given_path):
    host = 'www.omdbapi.com'
    apikey = '?apikey=2820b54'
    path = f'&t={given_path}'
    response = requests.get(f'https://{host}/{apikey}{path}')
    outmap = response.json()
    return outmap['Title'], outmap['Director'], outmap['Year'], outmap['Genre']
