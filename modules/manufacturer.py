from .company import Company
from main import *
import db_config 
from . import modules

@modules.route('/bussiness/register', methods=['POST'])
def registerBussines():
    try:
        negocio= Company()
        _json= request.get_json(force=True)
        _id_usuario= _json['user_id']
        _strnombre_empresa= _json['strname_company']
        _strrif_empresa = _json['strrif_company']
        _strdireccion = _json['straddress']
        _strcodigo_postal = _json['strpostal_code']
        _strhorario_empresa= _json['strschedule_company']        
        _id_estado=_json['id_estado']      
        _id_municipio= _json['id_municipio']              
        _id_ciudad=_json['id_ciudad']            

        # validate the received values
        if request.method == 'POST':
            if  not _id_usuario :
                resp = jsonify({"status":'error', "msj":"Debe ingresar un usuario"})
                return sendResponse(resp)

            if not _strnombre_empresa:             
                resp = jsonify({"status":'error', "msj":"Debe ingresar un nombre para la empresa"})
                return sendResponse(resp)

            if not _strrif_empresa: 
                resp = jsonify({"status":'error', "msj":"Debe ingresar un R.I.F"})
                return sendResponse(resp)

            if not _strdireccion:
                resp = jsonify({"status":'error', "msj":"Debe ingresar una dirección"})
                return sendResponse(resp)

            if not _strcodigo_postal:   
                resp = jsonify({"status":'error', "msj":"Debe ingresar un código postal"})
                return sendResponse(resp)

            if not _strhorario_empresa:
                resp = jsonify({"status":'error', "msj":"Debe ingresar un horario"})
                return sendResponse(resp)

            if not _id_estado:
                resp = jsonify({"status":'error', "msj":"Debe seleccionar un estado"})
                return sendResponse(resp)

            if not _id_ciudad:
                resp = jsonify({"status":'error', "msj":"Debe seleccionar una ciudad"})
                return sendResponse(resp)

            if not _id_municipio:
                resp = jsonify({"status":'error', "msj":"Debe seleccionar una municipio"})
                return  sendResponse(resp)     

            existe_company=negocio.existeCompany(_strrif_empresa)
            if existe_company:
                resp = jsonify({"status":'error', "msj":"El negocio se encuentra registrado"})
                return sendResponse(resp)
            else:
                comercio=negocio.registerCompany(_id_usuario, _strnombre_empresa, _strrif_empresa, _strdireccion, _strcodigo_postal, _id_estado, _id_ciudad, _id_municipio)
                if comercio:
                    resp = jsonify({"status":'success', "msj":"El negocio fue registrado"})
                    return sendResponse(resp)

    except Exception as e:
        print(e)    