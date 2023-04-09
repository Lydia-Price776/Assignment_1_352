import json
import random

import questionAnalysisCareer
from requestFiles import *


def analyse_form_data():
    file = open('user_data/user_data.json')
    data = json.load(file)
    file.close()
    recommended_career = determine_career_recommendation(data)
    recommended_movies = determine_movie_recommendation(recommended_career)

    analyse = {
        "Name": data['name'],
        "Birthyear": data['birthyear'],
        "Birthplace": data['residence'],
        "Career Chosen": data['job'],
        "Recommended Career": recommended_career,
        "Message": data['message'],
        "Movies": recommended_movies
    }
    if "gender" in data:
        analyse['Gender'] = data['gender']
    if "pet[0]" in data:
        analyse['Dog'] = get_dog_uri()
    if "pet[1]" in data:
        analyse['Cat'] = get_cat_uri()
    if "pet[1]" in data:
        analyse['Duck'] = get_duck_uri()

    return analyse


def determine_career_recommendation(data):
    careers = {
        'ceo': 0,
        'doctor': 0,
        'model': 0,
        'astronaut': 0,
        'rockstar': 0,
    }

    question_attr = dir(questionAnalysisCareer)

    question_functions = [attr for attr in question_attr if
                          callable(getattr(questionAnalysisCareer, attr))
                          and not attr.startswith("__")]

    for function_name in question_functions:
        question = getattr(questionAnalysisCareer, function_name)
        careers = question(data, careers)

    max_value = max(careers.values())

    recommended = [key for key, value in careers.items() if value == max_value]

    if len(recommended) < 2:
        return recommended[0]
    else:
        return recommended[random.randint(0, len(recommended) - 1)]


def determine_movie_recommendation(career):
    match career:
        case 'ceo':
            return get_movies('strong', 'bold', 'leader')
        case 'doctor':
            return get_movies('medicine', 'Dr', 'bones')
        case 'astronaut':
            return get_movies('space', 'rocket', 'star')
        case 'rockstar':
            return get_movies('music', 'soulful', 'tempo')
        case 'model':
            return get_movies('fashion', 'clothes', 'textiles')
