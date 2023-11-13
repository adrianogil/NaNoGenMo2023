import random

def generate_medieval_castle_name(*args, **kwargs):
    prefixes = ["Castle", "Fortress", "Keep", "Citadel", "Tower", "Palace"]
    adjectives = ["Dark", "Majestic", "Silent", "Hidden", "Enchanted", "Ancient"]
    nouns = ["Shadow", "Stone", "Wolf", "Eagle", "Mist", "Fire"]

    prefix = random.choice(prefixes)
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    return f"{prefix} of the {adjective} {noun}"

def setup_game(metagame):
    metagame.set_concept("generate_castle_name", generate_medieval_castle_name)
