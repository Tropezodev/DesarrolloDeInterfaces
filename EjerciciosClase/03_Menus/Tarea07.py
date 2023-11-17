#Vamos a crear un editor de texto plano muy simple con el aspecto que ves en la imagen.
#Tendrá tres acciones:
#Abrir archivo, en el menú y en la barra de herramientas. Atajo: Ctrl + o
#Guardar archivo, en el menú y en la barra de herramientas. Atajo: Ctrl + s
#Salir, en el menú. Atajo: Ctrl + q
#El archivo en donde guarda o que puede cargar siempre será el mismo, archivo.txt, y estará situado en la misma ruta que el ejecutable.
#Al guardar, el archivo se sobrescribirá

import os
import platform
from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QToolBar, QLabel, QDockWidget, QTextEdit, QWhatsThis

#Clase Ventana, hereda de QWidget, componente base
class Ventana(QMainWindow):
    #Constructor de la clase Ventana
    def __init__(self):
        #Llamada al constructor de la superclase
        super().__init__()
        #Asignamos el título de la ventana
        self.setWindowTitle("Editor de texto plano")
        #Modificamos el tamaño de la ventana
        self.resize(500,500)

        #Creamos el objeto con las rutas de los iconos
        path_abrir_icon = os.path.join(os.path.dirname(__file__),"Abrir.png")
        path_guardar_icon = os.path.join(os.path.dirname(__file__),"Guardar.png")
        path_salir_icon = os.path.join(os.path.dirname(__file__),"Salir.png")
        
        #Creamos la accón Abrir Archivo, le damos el atajo de teclado y hacemos la conexión
        acc_abrir = QAction(QIcon(path_abrir_icon),"Abrir archivo", self)
        acc_abrir.setShortcut(QKeySequence("Ctrl+o"))
        acc_abrir.triggered.connect(self.fun_abrir)
        
        #Creamos la accón Guardar Archivo, le damos el atajo de teclado, hacemos la conexión
        acc_guardar = QAction(QIcon(path_guardar_icon),"Guardar archivo", self)
        acc_guardar.setShortcut(QKeySequence("Ctrl+s"))
        acc_guardar.triggered.connect(self.fun_guardar)
        
        #Creamos las Acción Salir, le damos el atajo de teclado y hacemos la conexión
        acc_salir = QAction(QIcon(path_salir_icon),"Salir", self)
        acc_salir.setShortcut(QKeySequence("Ctrl+q"))
        acc_salir.triggered.connect(self.fun_salir)

        #Creamos el objeto de Barra de Menús, le damos un atajo de teclado con "&" y le añadimos las acciones Abrir, Guardar y Salir
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")
        menu.addAction(acc_abrir)
        menu.addAction(acc_guardar)
        menu.addAction(acc_salir)

        #Creamos la barra de herramientas, le damos estilos a los botones y le añadimos las acciones de Abrir y Guardar
        barra_herramientas = QToolBar("Barra de herramientas")
        barra_herramientas.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        barra_herramientas.addAction(acc_abrir)
        barra_herramientas.addAction(acc_guardar)
        self.addToolBar(barra_herramientas)

        #Creamos el componente base del Dock
        dock = QDockWidget()
        dock.setWindowTitle("Documento")
        self.texto=QTextEdit("")
        dock.setWidget(self.texto)
        dock.setMinimumWidth(100)
        dock.setMinimumHeight(100)
        self.addDockWidget(Qt.TopDockWidgetArea, dock)

    def fun_abrir(self):
        path_archivo = os.path.join(os.path.dirname(__file__),"archivo.txt")
        a = open(path_archivo,'r+')
        self.texto.setPlainText(a.read())
        
    def fun_guardar(self):
        path_archivo = os.path.join(os.path.dirname(__file__),"archivo.txt")
        a = open(path_archivo,'w+')
        b = self.texto.toPlainText()
        a.write(b)

    def fun_salir(self):
        exit ()

if __name__ == "__main__":
    #Cada aplicación será una sola instancia de QApplication.
    app = QApplication([])
    #Creamos un objecto ventana.
    ventana = Ventana()
    #Mostramos la ventana, por defecto los componentes están ocultos.
    ventana.show()
    #Iniciamos el bucle de eventos.
    app.exec()
        