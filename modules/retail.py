from .company import Company
from main import *
import db_config 
from . import modules
import os,time
from werkzeug.utils import secure_filename
from .moduser import *

@modules.route('/business/register', methods=['POST'])
def bussinesRegister():
    try:
        print("entro en /bussiness/register ")
        retail= Company() #Instancia   
        _json=json.loads(request.values['data'])
        print(_json)      
        retail.strnombre_empresa=str(_json['strname_company'])
        retail.strrif_empresa=str(_json['strrif_company'])
        retail.strnombre_representante=str(_json['strlegal_representative'])
        retail.strdireccion =str(_json['straddress'])
        strusuario=str(_json['struser'])
        retail.strcorreo=str(_json['stremail'])
        retail.strtelefono=str(_json['strphone'])
        retail.id_tipo=_json['id_type']

        if not _json['id_type']==2:
            resp = jsonify({"status":'error', "msj":"El tipo de empresa debe ser Comercio"})
            return sendResponse(resp)
        strcontrasena=_json['strpassword']
        strverifcontrasena=_json['verifpassword']

        print("antes de validar")
        # validate the received values
        if request.method == 'POST':     
            print("entró en validacion post")
            if not retail.strnombre_empresa:             
                resp = jsonify({"status":'error', "msj":"Debe ingresar un nombre para la empresa"})
                return sendResponse(resp)

            if not retail.strrif_empresa or retail.strrif_empresa=='None': 
                resp = jsonify({"status":'error', "msj":"Debe ingresar un R.I.F"})
                return sendResponse(resp)
            if not(len(retail.strrif_empresa)==11):
                resp = jsonify({"status":'error', "msj":"Debe ingresar un R.I.F válido"})
                return sendResponse(resp)
            
            if not retail.strnombre_representante:
                resp = jsonify({"status":"error","msj":"Debe ingresar el nombre del representante legal"})
                return sendResponse(resp)

            if not retail.strdireccion:
                resp = jsonify({"status":'error', "msj":"Debe ingresar una dirección"})
                return sendResponse(resp)
            
            if not retail.strcorreo:
                resp = jsonify({"status":'error', "msj":"Debe ingresar un correo electrónico"})
                return sendResponse(resp)
            
            if not retail.strtelefono:
                resp = jsonify({"status":'error', "msj":"Debe ingresar un número telefónico"})
                return sendResponse(resp)
            
            if not retail.id_tipo:
                resp = jsonify({"status":'error', "msj":"Debe ingresar tipo empresa"})
                return sendResponse(resp)
            print("antes de validar company")
            
            if not strcontrasena==strverifcontrasena:
                resp = jsonify({"status":'error', "msj":"Las contraseñas no coinciden"})
                return sendResponse(resp)

            print(retail.strrif_empresa)                    
            existe_company=retail.existeCompany() 
            existe_email=retail.existeEmail(retail.strcorreo)
                        
            if  existe_company:
                resp = jsonify({"status":'error', "msj":"El negocio se encuentra registrado"})
                return sendResponse(resp)

            if existe_email:
                resp = jsonify({"status":'error', "msj":"El correo se encuentra registrado"})
                return sendResponse(resp)
            else:
                comercio=retail.registerCompany()
                if comercio:     
                    print("registro")                                
                    retail.id_empresa=comercio
                    print("files abajo")
                    
                    print(request.files)  
                    if request.files:
                        print("request.files")
                        fileRegistroMercantil=request.files['file[0]']
                        fileRif=request.files['file[1]']
                        fileCi=request.files['file[2]']
                        #fileReciboServicio=request.files['file[3]']                    
                        #Creación de la carpeta 
                        folder_documents=time.strftime("%Y%m%d")
                        ruta=app.config['UPLOAD_FOLDER']+folder_documents
                        if not os.path.exists(ruta):  #Si la carpeta no existe la crea de lo contrario usa la del día               
                            os.makedirs(app.config['UPLOAD_FOLDER']+folder_documents)
                            path_folder_documents=app.config['UPLOAD_FOLDER']+folder_documents
                        else: 
                            path_folder_documents=ruta
                        
                        if  fileRegistroMercantil:            
                            if not fileRegistroMercantil.filename.split('.')[1]=='pdf':
                                resp = jsonify({"status":'error', "msj":"El registro mercantil de estar en formato .pdf"})
                                return sendResponse(resp) 
                        else:
                            resp = jsonify({"status":'error', "msj":"Debe adjuntar el Registro Mercantil"})
                            return sendResponse(resp)            
                        
                        if  fileRif:
                            if not fileRif.filename.split('.')[1]=='pdf':
                                resp = jsonify({"status":'error', "msj":"El R.I.F debe estar en formato .pdf"})
                                return sendResponse(resp) 
                        else:
                            resp = jsonify({"status":'error', "msj":"Debe adjuntar el R.I.F"})
                            return sendResponse(resp)            

                        if  fileCi:
                            if not fileCi.filename.split('.')[1]=='pdf':
                                resp = jsonify({"status":'error', "msj":"La Cédula de Identidad debe estar en formato .pdf"})
                                return sendResponse(resp) 
                        else:
                            resp = jsonify({"status":'error', "msj":"Debe adjuntar la Cédula de Identidad"})
                            return sendResponse(resp)             

                        ruta_comercio=path_folder_documents+"/"+str(retail.strrif_empresa)
                        
                        if not os.path.exists(ruta_comercio):
                            print("crear carpeta")
                            os.makedirs(ruta_comercio)                    
                        else:
                            print("existe carpeta")               
                    else:
                        retailDel=retail.deleteCompany()
                        if retailDel:
                            resp = jsonify({"status":'error', "msj":"El comercio no fue registrado"})                    
                            return sendResponse(resp)

                    #Guardado de los archivos en el servidor y el registro de la ruta en base de datos
                    filename_regmercantil="RM_"+secure_filename(fileRegistroMercantil.filename)
                    fileRegistroMercantil.save(os.path.join(ruta_comercio,filename_regmercantil))          
                    print(filename_regmercantil)
                    urlArchivoRm=str(ruta_comercio+"/"+filename_regmercantil)
                    print(retail.id_empresa)
                    #documentosRM=retail.registerDocumentsCompany(urlArchivoRm,retail.id_empresa,3)

                    filename_rif="RIF_"+secure_filename(fileRif.filename)
                    fileRif.save(os.path.join(ruta_comercio,filename_rif))
                    print(filename_rif)
                    urlArchivoRif=str(ruta_comercio+"/"+filename_rif)
                    #documentosRIF=retail.registerDocumentsCompany(urlArchivoRif,retail.id_empresa,4)

                    filename_ci="CI_"+secure_filename(fileCi.filename)
                    fileCi.save(os.path.join(ruta_comercio,filename_ci))
                    print(filename_ci)
                    urlArchivoCi=str(ruta_comercio+"/"+filename_ci)
                    datfecha=time.strftime("%Y-%m-%d")
                    print(datfecha,retail.id_empresa,ruta_comercio)
                    documentos_guardados=retail.registerDocumentsCompany(ruta_comercio,retail.id_empresa,datfecha)

                    """filename_rs= "RS_"+str(retail.id_empresa)+"."+secure_filename(fileReciboServicio.filename)
                    fileReciboServicio.save(os.path.join(ruta_comercio,filename_rs))
                    print(filename_rs+"recibo servicios")
                    urlArchivoRs=str(ruta_comercio+"/"+filename_rs)
                    documentosRS=retail.registerDocumentsCompany(urlArchivoRs,retail.id_empresa,6)"""    
                    

                    if documentos_guardados:
                        adduser_retail=addUserRetail(strusuario,retail.strcorreo,strcontrasena,retail.strnombre_representante,retail.id_empresa)
                        if adduser_retail:
                            #send_mailCompany(retail.strcorreo,retail.strnombre_empresa)
                            @copy_current_request_context
                            def send_message(strcorreo,strnombre_empresa):
                                send_mailCompany(strcorreo,strnombre_empresa)

                            sender= threading.Thread(name='mail_sender',target=send_message, args=(retail.strcorreo,retail.strnombre_empresa))
                            sender.start()  
                            resp = jsonify({"status":'success', "msj":"El comercio fue preafiliado con éxito"})
                            return sendResponse(resp) 
                        else:
                            retailDelDoc=retail.deleteDocuments()
                            if retailDelDoc:
                                retailDel=retail.deleteCompany()
                                if retailDel:
                                    resp = jsonify({"status":'error', "msj":"El comercio no fue preafiliado"})                    
                                    return sendResponse(resp)   
                    else:
                        retailDelDoc=retail.deleteDocuments()
                        if retailDelDoc:
                            retailDel=retail.deleteCompany()
                            if retailDel:
                                resp = jsonify({"status":'error', "msj":"El comercio no fue preafiliado"})                    
                                return sendResponse(resp)                                   
                else:
                    resp = jsonify({"status":'error', "msj":"El comercio no fue registrado"})                    
                    return sendResponse(resp)
        else:
            resp = jsonify({"status":'error', "msj":"Debe enviar datos"})                    
            return sendResponse(resp)
    except Exception as e:
        print(e)    

