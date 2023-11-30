#Importamos las clases a utilizar
import os
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (QApplication, QMainWindow, QToolBar, QWhatsThis, QDockWidget, QLabel, QTextEdit)

#Clase Ventana, hereda de QWidget, componente base
class Ventana(QMainWindow):
    #Constructor de la clase Ventana
    def __init__(self):
        #Llamada al constructor de la superclase
        super().__init__()
        
        #Asignamos el título de la ventana
        self.setWindowTitle("¿Cual es la asignatura más importante?")
        
        #Modificamos el tamaño de la ventana
        self.resize(500,500)
        
        #Creamos el diccionario de imágenes
        self.img_dict = {"ayuda":os.path.join(os.path.dirname(__file__),"ayuda.png"), "libros":os.path.join(os.path.dirname(__file__),"libros.png")}
        
        #Creamos la accón Prioridad... le damos el atajo de teclado y hacemos la conexión
        acc_prio = QAction(QIcon(self.img_dict["libros"]),"Prioridad de asignaturas\n 2ºDAM", self)
        acc_prio.setShortcut(QKeySequence("Ctrl+p"))
        acc_prio.setStatusTip("Prioridad de asignaturas 2ºDAM")
        acc_prio.setWhatsThis("Nos indica cual es la asignatura más importante de 2ºDAM")
        acc_prio.triggered.connect(self.prioridadAsignaturas)
        
        #Creamos la acción Ayuda, hacemos la conexión a la acción
        acc_ayuda = QAction(QIcon(self.img_dict["ayuda"]),"Ayuda", self)
        acc_ayuda.setShortcut(QKeySequence("Shift+F1"))
        acc_ayuda.setStatusTip("Ayuda")
        acc_ayuda.setWhatsThis("Activamos el modo ayuda")
        acc_ayuda.triggered.connect(self.ayuda)
        
        #Creamos el objeto de Barra de Menús, le damos un atajo de teclado con "&" y le añadimos las acciones
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Asignaturas")
        menu.addAction(acc_prio)
        menu.addAction(acc_ayuda)
        
        #Creamos la barra de herramientas, le damos estilos a los botones y le añadimos las acciones
        barra_herramientas = QToolBar("Barra de herramientas")
        barra_herramientas.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        barra_herramientas.addAction(acc_prio)
        barra_herramientas.addAction(acc_ayuda)
        self.addToolBar(barra_herramientas)
        
        #Creamos el componente base del Dock
        dock = QDockWidget()
        dock.setWindowTitle("El subsconsciente del alumno")
        self.texto=QTextEdit("")
        dock.setWidget(self.texto)
        dock.setMinimumWidth(100)
        dock.setMinimumHeight(100)
        self.addDockWidget(Qt.TopDockWidgetArea, dock)
        
    def prioridadAsignaturas(self):
        self.texto.insertPlainText("La asignatura más importante de 2ºDAM es Desarrollo de interfaces.\n")
        
    def ayuda(self):
        if QWhatsThis.inWhatsThisMode():
            QWhatsThis.leaveWhatsThisMode()
        else:
            QWhatsThis.enterWhatsThisMode()

if __name__ == "__main__":
    #Cada aplicación será una sola instancia de QApplication.
    app = QApplication([])
    #Creamos un objecto ventana.
    ventana = Ventana()
    #Mostramos la ventana, por defecto los componentes están ocultos.
    ventana.show()
    #Iniciamos el bucle de eventos.
    app.exec()