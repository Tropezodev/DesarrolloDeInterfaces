#Vamos a crear un editor de texto plano muy simple con el aspecto que ves en la imagen.
#Tendrá ocho acciones:
#Atajos:
    #Nuevo: Ctrl + n | Abrir: Ctrl + o | Guardar: Ctrl + g | Deshacer: Ctrl + z
    #Rehacer: Ctrl + y | Cortar : Ctrl + x | Copiar: Ctrl + c | Pegar: Ctrl + v
#El archivo en donde guarda o que puede cargar siempre será el mismo, archivo.txt, y estará situado en la misma ruta que el ejecutable.

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
        self.setWindowTitle("Editor de texto plano 2")
        #Modificamos el tamaño de la ventana
        self.resize(500,500)

        '''
        #Creamos el objeto con las rutas de los iconos
        path_abrir_icon = os.path.join(os.path.dirname(__file__),"abrir.png")
        path_copiar_icon = os.path.join(os.path.dirname(__file__),"copiar.png")
        path_cortar_icon = os.path.join(os.path.dirname(__file__),"cortar.png")
        path_deshacer_icon = os.path.join(os.path.dirname(__file__),"deshacer.png")
        path_guardar_icon = os.path.join(os.path.dirname(__file__),"guardar.png")
        path_nuevo_icon = os.path.join(os.path.dirname(__file__),"nuevo.png")
        path_pegar_icon = os.path.join(os.path.dirname(__file__),"pegar.png")
        path_rehacer_icon = os.path.join(os.path.dirname(__file__),"rehacer.png")
        '''
        
        #Creamos el Diccionario de imágenes
        img_dict = {"abrir":os.path.join(os.path.dirname(__file__),"abrir.png"),"copiar":os.path.join(os.path.dirname(__file__),"copiar.png"),
                    "cortar": os.path.join(os.path.dirname(__file__),"cortar.png"),"deshacer":os.path.join(os.path.dirname(__file__),"deshacer.png"),
                    "guardar":os.path.join(os.path.dirname(__file__),"guardar.png"),"nuevo":os.path.join(os.path.dirname(__file__),"nuevo.png"),
                    "pegar":os.path.join(os.path.dirname(__file__),"pegar.png"),"rehacer":os.path.join(os.path.dirname(__file__),"rehacer.png")}
        
        #Creamos el objeto con la ruta del archivo
        self.path_archivo = os.path.join(os.path.dirname(__file__),"archivo.txt")
        
        #Creamos la acción Nuevo, le damos el atajo de teclado y hacemos la conexión
        acc_nuevo = QAction(QIcon(img_dict["nuevo"]),"Nuevo", self)
        acc_nuevo.setShortcut(QKeySequence("Ctrl+n"))
        acc_nuevo.triggered.connect(self.fun_nuevo)
        
        #Creamos la acción Abrir, le damos el atajo de teclado y hacemos la conexión
        acc_abrir = QAction(QIcon(img_dict["abrir"]),"Abrir", self)
        acc_abrir.setShortcut(QKeySequence("Ctrl+o"))
        acc_abrir.triggered.connect(self.fun_abrir)
        
        #Creamos la acción Guardar, le damos el atajo de teclado, hacemos la conexión
        acc_guardar = QAction(QIcon(img_dict["guardar"]),"Guardar", self)
        acc_guardar.setShortcut(QKeySequence("Ctrl+s"))
        acc_guardar.triggered.connect(self.fun_guardar)
        
        #Creamos la acción Deshacer, le damos el atajo de teclado y hacemos la conexión
        acc_deshacer = QAction(QIcon(img_dict["deshacer"]),"Deshacer", self)
        acc_deshacer.setShortcut(QKeySequence("Ctrl+z"))
        acc_deshacer.triggered.connect(self.fun_deshacer)
        
        #Creamos las acción Rehacer, le damos el atajo de teclado y hacemos la conexión
        acc_rehacer = QAction(QIcon(img_dict["rehacer"]),"Rehacer", self)
        acc_rehacer.setShortcut(QKeySequence("Ctrl+y"))
        acc_rehacer.triggered.connect(self.fun_rehacer)
        
        #Creamos la acción Cortar, le damos el atajo de teclado y hacemos la conexión
        acc_cortar = QAction(QIcon(img_dict["cortar"]),"Cortar", self)
        acc_cortar.setShortcut(QKeySequence("Ctrl+x"))
        acc_cortar.triggered.connect(self.fun_cortar)
        
        #Creamos la acción Copiar, le damos el atajo de teclado y hacemos la conexión
        acc_copiar = QAction(QIcon(img_dict["copiar"]),"Copiar", self)
        acc_copiar.setShortcut(QKeySequence("Ctrl+c"))
        acc_copiar.triggered.connect(self.fun_copiar)
        
        #Creamos la acción Pegar, le damos el atajo de teclado y hacemos la conexión
        acc_pegar = QAction(QIcon(img_dict["pegar"]),"Pegar", self)
        acc_pegar.setShortcut(QKeySequence("Ctrl+v"))
        acc_pegar.triggered.connect(self.fun_pegar)

        #Creamos el objeto de Barra de Menús, creamos los menús Archivo y Editar le damos un atajo de teclado con "&"
        barra_menus = self.menuBar()
        archivo = barra_menus.addMenu("&Archivo")
        editar = barra_menus.addMenu("&Editar")
        
        #A cada menú le añadimos sus acciones.
        archivo.addActions([acc_nuevo,acc_abrir,acc_guardar,acc_deshacer,acc_rehacer])
        editar.addActions([acc_cortar,acc_copiar,acc_pegar])

        #Creamos la barra de herramientas, le damos estilos a los botones y le añadimos las acciones
        barra_herramientas = QToolBar("Barra de herramientas")
        barra_herramientas.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        barra_herramientas.addActions([acc_nuevo,acc_abrir,acc_guardar,acc_deshacer,acc_rehacer,acc_cortar,acc_copiar,acc_pegar])
        self.addToolBar(barra_herramientas)

        #Creamos el componente base del Dock
        dock = QDockWidget()
        dock.setWindowTitle("Documento")
        self.texto=QTextEdit("")
        dock.setWidget(self.texto)
        dock.setMinimumWidth(100)
        dock.setMinimumHeight(100)
        self.addDockWidget(Qt.TopDockWidgetArea, dock)

    def fun_nuevo(self):
        self.texto.setText("")

    def fun_abrir(self):
        a = open(self.path_archivo,'r+')
        self.texto.setPlainText(a.read())
        
    def fun_guardar(self):
        a = open(self.path_archivo,'w+')
        b = self.texto.toPlainText()
        a.write(b)
        
    def fun_deshacer(self):
        self.texto.undo()
        
    def fun_rehacer(self):
        self.texto.redo()
        
    def fun_cortar(self):
        self.texto.cut()
        
    def fun_copiar(self):
        self.texto.copy()
        
    def fun_pegar(self):
        self.texto.paste()


if __name__ == "__main__":
    #Cada aplicación será una sola instancia de QApplication.
    app = QApplication([])
    #Creamos un objecto ventana.
    ventana = Ventana()
    #Mostramos la ventana, por defecto los componentes están ocultos.
    ventana.show()
    #Iniciamos el bucle de eventos.
    app.exec()
        