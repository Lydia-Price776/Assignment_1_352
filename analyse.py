import inspect
import json
import questionAnalysis


def analyse_form_data():
    file = open('user_data/user_data.json')
    data = json.load(file)
    file.close()

    determine_career_recommendation(data)

    analyse = {
        "Name": data['name'],
        "Birthyear": data['birthyear'],
        "Birthplace": data['residence'],
        "Career Chosen": data['job'],
        "Recommended Career": determine_career_recommendation(data),
        "Message": data['message']
    }
    if 'gender' in data:
        analyse['Gender'] = data['gender']
    if 'pet[0]' in data:
        analyse['Dog'] = 'True'
    if 'pet[1]' in data:
        analyse['Cat'] = 'True'
    if 'pet[1]' in data:
        analyse['Duck'] = 'True'


#  for i in analyse:
# print(i, analyse[i])


def determine_career_recommendation(data):
    careers = {
        'ceo': 0,
        'doctor': 0,
        'model': 0,
        'astronaut': 0,
        'rockstar': 0,
    }
    functions = [func for func in dir(questionAnalysis)
                 if callable(getattr(questionAnalysis, func))
                 and func.startswith("question_")]

    for name in functions:
        func = getattr(questionAnalysis, name)
        print(f"Applying function {name} to variable")
        careers = func(data, careers)


analyse_form_data()
