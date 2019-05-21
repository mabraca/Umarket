from main import *
from . import modules
import re

@modules.route('/user/register', methods=['POST'])
def addUser():
    try:
        _json= request.get_json(force=True)
        print(_json)
        _strcorreo = _json['stremail']
        _id_rol=_json['id_rol']
        _strcontrasena = _json['strpassword']
        _strnombres = _json['strname']
        _strapellidos = _json['strsurname']
        _url_activacion=_json['url_activated']
        caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits
        longitud = 8  # La longitud que queremos
        _token = ''.join(random.choice(caracteres) for _ in range(longitud))

        # validate the received values
        if  request.method == 'POST':   
            if not _strcorreo: 
                resp = jsonify({"status":'error', "msj":"Debe ingresar un correo"})
                return  sendResponse(resp)  
            if not re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',_strcorreo.lower()):
                resp = jsonify({"status":'error', "msj":"Debe ingresar un correo válido"})
                return  sendResponse(resp)  
            if not _strcontrasena:
                resp = jsonify({"status":'error', "msj":"Debe ingresar una contraseña"})
                return sendResponse(resp)           
            if not _strnombres:        
                resp = jsonify({"status":'error', "msj":"Debe ingresar un apellido"})
                return sendResponse(resp)
            if not _strapellidos:        
                resp = jsonify({"status":'error', "msj":"Debe ingresar un nombre"})
                return sendResponse(resp)   
            if not _id_rol:
                resp = jsonify({"status":'error', "msj":"Debe ingresar un rol"})
                return sendResponse(resp)                            
            _hashed_password = hashlib.md5(_strcontrasena.encode())
            print(_hashed_password)
            #existe_user=user_validate(_strusuario)
            #if not existe_user:                                
            existe_email=email_validate(_strcorreo)
            if not existe_email:
                # save edits
                sql = "INSERT INTO dt_usuarios(strcorreo, strcontrasena, id_rol, strnombres, strapellidos, token) VALUES(%s, %s, %s, %s, %s, %s)"
                data = (_strcorreo, _hashed_password.hexdigest(),_id_rol,_strnombres, _strapellidos, _token)
                nombapell= _strnombres + " " + _strapellidos
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()
                #Envío de correo usando hilos
                @copy_current_request_context
                def send_message(token,strcorreo,nombapell,url_activacion):
                    send_mail(token,strcorreo,nombapell,url_activacion)

                sender= threading.Thread(name='mail_sender',target=send_message, args=(_token,_strcorreo,nombapell,_url_activacion))
                sender.start()
                resp = jsonify({"status":'success', "msj":"El usuario fue registrado","token":_token})                                    
                resp.status_code = 200    
                
                
                #send_mail(_token,_strcorreo,nombapell,_url_activacion)
                return sendResponse(resp)
            else:
                resp = jsonify({"status":'error', "msj":"El usuario ya se encuentra registrado"})
                return  sendResponse(resp)                                                         
        else:
            resp = jsonify({"status":'error', "msj":"Debe ingresar un usuario"})
            return sendResponse(resp)
    except Exception as e:
        print(e)

@modules.route('/users') 
def users():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM dt_usuarios ")
        rows = cursor.fetchall()
        if rows:
            resp = jsonify(rows)            
            resp.status_code = 200
            return sendResponse(resp)
        elif not rows:
            resp = jsonify({"status":'error', "msj":"No se encuentran usuarios registrados"})
            return sendResponse(resp)      
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@modules.route('/user', methods=['POST'])
def user():
    try:
        _json = request.json
        _id = _json['id']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM dt_usuarios WHERE id_usuario=%s",_id)
        row = cursor.fetchone()
        resp = jsonify(row)        
        resp.status_code = 200
        return sendResponse(resp)

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@modules.route('/user_login', methods=['POST'])
def userLogin():
    try:             
        _json= request.get_json(force=True)
       # print(_json)
        _strcorreo = _json['stremail']
        _strcontrasena = _json['strpassword']
        if _strcorreo and  request.method == 'POST':
            if _strcontrasena:
                existe_user=user_validate(_strcorreo)  
                _hashed_password = hashlib.md5(_strcontrasena.encode())
                if existe_user:
                    if existe_user['id_status']==2:
                        if (existe_user['strcontrasena']==_hashed_password.hexdigest()):
                            caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits
                            longitud = 32  # La longitud que queremos
                            _token = ''.join(random.choice(caracteres) for _ in range(longitud))
                            resp = jsonify({"status":"success", "msj":"El usuario logeado","stremail":existe_user['strcorreo'], "strname":existe_user['strnombres'], "strsurname":existe_user['strapellidos'],"token":_token,"id_rol":existe_user['id_rol']})                                                      
                            resp.status_code = 200
                            return sendResponse(resp)
                        else:
                            resp = jsonify({"status":'warning', "msj":"La contraseña es inválida"})
                            return sendResponse(resp)                       
                    else:
                        resp = jsonify({"status": 'warning', "msj": "El usuario esta inactivo"})
                        return sendResponse(resp)
                else:
                    resp = jsonify({"status": 'error', "msj": "El usuario no existe"})
                    return sendResponse(resp)
            else:
                resp = jsonify({"status": 'error', "msj": "Debe ingresar una contraseña"})
                return sendResponse(resp)
        else:
            resp = jsonify({"status":"error", "msj": "Debe ingresar un usuario"})
            return sendResponse(resp)    
    except Exception as e:
        print(e)

