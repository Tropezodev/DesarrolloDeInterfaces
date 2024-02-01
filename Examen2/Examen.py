from PySide6.QtWidgets import QApplication, QFormLayout, QPushButton, QWidget
from Components.Componente import EditorUsuario

class Ventana(QWidget):    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Examen: Ventana Registro")
        self.resize(350,100)
        
        self.input_user = EditorUsuario()
        register_btn = QPushButton("Registrar")
        
        form_layout = QFormLayout()
        form_layout.addRow('Usuario', self.input_user)
        form_layout.addWidget(register_btn)
        
        self.setLayout(form_layout)
        
        register_btn.clicked.connect(self.autentificar)
        self.input_user.register_signal.connect(self.autentificar2)
        
    def autentificar(self):
        auth = self.input_user.es_usuario_valido()
        if (auth):
            print(f'El usuario " {self.input_user.text()} " es válido')
        else:
            print(f'El usuario " {self.input_user.text()} " es inválido')

    def autentificar2(self, auth):
        if (auth):
            print(f'El usuario " {self.input_user.text()} " es válido')
        else:
            print(f'El usuario " {self.input_user.text()} " es inválido')
        
if __name__ == "__main__":
    app = QApplication([])
    ventana = Ventana()
    ventana.show()
    app.exec()