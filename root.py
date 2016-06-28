# -*- encoding: utf-8 -*-
# ------------------------------------------------------------------------#
# Programa: Punto de venta 2.0				                              #
# ------------------------------------------------------------------------#
# Propósito: Ejecucion de la segunda pantalla                             #
# ------------------------------------------------------------------------#
# Autor: Abuelazo                                                         #
# ------------------------------------------------------------------------#
# Fecha: 12/04/2016                                                       #
# ------------------------------------------------------------------------#
#se importan las librerias necesarias
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui

#se importa la pantalla ""from (carpeta) import (archivo)""
from pantallas import root

#se importan los archivos complementarios
import logueo
import root_usuarios
import root_almacen
import root_venta
import root_corte


# se define la clase principal
class general(QMainWindow):
    def __init__(self, parent = None, *datos):
        super(general, self).__init__(parent)
        self.ui = root.Ui_MainWindow()
        self.ui.setupUi(self)
        #metodo para centrar ventana
        self.centrado()

#datos a tomar en cuenta
#clicked() = click con el mouse
#returnpressed() = enter
#triggered() = para menu y barra de herramientas


        # conectamos los metodos de la barra con los eventos
        self.ui.barra_venta.triggered.connect(self.pagina_ventas)
        self.ui.barra_inventario.triggered.connect(self.pagina_inventario)
        self.ui.barra_usuarios.triggered.connect(self.pagina_usuarios)
        self.ui.barra_corte.triggered.connect(self.pagina_corte)
        self.ui.barra_salir.triggered.connect(self.salir)

        #conectamos los metodos de el menu con los eventos
        self.ui.menu_salir.triggered.connect(self.salir)
        self.ui.menu_info.triggered.connect(self.informacion)

########conectamos los botones con los eventos para ingresar, modificar y eliminar usuario###########
        self.connect(self.ui.ingresar_ingresar, SIGNAL("clicked()"),self.ingresar_usuario)          #
        self.connect(self.ui.ingresar_ingresar, SIGNAL("returnpressed()"),self.ingresar_usuario)    #
#---------------------------------------------------------------------------------------------------#
        self.connect(self.ui.modificar_buscar, SIGNAL("clicked()"),self.modificar_mostrar)          #
        self.connect(self.ui.modificar_buscar, SIGNAL("returnpressed()"), self.modificar_mostrar)   #
        self.connect(self.ui.modificar_modificar, SIGNAL("clicked()"), self.modificar_usuario)      #
        self.connect(self.ui.modificar_modificar, SIGNAL("returnpressed()"), self.modificar_usuario)#
#---------------------------------------------------------------------------------------------------#
        self.connect(self.ui.eliminar_buscar, SIGNAL("clicked()"), self.eliminar_mostrar)           #
        self.connect(self.ui.eliminar_buscar, SIGNAL("returnpressed()"), self.eliminar_mostrar)     #
        self.connect(self.ui.eliminar_eliminar, SIGNAL("clicked()"), self.eliminar_eliminar)        #
        self.connect(self.ui.eliminar_eliminar, SIGNAL("returnpressed()"), self.eliminar_eliminar)  #
#####################################################################################################

########conectamos los botones con los eventos  para ingresar, modificar y eliminar productos########
        self.connect(self.ui.producto_ingresar, SIGNAL("clicked()"), self.ingresar_producto)        #
        self.connect(self.ui.producto_ingresar, SIGNAL("returnpressed()"), self.ingresar_producto)  #
#---------------------------------------------------------------------------------------------------#
        self.connect(self.ui.actualizar_buscar, SIGNAL("clicked()"), self.producto_mostrar)         #
        self.connect(self.ui.actualizar_buscar, SIGNAL("returnpressed()"), self.producto_mostrar)   #
        self.connect(self.ui.actualizar_actualizar, SIGNAL("clicked()"), self.producto_actualizar)  #
        self.connect(self.ui.actualizar_actualizar, SIGNAL("returnpressed()"), self.producto_actualizar)#
#---------------------------------------------------------------------------------------------------#
        self.connect(self.ui.eliminar_buscar_2, SIGNAL("clicked()"), self.eliminar_mostrar_producto)#
        self.connect(self.ui.eliminar_buscar_2, SIGNAL("returnpressed()"), self.eliminar_mostrar_producto)#
        self.connect(self.ui.eliminar_eliminar_2, SIGNAL("clicked()"), self.producto_eliminar)      #
        self.connect(self.ui.eliminar_eliminar_2, SIGNAL("returnpressed()"), self.producto_eliminar)#
####################################################################################################

#####################conectamos botones con los eventos de venta#####################################
        self.connect(self.ui.venta_buscar, SIGNAL("clicked()"), self.venta_mostrar)                 #
        self.connect(self.ui.venta_buscar, SIGNAL("returnpressed()"), self.venta_mostrar)           #
# --------------------------------------------------------------------------------------------------#
        self.ui.ventas_existencia.doubleClicked.connect(self.venta_click)                           #
        self.ui.ventas_final.doubleClicked.connect(self.quitar_producto)
          #
#  -------------------------------------------------------------------------------------------------#
        self.connect(self.ui.ventas_vender, SIGNAL("clicked()"), self.venta_final)                  #
        self.connect(self.ui.ventas_vender, SIGNAL("returnpressed()"), self.venta_final)
        self.connect(self.ui.ventas_cancelar, SIGNAL("clicked()"), self.cancelar_venta)
        self.connect(self.ui.ventas_cancelar, SIGNAL("returnpressed()"), self.cancelar_venta)
