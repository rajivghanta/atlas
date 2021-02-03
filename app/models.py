from app import db
from datetime import datetime
from sqlalchemy.dialects.postgresql.json import JSONB

class Job(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.DateTime, default=datetime.utcnow())
	url = db.Column(db.String(), index=True)
	dom = db.Column(db.Text)
	extracted_data = db.Column(JSONB)

	def __repr__(self):
		return '<Job {}>'.format(self.title)
