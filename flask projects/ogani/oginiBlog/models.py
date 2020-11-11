from datetime import datetime
from oginiBlog import db, login_manager ,app
from flask_login import UserMixin


class Users(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    active = db.Column(db.String(5), nullable=False, default='0')
    password = db.Column(db.String(60), nullable=False)
    

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))



class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    arabic_name = db.Column(db.String(100), nullable=False)
    english_name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(20), nullable=False)
    price_one = db.Column(db.Integer, nullable=False )
    price_two = db.Column(db.Integer, nullable=False )
    categories_id = db.Column(db.Integer, db.ForeignKey('categories.id'),nullable=False)
    categories = db.relationship('Categories',backref=db.backref('posts', lazy=True))

    

    def __repr__(self):
        return f"Categories('{self.arabic_name}', '{self.english_name}' , '{self.image}')"


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    arabic_name = db.Column(db.String(100), nullable=False)
    english_name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Categories('{self.arabic_name}', '{self.english_name}' , '{self.image}')"


