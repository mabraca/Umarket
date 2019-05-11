from .company import Company
from main import *
import db_config 
from . import modules
import os,time
from werkzeug.utils import secure_filename

@modules.route('/manufacturer/register', methods=['POST'])
def registerManufacturer():
    try:
        print("entro en /manufacturer/register ")
        manufacturer= Company() #Instancia  
        print("paso instancia")   
        _json=json.loads(request.values['data'])
        print(_json)      
        print(request.values)
        print(request.files)    
        print("asignacion de propiedades")         
        print(_json['strname_company'])
        manufacturer.strnombre_empresa=str(_json['strname_company'])
        manufacturer.strrif_empresa=str(_json['strrif_company'])
        manufacturer.strnombre_representante=str(_json['strlegal_representative'])
        manufacturer.strdireccion =str(_json['straddress'])
        manufacturer.strcorreo=str(_json['stremail'])
        manufacturer.strtelefono=str(_json['strphone'])
        manufacturer.id_tipo=_json['id_type']
        manufacturer.blnafiliacion=_json['validated']
        strcuenta=_json['strcuenta']
        if not _json['id_type']==1:
            resp = jsonify({"status":'error', "msj":"El tipo de empresa debe ser Fabricante"})
            return sendResponse(resp)
        print("antes de validar")
        # validate the received values
        if request.method == 'POST':     
            print("entró en validacion post")
            if not manufacturer.strnombre_empresa:             
                resp = jsonify({"status":'error', "msj":"Debe ingresar un nombre para la empresa"})
                return sendResponse(resp)

            if not manufacturer.strrif_empresa or manufacturer.strrif_empresa=='None': 
                resp = jsonify({"status":'error', "msj":"Debe ingresar un R.I.F"})
                return sendResponse(resp)

            if not(len(manufacturer.strrif_empresa)==11):
                resp = jsonify({"status":'error', "msj":"Debe ingresar un R.I.F válido"})
                return sendResponse(resp)
            
            if not manufacturer.strnombre_representante:
                resp = jsonify({"status":"error","msj":"Debe ingresar el nombre del representante legal"})
                return sendResponse(resp)

            if not manufacturer.strdireccion:
                resp = jsonify({"status":'error', "msj":"Debe ingresar una dirección"})
                return sendResponse(resp)
            
            if not manufacturer.strcorreo:
                resp = jsonify({"status":'error', "msj":"Debe ingresar un correo electrónico"})
                return sendResponse(resp)
            
            if not manufacturer.strtelefono:
                resp = jsonify({"status":'error', "msj":"Debe ingresar un número telefónico"})
                return sendResponse(resp)
            
            if not manufacturer.id_tipo:
                resp = jsonify({"status":'error', "msj":"Debe ingresar tipo empresa"})
                return sendResponse(resp)
            if not strcuenta:
                resp = jsonify({"status":'error', "msj":"Debe ingresar tipo empresa"})
                return sendResponse(resp)
            else:
                if len(strcuenta)<20 :
                    resp = jsonify({"status":'error', "msj":"Debe ingresar una cuenta de 20"})
                    return sendResponse(resp)

            print("antes de validar company")
            
            print(manufacturer.strrif_empresa)                    
            existe_company=manufacturer.existeCompany() 
            existe_email=manufacturer.existeEmail(manufacturer.strcorreo)
                        
            if  existe_company:
                resp = jsonify({"status":'error', "msj":"El fabricante se encuentra registrado"})
                return sendResponse(resp)

            if existe_email:
                resp = jsonify({"status":'error', "msj":"El correo se encuentra registrado"})
                return sendResponse(resp)
            else:
                fabricante=manufacturer.registerCompany()
                if fabricante:     
                    print("registro")                                
                    manufacturer.id_empresa=fabricante
                    print("files")                   
                    if request.files:
                        print("request.files")
                        fileRegistroMercantil=request.files['file[0]']
                        fileRif=request.files['file[1]']
                        fileCi=request.files['file[2]']
                        #fileReciboServicio=request.files['file[3]']                    
                        #Creación de la carpeta 
                        folder_documents=time.strftime("%Y-%m-%d")
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

                        """if  fileReciboServicio:
                            if not fileReciboServicio.filename.split('.')[1]=='pdf':
                                resp = jsonify({"status":'error', "msj":"El Reccibo de servicios debe estar en formato .pdf"})
                                return sendResponse(resp) 
                        else:
                            resp = jsonify({"status":'error', "msj":"Debe adjuntar el Recibo de Servicios"})
                            return sendResponse(resp) """   

                        ruta_fabricante=path_folder_documents+"/"+manufacturer.strrif_empresa
                        
                        if not os.path.exists(ruta_fabricante):
                            print("crear carpeta")
                            os.makedirs(ruta_fabricante)                    
                        else:
                            print("existe carpeta")               
                    else:
                        resp = jsonify({"status":'error', "msj":"Debe adjuntar los archivos del fabricante"})                    
                        return sendResponse(resp)

                    #Guardado de los archivos en el servidor y el registro de la ruta en base de datos
                    filename_regmercantil="RM_"+secure_filename(fileRegistroMercantil.filename)
                    fileRegistroMercantil.save(os.path.join(ruta_fabricante,filename_regmercantil))          
                    print(filename_regmercantil)
                    urlArchivoRm=str(ruta_fabricante+"/"+filename_regmercantil)
                    print(manufacturer.id_empresa)
                    #documentosRM=manufacturer.registerDocumentsCompany(urlArchivoRm,manufacturer.id_empresa,3)

                    filename_rif="RIF_"+secure_filename(fileRif.filename)
                    fileRif.save(os.path.join(ruta_fabricante,filename_rif))
                    print(filename_rif)
                    urlArchivoRif=str(ruta_fabricante+"/"+filename_rif)
                    #documentosRIF=manufacturer.registerDocumentsCompany(urlArchivoRif,manufacturer.id_empresa,4)

                    filename_ci="CI_"+secure_filename(fileCi.filename)
                    fileCi.save(os.path.join(ruta_fabricante,filename_ci))
                    print(filename_ci)
                    urlArchivoCi=str(ruta_fabricante+"/"+filename_ci)
                    documentos_guardados=manufacturer.registerDocumentsCompany(ruta_fabricante,manufacturer.id_empresa,folder_documents)

                    if documentos_guardados:
                        if manufacturer.blnafiliacion==True:
                            print("afiliacion true")
                            print("afiliacion->"+str(manufacturer.blnafiliacion))
                            user_manufacturer=search_user(manufacturer.id_empresa)
                            codigoAcceso=manufacturer.generateAccessCode(manufacturer.id_empresa,user_manufacturer['strusuario'])
                          
                            #adduser_manufacturer=addUserManufacturer(strusuario,retail.strcorreo,strcontrasena,retail.strnombre_representante,retail.id_empresa)
                            if user_manufacturer:
                                print("se envio correo de afiliacion")
                                #send_mailCompanyCode(manufacturer.strcorreo,manufacturer.strnombre_empresa,codigoAcceso)  

                                #Envío de correo usando hilos
                                @copy_current_request_context
                                def send_message(strcorreo,strnombre_empresa,codigoAcceso,strusuario):
                                    send_mailCompanyCode(strcorreo,strnombre_empresa,codigoAcceso,strusuario)

                                sender= threading.Thread(name='mail_sender',target=send_message, args=(manufacturer.strcorreo,manufacturer.strnombre_empresa,codigoAcceso,user_manufacturer['strusuario']))
                                sender.start()                      
                                resp = jsonify({"status":'success', "msj":"El Fabricante fue registrado con éxito"})
                                return sendResponse(resp)
                            else:
                                resp = jsonify({"status":'success', "msj":"El Fabricante no fue registrado"})
                                return sendResponse(resp)
                        else:
                            datos_bancarios=manufacturer.registerDataBank(manufacturer.id_empresa,strcuenta)
                            if datos_bancarios:
                                print("se envio correo de preafilicion")
                                #send_mailCompany(manufacturer.strcorreo,manufacturer.strnombre_empresa)  
                                @copy_current_request_context
                                def send_message(strcorreo,strnombre_empresa):
                                    send_mailCompany(strcorreo,strnombre_empresa)

                                sender= threading.Thread(name='mail_sender',target=send_message, args=(manufacturer.strcorreo,manufacturer.strnombre_empresa))
                                sender.start()  

                                resp = jsonify({"status":'success', "msj":"El Fabricante fue pre-afiliado con éxito"})
                                return sendResponse(resp)
                            else:
                                manufacturerDelDoc=manufacturer.deleteDocuments()
                                if manufacturerDelDoc:
                                    manufacturerDel=manufacturer.deleteCompany()
                                if manufacturerDel:
                                    deleteUserRetail=deleteUserManufacturer(manufacturer.id_empresa)
                                if deleteUserRetail:
                                    resp = jsonify({"status":'error', "msj":"El Fabricante no fue preafiliado"})                    
                                    return sendResponse(resp)
                    else:
                        manufacturerDelDoc=manufacturer.deleteDocuments()
                        if manufacturerDelDoc:
                            manufacturerDel=manufacturer.deleteCompany()
                        if manufacturerDel:
                            deleteUserRetail=deleteUserManufacturer(manufacturer.id_empresa)
                        if deleteUserRetail:
                            resp = jsonify({"status":'error', "msj":"El Fabricante no fue preafiliado"})                    
                            return sendResponse(resp)                              
        else:
            resp = jsonify({"status":'error', "msj":"Debe enviar datos"})                    
            return sendResponse(resp)
    except Exception as e:
        print(e)   

