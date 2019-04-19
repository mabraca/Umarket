
""""
 * Created by Visual Studio Code.
 * User: Javier Moreno
 * Date: 24/04/219
 * Time: 10:15 AM
""" 
from main import *

class Company():


    def registerCompany(id_usuario,strnombre_empresa,strrif_empresa,strdireccion,strcodigo_postal,id_estado,id_ciudad,id_municipio):
        try:                                                                         
            # save edits
            sql = "INSERT INTO dt_empresa(dt_usuario_id,strnombre_empresa,strrif_empresa, strdireccion,strcodigo_postal,id_estado,id_ciudad,id_municipio) VALUES(%s, %s, %s, %s, %s, %s, %s,%s, %s, %s)"
            data = (id_usuario,strnombre_empresa,strrif_empresa,strdireccion,strcodigo_postal,id_estado,id_ciudad,id_municipio)                   
            conn = mysql.connect()
            cursor = conn.cursor()
            resource=cursor.execute(sql, data)
            conn.commit()
            return resource
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def existeCompany(strrif_empresa):
        try:                    
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sql="SELECT * FROM dt_empresa WHERE strrif_empresa=%s"
            cursor.execute(sql,strrif_empresa)
            row = cursor.fetchone()
            return row
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    