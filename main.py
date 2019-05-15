import socket, json
from db_config import mysql, app, mail
from flaskext.mysql import MySQL, pymysql
from flask import flash, request,make_response, current_app, Blueprint, jsonify, Response, session, send_file, send_from_directory 
from werkzeug import generate_password_hash, check_password_hash
import hashlib
from flask_mail import Mail, Message
from flask import render_template
from validate_email import validate_email
import threading
from modules import *
from flask import copy_current_request_context
import db_config, string,random


app.register_blueprint(modules)


def send_mail(token,email,nombapell,url_activacion):
    #msj = "Activacion de usuario"
    msg= Message('Gracias por su Registro en UbiiMarket!', recipients = [email])
    msg.html= render_template('email_registro.html',nombapell=nombapell,url_activacion=url_activacion,token=token)
    mail.send(msg)

def send_mailCompany(email,company):
    #PreAfiliación"    
    msg = Message("Registro de Pre-Afiliación UbiiMarket", recipients = [email])
    msg.html= render_template('email_preafiliacion.html', company=company)
    mail.send(msg)

def send_mailCompanyCode(email,company,access_code,struser):
    #"Envío de credenciales al Fabricante"
    msg = Message("Registro de Afiliación UbiiMarket", recipients = [email])
    msg.html= render_template('email_afiliacion.html', company=company, strpassword=access_code, struser=struser)    
    mail.send(msg)

def send_mailCompanyActivation(email,company):
    #"Activacion de usuario de comercio"    
    msg = Message("Registro de Afiliación UbiiMarket", recipients = [email])
    msg.html= render_template('email_afiliacion_retail.html', company=company)
    mail.send(msg)

def sendResponse(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Content-Type', 'multipart/form-data')
    return response

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="0.0.0.0")
