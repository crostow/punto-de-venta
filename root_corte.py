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

#metodo para mostrar las ventas en una tabla
def mostrar_ventas(self, nombre):
    self.usuario_pv = nombre
    #se toma la fecha del sistema
    self.fecha = str(time.strftime("%d") + "-" + time.strftime("%m") + "-" + time.strftime("%Y"))
    archivo = os.getcwd()+"/corte/"+self.usuario_pv+"-" + self.fecha + ".csv"
    if os.path.isfile(archivo):
        #se abre el archivo y se asigna a una variable """OJO CAMBIAR LA DIRECCION POR DONDE VAYA A ESTAR SU ARCHIVO"""
        archivo_corte = csv.reader(open(os.getcwd()+"/corte/"+self.usuario_pv+"-" + self.fecha + ".csv", 'r'))
        #se cuenta la longitud del archivo """OJO CAMBIAR LA DIRECCION POR DONDE VAYA A ESTAR SU ARCHIVO"""
        filas_archivo = len(open(os.getcwd()+"/corte/"+self.usuario_pv+"-" + self.fecha + ".csv").readlines())
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
    archivo = os.getcwd()+"/corte/"+self.usuario_pv+"-" + self.fecha + ".csv"
    if os.path.isfile(archivo):
        respuesta = QtGui.QMessageBox.warning(self, "Informacion", "Corte realizado desea sobreescribir", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
        if respuesta == QtGui.QMessageBox.Ok:
            reporte_pdf(self)
        else:
            QtGui.QMessageBox.warning(self, "Informacion", "Corte cancelado")

    else:
        reporte_pdf(self)


def reporte_pdf(self):
    pdf = PDF("p", "pt", "A4")
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font("Arial", "I", 8)


    #corte mostrar
    informacion = []
    filas_total = self.ui.corte_mostrar.rowCount()
    for fila in xrange(filas_total):
        for columna in xrange(2):
            dato = unicode(self.ui.corte_mostrar.item(fila, columna).text())
            informacion.append(dato)


    print informacion
    print len(informacion)
    f = len(informacion)/4
    print f
    y = pdf.get_y()
    y2 = pdf.get_y()
    x = pdf.get_x()
    index = 0
    pagina = 0
    bandera = 0

    for eje_y in xrange(len(informacion)/4):
        #pdf.cell(150, 10, "fila " + str(eje_y), 0, 1)
        for eje_x in range(4):
            pdf.set_y(y)
            pdf.set_x(x)
            #pdf.cell(60, 10, "columna" + str(eje_x), 1, 1)
            pdf.cell(60, 10, str(informacion[index]), 1, 1)
            x = x + 100
            index = index + 1
            pagina = pagina +1

            #pdf.multi_cell(100, 10, str(informacion[0 + eje_x]), 1, 1)

        x = pdf.get_x()
        if (pagina > 275) and (bandera == 0):
            pdf.add_page()
            y = y2
            bandera = 1
            pagina = 0
        elif (pagina >= 275) and (bandera == 1):
            pdf.add_page()
            y = y2
            bandera = 0
            pagina = 0
        else:
            y = y + 10

    pdf.add_page()

    pdf.set_line_width(1)
    # arriba
    pdf.line(0, 785, 595, 785)
    # enmedio
    pdf.line(400, 775, 595, 775)
    # abajo
    pdf.line(400, 765, 595, 765)
    # 1 vertical
    pdf.line(400, 765, 400, 785)
    # 2 vertical
    pdf.line(595, 765, 595, 785)
    # 3 vertical
    pdf.line(497.5, 765, 497.5, 785)

    pdf.set_y(765)
    pdf.cell(380)
    pdf.cell(100, 10, "Total de productos", 0, 1)

    pdf.set_y(775)
    pdf.cell(380)

    pdf.cell(100, 10, "Total de efectivo", 0, 1)

    pdf.output(os.getcwd()+"/reportes/"+ self.usuario_pv + "-" + self.fecha + ".pdf", "F")

    # PARA WINDOWS: os.system("start AcroRD32 ruta_y_archivo.pdf &")
    os.system("atril "+os.getcwd()+"/reportes/"+ self.usuario_pv + "-" + self.fecha + ".pdf &")



class PDF(FPDF):
    def header(self):
        self.fecha = str(time.strftime("%d") + "-" + time.strftime("%m") + "-" + time.strftime("%Y"))
        # Logo
        self.image(os.getcwd() + "/iconos/cash_register.2.2.png", 500, 0, 79)
        # Tamaño y tipo de letra Arial bold 15
        self.set_font("Arial", "IB", 20)
        # mueve la posicion de la celda a la derecha
        self.cell(80)
        # titulo
        self.cell(250, 10, "Reporte de ventas realizado el dia: " + self.fecha, 0, 0, "C")
        self.ln(30)
        self.cell(80)
        self.cell(250, 10, "Empresa: Encom               Vendedor: ", 0, 0, "C")
        # definimos grosor de linea
        self.set_line_width(1)
        # creamos una linea
        self.line(0, 80, 595, 80)
        # salta a la linea 20
        self.ln(30)


    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 12)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

