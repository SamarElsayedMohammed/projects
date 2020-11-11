from flask import render_template, session, redirect, url_for, request, flash, current_app
from shop import app, db, bcrypt
from .forms import RegitrationForm, LoginForm
from shop.products.forms import Addproducts
from .models import User
from shop.products.models import AddProduct,Category,Brand
import os,secrets
from shop.products.routes import save_picture




@app.route('/admin')
def admin():
    if 'email' not in session:
        flash(f'please login first','danger')
        return redirect(url_for('login'))
    products = AddProduct.query.all()

    return render_template('admin/index.html',title="Admin",products=products)

@app.route('/brands')
def brands():
    if 'email' not in session:
        flash(f'please login first','danger')
        return redirect(url_for('login'))
    brands = Brand.query.order_by(Brand.id.desc()).all()

    return render_template('admin/brand.html',title="Brand page",brands=brands)

@app.route('/categories')
def categories():
    if 'email' not in session:
        flash(f'please login first','danger')
        return redirect(url_for('login'))
    categories = Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/brand.html', title='categories',categories=categories)


@app.route('/register',methods=['GET','POST'])
def register():
    form = RegitrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data ,username=form.username.data, email=form.email.data,password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'welcome {form.username.data}Thanks you for registering','success')
        return redirect(url_for('admin'))
    return render_template('admin/register.html',title='Register user',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email']=form.email.data
            flash(f'welcome {form.email.data}','success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('wrong or email please try again ','danger')

    return render_template('admin/login.html',title="Login Page",form=form)

@app.route('/updatebrand/<int:id>',methods=['GET','POST'])
def updatebrand(id):
    if 'email' not in session:
        flash(f'please login first','danger')
        return redirect(url_for('login'))
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method =="POST":
        updatebrand.name = brand
        flash(f'The brand {updatebrand.name} was changed to {brand}','success')
        db.session.commit()
        return redirect(url_for('brands'))
    return render_template('products/updatebrand.html', title='Udate brand',updatebrand=updatebrand)


@app.route('/deletebrand/<int:id>', methods=['GET','POST'])
def deletebrand(id):
    brand = Brand.query.get_or_404(id)
    
    if request.method=="POST":
        db.session.delete(brand)
        flash(f"The brand {brand.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f"The brand {brand.name} can't be  deleted from your database","warning")
    return redirect(url_for('admin'))

@app.route('/updatecat/<int:id>',methods=['GET','POST'])
def updatecat(id):
    if 'email' not in session:
        flash(f'please login first','danger')
        return redirect(url_for('login'))
    updatecat = Category.query.get_or_404(id)
    category = request.form.get('category')
    if request.method =="POST":
        updatecat.name = category
        flash(f'Your category  was changed to {updatecat.name}','success')
        db.session.commit()
        return redirect(url_for('categories'))
    return render_template('products/updatebrand.html', title='Udate category',updatecat=updatecat)

@app.route('/deletecat/<int:id>', methods=['GET','POST'])
def deletecat(id):
    category = Category.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(category)
        flash(f"The brand {category.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f"The brand {category.name} can't be  deleted from your database","warning")
    return redirect(url_for('admin'))

@app.route('/updateproduct/<int:id>', methods=['GET','POST'])
def updateproduct(id):
    categories = Category.query.all()
    brands = Brand.query.all()
    product = AddProduct.query.get_or_404(id)
    brand = request.form.get('brand')
    category = request.form.get('category')
    form = Addproducts(request.form)
    if request.method =="POST":
        product.name = form.name.data 
        product.price = form.price.data
        product.discount = form.discount.data
        product.stock = form.stock.data 
        product.colors = form.colors.data
        product.desc = form.discription.data
        product.category_id = category
        product.brand_id = brand
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
                product.image_1 = save_picture(request.files.get('image_1'))
            except:
               product.image_1 = save_picture(request.files.get('image_1'))
        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
                product.image_1 = save_picture(request.files.get('image_2'))
            except:
               product.image_1 = save_picture(request.files.get('image_2'))
        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
                product.image_1 = save_picture(request.files.get('image_3'))
            except:
               product.image_1 = save_picture(request.files.get('image_3'))
        flash('The product was updated','success')
        db.session.commit()
        return redirect(url_for('admin'))
    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
    form.stock.data = product.stock
    form.colors.data = product.colors
    form.discription.data = product.desc
    brand = product.brand.name
    category = product.category.name

    return render_template('products/updateproduct.html', form=form, title='updat a Product',categories=categories,brands=brands,product=product)

@app.route('/deleteproduct/<int:id>', methods=['POST'])
def deleteproduct(id):
    product = AddProduct.query.get_or_404(id)
    if request.method =="POST":
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
        except Exception as e:
            print(e)
        db.session.delete(product)
        db.session.commit()
        flash(f'The product {product.name} was delete from your record','success')
        return redirect(url_for('admin'))
    flash(f'Can not delete the product','success')
    return redirect(url_for('admin'))
