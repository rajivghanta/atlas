from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql.json import JSONB

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	jobs = db.relationship('Job', backref='author', lazy='dynamic')
	secret = db.Column(db.String())

	def __repr__(self):
		return '<User {}>'.format(self.email)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

class Job(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
	url = db.Column(db.String(), index=True)
	dom = db.Column(db.Text)
	extracted_job_data = db.Column(JSONB)
	user_job_data = db.Column(JSONB)

	def __repr__(self):
		return '<Job {}>'.format(self.url)
