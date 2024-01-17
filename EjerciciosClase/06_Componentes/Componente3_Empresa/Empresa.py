#Desarrolla un componente Empresa que nos muestre información de una empresa.
#Constará del logo de la empresa, el nombre y la dirección.
#Además, definiremos una señal que se emitirá al hacer doble click sobre el componente Empresa,
#enviando junto con esta la información de la empresa.

import json
import os
from signal import signal

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QSpacerItem, QSizePolicy, QLineEdit
from PySide6.QtGui import QPixmap, QMouseEvent, QIcon
from PySide6.QtCore import Qt, Signal, Property

class QWidgetMod(QWidget):
    
    #Creamos la señal que se emitirá al hacer doble click
    double_click = Signal(str)
  
    #Constructor de la clase QWidgetMod
    def __init__(self, empresa_dict:str, parent=None):
        
        #Llamada al constructor de la superclase
        super().__init__()
        
        #Asignamos el título de la ventana
        self.setWindowTitle("Componente Empresa")
        
        #Creamos los elementos del componente en referencia al diccionario que se va a obtener por parámetro en el constructor
        img = QPixmap(empresa_dict["img"])
        img_lb=QLabel(self)
        img_lb.setPixmap(img)
        
        name = QLabel(empresa_dict["name"])
        address = QLabel(empresa_dict["adress"])
        
        #Creamos el Layout
        layout = QHBoxLayout()
        
        hLayoud1 = QVBoxLayout()
        hLayoud2 = QVBoxLayout()
        
        hLayoud1.addWidget(img_lb)
        hLayoud2.addWidget(name)
        hLayoud2.addWidget(address)
        
        layout.addLayout(hLayoud1)
        layout.addLayout(hLayoud2)
        self.setLayout(layout)
        
        #Juntamos los String de los elementos a uno solo
        self.data = f'-Rutal del icono: {empresa_dict["img"]}\n -Nombre de la empresa: {empresa_dict["name"]}\n -Dirección de la empresa: {empresa_dict["adress"]}'
        
    #Redefinimos la función mouseDoubleClickEvent (override) para que emita la señal double_click
    def mouseDoubleClickEvent(self,e):
        
        #Conectamos la señal y emitimos con los datos del componente
        self.double_click.emit(self.data)

# Para probar el componente creamos una clase ventana que llame al componenete
# Clase Ventana, hereda de QMainWindow, componente base
class Ventana(QMainWindow):
    
    # Constructor de la clase Ventana
    def __init__(self):
        
        # Llamada al constructor de la superclase
        super().__init__()
        
        # Asignamos el título de la ventana
        self.setWindowTitle("Empresa")
        
        #Creamos el diccionario que le vamos a pasar por parámetro
        empresa_dict= {"img":os.path.join(os.path.dirname(__file__),"Pepo.png"),"name":"PepoInc","adress":"Calle Falsa 123"}
        
        #Instanciamos el componente QWidgetMod con el diccionario como parámetro
        empresa = QWidgetMod(empresa_dict)
        
        #Establecemos el componente como widget central
        self.setCentralWidget(empresa)

#Punto de entrada para la aplicación
if __name__ == "__main__":
    
    # Cada aplicación será una sola instancia de QApplication.
    app = QApplication([])
    
    # Creamos un objecto ventana.
    ventana = Ventana()
    
    # Mostramos la ventana, por defecto los componentes están ocultos.
    ventana.show()
    
    # Iniciamos el bucle de eventos.
    app.exec()