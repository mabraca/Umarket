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
        print("entro")   
        """_json= request.get_json(force=True) 
        print(_json)                   
        retail.strnombre_empresa=_json['strname_company']
        retail.strrif_empresa=_json['strrif_company']
        retail.strnombre_representante=_json['strlegal_representative']
        retail.strdireccion = _json['straddress']        
        retail.strcorreo=_json['stremail']
        retail.strtelefono=_json['strphone']
        retail.id_tipo=_json['id_type']"""
       
        print(request.files)       
        fileRegistroMercantil=request.files['file[0]']
        fileRif=request.files['file[1]']
        fileCi=request.files['file[2]']
        fileReciboServicio=request.files['file[3]']        

        print(fileRegistroMercantil.filename.split('.')[1])
        
        folder_documents=time.strftime("%Y%m%d")
        ruta=app.config['UPLOAD_FOLDER']+folder_documents

        if not os.path.exists(ruta):                 
            os.makedirs(app.config['UPLOAD_FOLDER']+folder_documents)
            path_folder_documents=app.config['UPLOAD_FOLDER']+folder_documents

        else: 
            path_folder_documents=ruta
            print("existe 02/05/19")
        


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
                if not fileRegistroMercantil.filename.split('.')[1]=='pdf':
                    resp = jsonify({"status":'error', "msj":"El registro mercantil de estar en formato .pdf"})
                    return sendResponse(resp) 
            else:
                resp = jsonify({"status":'error', "msj":"Debe adjuntar el Registro Mercantil"})
                return sendResponse(resp)
            print("fileRegistroMercantil")
            
            if  fileRif:
                if not fileRif.filename.split('.')[1]=='pdf':
                    resp = jsonify({"status":'error', "msj":"El R.I.F debe estar en formato .pdf"})
                    return sendResponse(resp) 
            else:
                resp = jsonify({"status":'error', "msj":"Debe adjuntar el R.I.F"})
                return sendResponse(resp)
            print("fileRif")
            
            if  fileCi:
                if not fileCi.filename.split('.')[1]=='pdf':
                    resp = jsonify({"status":'error', "msj":"La Cédula de Identidad debe estar en formato .pdf"})
                    return sendResponse(resp) 
            else:
                resp = jsonify({"status":'error', "msj":"Debe adjuntar la Cédula de Identidad"})
                return sendResponse(resp)
            print("fileCi")

            if  fileReciboServicio:
                if not fileReciboServicio.filename.split('.')[1]=='pdf':
                    resp = jsonify({"status":'error', "msj":"El Reccibo de servicios debe estar en formato .pdf"})
                    return sendResponse(resp) 
            else:
                resp = jsonify({"status":'error', "msj":"Debe adjuntar el Recibo de Servicios"})
                return sendResponse(resp)
            print("File recibo servicios")
            
            #existe_company=retail.existeCompany(retail.strrif_empresa) 
            #existe_email=retail.existeEmail(retail.strcorreo)            
            """if  existe_company:
                resp = jsonify({"status":'error', "msj":"El negocio se encuentra registrado"})
                return sendResponse(resp)"""
            existe_email=1
            if not  existe_email:
                resp = jsonify({"status":'error', "msj":"El correo se encuentra registrado"})
                return sendResponse(resp)
            else:
                #comercio=retail.registerCompany()
               # print(comercio)
                comercio=1
                if comercio:    
                    print("paso en comercio")                
                    #retail.id_empresa=comercio['id_empresa']
                    retail.id_empresa=1
                    print("path_folder_documents->"+path_folder_documents)
                    print("folder_documents"+folder_documents)
                    ruta_comercio=path_folder_documents+"/"+folder_documents+"-"+str(retail.id_empresa)
                    print("ruta comercio"+ruta_comercio)
                    if not os.path.exists(ruta_comercio):
                        print("crear carpeta")
                        os.makedirs(ruta_comercio)                    
                    else:
                        print("existe carpeta")
                    
                    print(ruta_comercio)
                    print("ruta_comercio")

                    filename_regmercantil="RM_"+str(retail.id_empresa)+"."+secure_filename(fileRegistroMercantil.filename.split('.')[1])
                    fileRegistroMercantil.save(os.path.join(ruta_comercio,filename_regmercantil))          
                    print(filename_regmercantil)
                    #documentosRM=retail.registerDocumentsCompany(ruta_comercio+filename_regmercantil,retail.id_empresa,3)

                    filename_rif="RIF_"+str(retail.id_empresa)+"."+secure_filename(fileRif.filename.split('.')[1])
                    fileRif.save(os.path.join(ruta_comercio,filename_rif))
                    print(filename_rif)
                    #documentosRIF=retail.registerDocumentsCompany(ruta_comercio+filename_rif,retail.id_empresa,4)

                    filename_ci="CI_"+str(retail.id_empresa)+"."+secure_filename(fileCi.filename.split('.')[1])
                    fileCi.save(os.path.join(ruta_comercio,filename_ci))
                    print(filename_ci)
                    #documentosCI=retail.registerDocumentsCompany(ruta_comercio+filename_ci,retail.id_empresa,5)

                    filename_rs= "RS_"+str(retail.id_empresa)+"."+secure_filename(fileReciboServicio.filename.split('.')[1])
                    fileReciboServicio.save(os.path.join(ruta_comercio,filename_rs))
                    print(filename_rs+"recibo servicios")
                    #documentosRS=retail.registerDocumentsCompany(ruta_comercio+filename_rs,retail.id_empresa,6)
                    if not filename_rs:
                    #if documentosRM and documentosRIF and documentosCI and documentosRS:"""
                        resp = jsonify({"status":'success', "msj":"El negocio no fue registrado"})
                        return sendResponse(resp)
                    else:
                        resp = jsonify({"status":'success', "msj":"El negocio fue registrado"})
                        #send_mailCompany(retail.strcorreo,retail.strnombre_empresa)
                        return sendResponse(resp)
                else:
                    resp = jsonify({"status":'error', "msj":"El negocio no fue registrado"})                    
                    return sendResponse(resp)
        else:
            resp = jsonify({"status":'error', "msj":"Debe enviar datos prueba"})                    
            return sendResponse(resp)


    except Exception as e:
        print(e)    