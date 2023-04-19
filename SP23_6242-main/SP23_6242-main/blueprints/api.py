# Use this blueprint to add API endpoints.
# Freely Remove or Update the default routes when needed

from db import db
from flask import Blueprint, render_template, current_app, request, jsonify
from utils.route_decorators import request_args
from utils.password_generator import simple_password, moderate_password, strong_password
from models.survey import Survey
from models.statistics import Statistics
import time

api_bp = Blueprint('api', __name__)


# Example:
@api_bp.route('/')
@request_args
def example_message(msg):
    return jsonify({
        "msg": msg
    })


@api_bp.route('/passwords')
@request_args
def get_passwords(complexity="simple", count=1):
    count = int(count)

    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    password_type = complexity
    number_of_passwords = count
    db.session.add(Statistics(timestamp=timestamp, password_type=password_type,
                              number_of_passwords=number_of_passwords))
    db.session.commit()

    if complexity.lower() == "simple":
        passwords = [simple_password() for i in range(count)]
        return jsonify(passwords)
    elif complexity.lower() == "moderate":
        passwords = [moderate_password() for i in range(count)]
        return jsonify(passwords)
    elif complexity.lower() == "complex":
        passwords = [strong_password() for i in range(count)]
        return jsonify(passwords)
    else:
        return "ruh roh"


@api_bp.route('/survey-results', methods=['GET', 'POST'])
def get_survey_data():
    total_surveys = Survey.query.count()

    question1_answer1 = Survey.query.filter(
        Survey.question1 == "Not very careful online").count()
    question1_answer2 = Survey.query.filter(
        Survey.question1 == "Moderatly careful online").count()
    question1_answer3 = Survey.query.filter(
        Survey.question1 == "Extremely careful online").count()

    question2_answer1 = Survey.query.filter(
        Survey.question2 == "All are the same").count()
    question2_answer2 = Survey.query.filter(
        Survey.question2 == "Some are the same/minor differences").count()
    question2_answer3 = Survey.query.filter(
        Survey.question2 == "All are different").count()

    question3_answer1 = Survey.query.filter(
        Survey.question3 == "Simple").count()
    question3_answer2 = Survey.query.filter(
        Survey.question3 == "Moderately complex").count()
    question3_answer3 = Survey.query.filter(
        Survey.question3 == "Complex").count()

    question4_answer1 = Survey.query.filter(
        Survey.question4 == "Never").count()
    question4_answer2 = Survey.query.filter(
        Survey.question4 == "Sometimes").count()
    question4_answer3 = Survey.query.filter(
        Survey.question4 == "Many times").count()

    question5_answer1 = Survey.query.filter(
        Survey.question5 == "No I don't").count()
    question5_answer2 = Survey.query.filter(
        Survey.question5 == "Perhaps when I have time").count()
    question5_answer3 = Survey.query.filter(
        Survey.question5 == "Yes I will").count()

    return jsonify(
        {
            "total_surveys": total_surveys,
            "question1": {
                "answer1_count": question1_answer1,
                "answer2_count": question1_answer2,
                "answer3_count": question1_answer3
            },
            "question2": {
                "answer1_count": question2_answer1,
                "answer2_count": question2_answer2,
                "answer3_count": question2_answer3
            },
            "question3": {
                "answer1_count": question3_answer1,
                "answer2_count": question3_answer2,
                "answer3_count": question3_answer3
            },
            "question4": {
                "answer1_count": question4_answer1,
                "answer2_count": question4_answer2,
                "answer3_count": question4_answer3
            },
            "question5": {
                "answer1_count": question5_answer1,
                "answer2_count": question5_answer2,
                "answer3_count": question5_answer3
            },
        })


@api_bp.route('/statistics_submission')
def statistic_submissions():
    stats = Statistics.query.all()
    stats_list = []
    for stat in stats:
        stat_dict = {
            'id': stat.id,
            'timestamp': stat.timestamp,
            'password_type': stat.password_type,
            'number_of_passwords': stat.number_of_passwords,
            'password_length': stat.password_length,
            'min_symbols': stat.min_symbols,
            'max_numbers': stat.max_numbers
        }
        stats_list.append(stat_dict)
    return jsonify(stats_list)
