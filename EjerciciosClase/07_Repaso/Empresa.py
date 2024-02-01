import json
import os
from signal import signal
 
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QSpacerItem, QSizePolicy, QLineEdit
from PySide6.QtGui import QPixmap, QMouseEvent
from PySide6.QtCore import Qt, Signal, Property
class Empresa(QWidget):
    doble_clic = Signal(str)
    def __init__(self, empresa:str, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        self.logo = QLabel()
        self.logo.setMaximumSize(60, 60)
        self.logo.setScaledContents(True)
        self.path_logo = os.path.join(os.path.dirname(__file__), empresa['logo'])
        self.logo.setPixmap(QPixmap(self.path_logo))
        layout.addWidget(self.logo)
 
        layout_secundario = QVBoxLayout()
        layout.addLayout(layout_secundario)
        self.nombre = QLabel(empresa['nombre'])
        self.direccion = QLabel(empresa['direccion'])
        layout_secundario.addWidget(self.nombre)
        layout_secundario.addWidget(self.direccion)
 
    def mouseDoubleClickEvent(self, e):
        self.doble_clic.emit(
            f'{{"nombre":"{self.nombre.text()}","direccion":"{self.direccion.text()}","logo":"{self.path_logo}"}}'
        )