from questionAnalysisCareer import *


def determine_career_suitability(data, chosen_career):
    match chosen_career:
        case 'ceo':
            return ceo_suitability(data)
        case 'doctor':
            return doctor_suitability(data)
        case 'model':
            return model_suitability(data)
        case 'rockstar':
            return rockstar_suitability(data)
        case 'astronaut':
            return astronaut_suitability(data)
        case _:
            return 'You are nothing.'


def ceo_suitability(data):
    return 'You are a CEO'


def doctor_suitability(data):
    return 'You are a doctor'


def model_suitability(data):
    return 'You are a model'


def rockstar_suitability(data):
    return 'You are a rockstar'


def astronaut_suitability(data):
    return 'You are an astronaut'
