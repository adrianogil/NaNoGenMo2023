
import random

# Define lists of name parts
prefixes = ['Al', 'Be', 'Ced', 'Ed', 'Fitz', 'God', 'Hen', 'Is', 'John', 'Lan', 'Mered', 'Nor', 'Or', 'Per', 'Quin', 'Rand', 'Si', 'Theo', 'Ul', 'Ver', 'Will', 'Xan', 'Yar', 'Zed']
suffixes = ['ard', 'bert', 'mund', 'fred', 'ric', 'son', 'wyn', 'dred', 'olf', 'stan', 'rick', 'ton', 'ion', 'ald', 'mar', 'mond']
female_endings = ['a', 'ia', 'ina', 'ara', 'wyn', 'elle', 'esse', 'trude', 'gund', 'lotte', 'line']
male_endings = ['bert', 'frid', 'gar', 'hard', 'mond', 'ric', 'win', 'ward', 'ulf', 'stan', 'son']

# Define a function to generate a name
def generate_name(*args, **kwargs):
    prefix = random.choice(prefixes)
    
    if "gender" in kwargs:
        gender = kwargs["gender"]
    else:
        gender='either'

    # Choose a suitable ending based on the gender
    if gender.lower() == 'female':
        suffix = random.choice(female_endings)
    elif gender.lower() == 'male':
        suffix = random.choice(male_endings)
    else:
        suffix = random.choice(suffixes)
    
    # Concatenate the chosen parts
    name = prefix + suffix
    return name


def setup_game(metagame):
    metagame.set_concept("generate_character_name", generate_name)
