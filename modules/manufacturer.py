from .company import Company
from main import *
import db_config 
from . import modules
import os,time
from werkzeug.utils import secure_filename

@modules.route('/bussiness/register', methods=['POST'])
def registerBussines():
    try:
        retail= Company()        
        _json= request.get_json(force=True)    
        """fileRegistro_mercantil= request.files['filemerchant_register']
        fileRifs= request.files['filerif']
        fileCi= request.files['fileci']
        fileReciboServicio= request.files['filereceipt_services']"""
        retail.strnombre_empresa=_json['strname_company']
        retail.strrif_empresa=_json['strrif_company']
        retail.strnombre_representante=_json['strlegal_representative']
        print(retail.strnombre_representante)
        retail.strdireccion = _json['straddress']        
        retail.strcorreo=_json['stremail']
        retail.strtelefono=_json['strphone']
        retail.id_tipo=_json['inttype']
        #retail.strcodigo_postal = _json['strpostal_code']
        #retail.strhorario_empresa= _json['strschedule_company']     
        #retail.id_estado=_json['id_estado']  
        #retail.id_ciudad=_json['id_ciudad']            
        #retail.id_municipio= _json['id_municipio']   
        
        """if not os.path.exists(time.strftime("%Y%m%d")):
            os.makedirs('modules/documents_company/'+time.strftime("%Y%m%d"))"""
        
        #print(time.strftime("%Y%m%d"))
        #print(os.path.exists(time.strftime("%Y%m%d")))
        # validate the received values
        if request.method == 'POST':           
            if not retail.strnombre_empresa:             
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
                return sendResponse(resp)
            
            """  if  os.path.isfile(fileRegistro_mercantil):
                if  os.path.splitext(fileRegistro_mercantil)=='.pdf':
                    

            else:
                resp = jsonify({"status":'error', "msj":"Debe adjuntar el archivo del Registro Mercantil"})
                return sendResponse(resp)"""

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
                    #retail.id_empresa=comercio['id_empresa']
                    #documentos=retail.registerDocumentsCompany()
                    """if documentos:
                        resp = jsonify({"status":'success', "msj":"El negocio fue registrado"})
                        return sendResponse(resp)
                    else:"""
                    resp = jsonify({"status":'success', "msj":"El negocio fue registrado"})
                    return sendResponse(resp)

    except Exception as e:
        print(e)    