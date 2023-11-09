
# Importamos las clases QApplication, QLabel, QWidget y QLineEdit
# del módulo QtWidgets del paquete PySide6
from PySide6.QtWidgets import QApplication, QWidget, QComboBox

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
        # Creamos un combobox con la ventana como parent
        self.combo = QComboBox(self)
        # Modificamos el tamaño del combobox
        self.combo.setFixedSize(100,30)
        #Creamos una Arraylist con los datos del combobox
        meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
        # Añadimos los items al combobox
        self.combo.addItems(meses)
        # Conectamos el evento de activated al método "modificar"
        self.combo.activated.connect(self.modificar)
    
    # Creamos el método "modificar" que establece que texto de la "etiqueta" será el texto del item seleccionado del combo
    def modificar (self):
        print(f'El mes {self.combo.currentIndex()+1} es: {self.combo.currentText()}')
        


if __name__ == "__main__":
    # Cada aplicación será una sola instancia de QApplication.
    app = QApplication([])
    # Creamos un objecto ventana.
    ventana1 = Ventana()
    # Mostramos la ventana, por defecto los componentes están ocultos.
    ventana1.show()
    # Iniciamos el bucle de eventos.
    app.exec()