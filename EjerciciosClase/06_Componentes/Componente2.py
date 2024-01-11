#La mayoría de aplicaciones ofrecen la posibilidad de acceder a ellas a través de un pequeño formulario de login,
#de forma que solo las personas que tengan las credenciales pueden acceder a dicha información.
#Vamos a desarrollar un widget que pueda mostrar/ocultar el texto de la contraseña.

import os
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QLineEdit, QApplication

class QLineEditMod(QLineEdit):
    #Constructor de la clase Ventana
    def __init__(self):
        #Llamada al constructor de la superclase
        super().__init__()
        
        #Asignamos el título de la ventana
        self.setWindowTitle("Componente 2")
        
        #Ponemos el texto del QlineEdit en modo Password
        self.setEchoMode(QLineEdit.EchoMode.Password)
        
        #Creamos el Diccionario de iconos
        self.icon_dict = {"hidden":os.path.join(os.path.dirname(__file__),"hidden.png"),
                          "visible":os.path.join(os.path.dirname(__file__),"visible.png")}
        
        #Agregamos el icono a QLineEdit y lo situamos en la derecha
        self.action = self.addAction(QIcon(self.icon_dict["visible"]), QLineEdit.TrailingPosition)
        
        #Hacemos que la acción sea marcable
        self.action.setCheckable(True)
        
        #Conectamos la señal "toggled" a la función fun_passSwitcher
        self.action.toggled.connect(self.fun_passSwitcher)

    def fun_passSwitcher(self, checked):
        #Si la acción esta marcada (checked), cambiamos el icono a "hidden" y pasamos el texto del QlineEdit a modo Normal
        if (checked):
            self.action.setIcon(QIcon(self.icon_dict["hidden"]))
            self.setEchoMode(QLineEdit.EchoMode.Normal)
        #Si la acción no esta marcada, cambiamos el icono a "visible" y pasamos el texto del QlineEdit a modo Password
        else:
            self.action.setIcon(QIcon(self.icon_dict["visible"]))
            self.setEchoMode(QLineEdit.EchoMode.Password)


if __name__ == "__main__":
    # Cada aplicación será una sola instancia de QApplication.
    app = QApplication([])
    # Creamos un objecto ventana.
    ventana = QLineEditMod()
    # Mostramos la ventana, por defecto los componentes están ocultos.
    ventana.show()
    # Iniciamos el bucle de eventos.
    app.exec()