@modules.route('/update', methods=['POST'])   
def updateUser():
    try:
        _json = request.json
        _id = _json['id_usuario']
        _strcorreo = _json['stremail']
        _strusuario = _json['struser']
        _strcontrasena = _json['strpassword']
        _strnombres = _json['strname']
        _strapellidos = _json['strsurname']
        _bt_estatus_id = _json['id_status']
        # validate the received values
        if _strcorreo and _strcontrasena and _id and request.method == 'POST':
            # do not save password as a plain text
            _hashed_password = generate_password_hash(_strcontrasena)
            # save edits
            sql = "UPDATE dt_usuarios SET strcorreo=%s,strcontrasena=%s WHERE id=%s"
            data = (_strcorreo, _hashed_password, _id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify({"status":"success","msj":"El usuario fue actualizado"})
            resp.status_code = 200
            return sendResponse(resp)
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@modules.route('/delete/')
def deleteUser():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dt_usuarios WHERE id=%s", (id,))
        conn.commit()
        resp = jsonify({"status":"success","msj":"El usuario fue eliminado"})
        resp.status_code = 200
        return sendResponse(resp)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#Funcion que valida si el usuario existe
def user_validate(strcorreo):
    try:
        print(strcorreo)
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM dt_usuarios WHERE strcorreo=%s",strcorreo)
        row = cursor.fetchone()
        return row
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#Funcion que valida si el correo electronico existe
def email_validate(strcorreo):
    try:
        _strcorreo=strcorreo
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql="SELECT * FROM dt_usuarios WHERE strcorreo=%s"
        cursor.execute(sql,_strcorreo)
        row = cursor.fetchone()
        return row
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@modules.route('/token',methods=['POST'])
def token():
    try:                
        _json= request.get_json(force=True)
        _token= _json['token']
        print(_token)
        if _token and  request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sql="SELECT id_usuario,token,id_status,id_rol FROM dt_usuarios WHERE token=%s"
            cursor.execute(sql,_token)
            row = cursor.fetchone()
            if row:
                if row['id_status']==1:
                    token=activate_user(_token)       
                    if token:
                        resp = jsonify({"status": 'success', "msj": "El token fue activado","id_rol":row['id_rol']})
                        return sendResponse(resp)
                    else:
                        resp = jsonify({"status": 'error', "msj": "El token no fue activado"})
                        return sendResponse(resp)
                else:
                    resp = jsonify({"status": 'error', "msj": "El token fue utilizado"})
                    return sendResponse(resp)
                                
            else:
                resp = jsonify({"status": 'error', "msj": "El token es inválido"})
                return sendResponse(resp)             
        else:
            resp = jsonify({"status": 'error', "msj": "Debe ingresar un token"})
            return sendResponse(resp)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#Funcion que activa el usuario
def activate_user(token):
    try:
        _token=token
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        afectado=cursor.execute("UPDATE dt_usuarios SET id_status=2 WHERE token=%s",_token)
        conn.commit()
        return True
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@modules.route('/regepassword', methods=['POST'])   
def regenePassword():
    try:
        _json = request.json
        _id = _json['id_usuario']
        _strcorreo = _json['stremail']
        _strusuario = _json['struser']
        _strcontrasena = _json['strpassword']
        _strnombres = _json['strname']
        _strapellidos = _json['strsurname']
        _bt_estatus_id = _json['id_status']
        # validate the received values
        if _strcorreo and _strcontrasena and _id and request.method == 'POST':
            # do not save password as a plain text
            _hashed_password = generate_password_hash(_strcontrasena)
            # save edits
            sql = "UPDATE dt_usuarios SET strcorreo=%s,strcontrasena=%s WHERE id=%s"
            data = (_strcorreo, _hashed_password, _id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify({"status":"success","msj":"El usuario fue actualizado"})
            resp.status_code = 200
            return sendResponse(resp)
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def activate_userRetail(id_empresa):
    try:    
        print("activar usuario")
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        afectado=cursor.execute("UPDATE dt_usuarios SET id_status=2 WHERE id_empresa=%s",id_empresa)
        conn.commit()
        return True
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#Funcion de logout
@modules.route('/logout',methods=['GET'])
def logout(token):
    try:
       
        return afectado
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def addUserRetail(strusuario,strcorreo,strcontrasena,strnombres,id_empresa):
    try:
        _hashed_password = hashlib.md5(strcontrasena.encode())
        sql = "INSERT INTO dt_usuarios(strusuario,strcorreo, strcontrasena, id_rol, strnombres, id_empresa) VALUES(%s, %s, %s,%s,%s, %s)"
        data = (strusuario, strcorreo, _hashed_password.hexdigest(), 3, strnombres,id_empresa)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        resource=cursor.lastrowid
        conn.commit()
        return  resource       
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def addUserManufacturer(strusuario,strcorreo,strcontrasena,strnombres,id_empresa):
    try:
        _hashed_password = hashlib.md5(strcontrasena.encode())
        sql = "INSERT INTO dt_usuarios(strusuario,strcorreo, strcontrasena, id_rol, strnombres, id_empresa) VALUES(%s, %s, %s,%s,%s, %s)"
        data = (strusuario, strcorreo, _hashed_password.hexdigest(), 3, strnombres,id_empresa)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        resource=cursor.lastrowid
        conn.commit()
        return  resource       
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def userBussiness_validate(strusuario):
    try:
        print(strusuario)
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM vw_business_user WHERE strusuario=%s",strusuario)
        row = cursor.fetchone()
        print(row)
        return row
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def search_user(id_empresa):
    try:

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql="SELECT * FROM dt_usuarios WHERE id_empresa=%s"
        cursor.execute(sql,id_empresa)
        row = cursor.fetchone()
        return row
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def deleteUserManufacturer():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dt_usuarios WHERE id_empresa=%s", (id_empresa,))
        conn.commit()
        resp = jsonify({"status":"success","msj":"El usuario fue eliminado"})
        resp.status_code = 200
        return sendResponse(resp)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@modules.route('/state/list') 
def stateList():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM dt_estados ORDER BY id_estado ")
        rows = cursor.fetchall()
        if rows:
            resp = jsonify(rows)            
            resp.status_code = 200
            return sendResponse(resp)
        elif not rows:
            resp = jsonify({"status":'error', "msj":"No se encuentran estados registrados"})
            return sendResponse(resp)      
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@modules.route('/city_municipality/search', methods=['POST'])
def cityMunicipalitySearch():
    try:
        _json= request.get_json(force=True)
        print("municipio")
        print(_json)
        _id_estado = _json['id_estado']
        if not _id_estado:
            resp = jsonify({"status":'error', "msj":"Debe seleccionar un estado"})
            return sendResponse(resp) 

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id_municipio,id_estado, strnombre_municipio FROM dt_municipios WHERE id_estado=%s ORDER BY id_estado,id_municipio ",_id_estado)
        rows1 = cursor.fetchall()

        cursor.execute("SELECT id_ciudad,id_estado,strnombre_ciudad FROM dt_ciudades WHERE id_estado=%s ORDER BY id_estado,id_ciudad ",_id_estado)
        rows2 = cursor.fetchall()
        if rows1 and rows2:
            data= ({'municipios':rows1, 'ciudades':rows2})
            resp = jsonify(data)            
            resp.status_code = 200
            return sendResponse(resp)
        elif not rows:
            resp = jsonify({"status":'error', "msj":"No se encuentran estados municipios y ciudades"})
            return sendResponse(resp)      
    except Exception as e:
        print(e)

@modules.route('/municipality/search', methods=['POST'])
def municipalitySearch():
    try:
        _json= request.get_json(force=True)
        print("municipio")
        print(_json)
        _id_estado = _json['id_estado']
        if not _id_estado:
            resp = jsonify({"status":'error', "msj":"Debe seleccionar un estado"})
            return sendResponse(resp) 

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM dt_municipios WHERE id_estado=%s ORDER BY id_municipio ",_id_estado)
        rows = cursor.fetchall()
        if rows:
            resp = jsonify(rows)            
            resp.status_code = 200
            return sendResponse(resp)
        elif not rows:
            resp = jsonify({"status":'error', "msj":"No se encuentran estados municipios"})
            return sendResponse(resp)      
    except Exception as e:
        print(e)


@modules.route('/city/search', methods=['POST'])
def citySearch():
    try:
        _json= request.get_json(force=True)
        print("city")
        print(_json)
        _id_estado = _json['id_estado']
        if not _id_estado:
            resp = jsonify({"status":'error', "msj":"Debe seleccionar un estado"})
            return sendResponse(resp) 
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM dt_ciudades WHERE id_estado=%s ORDER BY id_estado, id_ciudad ",_id_estado)
        rows = cursor.fetchall()
        if rows:
            resp = jsonify(rows)            
            resp.status_code = 200
            return sendResponse(resp)
        elif not rows:
            resp = jsonify({"status":'error', "msj":"No se encuentran estados registrados"})
            return sendResponse(resp)      
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()