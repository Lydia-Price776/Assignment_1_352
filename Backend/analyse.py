"""
Lydia Price, 20004521
The below functions aid in determining career suitability and finding movies recommendations for the user
"""

import json
from careerSuitabilty import determine_career_suitability
from requestFiles import *


# Analyses the form data, and returns a dictionary with relevant information
def analyse_form_data():
    file = open('Backend/user_data/user_data.json')
    data = json.load(file)
    file.close()
    career_suitability = determine_career_suitability(data, data['job'])
    recommended_movies = determine_movie_recommendation(data['job'])

    analyse = {
        "Name": data['name'],
        "Birthyear": data['birthyear'],
        "Birthplace": data['residence'],
        "Career Chosen": data['job'],
        "Career Suitability": career_suitability,
        "Message": data['message'],
        "Movies": recommended_movies
    }
    if "gender" in data:
        analyse['Gender'] = data['gender']

    for key in data:
        if key.startswith('pet'):
            match data[key]:
                case 'dog':
                    analyse['Dog'] = get_dog_uri()
                case 'cat':
                    analyse['Cat'] = get_cat_uri()
                case 'duck':
                    analyse['Duck'] = get_duck_uri()

    return analyse


def determine_movie_recommendation(career):
    # Gets movie recommendations based on users career choice
    match career:
        case 'ceo':
            return get_movies('strong', 'bold', 'leader')
        case 'doctor':
            return get_movies('medicine', 'help', 'bones')
        case 'astronaut':
            return get_movies('space', 'rocket', 'star')
        case 'rockstar':
            return get_movies('music', 'soulful', 'tempo')
        case 'model':
            return get_movies('fashion', 'clothes', 'textiles')
        case _:
            return get_movies('and', 'the', 'scary')