@modules.route('/business/preaffiliated', methods=['GET'])
def retailPreaffiliated():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM  vw_company WHERE  id_tipo_empresa=2 ORDER BY id_empresa, dtmfecha_creacion ")
        row = cursor.fetchall()
        if row:
            resp = jsonify(row)            
            resp.status_code = 200
            return sendResponse(resp)
        elif not row:
            resp = jsonify({"status":'warning', "msj":"No se encuentran comercios pre-afiliados"})
            return sendResponse(resp)    
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@modules.route('/business/list', methods=['GET'])
def retailList():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM  vw_company WHERE id_tipo_empresa=2 ORDER BY id_empresa, dtmfecha_creacion ")
        row = cursor.fetchall()
        if row:
            resp = jsonify(row)            
            resp.status_code = 200
            return sendResponse(resp)
        elif not row:
            resp = jsonify({"status":'warning', "msj":"No se encuentran comercios"})
            return sendResponse(resp)    
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@modules.route('/business/validated', methods=['POST'])
def retailValidated():
    try:
        if request.method == 'POST':   
            retail= Company() #Instancia  
            print("paso instancia")   
            _json= request.get_json(force=True)
            _id_empresa=_json['id_empresa']            
            if not _id_empresa:
                resp = jsonify({"status":'error', "msj":"De seleccionar un Comercio"})
                return sendResponse(resp)  
            existe_retail=retail.companyView(_id_empresa) 
            print("existe->"+str(existe_retail))
            if existe_retail==None:
                resp = jsonify({"status":'error', "msj":"El Comercio no existe"})
                return sendResponse(resp)  
            else:
                _id_tipo_empresa=existe_retail['id_tipo_empresa']
                if existe_retail['id_status']==3:
                    if _id_tipo_empresa==2:
                        print("entro en validar")
                        validar=retail.validateCompany(_id_empresa,_id_tipo_empresa)
                        activarUser=activate_userRetail(_id_empresa)                    
                    else:
                        resp = jsonify({"status":'error', "msj":"La empresa debe ser de tipo Comercio"})
                        return sendResponse(resp)  
                else:
                    resp = jsonify({"status":'warning', "msj":"El comercio ya fue validado"})
                    return sendResponse(resp)  

            if validar:                
                if activarUser:
                    print("envio de correo  activacion")
                    #send_mailCompanyActivation(existe_retail['strcorreo'],existe_retail['strnombre_empresa'])
                    #Envío de correo usando hilos
                    @copy_current_request_context
                    def send_message(strcorreo,strnombre_empresa):
                        send_mailCompanyActivation(strcorreo,strnombre_empresa)

                    sender= threading.Thread(name='mail_sender',target=send_message, args=(existe_retail['strcorreo'],existe_retail['strnombre_empresa']))
                    sender.start()

                    resp = jsonify({"status":'success', "msj":"El comercio fue validado con éxito"})
                    return sendResponse(resp)
            else:
                resp = jsonify({"status":'error', "msj":"El comercio no pudo ser validado"})
                return sendResponse(resp)          
        else:
            resp = jsonify({"status":'warning', "msj":"De seleccionar un Comercio   "})
            return sendResponse(resp)   
    except Exception as e:
        print(e)


