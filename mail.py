#################
#### imports ####
#################
 
from flask import Flask
from flask_mail import Mail
 
 
################
#### config ####
################
 
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')
 
mail = Mail(app)