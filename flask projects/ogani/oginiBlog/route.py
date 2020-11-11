from oginiBlog import bcrypt ,app ,login_manager ,db
from flask import render_template ,request ,flash ,url_for ,redirect 
from oginiBlog.forms import RegistrationForm ,LoginForm
from flask_login import login_user ,current_user ,logout_user ,login_required
from oginiBlog.models import Users ,Categories ,Products



@app.route('/')
def index():
    categories =Categories.query.all()
    products = Products.query.all()
    return render_template('index.html',categories=categories, products=products)

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog_details')
def blog_details():
    return render_template('blog_details.html')

@app.route('/check_out')
def check_out():
    return render_template('check_out.html')

@app.route('/fav')
def fav():
    return render_template('fav.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/shop_details')
def shop_details():
    return render_template('shop_details.html')

@app.route('/shop_grid')
def shop_grid():
    return render_template('shop_grid.html')

@app.route('/shoping_cart')
def shoping_cart():
    return render_template('shoping_cart.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)






