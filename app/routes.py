from flask import render_template, request
from app import app, db
from app.models import Job
import json
from app.job_data_extractor import job_data_extractor

@app.route('/')
@app.route('/index')
def index():
	jobs = Job.query.all()
	return render_template('index.html', title='Home', jobs=jobs)

@app.route('/job/', methods=['POST'])
@app.route('/job/<id>', methods=['GET'])
def job(id=None):
	if request.method == 'POST':
		data = request.get_json()
		# print(data)
		job = Job(url=data['url'], dom=data['dom'])
		job.extracted_data = job_data_extractor(data['url'], data['dom'])
		db.session.add(job)
		db.session.commit()
		return json.dumps({'success': True}), 200, {'ContentType':'application/json'}
	else:
		job = Job.query.get(id)
		return json.dumps(job), 200, {'ContentType':'application/json'}

@app.route('/job/delete/<id>', methods=['GET', 'DELETE'])
def job_delete(id):
	job = Job.query.get(id)
	db.session.delete(job)
	db.session.commit()
	return json.dumps({'success': True}), 200, {'ContentType':'application/json'}
