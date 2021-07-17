from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

from personale_medico.controller.controller_personale_medico import ControllerPersonaleMedico

from tools.menu_a_tendina_personale_medico import MenuATendinaPersonaleMedico
from tools import ridimensiona_widget


class ViewHomePersonaleMedico(QWidget):

    def __init__(self, personale_medico):
        """
        Costruttore della classe ViewHomePersonaleMedico, nella quale vengono creati e mostrati tutti gli
        oggetti della Graphical User Interface (GUI) relativi alla suddetta view

        :param personale_medico: Variabile d'istanza che rappresenta un oggetto della classe PersonaleMedico
        :type personale_medico: PersonaleMedico
        """
        super().__init__()

        self.personale_medico = personale_medico

        self.logo = QtWidgets.QLabel(self)
        self.titolo = QtWidgets.QLabel(self)
        self.scritta = QtWidgets.QLabel(self)
        self.setup_ui(self)

        self.menu_a_tendina = MenuATendinaPersonaleMedico(self)

        self.controller_personale_medico = ControllerPersonaleMedico(self)

        ridimensiona_widget.ridimensiona_view(self)

    def setup_ui(self, home_personale_medico):
        """
        Funzione che crea e determina le caratteristiche degli oggetti della ViewHomePersonaleMedico

        :param home_personale_medico: Oggetto della view che rappresenta la view stessa
        :type home_personale_medico: ViewHomePersonaleMedico
        """
        home_personale_medico.setObjectName("home_personale_medico")
        home_personale_medico.move(0, 0)
        home_personale_medico.resize(1920, 1080)
        home_personale_medico.setMinimumSize(QtCore.QSize(1920, 1080))
        home_personale_medico.setMaximumSize(QtCore.QSize(1920, 1080))
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
        home_personale_medico.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Immagini/logo_casa_alfredo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        home_personale_medico.setWindowIcon(icon)
        home_personale_medico.setStyleSheet("")
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

        self.retranslate_ui(home_personale_medico)
        QtCore.QMetaObject.connectSlotsByName(home_personale_medico)

    def retranslate_ui(self, home_personale_medico):
        """
        Funzione che formatta il testo degli oggetti creati all'interno della view

        :param home_personale_medico: Oggetto della view che rappresenta la view stessa
        :type home_personale_medico: ViewHomePersonaleMedico
        """
        _translate = QtCore.QCoreApplication.translate
        home_personale_medico.setWindowTitle(_translate("home_personale_medico", "Clinica Casa Alfredo"))
        self.scritta.setText(_translate("home_personale_medico", "Via Don Luigi Sturzo, 27, Roccamorice(PE)\n"
                                                                 "Telefono: 085 875 2684\n"
                                                                 "Fax: 085 132 0297\n"
                                                                 "E-mail: info@casalfredo.it"))
