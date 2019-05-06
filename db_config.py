from flask import Flask
from flaskext.mysql import MySQL
from flask_mail import Mail

app = Flask(__name__)
mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'ubiimarket_db_dev'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
#configuration flask to Mail
app.config['MAIL_SERVER'] = "just64.justhost.com"
app.config['MAIL_PORT'] = 26
app.config['MAIL_USERNAME'] = 'no-reply@ubiipagos.com'  #user mail
app.config['MAIL_PASSWORD'] = 'Ubiipagos.2017'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER']  =  'no-reply@ubiipagos.com' #user that will go email)
mail = Mail(app)
app.config['UPLOAD_FOLDER']='./modules/documents_company/'