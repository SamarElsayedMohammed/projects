from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os

from flask_msearch import Search
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail

# basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/myshop'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myshop.db'
app.config['SECRET_KEY']='8907aed45d0a4dcf2244ed6295a42b37'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False





db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
search = Search()
search.init_app(app)


#email configuration 

# app.config['MAIL_SERVER']='smtp.googlemail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USERNAME'] = 'samarelsayedmohammed12345@gmail.com'
# app.config['MAIL_PASSWORD'] = 'samar123elsayed123456789'
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = True

# mail = Mail(app)


migrate = Migrate(app, db)
with app.app_context():
    if db.engine.url.drivername == "sqlite":
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='customerLogin' #function login in route
login_manager.needs_refresh_message_category='danger'
login_manager.login_message = u"Please login first"

from shop.admin import routes
from shop.products import routes
from shop.carts import carts
from shop.customers import routes