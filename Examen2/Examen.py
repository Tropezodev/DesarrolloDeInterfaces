


#Importamos el componente
from PySide6.QtWidgets import QApplication, QMainWindow
from Components.Componente import 

class Ventana(QMainWindow):    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.resize(300,150)
        












if __name__ == "__main__":
    app = QApplication([])
    ventana = Ventana()
    ventana.show()
    app.exec()