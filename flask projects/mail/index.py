from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)


@app.route("/")
def index():
    msg = Message("Hello", sender="example@gmail.com", recipients=["to@gmail.com"])
    msg.body = "testing"
    msg.html = "<b>testing</b>"
    return mail.send(msg)


if __name__ == '__main__':
    app.run(debug=True)