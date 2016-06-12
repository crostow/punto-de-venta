# -*- encoding: utf-8 -*-
# ------------------------------------------------------------------------#
# Programa: Punto de venta 2.0				                              #
# ------------------------------------------------------------------------#
# Propósito: Realizar corte de las ventas echas                           #
# ------------------------------------------------------------------------#
# Autor: Abuelazo                                                         #
# ------------------------------------------------------------------------#
# Fecha: 01/05/2016                                                       #
# ------------------------------------------------------------------------#

#importamos librerias necesarias
import time
import csv
import os
from PyQt4 import QtGui
from fpdf import FPDF

def carpeta(self, nombre):
    self.usuario_pv = nombre
    self.usuario_os = os.getenv("USER")

    if(os.path.exists("/home/"+self.usuario_os+"/corte_pv")):
        print "directorio existente"
        mostrar_ventas(self)
    else:
        os.mkdir("/home/"+self.usuario_os+"/corte_pv",0o777)
        mostrar_ventas(self)

#metodo para mostrar las ventas en una tabla
def mostrar_ventas(self):
    #se toma la fecha del sistema
    self.fecha = str(time.strftime("%d") + "-" + time.strftime("%m") + "-" + time.strftime("%Y"))
    if os.path.isfile("/home/"+self.usuario_os+"/corte_pv/"+self.usuario_pv+"-" + self.fecha + ".csv"):
        #se abre el archivo y se asigna a una variable """OJO CAMBIAR LA DIRECCION POR DONDE VAYA A ESTAR SU ARCHIVO"""
        archivo_corte = csv.reader(open("/home/"+self.usuario_os+"/corte_pv/"+self.usuario_pv+"-" + self.fecha + ".csv", 'r'))
        #se cuenta la longitud del archivo """OJO CAMBIAR LA DIRECCION POR DONDE VAYA A ESTAR SU ARCHIVO"""
        filas_archivo = len(open("/home/"+self.usuario_os+"/corte_pv/"+self.usuario_pv+"-" + self.fecha + ".csv").readlines())
        #se definen las columnas para la tabla
        self.ui.corte_mostrar.setColumnCount(2)
        #se definen las filas para la tabla dependiendo la longitud del archivo
        self.ui.corte_mostrar.setRowCount(filas_archivo)

        # bucle para obtener los datos
        for dato, fila in enumerate(archivo_corte):
            # se crea un item
            item = QtGui.QTableWidgetItem()
            # se asigna el valor al item
            item.setText(fila[0])
            # se manda el valor a la pocision
            self.ui.corte_mostrar.setItem(dato, 0, item)
            # se crea un item
            item = QtGui.QTableWidgetItem()
            # se asigna el valor al item
            item.setText(fila[1])
            # se manda el valor a la pocision
            self.ui.corte_mostrar.setItem(dato, 1, item)
        # se manda llamar el metodo total_corte
        total_corte(self)

    else:
        QtGui.QMessageBox.warning(self, "Informacion", "Aun no se an realizado ventas", QtGui.QMessageBox.Ok)


#metodo para mostrar total de las ventas
def total_corte(self):
    #se crea una lista vacia
    corte = []
    #se cuentas las filas que existen en la tabla
    filas = self.ui.corte_mostrar.rowCount()
    #bucle para recorrer la tabla
    for suma in xrange(filas):
        #se asigna valor tomado de la tabla
        dato = float(self.ui.corte_mostrar.item(suma, 1).text())
        #se agrega a la lista
        corte.append(dato)

    #se manda llamar el metodo suma_total y se le pasa la lista
    suma_total(self, corte)

#metodo de suma_total y recibe la lista
def suma_total(self, lista):
    #se declara variable suma con valor de 0
    self.suma = 0
    #bucle para sumar los valores de la lista
    for i in range(0,len(lista)):
        #operacion para sumar los datos de la lista
        self.suma = self.suma + lista[i]
    #se manda el valor total al qline
    self.ui.corte_total.setText(str(float(self.suma)))
    reporte_realizado(self)


def reporte_realizado(self):
    if os.path.isfile("/home/"+self.usuario_os+"/corte_pv/"+self.usuario_pv+"-" + self.fecha + ".csv"):
        respuesta = QtGui.QMessageBox.warning(self, "Informacion", "Corte realizado desea sobreescribir", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
        if respuesta == QtGui.QMessageBox.Ok:
            reporte_pdf(self)
        else:
            pass
    else:
        reporte_pdf(self)


def reporte_pdf(self):
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font("arial", "", 12)


    #for i in range(1, 100):
     #   pdf.cell(0, 10, "Printing line number " + str(i), 0, 1)

    pdf.output("/home/" + self.usuario_os + "/Escritorio/" + self.usuario_pv + "-" + self.fecha + ".pdf", "F")




    # PARA WINDOWS: os.system("start AcroRD32 ruta_y_archivo.pdf &")
    os.system("atril /home/" + self.usuario_os + "/Escritorio/" + self.usuario_pv + "-" + self.fecha + ".pdf &")



class PDF(FPDF):
    def header(self):        # Logo
        self.image(os.getcwd() + "/iconos/cash_register.2.2.png", 200, 200,33 )
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

