import re
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLineEdit


class EditorUsuario(QLineEdit):
    #Creamos la señal que se emitirá
    register_signal= Signal(bool)
  
    def __init__(self):
        super().__init__()
                   
    def es_usuario_valido(self):
         usuario=self.text()
         patron = r'^[A-Za-z][A-Za-z0-9_-]{3,13}[A-Za-z0-9]$'
         return re.match(patron, usuario) is not None

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.register_signal.emit(self.es_usuario_valido())