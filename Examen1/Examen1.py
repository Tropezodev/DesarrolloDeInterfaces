#Importamos las clases a utilizar
import sys
from PySide6.QtWidgets import QApplication , QMainWindow , QWidget , QFormLayout , QVBoxLayout , QLabel, QLineEdit, QPushButton
# Clases necesarias para los atajos de teclado
from PySide6.QtGui import Qt, QKeySequence

#Clase Ventana, hereda de QWidget, componente base
class Ventana(QWidget):
    #Constructor de la clase Ventana
    def __init__(self):
        #Llamada al constructor de la superclase
        super().__init__()
        
        #Asignamos el título de la ventana
        self.setWindowTitle("Registro de Empleados")
        
        #Modificamos el tamaño de la ventana
        self.resize(300,150)
        
        #Creamos los elementos que se usarán en la ventana
        self.nombre_input = QLineEdit()
        self.edad_input = QLineEdit()
        self.direccion_input = QLineEdit()
        self.telefono_input = QLineEdit()
        self.cargo_input = QLineEdit()
        self.salario_input = QLineEdit()
        
        registrar_button = QPushButton("Registrar", self)
        
        self.registro_label = QLabel("Empleados Registrados:", self)
        
        #Creamos los Layouts que se van a usar
        princ_vlayout = QVBoxLayout()
        form_layout = QFormLayout()
        self.secun_vlayout = QVBoxLayout()

        #Añadimos los elementos al form_layout
        form_layout.addRow("Nombre: ", self.nombre_input)
        form_layout.addRow("Edad: ", self.edad_input)
        form_layout.addRow("Dirección: ", self.direccion_input)
        form_layout.addRow("Teléfono: ", self.telefono_input)
        form_layout.addRow("Cargo: ", self.cargo_input)
        form_layout.addRow("Salario: ", self.salario_input)
        
        #Añadimos los elementos al princ_vlayout
        princ_vlayout.addLayout(form_layout)
        princ_vlayout.addWidget(registrar_button)
        princ_vlayout.addWidget(self.registro_label)
        princ_vlayout.addLayout(self.secun_vlayout)
        
        # Establecemos el layout principal para la ventana
        self.setLayout(princ_vlayout)
        
        # Al botón "login_button" le añado un atajo con la tecla "Enter". Al pulsar la tecla "Enter", el botón se activa.
        registrar_button.setShortcut(QKeySequence(Qt.Key_Return))
        
        # Conectamos el evento 
        registrar_button.clicked.connect(self.registrarEmpleados)
        
    def registrarEmpleados(self):
        
        self.secun_vlayout.addWidget(QLabel(f"{self.nombre_input.text()} - {self.cargo_input.text()} - {self.salario_input.text()}"))
        self.nombre_input.clear()
        self.edad_input.clear()
        self.direccion_input.clear()
        self.telefono_input.clear()
        self.cargo_input.clear()
        self.salario_input.clear()

if __name__ == "__main__":
    # Cada aplicación será una sola instancia de QApplication.
    app = QApplication([])
    # Creamos un objecto ventana.
    ventana = Ventana()
    # Mostramos la ventana, por defecto los componentes están ocultos.
    ventana.show()
    # Iniciamos el bucle de eventos.
    app.exec()