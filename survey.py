from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class SurveyResponse(db.Model):
    __tablename__ = 'survey_responses'
    
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<SurveyResponse {self.id}: {self.answer[:50]}...>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'answer': self.answer,
            'created_at': self.created_at.isoformat()
        }

