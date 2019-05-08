from .company import Company
from main import *
import db_config 
from . import modules
import os,time
from werkzeug.utils import secure_filename

@modules.route('/bussiness/register', methods=['POST'])
def registerBussines():
    try:
        print("entro en /bussiness/register ")
        retail= Company() #Instancia  
        print("paso instancia")   
        _json=json.loads(request.values['data'])
        print(_json)      
        print(request.values)
        print(request.files)    
        print("asignacion de propiedades")         
        print(_json['strname_company'])
        retail.strnombre_empresa=str(_json['strname_company'])
        retail.strrif_empresa=str(_json['strrif_company'])
        retail.strnombre_representante=str(_json['strlegal_representative'])
        retail.strdireccion =str(_json['straddress'])
        retail.strcorreo=str(_json['stremail'])
        retail.strtelefono=str(_json['strphone'])
        retail.id_tipo=_json['id_type']
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

                    #resp = jsonify({"status":'success', "msj":"El negocio fue registrado con éxito","id_empresa":retail.id_empresa})
                    #return sendResponse(resp)
                    print("files abajo")
                    send_mailCompany(retail.strcorreo,retail.strnombre_empresa)  
                    #print(resp)                
                    #return sendResponse(resp)  
                    print(request.files)  
                    if request.files:
                        print("request.files")
                        fileRegistroMercantil=request.files['file[0]']
                        fileRif=request.files['file[1]']
                        fileCi=request.files['file[2]']
                        fileReciboServicio=request.files['file[3]']                    
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

                        if  fileReciboServicio:
                            if not fileReciboServicio.filename.split('.')[1]=='pdf':
                                resp = jsonify({"status":'error', "msj":"El Reccibo de servicios debe estar en formato .pdf"})
                                return sendResponse(resp) 
                        else:
                            resp = jsonify({"status":'error', "msj":"Debe adjuntar el Recibo de Servicios"})
                            return sendResponse(resp)    

                        ruta_comercio=path_folder_documents+"/"+folder_documents+"-"+str(retail.id_empresa)
                        
                        if not os.path.exists(ruta_comercio):
                            print("crear carpeta")
                            os.makedirs(ruta_comercio)                    
                        else:
                            print("existe carpeta")               
                    else:
                        resp = jsonify({"status":'error', "msj":"Debe adjuntar los archivos del comercio"})                    
                        return sendResponse(resp)

                    #Guardado de los archivos en el servidor y el registro de la ruta en base de datos
                    filename_regmercantil="RM_"+str(retail.id_empresa)+"."+secure_filename(fileRegistroMercantil.filename)
                    fileRegistroMercantil.save(os.path.join(ruta_comercio,filename_regmercantil))          
                    print(filename_regmercantil)
                    urlArchivoRm=str(ruta_comercio+"/"+filename_regmercantil)
                    print(retail.id_empresa)
                    documentosRM=retail.registerDocumentsCompany(urlArchivoRm,retail.id_empresa,3)

                    filename_rif="RIF_"+str(retail.id_empresa)+"."+secure_filename(fileRif.filename)
                    fileRif.save(os.path.join(ruta_comercio,filename_rif))
                    print(filename_rif)
                    urlArchivoRif=str(ruta_comercio+"/"+filename_rif)
                    documentosRIF=retail.registerDocumentsCompany(urlArchivoRif,retail.id_empresa,4)

                    filename_ci="CI_"+str(retail.id_empresa)+"."+secure_filename(fileCi.filename)
                    fileCi.save(os.path.join(ruta_comercio,filename_ci))
                    print(filename_ci)
                    urlArchivoCi=str(ruta_comercio+"/"+filename_ci)
                    documentosCI=retail.registerDocumentsCompany(urlArchivoCi,retail.id_empresa,5)

                    filename_rs= "RS_"+str(retail.id_empresa)+"."+secure_filename(fileReciboServicio.filename)
                    fileReciboServicio.save(os.path.join(ruta_comercio,filename_rs))
                    print(filename_rs+"recibo servicios")
                    urlArchivoRs=str(ruta_comercio+"/"+filename_rs)
                    documentosRS=retail.registerDocumentsCompany(urlArchivoRs,retail.id_empresa,6)    

                    if documentosRM and documentosRIF and documentosCI and documentosRS:
                        resp = jsonify({"status":'success', "msj":"El comercio fue registrado con éxito"})
                        return sendResponse(resp)                                        
                    else:
                        resp = jsonify({"status":'error', "msj":"El comercio no fue registrado"})                    
                        return sendResponse(resp)
        else:
            resp = jsonify({"status":'error', "msj":"Debe enviar datos"})                    
            return sendResponse(resp)
    except Exception as e:
        print(e)    



@modules.route('/bussiness/preaffiliated', methods=['GET'])
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