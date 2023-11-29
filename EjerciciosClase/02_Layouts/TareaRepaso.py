# Importamos las clases a utilizar del módulo QtWidgets del paquete PySide6
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QFormLayout
# Clases necesarias para los atajos de teclado
from PySide6.QtGui import Qt, QKeySequence

# Clase Ventana, hereda de QWidget, componente base
class Ventana(QWidget):
    # Constructor de la clase Ventana
    def __init__(self):
        # Llamada al constructor de la superclase
        super().__init__()
        
        # Asignamos el título de la ventana
        self.setWindowTitle("Login")
        
        # Modificamos el tamaño de la ventana
        self.resize(300,150)
        
        # Creo un label para la salida
        self.salida_label = QLabel(self)
        
        # Creo un QLineEdit para el usuario
        self.usuario_input = QLineEdit()
        self.usuario_input.setPlaceholderText("usuario")
        # Creo un QLineEdit con el EchoMode en Password para la contra
        self.contra_input = QLineEdit()
        self.contra_input.setPlaceholderText("contraseña")
        self.contra_input.setEchoMode(QLineEdit.EchoMode.Password)
        # Creo un QPushButton para el login
        login_button = QPushButton("Login", self)
        
        #Creamos el QFormLayout
        form_layout = QFormLayout()
        
        form_layout.addRow('Usuario', self.usuario_input)
        form_layout.addRow('Contraseña:', self.contra_input)
        form_layout.addWidget(login_button)
        form_layout.addWidget(self.salida_label)
        
        # Establecemos el layout principal para la ventana
        self.setLayout(form_layout)
        
        # Al botón "login_button" le añado un atajo con la tecla "Enter". Al pulsar la tecla "Enter", el botón se activa.
        login_button.setShortcut(QKeySequence(Qt.Key_Return))
        
        # Conectamos el evento 
        login_button.clicked.connect(self.autentificar)
    
    # Creamos el método "modificar" que establece que texto de la "etiqueta" será el texto del item seleccionado del combo
    def autentificar (self):
        if (self.usuario_input.text() == "Admin" and self.contra_input.text() == "Admin"):
            self.salida_label.setText("Usuario Correcto")
            self.salida_label.setStyleSheet("""
            color: "green";
            """)
        else:
            self.salida_label.setText("Usuario Incorrecto")
            self.salida_label.setStyleSheet("""
            color: "red";
            """)

if __name__ == "__main__":
    # Cada aplicación será una sola instancia de QApplication.
    app = QApplication([])
    # Creamos un objecto ventana.
    ventana = Ventana()
    # Mostramos la ventana, por defecto los componentes están ocultos.
    ventana.show()
    # Iniciamos el bucle de eventos.
    app.exec()
        
        