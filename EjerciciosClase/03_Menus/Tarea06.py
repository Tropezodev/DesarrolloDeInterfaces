#Crea una aplicación con un componente tipo dock con un QTextEdit a la aplicación y un componente principal.
#Por defecto, el dock se situará en la parte superior de la ventana.
#Añadimos una acción «Imprimir en dock» que imprima en un dock «Acción Pulsada».
#Su atajo será Ctrl + P y, además, aparecerá en una barra de herramientas y en un menú.
#Su texto de ayuda será el siguiente: «Al ejecutar esta acción, se añadirá el texto "Acción pulsada" en el dock.
#Se puede lanzar por Menú > Imprimir en dock, con Ctrl + P o haciendo clic en el botón correspondiente de la barra de herramientas».
#Añadimos un botón ¿Qué es esto? a la aplicación con el comportamiento habitual

import os
import platform
from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QLabel, QDockWidget, QTextEdit, QWhatsThis

# Clase Ventana, hereda de QWidget, componente base
class Ventana(QMainWindow):
    # Constructor de la clase Ventana
    def __init__(self):
        # Llamada al constructor de la superclase
        super().__init__()
        # Asignamos el título de la ventana
        self.setWindowTitle("Ventana principal con menús")
        # Modificamos el tamaño de la ventana
        self.resize(500,500)
        
        #Creamos el objeto de Barra de Menús y le damos un atajo de teclado con "&"
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")
        
        #Creamos objetos con la ruta de los iconos
        ruta_a_imprimir_icon = os.path.join(os.path.dirname(__file__),"Imprimir.png")
        ruta_a_ayuda_icon = os.path.join(os.path.dirname(__file__),"Ayuda.png")
        
        #Creamos la acción de Imprimir, le damos el atajo de teclado, hacemos la conexión a la acción y la añadimos a la barra de menús
        imprimir = QAction(QIcon(ruta_a_imprimir_icon),"Imprimir en dock", self)
        imprimir.setWhatsThis('Al ejecutar esta acción, se añadirá el texto "Acción pulsada" en el dock. Se puede lanzar por Menú > Imprimir en dock, con Ctrl + P o haciendo clic en el botón correspondiente de la barra de herramientas.')
        imprimir.setShortcut(QKeySequence("Ctrl+p"))
        imprimir.triggered.connect(self.imprimir)
        menu.addAction(imprimir)
        
        #Creamos la acción Ayuda, hacemos la conexión a la acción y la añadimos a la barra de menús
        ayuda = QAction(QIcon(ruta_a_ayuda_icon),"Qué es esto?", self)
        ayuda.triggered.connect(self.ayuda)
        menu.addAction(ayuda)
        
        #Creamos la barra de herramientas y le añadimos las acciones de Imprimir y de Ayuda 
        barra_herramientas = QToolBar("Barra de herramientas")
        barra_herramientas.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        barra_herramientas.addAction(imprimir)
        barra_herramientas.addAction(ayuda)
        self.addToolBar(barra_herramientas)
        
        #Creamos el componente base del Dock
        dock = QDockWidget()
        dock.setWindowTitle("Dock")
        self.texto=QTextEdit("")
        dock.setWidget(self.texto)
        dock.setMinimumWidth(100)
        dock.setMinimumHeight(100)
        self.addDockWidget(Qt.TopDockWidgetArea, dock)
        
    def imprimir(self):
        self.texto.insertPlainText("Acción Pulsada\n")
        
    def ayuda(self):
        if QWhatsThis.inWhatsThisMode():
            QWhatsThis.leaveWhatsThisMode()
        else:
            QWhatsThis.enterWhatsThisMode()

if __name__ == "__main__":
    # Cada aplicación será una sola instancia de QApplication.
    app = QApplication([])
    # Creamos un objecto ventana.
    ventana = Ventana()
    # Mostramos la ventana, por defecto los componentes están ocultos.
    ventana.show()
    # Iniciamos el bucle de eventos.
    app.exec()
        
