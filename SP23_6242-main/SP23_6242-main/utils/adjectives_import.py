def adjectives_import():
    with open("utils/adjectives.txt", "r") as file:
        return {adjective.strip() for adjective in file.readlines()}
