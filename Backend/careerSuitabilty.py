from questionAnalysisCareer import *


def determine_career_suitability(data, chosen_career):
    match chosen_career:
        case 'ceo':
            functions = ceo_suitability(data)
        case 'doctor':
            functions = doctor_suitability(data)
        case 'model':
            functions = model_suitability(data)
        case 'rockstar':
            functions = rockstar_suitability(data)
        case 'astronaut':
            functions = astronaut_suitability(data)
        case _:
            return "No career selected to analyse"
    total = 0
    for func in functions:
        if func:
            total += 1
    return f'Your career suitabilty is {round(total / len(functions) * 100)}%'


def ceo_suitability(data):
    return [is_talkative(data), is_thorough(data), is_original(data), is_unselfish(data), is_curious(data),
            is_reliable(data), is_teamplayer(data), is_faultfinder(data), not is_disorganised(data)]


def doctor_suitability(data):
    return [is_thorough(data), is_unselfish(data), is_relaxed(data), is_curious(data), is_reliable(data),
            is_deepthinker(data), is_teamplayer(data), not is_lazy(data), not is_argumentative(data),
            not is_careless(data)]


def model_suitability(data):
    return [is_thorough(data), is_original(data), is_unselfish(data), is_relaxed(data),
            is_energetic(data), is_reliable(data), is_quiet(data), not is_nervous(data), not is_shy(data),
            not is_disorganised(data)]


def rockstar_suitability(data):
    return [is_talkative(data), is_original(data), is_relaxed(data), is_energetic(data), is_argumentative(data),
            is_deepthinker(data), is_disorganised(data), not is_shy(data), not is_nervous(data)]


def astronaut_suitability(data):
    return [not is_nervous(data), not is_careless(data), is_curious(data), is_reliable(data), not is_worrier(data),
            is_quiet(data), is_shy(data), is_teamplayer(data)]
