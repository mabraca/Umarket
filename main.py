import pymysql, string, random
import socket, json
from db_config import mysql, app, mail
from flaskext.mysql import MySQL
from flask import jsonify
from flask import flash, request,make_response, current_app
from werkzeug import generate_password_hash, check_password_hash
import hashlib
from flask_mail import Mail, Message
from validate_email import validate_email

#print_lock = threading.Lock()

@app.route('/')
def root_response():
    return jsonify({"Msj":"API REST UbiiMarket."})
@app.route('/register', methods=['POST'])
def add_user():
    try:
        _json= request.get_json(force=True)
        _strcorreo = _json['stremail']
        _strusuario = _json['struser']
        _strcontrasena = _json['strpassword']
        _strnombres = _json['strname']
        _strapellidos = _json['strsurname']
        _bt_estatus_id = _json['bt_estatus_id']
        caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits
        longitud = 8  # La longitud que queremos
        _token = ''.join(random.choice(caracteres) for _ in range(longitud))

        # validate the received values
        if  _strusuario and request.method == 'POST': 
            if _strcontrasena:
                if _strcorreo: 
                    if _strnombres:
                        if _strapellidos:                            
                            _hashed_password = hashlib.md5(_strcontrasena.encode())
                            existe_user=user_validate(_strusuario)
                            if not existe_user:                                
                                existe_email=email_validate(_strcorreo)
                                if not existe_email:
                                    # save edits
                                    sql = "INSERT INTO dt_usuarios(strcorreo_electronico, strusuario, strcontrasena, strnombres, strapellidos, tb_estatus_id, token) VALUES(%s, %s, %s, %s, %s, %s, %s)"
                                    data = (_strcorreo, _strusuario, _hashed_password.hexdigest(), _strnombres, _strapellidos, _bt_estatus_id, _token)
                                    nombapell= _strnombres + " " + _strapellidos
                                    conn = mysql.connect()
                                    cursor = conn.cursor()
                                    cursor.execute(sql, data)
                                    conn.commit()
                                    resp = jsonify({"status":'success', "msj":"El usuario fue registrado","token":_token})
                                    resp.headers.add('Access-Control-Allow-Origin', '*')
                                    resp.status_code = 200                                    
                                    send_mail(_token,_strcorreo,nombapell)
                                    return resp
                                else:
                                    resp = jsonify({"status":'error', "msj":"El correo ya se encuentra registrado"})
                                    resp.headers.add('Access-Control-Allow-Origin', '*')
                                    #resp.status_code = 400
                                    return resp
                            else:
                                resp = jsonify({"status":'error', "msj":"El usuario ya se encuentra registrado"})
                                resp.headers.add('Access-Control-Allow-Origin', '*')
                                #resp.status_code = 400
                                return resp
                        else:
                            resp = jsonify({"status":'error', "msj":"Debe ingresar un apellido"})
                            resp.headers.add('Access-Control-Allow-Origin', '*')
                            #resp.status_code = 400
                            return resp
                    else:
                        resp = jsonify({"status":'error', "msj":"Debe ingresar un nombre"})
                        resp.headers.add('Access-Control-Allow-Origin', '*')
                        #resp.status_code = 400
                        return resp
                else:
                    resp = jsonify({"status":'error', "msj":"Debe ingresar un correo"})
                    resp.headers.add('Access-Control-Allow-Origin', '*')
                    #resp.status_code = 400
                    return resp
            else:
                resp = jsonify({"status":'error', "msj":"Debe ingresar una contraseña"})
                resp.headers.add('Access-Control-Allow-Origin', '*')
                #resp.status_code = 404
                return resp
        else:
            resp = jsonify({"status":'error', "msj":"Debe ingresar un usuario"})
            resp.headers.add('Access-Control-Allow-Origin', '*')
            #resp.status_code = 400
            return resp
    except Exception as e:
        print(e)
    
@app.route('/users')
def users():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM dt_usuarios ")
        rows = cursor.fetchall()
        if rows:
            resp = jsonify(rows)
            resp.headers['Access-Control-Allow-Origin']='*'
            resp.status_code = 200
            return resp
        elif not rows:
            resp = jsonify({"status":False, "msj":"No se encuentran usuarios registrados"})
            resp.headers['Access-Control-Allow-Origin']='*'
            return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/user', methods=['POST'])
def user():
    try:
        _json = request.json
        _id = _json['id']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM dt_usuarios WHERE id=%s",_id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.headers.add('Access-Control-Allow-Origin', '*')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/user_login', methods=['POST'])
