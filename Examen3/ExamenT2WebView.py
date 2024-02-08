from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QComboBox
from PySide6.QtCore import QUrl, QDir
from PySide6.QtWebEngineWidgets import QWebEngineView
 
class VentanaInformes(QWidget):
 
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout_vertical = QVBoxLayout()
        self.setLayout(self.layout_vertical)
 
        combo_informes = QComboBox()
        combo_informes.addItem('ExamenT2.html')
        combo_informes.addItem('ExamenT2_1.html')
        combo_informes.addItem('ExamenT2_2.html')
        combo_informes.currentTextChanged.connect(self.cargar_informe)
        self.layout_vertical.addWidget(combo_informes)
        self.view = QWebEngineView()#Se inicializa fuera de la función para cargarle el informe por defecto
        self.layout_vertical.addWidget(self.view)
        self.resize(800,600)
        self.cargar_informe('ExamenT2.html')#Aquí se carga el informe
    def cargar_informe(self, informe):        
        ruta_absoluta = QDir().absoluteFilePath('./' + informe)        
        self.view.load(QUrl.fromLocalFile(ruta_absoluta))
 
if __name__ == "__main__":
    app = QApplication([])
    ventana_informes = VentanaInformes()
    ventana_informes.show()
    app.exec()