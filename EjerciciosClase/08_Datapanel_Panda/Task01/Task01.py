from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QComboBox
from PySide6.QtCore import QUrl, QDir
from PySide6.QtWebEngineWidgets import QWebEngineView
 
class VentanaInformes(QWidget):
 
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout_vertical = QVBoxLayout()
        self.setLayout(self.layout_vertical)
 
        combo_informes = QComboBox()
        combo_informes.addItem('Task19.html')
        combo_informes.addItem('Task20.html')
        combo_informes.addItem('Task21.html')
        combo_informes.currentTextChanged.connect(self.cargar_informe)
        self.layout_vertical.addWidget(combo_informes)
        self.view = QWebEngineView()
        self.layout_vertical.addWidget(self.view)
        self.resize(800,600)
        self.cargar_informe('Task19.html')
    def cargar_informe(self, informe):        
        ruta_absoluta = QDir().absoluteFilePath('./' + informe)        
        self.view.load(QUrl.fromLocalFile(ruta_absoluta))
 
if __name__ == "__main__":
    app = QApplication([])
    ventana_informes = VentanaInformes()
    ventana_informes.show()
    app.exec()