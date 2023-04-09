# Is talkative?
def question_1(data, careers):
    if int(data['question[1]']) >= 3:
        careers['ceo'] += 1
        careers['rockstar'] += 2
        careers['doctor'] += 1
    return careers


# Does a thorough job
def question_2(data, careers):
    if int(data['question[2]']) >= 3:
        careers['ceo'] += 1
        careers['doctor'] += 1
        careers['astronaut'] += 1
    return careers


# Is original, comes up with new ideas
def question_3(data, careers):
    if int(data['question[3]']) >= 3:
        careers['ceo'] += 1
        careers['rockstar'] += 2
        careers['model'] += 1
    return careers


# is helpful, unselfish with others
def question_4(data, careers):
    if int(data['question[4]']) >= 3:
        careers['doctor'] += 1
        careers['ceo'] += 1
    return careers


# Can be somewhat careless
def question_5(data, careers):
    if int(data['question[5]']) < 3:
        careers['doctor'] += 2
        careers['ceo'] += 1
        careers['astronaut'] += 1
    return careers


# is relaxed, handles stress well
def question_6(data, careers):
    if int(data['question[6]']) >= 3:
        careers['model'] = + 1
        careers['doctor'] = + 1

    return careers


# Is curious about many things
def question_7(data, careers):
    if int(data['question[7]']) > 3:
        careers['doctor'] += 1
        careers['astronaut'] += 1
        careers['rockstar'] += 1
    return careers


# Is full of energy
def question_8(data, careers):
    if int(data['question[8]']) > 3:
        careers['model'] += 1
        careers['rockstar'] += 1
    return careers


# Starts quarrels with others
def question_9(data, careers):
    if int(data['question[9]']) > 3:
        careers['doctor'] -= 2
        careers['ceo'] -= 2
    return careers


# Is a reliable worker
def question_10(data, careers):
    if int(data['question[10]']) >= 3:
        careers['doctor'] += 2
        careers['rockstar'] += 1
    return careers


# Is a deep thinker
def question_11(data, careers):
    if int(data['question[11]']) > 3:
        careers['rockstar'] += 1
        careers['doctor'] += 1
    return careers


# Tends to be disorganized
def question_12(data, careers):
    if int(data['question[12]']) >= 3:
        careers['ceo'] -= 2
        careers['astronaut'] -= 1
    return careers


# Worries a lot
def question_13(data, careers):
    if int(data['question[13]']) > 3:
        careers['model'] += 1
        careers['rockstar'] += 1
    return careers


# Tends to be quiet
def question_14(data, careers):
    if int(data['question[14]']) > 3:
        careers['model'] += 2
    return careers


# Tends to be lazy
def question_15(data, careers):
    if int(data['question[15]']) > 3:
        careers['doctor'] -= 1
        careers['ceo'] -= 1
    return careers


# Sometimes shy
def question_16(data, careers):
    if int(data['question[16]']) > 3:
        careers['model'] -= 1
        careers['rockstar'] -= 1
    return careers


# Is sometimes rude to others
def question_17(data, careers):
    if int(data['question[17]']) > 3:
        careers['ceo'] -= 2
        careers['doctor'] -= 2

    return careers


# Tends to find fault with others
def question_18(data, careers):
    if int(data['question[18]']) > 3:
        careers['doctor'] += 2  # its generally what doctors tend to do :)
    return careers


# Gets nervous easily
def question_19(data, careers):
    if int(data['question[19]']) > 3:
        careers['rockstar'] -= 2
        careers['model'] -= 1

    return careers


# Likes to work in a team
def question_20(data, careers):
    if int(data['question[20]']) > 3:
        careers['astronaut'] += 1
        careers['doctor'] += 1
        careers['rockstar'] += 1

    return careers
