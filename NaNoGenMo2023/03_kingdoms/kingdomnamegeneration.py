import random

def generate_medieval_kingdom_name(*args, **kwargs):
    prefixes = ["Kingdom of", "Duchy of", "Realm of", "Sovereignty of", "Empire of", "Principality of"]
    adjectives = ["Eternal", "Mighty", "Golden", "Mystic", "Ancient", "Forgotten"]
    nouns = ["Dragons", "Swords", "Shadows", "Thrones", "Spirits", "Forests"]

    prefix = random.choice(prefixes)
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    return f"{prefix} {adjective} {noun}"

def setup_game(metagame):
    metagame.set_concept("generate_kingdom_name", generate_medieval_kingdom_name)

