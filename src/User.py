class User:

    def __init__(self, nombre, DNI, Dir_Postal, telf, mail):
        self.nombre = nombre
        self.DNI = DNI
        self.Dir_Postal = Dir_Postal
        self.telf = telf
        self.mail = mail
        pass
   
    def comprueba_datos(self, nombre, DNI, Dir_Postal, telf, mail):
        correcto = True
        if (nombre.isdigit()):
            correcto=False
        elif (DNI.isalpha()):
            correcto=False
        elif (Dir_Postal.isalpha()):
            correcto=False
        elif (telf.isalpha()): 
            correcto=False
        elif (mail.isdigit()):
            correcto=False
        return correcto
        
    def datos_completos(self, nombre, DNI, Dir_Postal, telf, mail):
        correcto = True
        if (nombre==' '):
            correcto=False
        elif (DNI==' '):
            correcto=False
        elif (Dir_Postal==' '):
            correcto=False
        elif (telf==' '):
            correcto=False
        elif (mail==' '):
            correcto=False
        return correcto

    def factura(self, nombre, DNI, Dir_Postal, telf, mail):
        aux = []
        aux.append(nombre)
        aux.append(DNI)
        aux.append(Dir_Postal)
        aux.append(telf)
        aux.append(mail)

        return aux