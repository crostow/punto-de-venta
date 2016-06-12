# -*- encoding: utf-8 -*-
# ------------------------------------------------------------------------#
# Programa: Punto de venta 2.0				                              #
# ------------------------------------------------------------------------#
# Propósito: Administracion para acceso de usuarios                       #
# ------------------------------------------------------------------------#
# Autor: Abuelazo                                                         #
# ------------------------------------------------------------------------#
# Fecha: 12/04/2016                                                       #
# ------------------------------------------------------------------------#

#se importan librerias necesarias
import hashlib
import conexion
from PyQt4 import QtGui

######################### metodos para ingresarusuario##########################################################################################
#metodo para evaluar campos
def campo_vacio(self):
    #si evalua si la longitud del campoes = 0
    if len(self.ui.ingresar_nombre.text()) == 0:
        QtGui.QMessageBox.warning(self, "Informacion", """Te falta nombre""", QtGui.QMessageBox.Ok)
    # si evalua si la longitud del campoes = 0
    elif len(self.ui.ingresar_password.text()) == 0:
        QtGui.QMessageBox.warning(self, "Informacion", """Te falta contraseña""", QtGui.QMessageBox.Ok)
    #se evalua si cual radio buton esta activado
    elif self.ui.permiso_usuario.isChecked():
        #se aigna el valor a una variable 2 = usuario normal
        permisos = 2
        #se manda a llamar metodo ingresar_usuario y se le pasa el parametro permisos
        ingresar_usuario(self, permisos)
     #se evalua si el radiobutton esta activado
    elif self.ui.permiso_administrador.isChecked():
        #se aigna una valor a una variable
        permisos = 1
        #se manda a llamar el metodo ingresar_usuario y se le pasan parametros
        ingresar_usuario(self, permisos)
    #en caso contrario
    else:
        QtGui.QMessageBox.warning(self, "Informacion", """te faltan seleccionar los permisos""", QtGui.QMessageBox.Ok)

#----------------------------------------------------------------------------------------------------------------------------------------------
#metodo para ingresar usuarios que recibe parametros
def ingresar_usuario(self, permisos):
    #se toman los valores de los campos
    nombre = unicode(self.ui.ingresar_nombre.text())
    password = unicode(self.ui.ingresar_password.text())
    #se cifra la contraseña
    cifrado = hashlib.sha1(password.encode('utf-8'))
    #se crea un query para insetar los datos
    query = unicode("INSERT INTO usuarios VALUES(NULL ,\"{0}\",\"{1}\",\"{2}\")").format(nombre, unicode(cifrado.hexdigest()), permisos)
    #se ejecuta el query
    conexion.consultas(query)
    #se limpian los campos
    self.ui.ingresar_password.setText('')
    self.ui.ingresar_nombre.setText('')
################################################################################################################################################

#################################metodos para modificar a los usuarios##########################################################################
#metodo para modificar los usuarios
def buscar_usuarios(self):
    #se crea un query para mostrar los usuarios
    query = unicode("SELECT * FROM usuarios ")
    #se ejcuta el query y se almacena enuna variable
    datos_obtenidos = conexion.consultas(query)
    #se asignan la longitud del la cconsulta a una variable global
    self.total_usuarios = len(datos_obtenidos)
    #se asignan el numero de columnas para la tabla
    self.ui.modificar_lista.setColumnCount(4)
    #se asignan el numero de filas dado la longitud de la consulta
    self.ui.modificar_lista.setRowCount(len(datos_obtenidos))

     #bucle para llenar la tabla por filas
    for fila in xrange(len(datos_obtenidos)):
        #bucle para llenar la tabla por columnas
        for columna in xrange(4):
            #se crea un item
            item = QtGui.QTableWidgetItem()
            #se asignan el valor a enviar
            item.setText("%s" % (unicode(datos_obtenidos[fila][columna])))
            #se manda el valor por posición fila columna
            self.ui.modificar_lista.setItem(fila, columna, item)
