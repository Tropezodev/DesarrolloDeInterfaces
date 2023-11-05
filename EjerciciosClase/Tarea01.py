
# Importamos las clases QApplication, QLabel, QWidget y QLineEdit
# del módulo QtWidgets del paquete PySide6
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit

# Clase Ventana, hereda de QWidget, componente base
class Ventana(QWidget):
    # Constructor de la clase Ventana
    def __init__(self):
        # Llamada al constructor de la superclase
        super().__init__()
        # Asignamos el título de la ventana
        self.setWindowTitle("Ventana")
        #┘Modificamos el tamaño de la ventana
        self.resize(80,30)
        # Creamos una etiqueta con la ventana como parent
        self.etiqueta = QLabel(self)
        # Modificamos el tamaño de la etiqueta
        self.etiqueta.setFixedSize(50,30)
        # Movemos la etiqueta 50px a la derecha
        self.etiqueta.move(50,0)
        # Creamos una línea con la ventana como parent
        self.linea = QLineEdit(self)
        # Marcamos el tamaño máximo de la línea en 5 carácteres
        self.linea.setMaxLength(5)
        # Modificamos el tamaño de la línea
        self.linea.setFixedSize(50,30)
        # Conectamos el evento de textChanged (modificación de texto) al método "modificar"
        self.linea.textChanged.connect(self.modificar)
    
    # Creamos el método "modificar" que establece que texto de la "etiqueta" será el texto de la "línea"
    def modificar (self):
        self.etiqueta.setText(self.linea.text())
        


if __name__ == "__main__":
    # Cada aplicación será una sola instancia de QApplication.
    app = QApplication([])
    # Creamos un objecto ventana.
    ventana1 = Ventana()
    # Mostramos la ventana, por defecto los componentes están ocultos.
    ventana1.show()
    # Iniciamos el bucle de eventos.
    app.exec()