def userlogin():
    try:             
        _json= request.get_json(force=True)
       # print(_json)
        _strusuario = _json['struser']
        _strcontrasena = _json['strpassword']
        if _strusuario and  request.method == 'POST':
            if _strcontrasena:
                existe_user=user_validate(_strusuario)  
                _hashed_password = hashlib.md5(_strcontrasena.encode())
                if existe_user:
                    if existe_user['tb_estatus_id']==2:
                        if (existe_user['strcontrasena']==_hashed_password.hexdigest()):
                            caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits
                            longitud = 32  # La longitud que queremos
                            _token = ''.join(random.choice(caracteres) for _ in range(longitud))
                            resp = jsonify({"status":"success", "msj":"El usuario logeado","strusuario":existe_user['strusuario'], "strnombres":existe_user['strnombres'], "strapellidos":existe_user['strapellidos'],"strcorreo":existe_user['strcorreo_electronico'],"token":_token})
                            resp.headers.add('Access-Control-Allow-Origin', '*')
                            resp.headers.add('Content-Type', 'application/json')
                            resp.status_code = 200
                            return resp
                        else:
                            resp = jsonify({"status":'error', "msj":"La contraseña es inválida"})
                            resp.headers.add('Access-Control-Allow-Origin', '*')
                            resp.headers.add('Content-Type', 'application/json')
                            return resp                       
                    else:
                        resp = jsonify({"status": 'error', "msj": "El usuario inactivo"})
                        resp.headers.add('Access-Control-Allow-Origin', '*')   
                        resp.headers.add('Content-Type', 'application/json')         
                        return resp
                else:
                    resp = jsonify({"status": 'error', "msj": "El usuario no existe"})
                    resp.headers.add('Access-Control-Allow-Origin', '*')   
                    resp.headers.add('Content-Type', 'application/json')         
                    return resp
            else:
                resp = jsonify({"status": 'error', "msj": "Debe ingresar una contraseña"})
                resp.headers.add('Access-Control-Allow-Origin', '*')  
                resp.headers.add('Content-Type', 'application/json')          
                return resp
        else:
            resp = jsonify({"status": False, "msj": "Debe ingresar un usuario"})
            resp.headers.add('Access-Control-Allow-Origin', '*') 
            resp.headers.add('Content-Type', 'application/json')           
            return resp    
    except Exception as e:
        print(e)
    
@app.route('/update', methods=['POST'])
def update_user():
    try:
        _json = request.json
        _id = _json['id']
        _strcorreo = _json['stremail']
        _strusuario = _json['struser']
        _strcontrasena = _json['strpassword']
        _strnombres = _json['strname']
        _strapellidos = _json['strsurname']
        _bt_estatus_id = _json['bt_estatus_id']
        # validate the received values
        if _strcorreo and _strcontrasena and _id and request.method == 'POST':
            # do not save password as a plain text
            _hashed_password = generate_password_hash(_strcontrasena)
            # save edits
            sql = "UPDATE dt_usuarios SET strcorreo_electronico=%s,strcontrasena=%s WHERE id=%s"
            data = (_strcorreo, _hashed_password, _id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('El usuario fue actualizado')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/delete/')
def delete_user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dt_usuarios WHERE id=%s", (id,))
        conn.commit()
        resp = jsonify('User deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def user_validate(strusuario):
    try:
        _strusuario=strusuario
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM dt_usuarios WHERE strusuario=%s",_strusuario)
        row = cursor.fetchone()
        return row
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def email_validate(strcorreo):
    try:
        _strcorreo=strcorreo
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql="SELECT * FROM dt_usuarios WHERE strcorreo_electronico=%s"
        cursor.execute(sql,_strcorreo)
        row = cursor.fetchone()
        return row
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/token',methods=['POST'])
def token():
    try:        
        _json= request.get_json(force=True)
        _token= _json['token']
        if _token and  request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sql="SELECT id,token,tb_estatus_id FROM dt_usuarios WHERE token=%s"
            cursor.execute(sql,_token)
            row = cursor.fetchone()
            if row:
                if row['tb_estatus_id']==1:
                    token=activate_user(_token)       
                    if token:
                        resp = jsonify({"status": 'success', "msj": "El token fue activado"})
                        resp.headers.add('Access-Control-Allow-Origin', '*') 
                        resp.headers.add('Content-Type', 'application/json')           
                        return resp
                    else:
                        resp = jsonify({"status": 'error', "msj": "El token no fue activado"})
                        resp.headers.add('Access-Control-Allow-Origin', '*') 
                        resp.headers.add('Content-Type', 'application/json')           
                        return resp
                else:
                    resp = jsonify({"status": 'error', "msj": "El token fue utilizado"})
                    resp.headers.add('Access-Control-Allow-Origin', '*') 
                    resp.headers.add('Content-Type', 'application/json')           
                    return resp
                                
            else:
                resp = jsonify({"status": 'error', "msj": "El token es inválido"})
                resp.headers.add('Access-Control-Allow-Origin', '*') 
                resp.headers.add('Content-Type', 'application/json')           
                return resp               
        else:
            resp = jsonify({"status": 'error', "msj": "Debe ingresar un token"})
            resp.headers.add('Access-Control-Allow-Origin', '*') 
            resp.headers.add('Content-Type', 'application/json')           
            return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def activate_user(token):
    try:
        _token=token
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        afectado=cursor.execute("UPDATE dt_usuarios SET tb_estatus_id=2 WHERE token=%s",_token)
        conn.commit()
        return afectado
        
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def send_mail(token,email,nombapell):
    """Envio ."""
    #msj = "Activacion de usuario"
    recipients = [email]
    msg_object = Message("Activacion de usuario "+nombapell, recipients)
    msg_object.body = "Activacion de usuario "+nombapell+", Código:"+ token
    mail.send(msg_object)
    return "Sent"

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