#####################################################################################################

#####################conectamos botones con los eventos de corte#####################################
        self.connect(self.ui.corte_generar, SIGNAL("clicked()"), self.archivo_mostrar)              #
        self.connect(self.ui.corte_generar, SIGNAL("returnpressed()"), self.archivo_mostrar)        #
#####################################################################################################



        self.vendedor = datos[0][1]

        #se evaluan los permisos
        if datos[0][0] == '1':
            #si son 1 tienes acceso a todas las opciones
            #print "administrador"
            pass
        #en caso contrario
        else:
            #se desactivan botones de la barra
            self.ui.barra_inventario.setVisible(False)
            self.ui.barra_usuarios.setVisible(False)





################lamado de paginas####################
    def pagina_ventas(self):                        #
        self.ui.paginas.setCurrentIndex(0)          #
        self.ui.ventas_existencia.clearContents()   #
        self.ui.ventas_existencia.setRowCount(0)    #
        self.ui.ventas_final.clearContents()        #
        self.ui.ventas_final.setRowCount(0)         #
#---------------------------------------------------#
    def pagina_inventario(self):                    #
        self.ui.paginas.setCurrentIndex(1)          #
        self.ui.actualizar_lista.clearContents()    #
        self.ui.actualizar_lista.setRowCount(0)     #
        self.ui.eliminar_lista_2.clearContents()    #
        self.ui.eliminar_lista_2.setRowCount(0)     #
#---------------------------------------------------#
    def pagina_usuarios(self):                      #
        self.ui.paginas.setCurrentIndex(2)          #
        self.ui.modificar_lista.clearContents()     #
        self.ui.modificar_lista.setRowCount(0)      #
        self.ui.eliminar_lista.clearContents()      #
        self.ui.eliminar_lista.setRowCount(0)       #
#---------------------------------------------------#
    def pagina_corte(self):                         #
        self.ui.paginas.setCurrentIndex(3)          #
        self.ui.corte_mostrar.clearContents()
        self.ui.corte_mostrar.setRowCount(0)
#####################################################


###########metodos para gestion de usuarios##########
    def ingresar_usuario(self):                     #
        root_usuarios.campo_vacio(self)             #
#---------------------------------------------------#
    def modificar_mostrar(self):                    #
        root_usuarios.buscar_usuarios(self)         #
        self.ui.modificar_modificar.setEnabled(True)#
#---------------------------------------------------#
    def modificar_usuario(self):                    #
        root_usuarios.modificar_vacio(self)         #
#---------------------------------------------------#
    def eliminar_mostrar(self):                     #
        root_usuarios.eliminar_mostrar(self)        #
        self.ui.eliminar_eliminar.setEnabled(True)  #
#---------------------------------------------------#
    def eliminar_eliminar(self):                    #
        root_usuarios.eliminar_usuario(self)        #
         #
#####################################################


##########metodos para gestion de productos##########
    def ingresar_producto(self):                    #
        root_almacen.campo_vacio(self)              #
#---------------------------------------------------#
    def producto_mostrar(self):                     #
        root_almacen.buscar_producto(self)          #
        self.ui.actualizar_actualizar.setEnabled(True)#
#---------------------------------------------------#
    def producto_actualizar(self):                  #
        root_almacen.alterar_producto(self)         #
#---------------------------------------------------#
    def eliminar_mostrar_producto(self):            #
        root_almacen.eliminar_mostrar(self)         #
        self.ui.eliminar_eliminar_2.setEnabled(True)#
#---------------------------------------------------#
    def producto_eliminar(self):                    #
        root_almacen.eliminar_producto(self)        #
        self.ui.eliminar_eliminar_2.setEnabled(False)#
#####################################################


#########metodos para venta de productos#############
    def venta_mostrar(self):                        #
        root_venta.ventas_mostrar(self)             #
#---------------------------------------------------#
    def venta_click(self):                          #
        self.ui.ventas_vender.setEnabled(True)      #
        self.ui.ventas_cancelar.setEnabled(True)    #
        root_venta.mandar_venta(self)               #
#---------------------------------------------------#
    def   quitar_producto(self):    #
        root_venta.eliminar_producto(self)
# ---------------------------------------------------#



    def venta_final(self):                          #
        self.ui.ventas_vender.setEnabled(False)     #
        self.ui.ventas_cancelar.setEnabled(False)
        root_venta.completar_venta(self, self.vendedor)            #
# --------------------------------------------------#
    def cancelar_venta(self):                       #
        self.ui.ventas_vender.setEnabled(False)
        self.ui.ventas_cancelar.setEnabled(False)  #
        root_venta.cancelar(self)                   #
#---------------------------------------------------#


#########metodos para generar corte##################
    def archivo_mostrar(self):                      #
        root_corte.mostrar_ventas(self, self.vendedor)   #
#---------------------------------------------------#

#metodo para informacion del programador
    def informacion(self):
        msg = QtGui.QMessageBox.about(self, "Acerca de", '''        Punto de venta
        realizado por Abuelazo
        correo mauro_ruiz2001@hotmail.com
                crostow.ewinkeiton@gmail.com
                                                   ''')
#metodo para salir
    def salir(self):
        self.close()
        ventana_1 = logueo.Logueo(self)
        ventana_1.show()

#metodo para centrar la ventana
    def centrado(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

# codigo para lanzar la aplicacion
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = general()
    ventana.show()
    sys.exit(app.exec_())
