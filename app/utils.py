import random
from app.models import Question, User
from app import db

def get_next_question(user):
    """
    Determines the next question to present to the user based on their previous performance.
    Adjusts the difficulty level based on the user's last score.
    """
    last_score = user.last_score if user.last_score is not None else 0
    difficulty = 1  # Default difficulty level
    
    # Adjust difficulty based on the user's last performance
    if last_score > 80:
        difficulty = min(user.last_question.difficulty + 1, 5)
    elif last_score < 50:
        difficulty = max(user.last_question.difficulty - 1, 1)
    
    # Fetch a question from the database with the appropriate difficulty level
    questions = Question.query.filter_by(difficulty=difficulty).all()
    
    # Return a random question from the selected difficulty level
    if questions:
        return random.choice(questions)
    
    return None


def update_learner_model(user, question, score):
    """
    Updates the learner model for the user based on their response to a question.
    """
    user.last_score = score
    user.last_question = question
    db.session.commit()

