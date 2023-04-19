from db import db
from models.survey import Survey
from models.statistics import Statistics
from models.word import Word
from utils.adjectives_import import adjectives_import
from utils.nouns_import import nouns_import


def create_words(word_type, word_list):
    words_objects_list = []
    for word in word_list:
        newWord = Word(word_type=word_type, word=word)
        words_objects_list.append(newWord)
    return words_objects_list


def create_data():
    data_to_save = []
    nouns = create_words(word_type="noun", word_list=nouns_import())
    data_to_save.extend(nouns)
    adjectives = create_words(word_type="adjective",
                              word_list=adjectives_import())
    data_to_save.extend(adjectives)

    data_to_save.append(Survey(question1="Moderatly careful online", question2="All are the same",
                        question3="Moderatly complex", question4="Sometimes", question5="No I don't"))
    data_to_save.append(Survey(question1="Extreamly careful online", question2="All are different",
                        question3="Moderatly complex", question4="Sometimes", question5="Yes I will"))
    data_to_save.append(Survey(question1="Not very careful online", question2="All are the same",
                        question3="Simple", question4="Sometimes", question5="Perhaps when I have time"))
    data_to_save.append(Survey(question1="Moderatly careful online", question2="All are the same",
                        question3="Moderatly complex", question4="Sometimes", question5="No I don't"))
    data_to_save.append(Survey(question1="Moderatly careful online", question2="Some are the same/minor differences",
                        question3="Complex", question4="Sometimes", question5="No I don't"))
    data_to_save.append(Survey(question1="Moderatly careful online", question2="All are the same",
                        question3="Simple", question4="Sometimes", question5="No I don't"))
    data_to_save.append(Survey(question1="Moderatly careful online", question2="All are the same",
                        question3="Moderatly complex", question4="Sometimes", question5="No I don't"))
    data_to_save.append(Survey(question1="Moderatly careful online", question2="All are the same",
                        question3="Complex", question4="Sometimes", question5="No I don't"))
    data_to_save.append(Survey(question1="Moderatly careful online", question2="All are the same",
                        question3="Moderatly complex", question4="Sometimes", question5="No I don't"))
    data_to_save.append(Survey(question1="Moderatly careful online", question2="Some are the same/minor differences",
                        question3="Moderatly complex", question4="Sometimes", question5="No I don't"))
    
    data_to_save.append(Statistics(timestamp="11:24:13",
                        password_type="Moderate", number_of_passwords="2", password_length="10", min_symbols="3", max_numbers="6"))
    data_to_save.append(Statistics(timestamp="12:27:52",
                        password_type="Simple", number_of_passwords="4", password_length="6", min_symbols="1", max_numbers="5"))
    data_to_save.append(Statistics(timestamp="18:34:12",
                        password_type="Moderate", number_of_passwords="6", password_length="10", min_symbols="6", max_numbers="1"))
    data_to_save.append(Statistics(timestamp="09:54:53",
                        password_type="Complex", number_of_passwords="7", password_length="7", min_symbols="3", max_numbers="2"))
    data_to_save.append(Statistics(timestamp="05:14:24",
                        password_type="Moderate", number_of_passwords="1", password_length="5", min_symbols="3", max_numbers="2"))

    db.session.bulk_save_objects(data_to_save)
    db.session.commit()
    print(f"Total Objects Saved {len(data_to_save)}")
