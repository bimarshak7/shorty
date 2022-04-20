from main import app,db
import uuid
from flask import jsonify, render_template, request,redirect
from models import Shorten

@app.route('/',methods=['GET','POST'])
def home():
	if request.method == 'POST':
		url = request.form.get('url')
		name = request.form.get('shortcode')
		print(url,name)
		if not name:name = str(uuid.uuid4())[:5]
		link = Shorten.query.filter_by(short_url=name).first()
		if link: return render_template('index.html',msg='Short name already used!')
		link = Shorten.query.filter_by(orig_url=url).first()
		if link: 
			s_url = request.base_url+link.short_url
			return render_template('index.html',new=False,msg='Shortened url already exist!',link=s_url)
		
		new_link = Shorten(orig_url=url,short_url=name)
		db.session.add(new_link)
		db.session.commit()
		print(new_link)
		s_url = request.base_url+name
		return render_template('index.html',new=True,msg1='Hooray! Link Shortened.',link=s_url)

	return render_template('index.html')

@app.route("/<name>")
def work(name):
	print("Url request: ",name)
	link = Shorten.query.filter_by(short_url=name).first()
	if link:return redirect(link.orig_url)