@modules.route('/manufacturer/list', methods=['GET'])
def manufacturerList():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM  vw_company WHERE id_tipo_empresa=1 ORDER BY id_empresa, dtmfecha_creacion ")
        row = cursor.fetchall()
        if row:
            resp = jsonify(row)            
            resp.status_code = 200
            return sendResponse(resp)
        elif not row:
            resp = jsonify({"status":'warning', "msj":"No se encuentran fabricantes"})
            return sendResponse(resp)    
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@modules.route('/manufacturer/validated', methods=['POST'])
def manufacturerValidate():
    try:
        if request.method == 'POST':   
            manufacturer= Company() #Instancia  
            print("paso instancia")   
            _json= request.get_json(force=True)
            _id_empresa=_json['id_empresa']            
            if not _id_empresa:
                resp = jsonify({"status":'error', "msj":"De seleccionar un Fabricante"})
                return sendResponse(resp)  
            existe_manufacturer=manufacturer.companyView(_id_empresa) 
            print("existe->"+str(existe_manufacturer))
            if existe_manufacturer==None:
                resp = jsonify({"status":'error', "msj":"El Fabricante no existe"})
                return sendResponse(resp)  
            else:
                _id_tipo_empresa=existe_manufacturer['id_tipo']
                if existe_manufacturer['id_status']==3:
                    if _id_tipo_empresa==1:
                        validar=manufacturer.validateCompany(_id_empresa,_id_tipo_empresa)
                    else:
                        resp = jsonify({"status":'error', "msj":"La empresa debe ser de tipo Fabricante"})
                        return sendResponse(resp)  
                else:
                    resp = jsonify({"status":'error', "msj":"El fabricate ya fue validado"})
                    return sendResponse(resp)  
            if validar:
                usuario_fabricante=search_user(id_empresa)
                codigoAcceso=manufacturer.generateAccessCode(_id_empresa,usuario_fabricante['strusuario'])
                if usuario_fabricante:
                    send_mailCompanyCode(existe_manufacturer['strcorreo'],existe_manufacturer['strnombre_empresa'],codigoAcceso)

                    #Envío de correo usando hilos
                    @copy_current_request_context
                    def send_message(strcorreo,strnombre_empresa,codigoAcceso,strusuario):
                        send_mailCompanyCode(strcorreo,strnombre_empresa,codigoAcceso,strusuario)
                    
                    sender= threading.Thread(name='mail_sender',target=send_message, args=(existe_manufacturer['strcorreo'],existe_manufacturer['strnombre_empresa'],codigoAcceso,usuario_fabricante['strusuario']))
                    sender.start()       

                    resp = jsonify({"status":'success', "msj":"El fabricante fue validado con éxito"})
                    return sendResponse(resp)
            else:
                resp = jsonify({"status":'error', "msj":"El fabricante no pudo ser validado"})
                return sendResponse(resp)          
        else:
            resp = jsonify({"status":'warning', "msj":"De seleccionar un Fabricante"})
            return sendResponse(resp)   
    except Exception as e:
        print(e)

