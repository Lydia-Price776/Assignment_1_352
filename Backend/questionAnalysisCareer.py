"""
Lydia Price, 20004521
The below functions aid in determining career suitability by determining the users answer to each question
"""


# Is talkative?
def is_talkative(data):
    if int(data['question[1]']) >= 3:
        return True


# Does a thorough job
def is_thorough(data):
    if int(data['question[2]']) >= 3:
        return True


# Is original, comes up with new ideas
def is_original(data):
    if int(data['question[3]']) >= 3:
        return True


# is helpful, unselfish with others
def is_unselfish(data):
    if int(data['question[4]']) >= 3:
        return True


# Can be somewhat careless
def is_careless(data):
    if int(data['question[5]']) > 3:
        return True


# is relaxed, handles stress well
def is_relaxed(data):
    if int(data['question[6]']) >= 3:
        return True


# Is curious about many things
def is_curious(data):
    if int(data['question[7]']) > 3:
        return True


# Is full of energy
def is_energetic(data):
    if int(data['question[8]']) > 3:
        return True


# Starts quarrels with others
def is_argumentative(data):
    if int(data['question[9]']) > 3:
        return True


# Is a reliable worker
def is_reliable(data):
    if int(data['question[10]']) >= 3:
        return True


# Is a deep thinker
def is_deepthinker(data):
    if int(data['question[11]']) > 3:
        return True


# Tends to be disorganized
def is_disorganised(data):
    if int(data['question[12]']) >= 3:
        return True


# Worries a lot
def is_worrier(data):
    if int(data['question[13]']) > 3:
        return True


# Tends to be quiet
def is_quiet(data):
    if int(data['question[14]']) > 3:
        return True


# Tends to be lazy
def is_lazy(data):
    if int(data['question[15]']) > 3:
        return True


# Sometimes shy
def is_shy(data):
    if int(data['question[16]']) > 3:
        return True


# Is sometimes rude to others
def is_rude(data):
    if int(data['question[17]']) > 3:
        return True


# Tends to find fault with others
def is_faultfinder(data):
    if int(data['question[18]']) > 3:
        return True


# Gets nervous easily
def is_nervous(data):
    if int(data['question[19]']) > 3:
        return True


# Likes to work in a team
def is_teamplayer(data):
    if int(data['question[20]']) > 3:
        return True
