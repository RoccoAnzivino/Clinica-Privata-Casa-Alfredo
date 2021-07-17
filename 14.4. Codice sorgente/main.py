import cgitb
import sys

from PyQt5.QtWidgets import QApplication

from utente.view_home_utente import ViewHomeUtente


if __name__ == '__main__':
    cgitb.enable(format='text')
    app = QApplication(sys.argv)
    utente_window = ViewHomeUtente()
    utente_window.show()
    sys.exit(app.exec_())
