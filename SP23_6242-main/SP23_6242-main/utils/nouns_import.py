def nouns_import():
    with open("utils/nouns.txt", "r") as file:
        return {noun.strip() for noun in file.readlines()}
