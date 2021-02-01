from flask import render_template, request
from app import app, db
from app.models import Bookmark
import json

@app.route('/')
@app.route('/index')
def index():
	bookmarks = Bookmark.query.all()
	return render_template('index.html', title='Home', bookmarks=bookmarks)

@app.route('/add', methods=['GET', 'POST'])
def add():
	data = request.get_json()
	print(data)
	bookmark = Bookmark(url=data['url'], title=data['title'])
	db.session.add(bookmark)
	db.session.commit()
	return json.dumps({'success': True}), 200, {'ContentType':'application/json'} 
