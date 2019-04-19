
""""
 * Created by Visual Studio Code.
 * User: Javier Moreno
 * Date: 24/04/219
 * Time: 10:15 AM
""" 
import main

class Company():
    def __init__(self,intempresa_id, intusuario_id, strnombre_empresa, strrif_empresa, strdireccion, strcodigo_postal, strhorario_empresa,intparroq_id, intestado_id, intciudad_id,intpais_id):
        self.intempresa_id=intempresa_id
        self.intusuario_id=intusuario_id
        self.strnombre_empresa=strnombre_empresa
        self.strrif_rif_empresa=strrif_empresa
        self.strdireccion=strdireccion
        self.strcodigo_postal=strcodigo_postal
        self.strshorario=strhorario_empresa
        self.intparroq_id=intparroq_id
        self.intestado_id=intestado_id
        self.intciudad_id=intciudad_id
        self.intpais_id=intpais_id


    def registerCompany():
        try:
            _json= request.get_json(force=True)
            _dt_usuario_id = _json['user_id']
            _strnombre_empresa = _json['strname_company']
            _strrif_empresa = _json['strrif_company']
            _strdireccion = _json['straddress']
            _strcodigo_postal = _json['strpostal_code']
            _strhorario_empresa= _json['strschedule_company']
            _tm_parroquia_id= _json['tm_parroquia_id']
            _tm_municipio_id= _json['tm_municipio']
            _tm_estado_id=_json['tm_estado_id']            
            _tm_ciudad_id=_json['tm_ciudad_id']            
            _tm_estado_id= _json['tm_pais']
            _pais_id=58

            # validate the received values
            and request.method == 'POST'
            if  not _dt_usuario_id :
                resp = jsonify({"status":'error', "msj":"Debe ingresar un usuario"})
                sendResponse(resp)

            if not _strnombre_empresa:             
                resp = jsonify({"status":'error', "msj":"Debe ingresar un nombre para la empresa"})
                sendResponse(resp)

            if not _strrif_empresa: 
                resp = jsonify({"status":'error', "msj":"Debe ingresar un R.I.F"})
                sendResponse(resp)

            if not _strdireccion:
                resp = jsonify({"status":'error', "msj":"Debe ingresar una dirección"})
                sendResponse(resp)

            if not _strcodigo_postal:   
                resp = jsonify({"status":'error', "msj":"Debe ingresar un código postal"})
               sendResponse(resp)

            if not _strhorario_empresa:
                resp = jsonify({"status":'error', "msj":"Debe ingresar un horario"})
                sendResponse(resp)

            if _tm_estado_id:
                resp = jsonify({"status":'error', "msj":"Debe seleccionar un estado"})
                sendResponse(resp)

            if _tm_ciudad_id:
                resp = jsonify({"status":'error', "msj":"Debe seleccionar una ciudad"})
               sendResponse(resp)

            if _tm_municipio_id:
                resp = jsonify({"status":'error', "msj":"Debe seleccionar una municipio"})
                sendResponse(resp)

            if _tm_parroquia_id:     
                resp = jsonify({"status":'error', "msj":"Debe seleccionar una parroquia"})
                sendResponse(resp)      

            existe_company=existeCompany(_strrif_empresa)
            if not existe_company:                                           
                    # save edits
                    sql = "INSERT INTO dt_empresa(dt_usuario_id,strnombre_empresa,strrif_empresa, strdireccion,strcodigo_postal,tm_pais_id, tm_estado_id, tm_ciudad_id, tm_municipio_id, tm_parroquia_id) VALUES(%s, %s, %s, %s, %s, %s, %s,%s, %s, %s)"
                    data = (_dt_usuario_id, _strnombre_empresa,_strrif_empresa,_strdireccion,_strcodigo_postal, _pais_id,tm_estado_id,_tm_ciudad_id,_tm_municipio_id,_tm_parroquia_id)                   
                    conn = mysql.connect()
                    cursor = conn.cursor()
                    cursor.execute(sql, data)
                    conn.commit()
                    resp = jsonify({"status":'success', "msj":"La empresa fue registrada","token":_token})                  
                    resp.status_code = 200                                    
                    sendResponse(resp)                     
            else:
                resp = jsonify({"status":'error', "msj":"El empresa ya se encuentra registrada"})
                sendResponse(resp)                                                     
        except Exception as e:
            print(e)

    def saveDocument():


    def existeCompany(strrif_empresa)
        try:
            _strrif_empresa=strrif_empresa
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sql="SELECT * FROM dt_empresa WHERE strrif_empresa=%s"
            cursor.execute(sql,_strcorreo)
            row = cursor.fetchone()
            return row
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    