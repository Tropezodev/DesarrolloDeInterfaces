# Importamos las clases a utilizar del módulo QtWidgets del paquete PySide6
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QComboBox
# Clases necesarias para los atajos de teclado
from PySide6.QtGui import Qt, QKeySequence

# Clase Ventana, hereda de QWidget, componente base
class Ventana(QWidget):
    # Constructor de la clase Ventana
    def __init__(self):
        # Llamada al constructor de la superclase
        super().__init__()
        
        # Asignamos el título de la ventana
        self.setWindowTitle("Conversor Temperatura (Fahrenheit y Celsius)")
        
        # Modificamos el tamaño de la ventana
        self.resize(300,150)
        
        # Creamos los elementos que se usarán en la ventana
            # Creo los QLabel necesarios
        self.resultado_label = QLabel("Resultado:")
        self.resultado_label.setFixedHeight(30)
        a_label = QLabel("a")
        a_label.setFixedSize(10,30)
        
            # Creo un QLineEdit para la temperatura
        self.temperatura_input = QLineEdit()
        self.temperatura_input.setFixedHeight(30)
        self.temperatura_input.setPlaceholderText("Ingrese temperatura")

            # Creo un QPushButton para convertir
        convertir_button = QPushButton("Convertir", self)
        
            # Creo 2 QComboBox
        self.temperatura1_combo = QComboBox()
        datos_combo= ["Celsius","Fahrenheit"]
        self.temperatura1_combo.setFixedSize(150,30)
        self.temperatura1_combo.addItems(datos_combo)

        self.temperatura2_combo = QComboBox()
        self.temperatura2_combo.setFixedSize(150,30)
        
        self.temperatura2_combo.addItems(datos_combo)
        
        # Creamos un objeto layout vertical con QVBoxLayout
        vlayout = QVBoxLayout()
        
        # Creammos un objeto layout horizontal con QHBoxLayout
        hlayout1 = QHBoxLayout()
        
        # Añadimos los elementos a los QHBoxLayout
        hlayout1.addWidget(self.temperatura1_combo)
        hlayout1.addWidget(a_label)
        hlayout1.addWidget(self.temperatura2_combo)

        # Añadimos los objetos al QVBoxLayout
        vlayout.addLayout(hlayout1)
        vlayout.addWidget(self.temperatura_input)
        vlayout.addWidget(convertir_button)
        vlayout.addWidget(self.resultado_label)
        
        # Establecemos el layout principal para la ventana
        self.setLayout(vlayout)
       
        # Al botón "login_button" le añado un atajo con la tecla "Enter". Al pulsar la tecla "Enter", el botón se activa.
        convertir_button.setShortcut(QKeySequence(Qt.Key_Return))
        
        # Conectamos el evento 
        convertir_button.clicked.connect(self.convertir)
    
    # Creamos el método "modificar" que establece que texto de la "etiqueta" será el texto del item seleccionado del combo
    def convertir (self):
        self.resultado_label.setStyleSheet("""
            color: "green";
            """)
        try:
            if (self.temperatura1_combo.currentText()=="Celsius" and self.temperatura2_combo.currentText()=="Celsius"):
                resultado = float(self.temperatura_input.text())
                self.resultado_label.setText(f"Resultado: {resultado} Celsius")
            elif (self.temperatura1_combo.currentText()=="Celsius" and self.temperatura2_combo.currentText()=="Fahrenheit"):
                resultado = float(self.temperatura_input.text())
                resultado = ((resultado*9/5)+32)
                self.resultado_label.setText(f"Resultado: {resultado} Fahrenheit")
            elif (self.temperatura1_combo.currentText()=="Fahrenheit" and self.temperatura2_combo.currentText()=="Fahrenheit"):
                resultado = float(self.temperatura_input.text())
                self.resultado_label.setText(f"Resultado: {resultado} Fahrenheit")
            else:
                resultado = float(self.temperatura_input.text())
                resultado = ((resultado-32)*5/9)
                self.resultado_label.setText(f"Resultado: {resultado} Fahrenheit")
        except:
            self.resultado_label.setStyleSheet("""
            color: "red";
            """)
            self.resultado_label.setText("Dato Introducido Erróneo")
            

if __name__ == "__main__":
    # Cada aplicación será una sola instancia de QApplication.
    app = QApplication([])
    # Creamos un objecto ventana.
    ventana = Ventana()
    # Mostramos la ventana, por defecto los componentes están ocultos.
    ventana.show()
    # Iniciamos el bucle de eventos.
    app.exec()