//Creating the alchemy database and the movie model
# TODO - Create SQLAlchemy DB and Movie model
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225), nullable=False)
    director = db.Column(db.String(225), nullable=False)
    rating = db.Column(db.String, nullable=False)