@modules.route('/manufacturer/preaffiliated', methods=['GET'])
def manufacturerPreaffiliated():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM  vw_company WHERE id_status=3 AND id_tipo_empresa=1 ORDER BY id_empresa, dtmfecha_creacion ")
        row = cursor.fetchone()
        if row:
            resp = jsonify(row)            
            resp.status_code = 200
            return sendResponse(resp)
        elif not row:
            resp = jsonify({"status":'warning', "msj":"No se encuentran fabricantes pre-afiliados"})
            return sendResponse(resp)    
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@modules.route('/manufacturer/documents', methods=['POST'])
def manufacturerDocuments():
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

@modules.route('/manufacturer/access', methods=['POST'])
def manufacturerAccess():
    try:        
        if request.method== 'POST':
            _json= request.get_json(force=True)
            print(_json)
            _strcodigo_acceso = _json['straccess_code']
            if _strcodigo_acceso and  request.method == 'POST':            
                    existe_manufacturer=validateCode(_strcodigo_acceso)
                    if existe_manufacturer:
                        if existe_manufacturer['id_status']==4:                        
                                caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits
                                longitud = 32  # La longitud que queremos
                                _token = ''.join(random.choice(caracteres) for _ in range(longitud))
                                resp = jsonify({"status":"success", "msj":"El fabricante logeado","strnombre_empresa":existe_manufacturer['strnombre_empresa'],"strrif_empresa":existe_manufacturer['strrif_empresa'],"strnombre_representante":existe_manufacturer['strnombre_representante'],"stremail":existe_manufacturer['strcorreo'],"id_tipo_empresa":existe_manufacturer['id_tipo_empresa'],"token":_token})                                                      
                                resp.status_code = 200
                                return sendResponse(resp)                                      
                        else:
                            resp = jsonify({"status": 'warning', "msj": "El fabricante esta inactivo"})
                            return sendResponse(resp)
                    else:
                        resp = jsonify({"status": 'error', "msj": "El fabricante no existe"})
                        return sendResponse(resp)
            else:
                resp = jsonify({"status":"error", "msj": "Debe ingresar un código de acceso"})
                return sendResponse(resp)
        else:
            resp = jsonify({"status":"error", "msj": "Acceso denegado"})
            return sendResponse(resp)
    except Exception as e:
        print(e)

def validateCode(strcodigo_acceso):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM  vw_company WHERE id_status=4 AND id_tipo_empresa=1 AND strcodigo_acceso=%s",strcodigo_acceso)
        row = cursor.fetchone()
        return row
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


"""
@modules.route('/manufacturer/documents/download', methods=['POST'])
def manufacturerDocumentsSend():
    try:
        pass
    except expression as identifier:
        pass
    finally:
        pass"""