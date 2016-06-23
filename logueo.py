# -*- encoding: utf-8 -*-
# ------------------------------------------------------------------------#
# Programa: Punto de venta 2.0				                              #
# ------------------------------------------------------------------------#
# Propósito: validacion de usuario                                        #
# ------------------------------------------------------------------------#
# Autor: Abuelazo                                                         #
# ------------------------------------------------------------------------#
# Fecha: 07/04/2016                                                       #
# ------------------------------------------------------------------------#

# importamos librerias necesarias
import sys, os
import hashlib
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui

# importamos de la carpeta pantallas el archivo de logueo
from pantallas import logueo

#importamos el archivo root
import root

# importamos de la carpeta mysql el archivo de conexion a la base de datos con formato "" from carpeta.archivo import funcion ""
import conexion



# se define la clase principal
class Logueo(QMainWindow):
    def __init__(self, parent=None):
        super(Logueo, self).__init__(parent)
        self.ui = logueo.Ui_MainWindow()
        self.ui.setupUi(self)

        #metodo para centrar la ventana
        self.centrado()


        # conectamos los eventos con el boton de ingresar #### clicked = mouse :::  returnPressed == enter ####
        self.connect(self.ui.logueo_aceptar, SIGNAL('clicked()'), self.campo_vacio)
        self.connect(self.ui.logueo_aceptar, SIGNAL('returnPressed()'), self.campo_vacio)

        # conectamos los eventos con el boton de salir   #### clicked = mouse :::  returnPressed == enter ####
        self.connect(self.ui.logueo_cancelar, SIGNAL('clicked()'), self.salir)
        self.connect(self.ui.logueo_cancelar, SIGNAL('returnPressed()'), self.salir)




    #metodo par centrar ventana
    def centrado(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)



    #metodo para cotejar los campos de logueo
    def campo_vacio(self):
        #valora si la longitud del campo es 0
        if len(self.ui.logueo_usuario.text()) == 0 :
            #mensaje falta ususario
            QtGui.QMessageBox.warning(self, "Informacion", """Te falta usuario""", QtGui.QMessageBox.Ok)
            #print "te faltan usuario"
        #valora si la longitud del campo es 0
        elif len(self.ui.logueo_password.text()) == 0 :
            #mensaje falta contraseña
            QtGui.QMessageBox.warning(self, "Informacion", """Te falta contraseña""", QtGui.QMessageBox.Ok)
            #print "te falta contraseña"
        else:
            #llama al metodo usuario
            self.usuario()
        


    # funcion para checar si el usuario existe en la bd
    def usuario(self):
        #se toma el valor de el campo usuario
        usuario = unicode(self.ui.logueo_usuario.text())
        #se crea una consulta a la bd para cotejar usuario
        query = ("SELECT * FROM usuarios WHERE nombre = \"{0}\" ").format(usuario)
        #se ejecuta la consulta
        self.datos = conexion.consultas(query)
        #se coteja el resultado de la consulta si la longitud del campo es 0
        if len(self.datos) == 0:
            QtGui.QMessageBox.warning(self, "Informacion", """No existe usuario en la bd""", QtGui.QMessageBox.Ok)
            #print "no existe el usuario en la bd"
        #se coteja si el usuario es igual el obtenido en la consulta a la bd
        elif usuario == self.datos[0][1]:
            #Se manda a llamar el metodo contraseña
            self.contrasena()
        #en caso contrario
        else:
            #mensaje de usuario incorrecto
            QtGui.QMessageBox.warning(self, "Informacion", """Usuario incorrecto""", QtGui.QMessageBox.Ok)
            #print "usuario incorrecto"
        return

    #metodo contraseña
    def contrasena(self):
        #se toma el valor de la contraseña y se asigna a la variable password
        password = unicode(self.ui.logueo_password.text())
        #se cifra la variable password
        cifrado = hashlib.sha1(password.encode('utf-8'))
        #se coteja la valiable cifrada con la obtenida en la consulta
        if cifrado.hexdigest() == self.datos[0][2]:
            #se manda llamar el metodo permiso"
            self.permisos()
        else:
            QtGui.QMessageBox.warning(self, "Informacion", """Contraseña incorrecta""", QtGui.QMessageBox.Ok)
            #print "contraseña incorrecta"

    #metodo permisos
    def permisos(self):
        #se toma el valor de la consulta realizada

        permiso = self.datos[0][3]
        nombre = self.datos[0][1]
        datos = []
        datos.append(permiso)
        datos.append(nombre)
        #se cierra la ventana
        self.close()
        #se asigna el archivo root a la variable y se le pasa el parametro permiso
        ventana_2 = root.general(self, datos)
        #se muestra la ventana
        ventana_2.show()

    # funcion para cerrar ventana
    def salir(self):
        #se cierra la ventana
        self.close()


# codigo para lanzar la aplicacion
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Logueo()
    ventana.show()
    sys.exit(app.exec_())