@modules.route('/business/login', methods=['POST'])
def bussinessLogin():
    try:             
        _json= request.get_json(force=True)
        print(_json)
        _strusuario = _json['struser']
        _strcontrasena = _json['strpassword']
        if _strusuario and  request.method == 'POST':
            if _strcontrasena:
                existe_user=userBussiness_validate(_strusuario)
                _hashed_password = hashlib.md5(_strcontrasena.encode())
                if existe_user:
                    print("existe user")
                    print(existe_user)
                    if existe_user['id_status_user']==2 and existe_user['id_empresa']:
                        if (existe_user['strcontrasena']==_hashed_password.hexdigest()):
                            caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits
                            longitud = 32  # La longitud que queremos
                            _token = ''.join(random.choice(caracteres) for _ in range(longitud))
                            resp = jsonify({"status":"success", "msj":"El usuario logeado","stremail":existe_user['strcorreo'], "strname":existe_user['strnombres'], "strsurname":existe_user['strapellidos'],"id_rol":existe_user['id_rol'],"id_empresa":existe_user['id_empresa'],"strnombre_empresa":existe_user['strnombre_empresa'], "id_tipo_empresa":existe_user['id_tipo_empresa'],"strrif_empresa":existe_user['strrif_empresa'],"strtelefono":existe_user['strtelefono'],"strdireccion":existe_user['strdireccion'],"token":_token})                                                      
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
    
