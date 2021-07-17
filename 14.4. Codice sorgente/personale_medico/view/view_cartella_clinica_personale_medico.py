from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

from paziente.controller import controller_cartella_clinica

from tools import ridimensiona_widget, tool_cartella_clinica_paziente
from tools.menu_a_tendina_personale_medico import MenuATendinaPersonaleMedico


class ViewCartellaClinicaPersonaleMedico(QWidget):
    def __init__(self, paziente, personale_medico):
        """
        Costruttore della classe ViewCartellaClinicaPersonaleMedico, nella quale vengono creati e mostrati tutti gli
        oggetti della Graphical User Interface (GUI) relativi alla suddetta view

        :param paziente: Variabile d'istanza che rappresenta un oggetto della classe Paziente
        :type paziente: Paziente
        :param personale_medico: Variabile d'istanza che rappresenta un oggetto della classe PersonaleMedico
        :type personale_medico: PersonaleMedico
        """
        super().__init__()

        self.paziente = paziente
        self.personale_medico = personale_medico

        self.cartella_clinica = QtWidgets.QLabel(self)
        self.logo = QtWidgets.QLabel(self)
        self.titolo = QtWidgets.QLabel(self)
        self.emissione = QtWidgets.QLabel(self)
        self.clinica_privata_casa_alfredo = QtWidgets.QLabel(self)
        self.data_emissione = QtWidgets.QLabel(self)
        self.dati_personali = QtWidgets.QLabel(self)
        self.operatori_medici = QtWidgets.QLabel(self)
        self.nome_label = QtWidgets.QLabel(self)
        self.cognome_label = QtWidgets.QLabel(self)
        self.data_di_nascita_label = QtWidgets.QLabel(self)
        self.eta_label = QtWidgets.QLabel(self)
        self.sesso_label = QtWidgets.QLabel(self)
        self.provincia_label = QtWidgets.QLabel(self)
        self.citta_di_nascita_label = QtWidgets.QLabel(self)
        self.codice_fiscale_label = QtWidgets.QLabel(self)
        self.operatori_medici_label = QtWidgets.QLabel(self)
        self.patologie_riscontrate = QtWidgets.QLabel(self)
        self.torna_indietro = QtWidgets.QPushButton(self)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.patologia_label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.patologia_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.setup_ui(self)

        self.menu_a_tendina = MenuATendinaPersonaleMedico(self)

        self.controller_cartella_clinica = controller_cartella_clinica.ControllerCartellaClinica(self)

        self.tool_cartella_clinica = tool_cartella_clinica_paziente.ToolCartellaClinicaPaziente(
            self, self.scrollArea, self.scrollAreaWidgetContents,
            self.controller_cartella_clinica.model_cartella_clinica.lista_prenotazioni_cartella_clinica)

        ridimensiona_widget.ridimensiona_view(self)

    def setup_ui(self, cartella_clinica_paziente):
        """
        Funzione che crea e determina le caratteristiche degli oggetti della ViewCartellaClinicaPersonaleMedico

        :param cartella_clinica_paziente: Oggetto della view che rappresenta la view stessa
        :type cartella_clinica_paziente: ViewCartellaClinicaPersonaleMedico
        """
        cartella_clinica_paziente.setObjectName("cartella_clinica_paziente")
        cartella_clinica_paziente.move(0, 0)
        cartella_clinica_paziente.resize(1920, 1080)
        cartella_clinica_paziente.setMinimumSize(QtCore.QSize(1920, 1080))
        cartella_clinica_paziente.setMaximumSize(QtCore.QSize(1920, 1080))
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
        cartella_clinica_paziente.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Immagini/logo_casa_alfredo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cartella_clinica_paziente.setWindowIcon(icon)
        cartella_clinica_paziente.setStyleSheet("")
        self.cartella_clinica.setGeometry(QtCore.QRect(530, 20, 981, 131))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.cartella_clinica.setFont(font)
        self.cartella_clinica.setStyleSheet("color: rgb(84, 149, 223);")
        self.cartella_clinica.setObjectName("cartella_clinica")
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
        self.emissione.setGeometry(QtCore.QRect(50, 170, 1750, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.emissione.setFont(font)
        self.emissione.setStyleSheet("background-color: rgb(84, 149, 223);\n"
                                     "border: 2px solid")
        self.emissione.setObjectName("emissione")
        self.clinica_privata_casa_alfredo.setGeometry(QtCore.QRect(50, 193, 875, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(18)
        self.clinica_privata_casa_alfredo.setFont(font)
        self.clinica_privata_casa_alfredo.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                                        "border: 2px solid")
        self.clinica_privata_casa_alfredo.setObjectName("clinica_privata_casa_alfredo")
        self.data_emissione.setGeometry(QtCore.QRect(923, 193, 877, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(18)
        self.data_emissione.setFont(font)
        self.data_emissione.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                          "border: 2px solid")
        self.data_emissione.setObjectName("data_emissione")
        self.dati_personali.setGeometry(QtCore.QRect(50, 251, 875, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.dati_personali.setFont(font)
        self.dati_personali.setStyleSheet("background-color: rgb(84, 149, 223);\n"
                                          "border: 2px solid")
        self.dati_personali.setObjectName("dati_personali")
        self.operatori_medici.setGeometry(QtCore.QRect(923, 251, 877, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.operatori_medici.setFont(font)
        self.operatori_medici.setStyleSheet("background-color: rgb(84, 149, 223);\n"
                                            "border: 2px solid")
        self.operatori_medici.setObjectName("operatori_medici")
        self.nome_label.setGeometry(QtCore.QRect(50, 274, 438, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(18)
        self.nome_label.setFont(font)
        self.nome_label.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                      "border: 2px solid")
        self.nome_label.setObjectName("nome_label")
        self.cognome_label.setGeometry(QtCore.QRect(50, 332, 438, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(18)
        self.cognome_label.setFont(font)
        self.cognome_label.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                         "border: 2px solid")
        self.cognome_label.setObjectName("cognome_label")
        self.data_di_nascita_label.setGeometry(QtCore.QRect(50, 390, 438, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(18)
        self.data_di_nascita_label.setFont(font)
        self.data_di_nascita_label.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                                 "border: 2px solid")
        self.data_di_nascita_label.setObjectName("data_di_nascita_label")
        self.eta_label.setGeometry(QtCore.QRect(50, 448, 438, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(18)
        self.eta_label.setFont(font)
        self.eta_label.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                     "border: 2px solid")
        self.eta_label.setObjectName("eta_label")
        self.sesso_label.setGeometry(QtCore.QRect(486, 274, 439, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(18)
        self.sesso_label.setFont(font)
        self.sesso_label.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                       "border: 2px solid")
        self.sesso_label.setObjectName("sesso_label")
        self.provincia_label.setGeometry(QtCore.QRect(486, 332, 439, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(18)
        self.provincia_label.setFont(font)
        self.provincia_label.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                           "border: 2px solid")
        self.provincia_label.setObjectName("provincia_label")
        self.citta_di_nascita_label.setGeometry(QtCore.QRect(486, 390, 439, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(18)
        self.citta_di_nascita_label.setFont(font)
        self.citta_di_nascita_label.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                                  "border: 2px solid")
        self.citta_di_nascita_label.setObjectName("citta_di_nascita_label")
        self.codice_fiscale_label.setGeometry(QtCore.QRect(486, 448, 439, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(18)
        self.codice_fiscale_label.setFont(font)
        self.codice_fiscale_label.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                                "border: 2px solid")
        self.codice_fiscale_label.setObjectName("codice_fiscale_label")
        self.operatori_medici_label.setGeometry(QtCore.QRect(923, 274, 877, 234))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(18)
        self.operatori_medici_label.setFont(font)
        self.operatori_medici_label.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                                  "border: 2px solid")
        self.operatori_medici_label.setText("")
        self.operatori_medici_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.operatori_medici_label.setObjectName("operatori_medici_label")
        self.patologie_riscontrate.setGeometry(QtCore.QRect(50, 506, 1750, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.patologie_riscontrate.setFont(font)
        self.patologie_riscontrate.setStyleSheet("background-color: rgb(84, 149, 223);\n"
                                                 "border: 2px solid")
        self.patologie_riscontrate.setObjectName("patologie_riscontrate")
        self.torna_indietro.setGeometry(QtCore.QRect(47, 138, 151, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.torna_indietro.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.torna_indietro.setFont(font)
        self.torna_indietro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.torna_indietro.setStyleSheet("QPushButton#torna_indietro {\n"
                                          "color: rgb(0, 0, 255);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton#torna_indietro:pressed {\n"
                                          "background-color: rgb(0, 0, 0, 0);\n"
                                          "color: rgb(0, 0, 180);\n"
                                          "}")
        self.torna_indietro.setFlat(True)
        self.torna_indietro.setObjectName("torna_indietro")
        self.scrollArea.setGeometry(QtCore.QRect(50, 530, 1771, 511))
        self.scrollArea.setStyleSheet("border: 0px solid;\n"
                                      "background-color: rgb(255, 255, 255);")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1771, 511))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.patologia_label_2.setGeometry(QtCore.QRect(873, -1, 877, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(18)
        self.patologia_label_2.setFont(font)
        self.patologia_label_2.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                             "border: 2px solid")
        self.patologia_label_2.setText("")
        self.patologia_label_2.setObjectName("patologia_label_2")
        self.patologia_label.setGeometry(QtCore.QRect(0, -1, 875, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(18)
        self.patologia_label.setFont(font)
        self.patologia_label.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                           "border: 2px solid")
        self.patologia_label.setText("")
        self.patologia_label.setObjectName("patologia_label")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslate_ui(cartella_clinica_paziente)
        QtCore.QMetaObject.connectSlotsByName(cartella_clinica_paziente)

    def retranslate_ui(self, cartella_clinica_paziente):
        """
        Funzione che formatta il testo degli oggetti creati all'interno della view

        :param cartella_clinica_paziente: Oggetto della view che rappresenta la view stessa
        :type cartella_clinica_paziente: ViewCartellaClinicaPersonaleMedico
        """
        _translate = QtCore.QCoreApplication.translate
        cartella_clinica_paziente.setWindowTitle(_translate("cartella_clinica_paziente", "Clinica Casa Alfredo"))
        self.cartella_clinica.setText(_translate("cartella_clinica_paziente", "- Cartella Clinica"))
        self.emissione.setText(_translate("cartella_clinica_paziente", "Emissione"))
        self.clinica_privata_casa_alfredo.setText(
            _translate("cartella_clinica_paziente", "Clinica privata Casa Alfredo"))
        self.data_emissione.setText(_translate("cartella_clinica_paziente", "Data di emissione:"))
        self.dati_personali.setText(_translate("cartella_clinica_paziente", "Dati personali"))
        self.operatori_medici.setText(_translate("cartella_clinica_paziente", "Operatori medici"))
        self.nome_label.setText(_translate("cartella_clinica_paziente", "Nome:"))
        self.cognome_label.setText(_translate("cartella_clinica_paziente", "Cognome:"))
        self.data_di_nascita_label.setText(_translate("cartella_clinica_paziente", "Data di nascita:"))
        self.eta_label.setText(_translate("cartella_clinica_paziente", "Età:"))
        self.sesso_label.setText(_translate("cartella_clinica_paziente", "Sesso:"))
        self.provincia_label.setText(_translate("cartella_clinica_paziente", "Provincia:"))
        self.citta_di_nascita_label.setText(_translate("cartella_clinica_paziente", "Città di nascita:"))
        self.codice_fiscale_label.setText(_translate("cartella_clinica_paziente", "Codice fiscale:"))
        self.patologie_riscontrate.setText(_translate("cartella_clinica_paziente", "Patologie riscontrate"))
        self.torna_indietro.setText(_translate("cartella_clinica_paziente", "Torna Indietro"))