from PyQt5.QtWidgets import QApplication
import sys
from schermata_utente import Ui_schermataIniziale

if __name__ == '__main__':
    app = QApplication(sys.argv)
    utente_window = Ui_schermataIniziale()
    utente_window.show()
    sys.exit(app.exec_())
