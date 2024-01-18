#Crea otro componente Empresas que contenga una lista de empresas dentro de un �rea de desplazamiento (QScrollArea).
#Tambi�n emitir� una se�al con el nombre de empresa que ha recibido el doble clic.

import json
import os
from signal import signal
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QSpacerItem, QSizePolicy, QLineEdit
from PySide6.QtGui import QPixmap, QMouseEvent, QIcon
from PySide6.QtCore import Qt, Signal, Property

class ListaEmpresas(QScrollArea):
    
    #Creamos la se�al que se emitir� al hacer doble click
    double_click = Signal(str)
  
    #Constructor de la clase QWidgetMod
    def __init__(self, empresas_dict:str, parent=None):
        
        #Llamada al constructor de la superclase
        super().__init__()
        
        #Creamos el Widget que se a�adir� al QScrollArea
        self.empresa = QWidget()
        
        #Creamos el layout de empresa para a�adirle los QWidget
        layout = QVBoxLayout()
        

        self.empresa.setLayout(layout)
        
        #Juntamos los String de los elementos a uno solo
        self.data = f'  -Rutal del icono: {empresa_dict["img"]}\n  -Nombre de la empresa: {empresa_dict["name"]}\n  -Direcci�n de la empresa: {empresa_dict["adress"]}'
        
    #Redefinimos la funci�n mouseDoubleClickEvent (override) para que emita la se�al double_click
    def mouseDoubleClickEvent(self,e):
        
        #Conectamos la se�al y emitimos con los datos del componente
        self.double_click.emit(self.data)

# Para probar el componente creamos una clase ventana que llame al componenete
# Clase Ventana, hereda de QMainWindow, componente base
class Ventana(QMainWindow):
    
    # Constructor de la clase Ventana
    def __init__(self):
        
        # Llamada al constructor de la superclase
        super().__init__()
        
        # Asignamos el t�tulo de la ventana
        self.setWindowTitle("Empresa")
        
        #Creamos el diccionario que le vamos a pasar por par�metro
        empresas_dict= {
                        0:{"img":os.path.join(os.path.dirname(__file__),"Pepo.png"),"name":"PepoInc0","adress":"Calle Falsa 1"},
                        1:{"img":os.path.join(os.path.dirname(__file__),"Pepo.png"),"name":"PepoInc1","adress":"Calle Falsa 2"},
                        2:{"img":os.path.join(os.path.dirname(__file__),"Pepo.png"),"name":"PepoInc2","adress":"Calle Falsa 3"},
                        3:{"img":os.path.join(os.path.dirname(__file__),"Pepo.png"),"name":"PepoInc3","adress":"Calle Falsa 4"},
                        4:{"img":os.path.join(os.path.dirname(__file__),"Pepo.png"),"name":"PepoInc4","adress":"Calle Falsa 5"},
                        5:{"img":os.path.join(os.path.dirname(__file__),"Pepo.png"),"name":"PepoInc5","adress":"Calle Falsa 6"}
                       }
        
        #Instanciamos el componente QWidgetMod con el diccionario como par�metro
        empresa = QWidgetMod(empresa_dict)
        
        #Establecemos el componente como widget central
        self.setCentralWidget(empresa)

        #Conectamos la se�al "double_click" al m�todo recibir_datos
        empresa.double_click.connect(self.recibir_datos)
        
    #El m�todo recibir_datos imprime los datos recibidos como par�metro de la se�al double_click
    def recibir_datos(self, data):
        print(data)

#Punto de entrada para la aplicaci�n
if __name__ == "__main__":
    
    # Cada aplicaci�n ser� una sola instancia de QApplication.
    app = QApplication([])
    
    # Creamos un objecto ventana.
    ventana = Ventana()
    
    # Mostramos la ventana, por defecto los componentes est�n ocultos.
    ventana.show()
    
    # Iniciamos el bucle de eventos.
    app.exec()