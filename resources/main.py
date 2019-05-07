
""""
 * Created by Visual Studio Code.
 * User: Javier Moreno
 * Date: 05/05/219
 * Time: 3:15 PM
""" 
import db_config

class Main():

    _ambiente=None
    _tabla=None
    _data=None
    _campos=None
    _hoy=None

    #Datos de configuración del servidor de correo
    _smpt_host='just64.justhost.com'
    _mail_addres= 'no-reply@ubiipagos.com'
    _smpt_username= 'no-reply@ubiipagos.com'
    _smpt_pasword='Ubiipagos.2017'


    #Metodos de la clase
    #Getter and Setter
    def getAmbiente(self):
        return self._ambiente
    
    def setAmbiente(self,ambiente):
        self._ambiente=ambiente
        
    def getHoy(self):
        return self._hoy

    def setHoy(self,hoy):
        self._hoy=_hoy


    def log():
    
    def search_in_string():

    #Este metodo agrega un registro de la tabla que desee
    def add():
    

    #Este metodo permite editar un registro de la table qu desee
    def edit():
    

    #Este metodo permite obtener de la tabla que desee retornando el o los campos enviados como parametros en la función
    def get_info(tabla, campos, condicion, debug = false):
        try:
            if not tabla:   
                if len(campos)>0:
                    temp=""
                    sw=True
                    for campos in nombres
                        if sw:
                            temp+=nombres
                            sw = False
                        else:
                            temp += "," +nombres
                else:
                    temp = campos
                
                if len(condicion)>0:
                    if not condicion.find('where')==0 or not condicion.find('WHERE')==0:
                        condicion=' WHERE '+ condicion
                
                sql=" SELECT %s FROM %s %s "%(campos, tabla, condicion)



        except Exception as e:
            print(e)
        finally:
            pass

        
     
