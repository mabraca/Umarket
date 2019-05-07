
""""
 * Created by Visual Studio Code.
 * User: Javier Moreno
 * Date: 24/04/219
 * Time: 10:15 AM
""" 
from main import *

class Company():  
    id_empresa=None
    strnombre_empresa=None
    strrif_empresa=None
    strnombre_representante=None
    id_tipo=None
    strdireccion=None
    strcorreo=None
    strtelefono=None
    #strcodigo_postal=None
    #strhorario_empresa=None
    #id_estado=None
    #id_ciudad=None
    #id_municipio=None
    
    """def __init__(self):        
        self.id_empresa=id_empresa
        self.strnombre_empresa=strnombre_empresa
        self.strrif_empresa=strrif_empresa
        self.strnombre_representante=strnombre_representante
        self.strdireccion=strdireccion
        self.strcorreo=strcorreo
        self.strtelefono=strtelefono
        self.id_tipo=id_tipo"""
        #self.strcodigo_postal=strcodigo_postal
        #self.strhorario_empresa=strhorario_empresa
        #self.id_estado=id_estado
        #self.id_ciudad=id_ciudad
        #self.id_municipio=id_municipio


    def registerCompany(self):
        try:                                                                                                          
            # save edits
            sql = "INSERT INTO dt_empresa(strnombre_empresa,strrif_empresa,strnombre_representante, strdireccion,strcorreo,strtelefono,id_tipo) VALUES(%s, %s, %s, %s, %s, %s, %s)"
            data = (self.strnombre_empresa,self.strrif_empresa,self.strnombre_representante,self.strdireccion,self.strcorreo,self.strtelefono,self.id_tipo)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            resource=cursor.lastrowid
            print(resource)
            conn.commit()
            return int(resource)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def existeCompany(self):
        try:   
            #print(strrif_empresa)                 
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sql="SELECT * FROM dt_empresa WHERE ltrim(rtrim(UPPER(strrif_empresa)))=ltrim(rtrim(UPPER(%s)))"       
            print(sql)    
            cursor.execute(sql,self.strrif_empresa)
            row = cursor.fetchall()
            print(row)
            return row
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    
    def existeEmail(self,strcorreo):
        try:   
            #print(strrif_empresa)                 
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sql="SELECT * FROM dt_empresa WHERE UPPER(strcorreo)=UPPER(%s)"          
            cursor.execute(sql,strcorreo)
            row = cursor.fetchall()
            print(row)
            return row
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    
    def registerDocumentsCompany(self,strulr,id_empresa,id_tipo):
        try:
            conn=mysql.connect()
            cursor=conn.cursor(pymysql.cursors.DictCursor)
            sql="INSERT INTO dt_documentos_empresa (id_empresa,id_tipo,strurl_documento)VALUES(%s, %s, %s)"
            data=(id_empresa,id_tipo,strulr)
            cursor.execute(sql,data)
            resource=cursor.lastrowid
            conn.commit()
            return resource
                    
        except Exception as e:
            print(e)
        


    