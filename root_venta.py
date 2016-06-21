# -*- encoding: utf-8 -*-
# ------------------------------------------------------------------------#
# Programa: Punto de venta 2.0				                              #
# ------------------------------------------------------------------------#
# Propósito: Administracion de venta de productos|                        #
# ------------------------------------------------------------------------#
# Autor: Abuelazo                                                         #
# ------------------------------------------------------------------------#
# Fecha: 17/04/2016                                                       #
# ------------------------------------------------------------------------#
#importamos librerias necesarias
import os
import conexion
import time

from PyQt4 import QtGui

#metodo para mostrar los productos de la bd
def ventas_mostrar(self):
    #se crea el qury para buscar los productos de la bd
    query = unicode("SELECT * FROM productos WHERE producto LIKE \"%{0}%\" ").format(unicode(self.ui.venta_buscar_nombre.text()))
    #se ejecuta el query
    datos_obtenidos = conexion.consultas(query)
    #se asigna el numero de columnas de qtablewidget
    self.ui.ventas_existencia.setColumnCount(5)
    #se asignan el numero de filas dado la longitud del resultado de la consulta
    self.ui.ventas_existencia.setRowCount(len(datos_obtenidos))
    #bucle para llenar el qtablewidget por filas
    for filas in xrange(len(datos_obtenidos)):
        #bucle pata llenar el qtablewidget por columnas
        for columnas in xrange(5):
            #se crea un item
            dato = QtGui.QTableWidgetItem()
            #se asigna la informacion a mandar
            dato.setText("%s" %(unicode(datos_obtenidos[filas][columnas])))
            #se manda informacion a la qtablewidget
            self.ui.ventas_existencia.setItem(filas, columnas, dato)

#metodo para enviar la venta a la segunda qtablewidget
def mandar_venta(self):
    #se toma el valor de la fila seleccionada
    fila = self.ui.ventas_existencia.currentIndex().row()
    #se crea una lista vacia
    datos_vender = []
    #bucle para obtener los datos
    for columna in xrange(4):
        #se obtiene los datos de el qtablewidget
        dato = unicode(self.ui.ventas_existencia.item(fila, columna).text())
        #se agregan los datos a la lisa
        datos_vender.append(dato)
    #se elimina el valor en la posicion 3
    datos_vender.pop(3)
    #se inserta una fila en el 2do qtable widget
    self.ui.ventas_final.insertRow(self.ui.ventas_final.rowCount())
    #se asigna el numero de columnas a el 2d0 qtablewidget
    self.ui.ventas_final.setColumnCount(3)
    #se crea un item
    id = QtGui.QTableWidgetItem()
    #se le asigna el valor
    id.setText(datos_vender[0])
    #se manda al segundo qtablewidget
    self.ui.ventas_final.setItem(self.ui.ventas_final.rowCount()-1, 0, id)
    # se crea un item
    producto = QtGui.QTableWidgetItem()
    # se le asigna el valor
    producto.setText(datos_vender[1])
    # se manda al segundo qtablewidget
    self.ui.ventas_final.setItem(self.ui.ventas_final.rowCount()-1, 1, producto)
    # se crea un item
    precio = QtGui.QTableWidgetItem()
    # se le asigna el valor
    precio.setText(datos_vender[2])
    # se manda al segundo qtablewidget
    self.ui.ventas_final.setItem(self.ui.ventas_final.rowCount()-1, 2, precio)


#metodo para vender en el segundo qtablewidget
def completar_venta(self, usuario_pv):
    self.usuario_pv = usuario_pv
    self.usuario_os = os.getenv("USER")

    #se cuantan el numero de filas del 2do qtablewidget
    filas = self.ui.ventas_final.rowCount()
    #bucle para obtener los datos por fila
    for fila in xrange(filas):
        #se crea lista vacia
        datos_actualizar = []
        #bucle para obtener los datos por columna
        for columna in xrange(3):
            #se toman los valores
            dato = unicode(self.ui.ventas_final.item(fila, columna).text())
            #se agregan a la lista
            datos_actualizar.append(dato)
        #psecrea query para vender
        query = unicode("UPDATE productos SET cantidad = cantidad - 1 WHERE id = \"{0}\"").format(datos_actualizar[0])
        #se ejecuta el query
        conexion.consultas(query)
    #se mana a llamar el metodo mostrar ventas para actualizar los productos
    ventas_mostrar(self)
    #se manda a llamar el metodo verificar archivp
    verificar_archivo(self)

#funcion para ver si existe el archivo
def verificar_archivo(self):
    #se obtiene la fecha del sistema
    self.fecha = str(time.strftime("%d") + "-" + time.strftime("%m") + "-" + time.strftime("%Y"))
    #se almacena la direccion del archivo en la variable archivo """OJO CAMBIAR LA DIRECCION POR DONDE VAYA A ESTAR SU ARCHIVO"""
    #archivo = "/home/"+ self.usuario_os +"/corte_pv/"+ self.usuario_pv +"-" + self.fecha + ".csv"
    archivo = os.getcwd() +"/corte/"+ self.usuario_pv +"-" + self.fecha + ".csv"
    #compara con path si existe el archivo
    if os.path.isfile(archivo):
		#si existe el archivo manda msj
		#pass
        #print "archivo existe"
        #escribir archivo
        escribir_archivo(self)
		#en caso contrario manda a llamar la funcion para crear el archivo
    else:
        #print "se brinco"
        #se manda a llamar la funcio crear archivo
    	crear_archivo(self)

#funcion para crear archivo
def crear_archivo(self):
    #se obtiene la fecha
    fecha = str(time.strftime("%d") + "-" + time.strftime("%m") + "-" + time.strftime("%Y"))
    # linea de comando para crear archivo en blanco """OJO CAMBIAR LA DIRECCION POR DONDE VAYA A ESTAR SU ARCHIVO"""
    archivo = open(os.getcwd()+"/corte/"+ self.usuario_pv +"-" + self.fecha + ".csv", 'w')
    # se cierra el archivo
    archivo.close()
    #se manda llamar el metodo para escribir en el archivo
    escribir_archivo(self)


#metodo para escribir archivo
def escribir_archivo(self):
    #se obtiene la decha
    fecha = str(time.strftime("%d") + "-" + time.strftime("%m") + "-" + time.strftime("%Y"))
    #se cuentas las filas de el qtablewidget
    filas = self.ui.ventas_final.rowCount()
    #bucle para escribir datos en el archivo
    for fila in xrange(filas):
        #se toman el datos de el qtablewidget
        producto = str(self.ui.ventas_final.item(fila, 1).text())
        precio = str(self.ui.ventas_final.item(fila, 2).text())
        #se almacenan los datos en una variable
        datos_almacenar = '{0},{1}\n'.format(producto, precio)
        #se abre el archivo para escribir en el """OJO CAMBIAR LA DIRECCION POR DONDE VAYA A ESTAR SU ARCHIVO"""
        archivo = open(os.getcwd()+"/corte/"+ self.usuario_pv +"-" + self.fecha + ".csv", 'a')
        #se escriben los datos
        archivo.write(datos_almacenar)
        #se cierra el archivo
        archivo.close()
    #se limpia los datos y las filas de los qtablewidget
    self.ui.ventas_final.clearContents()
    self.ui.ventas_existencia.clearContents()
    self.ui.ventas_final.setRowCount(0)
    self.ui.ventas_existencia.setRowCount(0)


def cancelar(self):
    self.ui.ventas_final.clearContents()
    self.ui.ventas_final.setRowCount(0)