#-----------------------------------------------------------------------------------------------------------------------------------------------
#metodo modificar vacio
def modificar_vacio(self):
    # si evalua si la longitud del campoes = 0
    if len(self.ui.modificar_usuario_2.text()) == 0 :
        QtGui.QMessageBox.warning(self, "Informacion", """te falta usuario a modificar""", QtGui.QMessageBox.Ok)
    # si evalua si la longitud del campoes = 0
    elif len(self.ui.modificar_password.text()) == 0:
        QtGui.QMessageBox.warning(self, "Informacion", """te falta contraseña a modificar""", QtGui.QMessageBox.Ok)
    #se evalua si cual radio buton esta activado
    elif self.ui.modificar_administrador.isChecked():
        #se asigna el valor a la variable
        permisos = 1
        #se llama al metodo altera_usuarios y se le pasa el parametro permiso
        alterar_usuarios(self, permisos)
    #se evalua si cual radio buton esta activado
    elif self.ui.modificar_usuario_3.isChecked():
        # se asigna el valor a la variable
        permisos = 2
        # se llama al metodo altera_usuarios y se le pasa el parametro permiso
        alterar_usuarios(self, permisos)
    else:
        QtGui.QMessageBox.warning(self, "Informacion", """te falta seleccionar permisos""", QtGui.QMessageBox.Ok)

#-----------------------------------------------------------------------------------------------------------------------------------------------
#metodo para modifiacar usuario con parametro recibido
def alterar_usuarios(self, permisos):
    #se toman los valores de los campos
    nombre = unicode(self.ui.modificar_usuario_2.text())
    nombre_nuevo = unicode(self.ui.modificar_nuevo_nombre.text())
    password= unicode(self.ui.modificar_password.text())
    # se cifra la contraseña
    cifrado = hashlib.sha1(password.encode('utf-8'))
    #se crea un query para modificar usuario
    query = unicode("UPDATE usuarios SET nombre = \"{0}\", password = \"{1}\", permisos = \"{2}\"  WHERE nombre = \"{3}\"  ").format(nombre_nuevo, unicode(cifrado.hexdigest()), permisos, nombre)
    #se ejecuta el query
    conexion.consultas(query)
    #se limpian los campos
    self.ui.modificar_usuario_2.setText('')
    self.ui.modificar_nuevo_nombre.setText('')
    self.ui.modificar_password.setText('')
    self.ui.modificar_modificar.setEnabled(False)


    #se limpia la tabla y se eliminan las filas
    self.ui.modificar_lista.clearContents()
    self.ui.modificar_lista.setRowCount(0)
    buscar_usuarios(self)
################################################################################################################################################

#######################################metodos para eliminar usuarios###########################################################################
#metodo para mostrar datos
def eliminar_mostrar(self):
    #se crea query para mostrar datos
    query = unicode("SELECT id, nombre FROM usuarios ")
    #se ejecuta el query y se almacena en una variable
    datos_obtenidos = conexion.consultas(query)
    #se toma la longitud de el resultado de la consulta
    self.total_usuarios = len(datos_obtenidos)
    #se signan las columnas para la tabla
    self.ui.eliminar_lista.setColumnCount(2)
    #se asignan las columnas para la tabla dado la longitud de la consulta
    self.ui.eliminar_lista.setRowCount(len(datos_obtenidos))
    #self.ui.modificar_lista.clear()

    #bucle para llenar tabla por fila
    for fila in xrange(len(datos_obtenidos)):
        #bucle para llenar tabla por columna
        for columna in xrange(2):
            #se crea un item
            item = QtGui.QTableWidgetItem()
            #se asigna el valor al item
            item.setText("%s" % (unicode(datos_obtenidos[fila][columna])))
            #se manda valor a la tabla por posición fila columna
            self.ui.eliminar_lista.setItem(fila, columna, item)
#-----------------------------------------------------------------------------------------------------------------------------------------------
#metodo para eliminr usuarios
def eliminar_usuario(self):
    #se toma el valor del campo
    id = unicode(self.ui.eliminar_id.text())

    if len(id) == 0 :
        QtGui.QMessageBox.warning(self, "Informacion", """te falta seleccionar id""", QtGui.QMessageBox.Ok)
    else:
        #se crea query para eliminar producto
        query = unicode("DELETE FROM usuarios WHERE id = \"{0}\" ").format(id)
        #se ejecuta query
        conexion.consultas(query)

        self.ui.eliminar_id.setText("")
        self.ui.eliminar_eliminar.setEnabled(False)
        self.ui.eliminar_lista.clearContents()
        self.ui.eliminar_lista.setRowCount(0)
        eliminar_mostrar(self)
################################################################################################################################################