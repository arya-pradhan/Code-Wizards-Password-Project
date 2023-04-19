from db import db
from flask import Blueprint, render_template, request, current_app, flash, redirect, url_for
from models.survey import Survey

survey_bp = Blueprint('survey', __name__)


@survey_bp.route('/')
def survey():
    return render_template('survey.html')


@survey_bp.route('/form')
def surveyform():
    return render_template('survey_form.html')


@survey_bp.route('/form', methods=['POST'])
def surveyform_post():
    current_app.logger.info('Survey Submitted Adding to database')
    question1 = request.form.get('questions1')
    question2 = request.form.get('questions2')
    question3 = request.form.get('questions3')
    question4 = request.form.get('questions4')
    question5 = request.form.get('questions5')

    try:
        survey = Survey()
        survey.question1 = question1
        survey.question2 = question2
        survey.question3 = question3
        survey.question4 = question4
        survey.question5 = question5
        db.session.add(survey)
        db.session.commit()

        current_app.logger.info(f'Saved {survey} to database')

        flash("Thanks for completing the survey!")
        return redirect(url_for("survey.survey"))
    except:
        current_app.logger.info(f'Error saving survey to database')
        flash("There was an error processing the survey")
        return redirect(url_for("survey.survey"))
