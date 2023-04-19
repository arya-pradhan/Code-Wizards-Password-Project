from db import db

word_type_enum = ('noun', 'adjective')


class Word(db.Model):
    __tablename__ = "words"

    def __init__(self, word_type: str = None, word: str = None):
        if word_type and word_type in word_type_enum:
            self.word_type = word_type
        if word:
            self.word = word

    id = db.Column(db.Integer, primary_key=True)
    word_type = db.Column(db.String, nullable=False)
    word = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Word {self.word}>"
