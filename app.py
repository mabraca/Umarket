from flask import Flask
from flask_mail import Mail
 


class app():
    app = Flask(__name__)
    mail=Mail(app)
    #configuration flask to Mail
    app.config['MAIL_SERVER'] = "just64.justhost.com"
    app.config['MAIL_PORT'] = 26
    app.config['MAIL_USERNAME'] = 'no-reply@ubiipagos.com'  #user mail
    app.config['MAIL_PASSWORD'] = 'Ubiipagos.2017'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_DEFAULT_SENDER']  =  'no-reply@ubiipagos.com' #user that will go email)
    mail = Mail(app)
