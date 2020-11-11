from flask import Flask, render_template
skill_app=Flask(__name__)
@skill_app.route('/')
def home():
    return render_template('home.html',pagetitle="home")


if __name__=='__main__':
    skill_app.run(debug=True,port=9000)