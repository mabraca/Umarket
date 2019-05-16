
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
    blnafiliacion=None
    id_status=None
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
            print("register company")
            if self.blnafiliacion==True:
                self.id_status=4
            else:
                self.id_status=3
            # save edits
            sql = "INSERT INTO dt_empresa(strnombre_empresa,strrif_empresa,strnombre_representante, strdireccion,strcorreo,strtelefono,id_tipo,id_status) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
            data = (self.strnombre_empresa,self.strrif_empresa,self.strnombre_representante,self.strdireccion,self.strcorreo,self.strtelefono,self.id_tipo,self.id_status)
            conn = mysql.connect()
            print(sql,data)
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
            print(strcorreo)                 
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
    
    def registerDocumentsCompany(self,strulr,id_empresa,datfecha):
        try:
            conn=mysql.connect()
            cursor=conn.cursor(pymysql.cursors.DictCursor)
            sql="INSERT INTO dt_documentos_empresa (id_empresa,strurl_documento,datfecha)VALUES(%s, %s, %s)"
            data=(id_empresa,strulr,datfecha)
            cursor.execute(sql,data)
            resource=cursor.lastrowid
            conn.commit()
            return resource                    
        except Exception as e:
            print(e)
    
    def validateCompany(self,id_empresa,id_tipo_empresa):
        try:
            conn=mysql.connect()
            cursor=conn.cursor(pymysql.cursors.DictCursor)
            sql="UPDATE dt_empresa SET id_status=4 WHERE id_empresa=%s AND id_tipo=%s"
            data=(id_empresa,id_tipo_empresa)
            afectado=cursor.execute(sql,data)
            conn.commit()
            print(afectado)
            return afectado
        except Exception as e:
            print(e)
        finally:
            conn.close
            cursor.close
    
    def generateAccessCode(self,id_empresa,strusuario):
        try:
            caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits
            longitud = 8  # La longitud que queremos
            codigo_acceso = ''.join(random.choice(caracteres) for _ in range(longitud))
            print("codigo->"+codigo_acceso)
            _hashed_password = hashlib.md5(codigo_acceso.encode())
            conn=mysql.connect()
            cursor=conn.cursor(pymysql.cursors.DictCursor)
            sql="UPDATE dt_usuarios SET strcontrasena=%s, id_status=2 WHERE id_empresa=%s AND strusuario=%s"
            data=(_hashed_password.hexdigest(),id_empresa, strusuario)
            afectado=cursor.execute(sql,data)
            conn.commit()
            return codigo_acceso
        except Exception as e:
            print(e)
        finally:
            pass
                
    def companyView(self,id_empresa):
        try:   
            #print(strrif_empresa)                 
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sql="SELECT * FROM vw_company WHERE id_empresa=%s"       
            print(sql)    
            cursor.execute(sql,id_empresa)
            row = cursor.fetchone()
            print(row)
            return row
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    
    def deleteCompany(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM dt_empresa WHERE id_empresa=%s", (self.id_empresa))
            conn.commit()
            return True
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    
    def deleteDocuments(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM dt_documentos_empresa WHERE id_empresa=%s", (self.id_empresa))
            conn.commit()
            return True
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    
    def registerDataBank(self,id_empresa,strcuenta):
        try:
            conn=mysql.connect()
            cursor=conn.cursor(pymysql.cursors.DictCursor)
            sql="INSERT INTO dt_datos_bancarios_empresa (id_empresa,strcuenta)VALUES(%s, %s)"
            data=(id_empresa,strcuenta)
            cursor.execute(sql,data)
            resource=cursor.lastrowid
            conn.commit()
            return resource
        except Exception as e:
            print(e)
        finally:
            pass
    
    def validatedAcountBank():
        try:
            pass
        except expression as identifier:
            pass
        finally:
            pass
    
    def updateCompany(self,nombre_campo,valor_campo,id_empresa):
        try:
            conn=mysql.connect()
            cursor=conn.cursor(pymysql.cursors.DictCursor)
            if type(valor_campo)==int:
                sql="UPDATE dt_empresa SET %s=%s WHERE id_empresa=%s "%(nombre_campo,valor_campo,id_empresa)
            elif type(valor_campo)==str:
                sql="UPDATE dt_empresa SET %s=trim('%s') WHERE id_empresa=%s "%(nombre_campo,valor_campo,id_empresa)

            print(sql)
            cursor.execute(sql)
            conn.commit()
            return True
        except Exception as e:
            print(e)
        finally:
            conn.close()
            cursor.close()