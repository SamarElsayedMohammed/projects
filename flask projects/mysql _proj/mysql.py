from flask import Flask ,render_template ,request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB'] ='Flask'

mysql = MySQL(app)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/login' , methods=['GET', 'POST'])
def login():
    if request.method =='GET':
        return 'loginvia the login form'
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']

        cr = mysql.connection.cursor()
        cr.execute('''insert into info_table values(%s,%s)''',(name,age))
        mysql.connection.commit()
        cr.close()
        return f'Done!'
app.run(host='localhost')