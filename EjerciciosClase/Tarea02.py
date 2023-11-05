
# Importamos las clases QApplication, QLabel, QWidget y QLineEdit
# del módulo QtWidgets del paquete PySide6
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QComboBox

# Clase Ventana, hereda de QWidget, componente base
class Ventana(QWidget):
    # Constructor de la clase Ventana
    def __init__(self):
        # Llamada al constructor de la superclase
        super().__init__()
        # Asignamos el título de la ventana
        self.setWindowTitle("Ventana")
        #┘Modificamos el tamaño de la ventana
        self.resize(200,30)
        # Creamos una etiqueta con la ventana como parent
        self.etiqueta = QLabel(self)
        # Modificamos el tamaño de la etiqueta
        self.etiqueta.setFixedSize(50,30)
        # Movemos la etiqueta 50px a la derecha
        self.etiqueta.move(100,0)
        # Creamos un combobox con la ventana como parent
        self.combo = QComboBox(self)
        # Modificamos el tamaño del combo
        self.combo.setFixedSize(80,30)
        # Añadimos los items al combo
        self.combo.addItem("Opción1",self)
        self.combo.addItem("Opción2",self)
        self.combo.addItem("Opción3",self)
        # Conectamos el evento de currentTextChanged (texto actual) al método "modificar"
        self.combo.currentTextChanged.connect(self.modificar)
        # Cuando quieres que se de la señal al clicar en cualquier opción en vez de cada vez que cambie el texto: se usa el combo.activated
        # self.combo.activated.connect(self.modificar)
    
    # Creamos el método "modificar" que establece que texto de la "etiqueta" será el texto del item seleccionado del combo
    def modificar (self):
        self.etiqueta.setText(self.combo.currentText())
        


if __name__ == "__main__":
    # Cada aplicación será una sola instancia de QApplication.
    app = QApplication([])
    # Creamos un objecto ventana.
    ventana1 = Ventana()
    # Mostramos la ventana, por defecto los componentes están ocultos.
    ventana1.show()
    # Iniciamos el bucle de eventos.
    app.exec()