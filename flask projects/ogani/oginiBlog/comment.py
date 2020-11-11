# @app.route('/login' ,methods=['POST','GET'])
# def login():

#     # if current_user.is_authenticated:
#     #     return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         email=form.email.data
#         query = f"select * from users where email='{email}'"
#         cr = mysql.connection.cursor()
#         s = cr.execute(query)
#         s = cr.fetchall()
#         # mysql.connection.commit()
#         # crr.close()
#         # print (f'<h1>{type(s)}</h1>')
#         sss =len(s)
#         return f'<h1>{s}</h1>'

#         # if s and bcrypt.check_password_hash(s.password, form.password.data):
#         #     return redirect(url_for('index'))
#         # else:
#         #     flash('Login Unsuccessful. Please check email and password', 'danger')


# @app.route('/register', methods=['POST','GET'])
# def register():
#     # if current_user.is_authenticated:
#     #     return redirect(url_for('index'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         username=form.username.data
#         email=form.email.data
#         password=hashed_password
#         query = f"select * from users where email='{email}'"
#         cr = mysql.connection.cursor()
#         s= cr.execute(query)
#         if s :
#            flash(f'Account : {email}! is exist','danger')
#            return redirect(url_for('register'))

#             # return "   exist"
#         elif cr.execute(f"select * from users where name='{username}'"):
#            flash(f'name : {username}! is exist','danger')
#            return redirect(url_for('register'))
#         else:
         
#             cr = mysql.connection.cursor()
#             cr.execute(f"insert into users (name,email,password) values ('{username}','{email}','{password}')")
#             mysql.connection.commit()
#             cr.close()
#             flash(f'Account created for {username}!^_^','success')

#             return redirect(url_for('index'))

#     return render_template('register.html' ,form=form)

# app.config['MYSQL_HOST']='localhost'
# app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']=''
# app.config['MYSQL_DB'] ='ogini'


# mysql = MySQL(app)

# INSERT INTO `ogini`.`categories` (`id`, `arabic_name`, `english_name`) VALUES ('10', 'شوفان', 'Oatmeal');
