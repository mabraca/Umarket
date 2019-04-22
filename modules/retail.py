from .company import Company
from main import *
import db_config 
from . import modules
import os,time
from werkzeug.utils import secure_filename
#from werkzeug.datastructures import ImmutableMultiDict


@modules.route('/bussiness/register', methods=['POST'])
def registerBussines():
    try:
        retail= Company()        
        """_json= request.get_json(force=True) 
        print(_json)                   
        retail.strnombre_empresa=_json['strname_company']
        retail.strrif_empresa=_json['strrif_company']
        retail.strnombre_representante=_json['strlegal_representative']
        retail.strdireccion = _json['straddress']        
        retail.strcorreo=_json['stremail']
        retail.strtelefono=_json['strphone']
        retail.id_tipo=_json['id_type']"""
        
        print(request.files.getlist("file[]"))
        fileRegistroMercantil= request.files.get('filemerchant_register')
        fileRif= request.files.get('filerif')
        fileCi= request.files.get('fileci')
        fileReciboServicio= request.files.get('filereceipt_services')
        
        print("paso")
        print(request.files)
        #print(fileRegistroMercantil.filename)
        if not  fileRegistroMercantil:
            resp = jsonify({"status":'error', "msj":"Debe adjuntar el registro mercantil"})            
            return sendResponse(resp)
        print(" ")
        print(fileRegistroMercantil)
        #resp = jsonify({"status":'success', "msj":"OK ->"+fileRegistroMercantil.filename})            
        # return sendResponse(resp)

        if  fileRegistroMercantil:      
            if not fileRegistroMercantil.filename.split('.')[1]=='pdf':
                resp = jsonify({"status":'error', "msj":"Debe adjuntar un archivo en formato .pdf"})
                return sendResponse(resp)   
        
        folder_documents=time.strftime("%Y%m%d")
        ruta=app.config['UPLOAD_FOLDER']+folder_documents
        #print(ruta)
        if not os.path.exists(ruta):                 
            os.makedirs(app.config['UPLOAD_FOLDER']+folder_documents)
            path_folder_documents=app.config['UPLOAD_FOLDER']+folder_documents
        else: 
            print("existe 02/05/19")
        
        #print(time.strftime("%Y%m%d"))
        #print(os.path.exists(time.strftime("%Y%m%d")))

        # validate the received values
        if request.method == 'POST':           
            """if not retail.strnombre_empresa:             
                resp = jsonify({"status":'error', "msj":"Debe ingresar un nombre para la empresa"})
                return sendResponse(resp)

            if not retail.strrif_empresa: 
                resp = jsonify({"status":'error', "msj":"Debe ingresar un R.I.F"})
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
                return sendResponse(resp)"""
            
            if  fileRegistroMercantil:            
                if not fileRegistroMercantil.filename.split('.')=='pdf':
                    resp = jsonify({"status":'error', "msj":"El registro mercantil de estar en formato .pdf"})
                    return sendResponse(resp) 
            else:
                resp = jsonify({"status":'error', "msj":"Debe adjuntar el Registro Mercantil"})
                return sendResponse(resp)
            
            if  fileRifs:
                if not fileRifs.filename.split('.')=='pdf':
                    resp = jsonify({"status":'error', "msj":"El R.I.F debe estar en formato .pdf"})
                    return sendResponse(resp) 
            else:
                resp = jsonify({"status":'error', "msj":"Debe adjuntar el R.I.F"})
                return sendResponse(resp)
            
            if  fileCi:
                if not fileCi.filename.slipt('.')=='pdf':
                    resp = jsonify({"status":'error', "msj":"La Cédula de Identidad debe estar en formato .pdf"})
                    return sendResponse(resp) 
            else:
                resp = jsonify({"status":'error', "msj":"Debe adjuntar la Cédula de Identidad"})
                return sendResponse(resp)

            if  fileReciboServicio:
                if not fileReciboServicio.filename.split('.')=='pdf':
                    resp = jsonify({"status":'error', "msj":"El Reccibo de servicios debe estar en formato .pdf"})
                    return sendResponse(resp) 
            else:
                resp = jsonify({"status":'error', "msj":"Debe adjuntar el Recibo de Servicios"})
                return sendResponse(resp)
            
            existe_company=retail.existeCompany(retail.strrif_empresa) 
            existe_email=retail.existeEmail(retail.strcorreo)            
            if  existe_company:
                resp = jsonify({"status":'error', "msj":"El negocio se encuentra registrado"})
                return sendResponse(resp)

            if existe_email:
                resp = jsonify({"status":'error', "msj":"El correo se encuentra registrado"})
                return sendResponse(resp)
            else:
                comercio=retail.registerCompany()
               # print(comercio)
                if comercio:                    
                    retail.id_empresa=comercio['id_empresa']
                    ruta_comercio=path_folder_documents+"-"+folder_documents+retail.id_empresa
                    if not os.path.exists(ruta_comercio):
                        os.makedirs(ruta_comercio)

                    filename_regmercantil="RM_"+secure_filename(fileRegistro_mercantil.filename)+retail.id_empresa
                    fileRegistroMercantil.save(os.path.join(ruta_comercio,filename_regmercantil))          

                    documentosRM=retail.registerDocumentsCompany(ruta_comercio+filename_regmercantil,retail.id_empresa,3)

                    filename_rif="RIF"+secure_filename(fileRif.filename)+retail.id_empresa
                    fileRif.save(os.path.join(ruta_comercio,filename_rif))

                    documentosRIF=retail.registerDocumentsCompany(ruta_comercio+filename_rif,retail.id_empresa,4)

                    filename_ci="CI"+secure_filename(fileCi)+retail.id_empresa
                    fileCi.save(os.path.join(ruta_comercio,filename_ci))

                    documentosCI=retail.registerDocumentsCompany(ruta_comercio+filename_ci,retail.id_empresa,5)

                    filename_rs= "RS"+secure_filename(fileReciboServicio)+retail.id_empresa
                    fileReciboServicio.save(os.path._join(ruta_comercio,filename_rs))

                    documentosRS=retail.registerDocumentsCompany(ruta_comercio+filename_rs,retail.id_empresa,6)

                    if documentosRM and documentosRIF and documentosCI and documentosRS:
                        resp = jsonify({"status":'success', "msj":"El negocio fue registrado"})
                        return sendResponse(resp)
                    else:
                        resp = jsonify({"status":'success', "msj":"El negocio fue registrado"})
                        send_mailCompany(retail.strcorreo,retail.strnombre_empresa)
                        return sendResponse(resp)
                else:
                    resp = jsonify({"status":'error', "msj":"El negocio no fue registrado"})                    
                    return sendResponse(resp)
        else:
            resp = jsonify({"status":'error', "msj":"Debe enviar datos prueba"})                    
            return sendResponse(resp)


    except Exception as e:
        print(e)    