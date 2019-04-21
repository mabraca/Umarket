from .company import Company
from main import *
import db_config 
from . import modules
import os,time
from werkzeug.utils import secure_filename

@modules.route('/manufacturer/register', methods=['POST'])
def registerManufacturar():
    try:
        manufacturer= Company()        
        _json= request.get_json(force=True)    
        """fileRegistro_mercantil= request.files['filemerchant_register']
        fileRifs= request.files['filerif']
        fileCi= request.files['fileci']
        fileReciboServicio= request.files['filereceipt_services']"""
        manufacturer.strnombre_empresa=_json['strname_company']
        manufacturer.strrif_empresa=_json['strrif_company']
        manufacturer.strnombre_representante=_json['strlegal_representative']
        print(manufacturer.strnombre_representante)
        manufacturer.strdireccion = _json['straddress']        
        manufacturer.strcorreo=_json['stremail']
        manufacturer.strtelefono=_json['strphone']
        manufacturer.id_tipo=_json['inttype']
        #manufacturer.strcodigo_postal = _json['strpostal_code']
        #manufacturer.strhorario_empresa= _json['strschedule_company']     
        #manufacturer.id_estado=_json['id_estado']  
        #manufacturer.id_ciudad=_json['id_ciudad']            
        #manufacturer.id_municipio= _json['id_municipio']   
        
        """if not os.path.exists(time.strftime("%Y%m%d")):
            os.makedirs('modules/documents_company/'+time.strftime("%Y%m%d"))"""
        
        #print(time.strftime("%Y%m%d"))
        #print(os.path.exists(time.strftime("%Y%m%d")))
        # validate the received values
        if request.method == 'POST':           
            if not manufacturer.strnombre_empresa:             
                resp = jsonify({"status":'error', "msj":"Debe ingresar un nombre para la empresa"})
                return sendResponse(resp)

            if not manufacturer.strrif_empresa: 
                resp = jsonify({"status":'error', "msj":"Debe ingresar un R.I.F"})
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
            
            """  if  os.path.isfile(fileRegistro_mercantil):
                if  os.path.splitext(fileRegistro_mercantil)=='.pdf':
                    

            else:
                resp = jsonify({"status":'error', "msj":"Debe adjuntar el archivo del Registro Mercantil"})
                return sendResponse(resp)"""

            existe_company=manufacturer.existeCompany(manufacturer.strrif_empresa) 
            existe_email=manufacturer.existeEmail(manufacturer.strcorreo)            
            if  existe_company:
                resp = jsonify({"status":'error', "msj":"El negocio se encuentra registrado"})
                return sendResponse(resp)

            if existe_email:
                resp = jsonify({"status":'error', "msj":"El correo se encuentra registrado"})
                return sendResponse(resp)
            else:
                comercio=manufacturer.registerCompany()
               # print(comercio)
                if comercio:
                    #manufacturer.id_empresa=comercio['id_empresa']
                    #documentos=manufacturer.registerDocumentsCompany()
                    """if documentos:
                        resp = jsonify({"status":'success', "msj":"El negocio fue registrado"})
                        return sendResponse(resp)
                    else:"""
                    resp = jsonify({"status":'success', "msj":"El negocio fue registrado"})
                    return sendResponse(resp)

    except Exception as e:
        print(e)    