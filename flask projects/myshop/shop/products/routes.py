from flask import redirect, render_template, url_for, flash, request
from shop import db ,app
from .models import Brand ,Category,AddProduct
from .forms import Addproducts
import secrets
from PIL import Image
import os




def brands():
    brands = Brand.query.join(AddProduct, (Brand.id == AddProduct.brand_id)).all()
    return brands

def categories():
    categories = Category.query.join(AddProduct,(Category.id == AddProduct.category_id)).all()
    return categories

@app.route('/')
def home():
    page = request.args.get('page',1, type=int)
    proudcts = AddProduct.query.filter(AddProduct.stock > 0).order_by(AddProduct.id.desc()).paginate(page=page, per_page=3)
    brands = Brand.query.join(AddProduct, (Brand.id == AddProduct.brand_id)).all()
    categories = Category.query.join(AddProduct,(Category.id == AddProduct.category_id)).all()
    return render_template('products/index.html',products=proudcts,brands=brands,categories=categories)

@app.route('/product/<int:id>')
def single_page(id):
    product = AddProduct.query.get_or_404(id)
    return render_template('products/single_page.html',product=product)



@app.route('/brand/<int:id>')
def get_brand(id):
    page = request.args.get('page',1, type=int)
    get_brand = Brand.query.filter_by(id=id).first_or_404()
    brand = AddProduct.query.filter_by(brand_id=id).paginate(page=page, per_page=2)
    brands = Brand.query.join(AddProduct, (Brand.id == AddProduct.brand_id)).all()
    categories = Category.query.join(AddProduct,(Category.id == AddProduct.category_id)).all()
    return render_template('products/index.html',brand=brand,brands=brands,categories=categories,get_brand=get_brand)


@app.route('/categories/<int:id>')
def get_category(id):
    page = request.args.get('page',1, type=int)  
    get_cat = Category.query.filter_by(id=id).first_or_404() 
    get_cat_prod = AddProduct.query.filter_by(category_id=id).paginate(page=page, per_page=3)
    brands = Brand.query.join(AddProduct, (Brand.id == AddProduct.brand_id)).all()
    categories = Category.query.join(AddProduct,(Category.id == AddProduct.category_id)).all()
    return render_template('products/index.html',get_cat_prod=get_cat_prod,categories=categories,brands=brands,get_cat=get_cat)

@app.route('/addbrand',methods=['GET','POST'])
def addbrand():
    if request.method =='POST':
        getBrand = request.form.get('brand')
        brand = Brand(name=getBrand)
        db.session.add(brand)

        flash(f'the Brand {getBrand} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html',brands='brands')

@app.route('/addcat',methods=['GET','POST'])
def addcat():
    if request.method =='POST':
        getcat = request.form.get('category')
        cat = Category(name=getcat)
        db.session.add(cat)

        flash(f'the category {getcat} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html')


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route('/addproduct',methods=['GET','POST'])
def addproduct():
    form = Addproducts(request.form)
    brands = Brand.query.all()
    categories = Category.query.all()
    if request.method=="POST":
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        desc = form.discription.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        image_1 = save_picture(request.files.get('image_1'))
        image_2 = save_picture(request.files.get('image_2'))
        image_3 = save_picture(request.files.get('image_3'))
        addproduct = AddProduct(name=name,price=price,discount=discount,stock=stock,colors=colors,desc=desc,category_id=category,brand_id=brand,image_1=image_1,image_2=image_2,image_3=image_3)
        db.session.add(addproduct)
        flash(f'The product {name} was added in database','success')
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('products/addproduct.html',title='Add product page' ,form=form,brands=brands,categories=categories)
