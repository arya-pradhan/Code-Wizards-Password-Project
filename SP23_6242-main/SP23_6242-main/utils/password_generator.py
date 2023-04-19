import random, string
import random
import string
from db import db
from models.word import Word


def get_nouns():
    return [word.word for word in db.session.query(Word).where(Word.word_type == "noun").all()]


def get_adjectives():
    return [word.word for word in db.session.query(Word).where(Word.word_type == "adjective").all()]

# returns a concatenated string of: an adjective, a noun, and single number. All picked at random


def simple_password():
    nouns = get_nouns()
    adjectives = get_adjectives()
    return str(random.choice(adjectives)) + str(random.choice(nouns)) + str(random.randint(1, 9))

# returns a concatenated string of: an adjective, a noun, and three numbers. All picked at random. Also replaces a random letter with a symbol


def moderate_password():
    nouns = get_nouns()
    adjectives = get_adjectives()
    simple = str(random.choice(adjectives)) + \
        str(random.choice(nouns)) + str(random.randint(100, 999))
    letters = 0
    for character in simple:
        if character in string.ascii_letters:
            letters += 1
    simple = list(simple)
    simple[random.randint(0, letters-1)] = random.choice(string.punctuation)
    return ''.join(simple)

# returns a random combination of letters, numbers, and symbols


def strong_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(random.randint(15, 18)))
