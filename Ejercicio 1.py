from gettext import find

class Email:
    __idCuenta: None
    __dominio: None
    __tipo_dominio: None
    __Contrasenia: None

    def __init__(self, id, dom, tipo, contra):
        self.__idCuenta = id
        self.__dominio = dom
        self.__tipo_dominio = tipo
        self.__Contrasenia = contra

    def retornaemail (self):
        dir_email = self.__idCuenta + '@' + self.__dominio + '.' + self.__tipo_dominio
        return dir_email

    def getdominio (self):
        return self.__dominio
    
    def crear (self, m): #arreglar despues
        print ('Prueba -> ', m)
        c1 = (m.find('@'))
        SI = m[:c1]
        c2 = (m.find('.'))
        SD = m[c1+1:c2]
        STD = m[c2+1:]
        SCon = input('Ingrese contrasenia: ')
        otroEmail = Email(SI, SD, STD, SCon)
        otroEmail.retornaemail()

def mod_password ():
    pasw = input('Ingrese contrasenia: ')
    if (pasw == unEmail.__Contrasenia):
        newpass = input('Ingrese nueva contraseña: ')
        unEmail.__Contrasenia == newpass
    else:
        print('CONTRASEÑA INCORRECTA')

if __name__ == '__main__':
    print('Ingrese los siguientes datos')
    n = input('Nombre: ')
    s = input('Id Cuenta: ')
    d = input('Dominio: ')
    t = input('Tipo de Dominio: ')
    c = input('Contrasenia: ')
    unEmail = Email(s, d, t, c)
    print('Estimado {} te enviaremos tus mensajes a la direccion {}'.format(n, unEmail.retornaemail()))
    print('-----------------------------------------------------')
    mod_password()
    mail = input('Ingrese direccion de mail: ')
    unEmail.crear(mail)
    