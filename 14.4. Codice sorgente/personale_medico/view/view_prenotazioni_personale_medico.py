from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

from personale_medico.controller.controller_lista_prenotazioni_personale_medico \
    import ControllerListaPrenotazioniPersonaleMedico

from tools.menu_a_tendina_personale_medico import MenuATendinaPersonaleMedico
from tools.tool_prenotazioni_personale_medico import ToolPrenotazioniPersonaleMedico
from tools import ridimensiona_widget


class ViewPrenotazioniPersonaleMedico(QWidget):

    def __init__(self, personale_medico):
        """
        Costruttore della classe ViewPrenotazioniPersonaleMedico, nella quale vengono creati e mostrati tutti gli
        oggetti della Graphical User Interface (GUI) relativi alla suddetta view

        :param personale_medico: Variabile d'istanza che rappresenta un oggetto della classe PersonaleMedico
        :type personale_medico: PersonaleMedico
        """
        super().__init__()

        self.personale_medico = personale_medico

        self.lista_prenotazioni = QtWidgets.QLabel(self)
        self.logo = QtWidgets.QLabel(self)
        self.titolo = QtWidgets.QLabel(self)
        self.tabella = QtWidgets.QScrollArea(self)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.nome = QtWidgets.QLabel(self)
        self.attivita_ambulatoriale = QtWidgets.QLabel(self)
        self.data_e_ora = QtWidgets.QLabel(self)
        self.visualizza_cartella_clinica = QtWidgets.QLabel(self)
        self.setup_ui(self)

        self.menu_a_tendina = MenuATendinaPersonaleMedico(self)

        self.controller_prenotazioni_personale_medico = ControllerListaPrenotazioniPersonaleMedico(self)

        self.tool_prenotazioni_personale_medico = \
            ToolPrenotazioniPersonaleMedico(self, self.tabella,
                                            self.scrollAreaWidgetContents,
                                            self.controller_prenotazioni_personale_medico.
                                            model_lista_prenotazioni_personale_medico.
                                            lista_prenotazioni_personale_medico)

        ridimensiona_widget.ridimensiona_view(self)

    def setup_ui(self, lista_prenotazioni_personale_medico):
        """
        Funzione che crea e determina le caratteristiche degli oggetti della ViewPrenotazioniPersonaleMedico

        :param lista_prenotazioni_personale_medico: Oggetto della view che rappresenta la view stessa
        :type lista_prenotazioni_personale_medico: ViewPrenotazioniPersonaleMedico
        """
        lista_prenotazioni_personale_medico.setObjectName("lista_prenotazioni_personale_medico")
        lista_prenotazioni_personale_medico.move(0, 0)
        lista_prenotazioni_personale_medico.resize(1920, 1080)
        lista_prenotazioni_personale_medico.setMinimumSize(QtCore.QSize(1920, 1080))
        lista_prenotazioni_personale_medico.setMaximumSize(QtCore.QSize(1920, 1080))
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
        lista_prenotazioni_personale_medico.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Immagini/Logo Casa Alfredo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        lista_prenotazioni_personale_medico.setWindowIcon(icon)
        lista_prenotazioni_personale_medico.setStyleSheet("")
        self.lista_prenotazioni.setGeometry(QtCore.QRect(530, 20, 981, 131))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.lista_prenotazioni.setFont(font)
        self.lista_prenotazioni.setStyleSheet("color: rgb(84, 149, 223);")
        self.lista_prenotazioni.setObjectName("lista_prenotazioni")
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
        self.tabella.setGeometry(QtCore.QRect(30, 160, 1755, 780))
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
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.nome.setGeometry(QtCore.QRect(30, 160, 400, 25))
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
        self.nome.setText("Nome")
        self.attivita_ambulatoriale.setGeometry(QtCore.QRect(428, 160, 500, 25))
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
        self.attivita_ambulatoriale.setText("Attività ambulatoriale")
        self.data_e_ora.setGeometry(QtCore.QRect(926, 160, 500, 25))
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
        self.data_e_ora.setText("Data e Ora")
        self.visualizza_cartella_clinica.setGeometry(QtCore.QRect(1424, 160, 340, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.visualizza_cartella_clinica.setFont(font)
        self.visualizza_cartella_clinica.setStyleSheet("background-color: rgb(13, 41, 73);\n"
                                                       "color: rgb(255, 255, 255);\n"
                                                       "border: 2px solid;")
        self.visualizza_cartella_clinica.setAlignment(QtCore.Qt.AlignCenter)
        self.visualizza_cartella_clinica.setObjectName("visualizza_cartella_clinica")
        self.visualizza_cartella_clinica.setText("Visualizza Cartella Clinica")

        self.retranslate_ui(lista_prenotazioni_personale_medico)
        QtCore.QMetaObject.connectSlotsByName(lista_prenotazioni_personale_medico)

    def retranslate_ui(self, lista_prenotazioni_personale_medico):
        """
        Funzione che formatta il testo degli oggetti creati all'interno della view

        :param lista_prenotazioni_personale_medico: Oggetto della view che rappresenta la view stessa
        :type lista_prenotazioni_personale_medico: ViewPrenotazioniPersonaleMedico
        """
        _translate = QtCore.QCoreApplication.translate
        lista_prenotazioni_personale_medico.setWindowTitle(
            _translate("lista_prenotazioni_personale_medico", "Clinica Casa Alfredo"))
        self.lista_prenotazioni.setText(_translate("lista_prenotazioni_personale_medico", "- Lista Prenotazioni"))
        self.nome.setText(_translate("lista_prenotazioni_personale_medico", "Nome"))
        self.attivita_ambulatoriale.setText(_translate("lista_prenotazioni_personale_medico", "Attività ambulatoriale"))
        self.data_e_ora.setText(_translate("lista_prenotazioni_personale_medico", "Data e Ora"))
        self.visualizza_cartella_clinica.setText(
            _translate("lista_prenotazioni_personale_medico", "Visualizza Cartella Clinica"))
