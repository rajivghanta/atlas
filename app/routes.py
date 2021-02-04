from flask import render_template, flash, redirect, request, url_for
from app import app, db
from app.models import User, Job
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
import json
from app.job_data_extractor import job_data_extractor


@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid email or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)
	return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route('/')
@app.route('/index')
@login_required
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
