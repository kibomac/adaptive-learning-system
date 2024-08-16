from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    last_score = db.Column(db.Integer, nullable=True)
    last_question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=True)
    last_question = db.relationship('Question', backref='users')

    def __repr__(self):
        return f"User('{self.username}', 'Last Score: {self.last_score}')"

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)  # 1 (Easy) to 5 (Hard)
    topic = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"Question('{self.content}', 'Difficulty: {self.difficulty}', 'Topic: {self.topic}')"
