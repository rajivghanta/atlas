from app import db

class Job(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String(1024), index=True, unique=True)
	title = db.Column(db.String(1024), index=True, unique=True)

	def __repr__(self):
		return '<Job {}>'.format(self.title)
