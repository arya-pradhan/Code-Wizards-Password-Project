from db import db


class Statistics(db.Model):
    __tablename__ = "statistics"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.String)
    password_type = db.Column(db.String)
    number_of_passwords = db.Column(db.String)
    password_length = db.Column(db.String)
    min_symbols = db.Column(db.String)
    max_numbers = db.Column(db.String)
