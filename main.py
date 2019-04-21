import socket, json
from db_config import mysql, app, mail
from flaskext.mysql import MySQL, pymysql
from flask import flash, request,make_response, current_app, Blueprint, jsonify, Response
from werkzeug import generate_password_hash, check_password_hash
import hashlib
from flask_mail import Mail, Message
from validate_email import validate_email
from modules import *
import db_config, string,random

app.register_blueprint(modules)


def send_mail(token,email,nombapell):
    """Envio ."""
    #msj = "Activacion de usuario"
    recipients = [email]
    msg_object = Message("Activacion de usuario UbiiMarket", recipients)
    msg_object.body = "Activacion de usuario "+nombapell+", Código: "+ token
    mail.send(msg_object)
    return "Sent"


def send_mailCompany(email,company):
    """Envio ."""
    #msj = "Activacion de usuario"
    recipients = [email]
    msg_object = Message("Registro de Pre-Afiliación UbiiMarket", recipients)
    msg_object.body = "Usted realizó el registro de Pre-Afiliación "+company
    mail.send(msg_object)
    return "Sent"

def sendResponse(response):
    #resp=json.dumps(response)
   # print(resp)
    """if resp.status=='error':
        response.status_code=204
    if resp.status=='warning':
        response.status_code=202 
    if resp.status=='success':
        response.status_code=200"""
        
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Content-Type', 'application/json')
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
    app.run(port=3000, host="0.0.0.0")
