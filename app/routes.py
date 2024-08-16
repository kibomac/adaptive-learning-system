from flask import Blueprint, render_template, jsonify, request
from app.utils import get_next_question, update_learner_model
from app.models import User, Question
from app import db
import plotly.express as px

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({"message": "Welcome to the Adaptive Learning System"})

@main.route('/plot_example')
def plot_example():
    data = {'x': [1, 2, 3, 4], 'y': [10, 11, 12, 13]}
    fig = px.line(data, x='x', y='y', title='Example Plot')
    plot_html = fig.to_html()
    return render_template('plot.html', plot_html=plot_html)

@main.route('/get_next_question/<int:user_id>', methods=['GET'])
def get_next_question_route(user_id):
    user = User.query.get_or_404(user_id)
    question = get_next_question(user)
    
    if question:
        return jsonify({
            'question': question.content,
            'difficulty': question.difficulty,
            'topic': question.topic,
        })
    return jsonify({"error": "No suitable question found."}), 404

@main.route('/submit_answer/<int:user_id>/<int:question_id>', methods=['POST'])
def submit_answer(user_id, question_id):
    user = User.query.get_or_404(user_id)
    question = Question.query.get_or_404(question_id)
    
    answer = request.json.get('answer')
    if answer == question.correct_answer:
        score = 100
    else:
        score = 0
    
    user.last_score = score
    user.last_question = question
    db.session.commit()
    
    return jsonify({"message": "Answer submitted successfully", "score": score})

from app.utils import get_next_question, update_learner_model



@main.route('/submit_answer/<int:user_id>/<int:question_id>', methods=['POST'])
def submit_answer(user_id, question_id):
    user = User.query.get_or_404(user_id)
    question = Question.query.get_or_404(question_id)
    
    answer = request.json.get('answer')
    if answer == question.correct_answer:
        score = 100
    else:
        score = 0
    
    update_learner_model(user, question, score)
    
    return jsonify({"message": "Answer submitted successfully", "score": score})
