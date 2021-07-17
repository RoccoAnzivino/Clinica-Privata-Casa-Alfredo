from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

from paziente.controller import controller_lista_prenotazioni_pazienti

from tools.tool_label_prenotazioni import LabelPrenotazioni
from tools.menu_a_tendina_paziente import MenuATendinaPaziente
from tools import ridimensiona_widget


class ViewListaPrenotazioni(QWidget):

    def __init__(self, paziente):
        """
        Costruttore della classe ViewListaPrenotazioni, nella quale vengono creati e mostrati tutti gli oggetti della
        Graphical User Interface (GUI) relativi alla suddetta view

        :param paziente: Variabile d'istanza che rappresenta un oggetto della classe Paziente
        :type paziente: Paziente
        """
        super().__init__()

        self.paziente = paziente

        self.le_mie_prenotazioni = QtWidgets.QLabel(self)
        self.i_miei_pazienti = QtWidgets.QLabel(self)
        self.logo = QtWidgets.QLabel(self)
        self.titolo = QtWidgets.QLabel(self)
        self.tabella = QtWidgets.QScrollArea(self)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.nome = QtWidgets.QLabel(self)
        self.attivita_ambulatoriale = QtWidgets.QLabel(self)
        self.medico = QtWidgets.QLabel(self)
        self.data_e_ora = QtWidgets.QLabel(self)
        self.apri = QtWidgets.QLabel(self)
        self.setup_ui(self)

        self.menu_a_tendina = MenuATendinaPaziente(self)

        self.controller_prenotazioni = controller_lista_prenotazioni_pazienti.ControllerListaPrenotazioniPazienti(self)

        self.tool_prenotazioni_paziente = LabelPrenotazioni(self, self.tabella, self.paziente,
                                                            self.scrollAreaWidgetContents,
                                                            self.controller_prenotazioni.lista_prenotazioni_paziente)

        ridimensiona_widget.ridimensiona_view(self)

    def setup_ui(self, prenotazioni_paziente):
        """
        Funzione che crea e determina le caratteristiche degli oggetti della ViewListaPrenotazioni

        :param prenotazioni_paziente: Oggetto della view che rappresenta la view stessa
        :type prenotazioni_paziente: ViewListaPrenotazioni
        """
        prenotazioni_paziente.setObjectName("prenotazioni_paziente")
        prenotazioni_paziente.move(0, 0)
        prenotazioni_paziente.resize(1920, 1080)
        prenotazioni_paziente.setMinimumSize(QtCore.QSize(1920, 1080))
        prenotazioni_paziente.setMaximumSize(QtCore.QSize(1920, 1080))
        prenotazioni_paziente.setMinimumSize(QtCore.QSize(1920, 1080))
        prenotazioni_paziente.setMaximumSize(QtCore.QSize(1920, 1080))
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
        prenotazioni_paziente.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Immagini/logo_casa_alfredo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        prenotazioni_paziente.setWindowIcon(icon)
        prenotazioni_paziente.setStyleSheet("")
        self.le_mie_prenotazioni.setGeometry(QtCore.QRect(530, 20, 981, 131))
        self.i_miei_pazienti.setGeometry(QtCore.QRect(530, 20, 981, 131))

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.le_mie_prenotazioni.setFont(font)
        self.le_mie_prenotazioni.setStyleSheet("color: rgb(84, 149, 223);")
        self.le_mie_prenotazioni.setObjectName("le_mie_prenotazioni")
        self.logo.setGeometry(QtCore.QRect(10, 5, 110, 130))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Immagini/logo_casa_alfredo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.titolo.setGeometry(QtCore.QRect(110, 20, 401, 110))
        self.titolo.setText("")
        self.titolo.setPixmap(QtGui.QPixmap("Immagini/titolo_casa_alfredo.png"))
        self.titolo.setScaledContents(True)
        self.titolo.setObjectName("titolo")
        self.tabella.setGeometry(QtCore.QRect(30, 160, 1811, 890))
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
        self.tabella.setPalette(palette)
        self.tabella.setStyleSheet("border: 0px solid;\n"
                                   "background-color: rgb(255, 255, 255);")
        self.tabella.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tabella.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tabella.setObjectName("tabella")

        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1811, 890))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.nome.setGeometry(QtCore.QRect(30, 160, 280, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.nome.setFont(font)
        self.nome.setStyleSheet("background-color: rgb(13, 41, 73);\n"
                                "color: rgb(255, 255, 255);\n"
                                "border: 2px solid;")
        self.nome.setAlignment(QtCore.Qt.AlignCenter)
        self.nome.setObjectName("nome")
        self.attivita_ambulatoriale.setGeometry(QtCore.QRect(308, 160, 575, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.attivita_ambulatoriale.setFont(font)
        self.attivita_ambulatoriale.setStyleSheet("background-color: rgb(13, 41, 73);\n"
                                                  "color: rgb(255, 255, 255);\n"
                                                  "border: 2px solid;")
        self.attivita_ambulatoriale.setAlignment(QtCore.Qt.AlignCenter)
        self.attivita_ambulatoriale.setObjectName("attivita_ambulatoriale")
        self.medico.setGeometry(QtCore.QRect(881, 160, 353, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.medico.setFont(font)
        self.medico.setStyleSheet("background-color: rgb(13, 41, 73);\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "border: 2px solid;")
        self.medico.setAlignment(QtCore.Qt.AlignCenter)
        self.medico.setObjectName("medico")
        self.data_e_ora.setGeometry(QtCore.QRect(1232, 160, 500, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.data_e_ora.setFont(font)
        self.data_e_ora.setStyleSheet("background-color: rgb(13, 41, 73);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border: 2px solid;")
        self.data_e_ora.setAlignment(QtCore.Qt.AlignCenter)
        self.data_e_ora.setObjectName("data_e_ora")
        self.apri.setGeometry(QtCore.QRect(1730, 160, 90, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.apri.setFont(font)
        self.apri.setStyleSheet("background-color: rgb(13, 41, 73);\n"
                                "color: rgb(255, 255, 255);\n"
                                "border: 2px solid;")
        self.apri.setAlignment(QtCore.Qt.AlignCenter)
        self.apri.setObjectName("apri")

        self.retranslate_ui(prenotazioni_paziente)
        QtCore.QMetaObject.connectSlotsByName(prenotazioni_paziente)

    def retranslate_ui(self, prenotazioni_paziente):
        """
        Funzione che formatta il testo degli oggetti creati all'interno della view

        :param prenotazioni_paziente: Oggetto della view che rappresenta la view stessa
        :type prenotazioni_paziente: ViewListaPrenotazioni
        """
        _translate = QtCore.QCoreApplication.translate
        prenotazioni_paziente.setWindowTitle(_translate("prenotazioni_paziente", "Clinica Casa Alfredo"))
        self.le_mie_prenotazioni.setText(_translate("prenotazioni_paziente", "- Le Mie Prenotazioni"))
        self.nome.setText(_translate("prenotazioni_paziente", "Numero prenotazione"))
        self.attivita_ambulatoriale.setText(_translate("prenotazioni_paziente", "Attività ambulatoriale"))
        self.medico.setText(_translate("prenotazioni_paziente", "Medico"))
        self.data_e_ora.setText(_translate("prenotazioni_paziente", "Data e Ora"))
        self.apri.setText(_translate("prenotazioni_paziente", "Apri"))
