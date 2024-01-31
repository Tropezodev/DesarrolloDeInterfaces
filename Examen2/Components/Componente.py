from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLineEdit


class QPassword(QLineEdit):
    #Creamos la señal que se emitirá al hacer """"""
    #"""""" = Signal(""""")
  
    def __init__(self):
        super().__init__()
        
        