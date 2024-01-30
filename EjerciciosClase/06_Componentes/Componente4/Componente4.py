import json
import os
from signal import signal

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QSpacerItem, QSizePolicy, QLineEdit
from PySide6.QtGui import QPixmap, QMouseEvent
from PySide6.QtCore import Qt, Signal, Property

from Empresa import QWidgetMod

class Empresas(QScrollArea):
    empresa_seleccionada = Signal(str)
    def __init__(self, empresas, parent=None):
        super().__init__(parent)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
 
        self.empresas = []
 
        self.widget = QWidget()
        self.setWidget(self.widget)
        self.empresasLayout = QVBoxLayout()
 
        for empresa in empresas:
            new_empresa = QWidgetMod(empresa)
            new_empresa.double_click.connect(self.dobleclick_empresa)
            self.empresasLayout.addWidget(new_empresa)
            self.empresas.append(new_empresa)
 
        # Para que una empresa ocupe verticalmente lo que le corresponde aunque se redimensione el scrollarea
        espaciador = QSpacerItem(5, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)  
        self.empresasLayout.addSpacerItem(espaciador)
 
        self.widget.setLayout(self.empresasLayout)
 
    def dobleclick_empresa(self, json_empresa):
        self.empresa_seleccionada.emit(json_empresa)
        
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.datos = [{
            "img": os.path.join(os.path.dirname (__file__), "Pepo.png"),
            "name": "Cesur S.L",
            "address": "Calle 4567"
            },
                      {
            "img": os.path.join(os.path.dirname (__file__), "Pepo.png"),
            "name": "PepoInc S.L",
            "address": "Calle 1234"
            },
            {
            "img": os.path.join(os.path.dirname (__file__), "Pepo.png"),
            "name": "Pipos S.L",
            "address": "Calle 3456"
            }]
        self.empresa = Empresas(self.datos)
        layout.addWidget(self.empresa)
        self.setCentralWidget(self.empresa)
        self.empresa.empresa_seleccionada.connect(self.detectEvent)
    def detectEvent(self, e):
        print(e)
        
if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
        




