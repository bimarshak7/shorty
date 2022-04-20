from main import db

class Shorten(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	orig_url = db.Column(db.String(100))
	short_url = db.Column(db.String(30))