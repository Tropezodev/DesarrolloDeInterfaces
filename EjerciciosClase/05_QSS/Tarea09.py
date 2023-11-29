#Modifica  los estilos de una casilla de verificación (QCheckBox) para que se muestre como un interruptor.
#Los ficheros 1.png y 2.png serán las imágenes a modificar (adjuntadas como img en la tarea).

import os
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox

class Ventana(QMainWindow):
    #Constructor de la clase Ventana
    def __init__(self):
        #Llamada al constructor de la superclase
        super().__init__()
        #Asignamos el título de la ventana
        self.setWindowTitle("QSS CheckBox")

        #Creamos el diccionario de imágenes
        self.img_dict = {"checked":os.path.join(os.path.dirname(__file__),"1.png"), "unchecked":os.path.join(os.path.dirname(__file__),"2.png")}

        #Creamos el elemento QCheckBox y le damos estilos a través de una función para hacerlo modular
        self.interruptor = QCheckBox(self)
        self.interruptor.setStyleSheet(self.estilo_interruptor())
        
        #Establecemos el elemento como Widget central
        self.setCentralWidget(self.interruptor)
        
    #Creamos la función que devuelve los estilos (en el return) para el QCheckBox
    def estilo_interruptor(self):
        
        return """ QCheckBox {
            spacing: 5px;
            }

            QCheckBox::indicator {
                width: 200px;
                height: 250px;
            }
            QCheckBox::indicator:checked {
                image: url(%s);
            }
            QCheckBox::indicator:unchecked {
                image: url(%s);
            } """ % (self.img_dict["checked"].replace("\\", "/"), self.img_dict["unchecked"].replace("\\", "/"))
            #Las referencias al diccionario se le pasan por externa al comentario (%s) para que ejecuten su función

if __name__ == "__main__":
    #Cada aplicación será una sola instancia de QApplication.
    app = QApplication([])
    #Creamos un objecto ventana.
    ventana = Ventana()
    #Mostramos la ventana, por defecto los componentes están ocultos.
    ventana.show()
    #Iniciamos el bucle de eventos.
    app.exec()
        