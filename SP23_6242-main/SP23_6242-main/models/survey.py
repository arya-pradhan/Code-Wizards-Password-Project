from db import db


class Survey(db.Model):
    __tablename__ = "survey"

    def __init__(self, question1=None, question2=None, question3=None, question4=None, question5=None):
        if question1:
            self.question1 = question1
        if question2:
            self.question2 = question2
        if question3:
            self.question3 = question3
        if question4:
            self.question4 = question4
        if question5:
            self.question5 = question5

    id = db.Column(db.Integer, primary_key=True)
    question1 = db.Column(db.String)
    question2 = db.Column(db.String)
    question3 = db.Column(db.String)
    question4 = db.Column(db.String)
    question5 = db.Column(db.String)