@modules.route('/business/files', methods=['POST'])
def businessFiles():
    try:
        if request.method=='POST':
            _json= request.get_json(force=True)
            _id_empresa=_json['id_empresa']
            if _id_empresa:
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                cursor.execute("SELECT * FROM  vw_documents_company WHERE id_empresa=%s",_id_empresa)
                row = cursor.fetchall()
                if row:
                    resp = jsonify(row)            
                    resp.status_code = 200
                    return sendResponse(resp)
                elif not row:
                    resp = jsonify({"status":'warning', "msj":"El fabricante no posee documentos"})
                    return sendResponse(resp)    
            else:
                resp = jsonify({"status":'error', "msj":"Debe seleccionar un fabricante"})
                return sendResponse(resp)  
        else:
            resp = jsonify({"status":'error', "msj":"Debe enviar datos"})
            return sendResponse(resp)  
    except Exception as e:
        print(e)
    finally:
        if _id_empresa:
            cursor.close()
            conn.close()
    

@modules.route('/business/update', methods=['POST'])
def businessUpdate():
    try:
        if request.method == 'POST':   
            retail= Company() #Instancia  

            print("paso instancia")   
            _json= request.get_json(force=True)
            print(_json)
            _id_empresa=_json['id_empresa']   
            _nombre_campo=_json['nombre_campo']         
            _valor_campo=_json['valor_campo']

            if not _id_empresa:
                resp = jsonify({"status":'error', "msj":"Debe enviar el id del Comercio"})
                return sendResponse(resp)  
            
            if not _nombre_campo:
                resp = jsonify({"status":'error', "msj":"No puede enviar el nombre del campos vacio"})
                return sendResponse(resp)  
            
            if not _valor_campo:
                resp = jsonify({"status":'error', "msj":"No puede enviar el valor del campo vacio"})
                return sendResponse(resp)  

            existe_retail=retail.companyView(_id_empresa) 
            print("existe->"+str(existe_retail))
            if existe_retail==None:
                resp = jsonify({"status":'error', "msj":"El Comercio no existe"})
                return sendResponse(resp)  
            else:
                _id_tipo_empresa=existe_retail['id_tipo_empresa']
               
                if _id_tipo_empresa==2:
                    print("Actualizar retail")
                    update_retail=retail.updateCompany(_nombre_campo,_valor_campo,_id_empresa)                        
                else:
                    resp = jsonify({"status":'error', "msj":"La empresa debe ser de tipo Comercio"})
                    return sendResponse(resp)  

            if update_retail:                                     
                    resp = jsonify({"status":'success', "msj":"El comercio fue actualizado con éxito"})
                    return sendResponse(resp)
            else:
                resp = jsonify({"status":'error', "msj":"El comercio no pudo ser actualizado"})
                return sendResponse(resp)          
        else:
            resp = jsonify({"status":'warning', "msj":"De seleccionar un Comercio"})
            return sendResponse(resp)   
    except Exception as e:
        print(e)


@modules.route('/business/query', methods=['POST'])
def retailQuery():
    try:
        retail= Company() #Instancia  

        if request.method=='POST':
            _json= request.get_json(force=True)
            _id_empresa=_json['id_empresa']
            existe_retail=retail.companyView(_id_empresa)
            
            if existe_retail:
                if existe_retail['id_tipo_empresa']==2:
                    resp = jsonify(existe_retail)            
                    resp.status_code = 200
                    return sendResponse(resp)
                else:
                    resp = jsonify({"status":'warning', "msj":"La empresa de ser tipo comercio"})
                    return sendResponse(resp)
            else:
                resp = jsonify({"status":'warning', "msj":"El comercio no existe"})
                return sendResponse(resp)    
    except Exception as e:
        print(e)
   