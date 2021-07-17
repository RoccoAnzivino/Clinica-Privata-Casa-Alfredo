from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

from paziente.controller.controller_paziente import ControllerPaziente

from tools.menu_a_tendina_paziente import MenuATendinaPaziente
from tools import ridimensiona_widget


class ViewHomePaziente(QWidget):

    def __init__(self, paziente):
        """
        Costruttore della classe ViewHomePaziente, nella quale vengono creati e mostrati tutti gli oggetti della
        Graphical User Interface (GUI) relativi alla suddetta view

        :param paziente: Variabile d'istanza che rappresenta un oggetto della classe Paziente
        :type paziente: Paziente
        """
        super().__init__()

        self.paziente = paziente

        self.logo = QtWidgets.QLabel(self)
        self.titolo = QtWidgets.QLabel(self)
        self.scritta = QtWidgets.QLabel(self)
        self.setup_ui(self)

        self.menu_a_tendina = MenuATendinaPaziente(self)

        self.controller_paziente = ControllerPaziente(self)

        ridimensiona_widget.ridimensiona_view(self)

    def setup_ui(self, home_paziente):
        """
        Funzione che crea e determina le caratteristiche degli oggetti della ViewHomePaziente

        :param home_paziente: Oggetto della view che rappresenta la view stessa
        :type home_paziente: ViewHomePaziente
        """
        home_paziente.setObjectName("home_paziente")
        home_paziente.move(0, 0)
        home_paziente.resize(1920, 1080)
        home_paziente.setMinimumSize(QtCore.QSize(1920, 1080))
        home_paziente.setMaximumSize(QtCore.QSize(1920, 1080))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        home_paziente.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Immagini/logo_casa_alfredo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        home_paziente.setWindowIcon(icon)
        home_paziente.setStyleSheet("")
        self.logo.setGeometry(QtCore.QRect(685, 62, 550, 620))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Immagini/logo_casa_alfredo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.titolo.setGeometry(QtCore.QRect(410, 620, 1100, 140))
        self.titolo.setText("")
        self.titolo.setPixmap(QtGui.QPixmap("Immagini/titolo_casa_alfredo.png"))
        self.titolo.setScaledContents(True)
        self.titolo.setObjectName("titolo")
        self.scritta.setGeometry(QtCore.QRect(695, 820, 530, 130))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(24)
        self.scritta.setFont(font)
        self.scritta.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.scritta.setObjectName("scritta")

        self.retranslate_ui(home_paziente)
        QtCore.QMetaObject.connectSlotsByName(home_paziente)

    def retranslate_ui(self, home_paziente):
        """
        Funzione che formatta il testo degli oggetti creati all'interno della view

        :param home_paziente: Oggetto della view che rappresenta la view stessa
        :type home_paziente: ViewHomePaziente
        """
        _translate = QtCore.QCoreApplication.translate
        home_paziente.setWindowTitle(_translate("home_paziente", "Clinica Casa Alfredo"))
        self.scritta.setText(_translate("home_paziente", "Via Don Luigi Sturzo, 27, Roccamorice(PE)\n"
                                                         "Telefono: 085 875 2684\n"
                                                         "Fax: 085 132 0297\n"
                                                         "E-mail: info@casalfredo.it"))
