from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

from personale_medico.controller.controller_lista_pazienti_visitati import ControllerListaPazientiVisitati

from tools.menu_a_tendina_personale_medico import MenuATendinaPersonaleMedico
from tools.tool_pazienti_da_modificare import ToolPazientiDaModificare
from tools.tool_pazienti_modificati import ToolPazientiModificati
from tools import ridimensiona_widget


class ViewListaPazientiVisitati(QWidget):

    def __init__(self, personale_medico):
        """
        Costruttore della classe ViewListaPazientiVisitati, nella quale vengono creati e mostrati tutti gli oggetti
        della Graphical User Interface (GUI) relativi alla suddetta view

        :param personale_medico: Variabile d'istanza che rappresenta un oggetto della classe PersonaleMedico
        :type personale_medico: PersonaleMedico
        """
        super().__init__()

        self.personale_medico = personale_medico

        self.i_miei_pazienti = QtWidgets.QLabel(self)
        self.logo = QtWidgets.QLabel(self)
        self.titolo = QtWidgets.QLabel(self)
        self.da_modificare = QtWidgets.QLabel(self)
        self.modificato = QtWidgets.QLabel(self)
        self.tabella_modificata = QtWidgets.QScrollArea(self)
        self.scrollAreaWidgetContents_mod = QtWidgets.QWidget()
        self.nome_mod = QtWidgets.QLabel(self)
        self.ambulatorio_mod = QtWidgets.QLabel(self)
        self.attivita_ambulatoriale_mod = QtWidgets.QLabel(self)
        self.data_e_ora_mod = QtWidgets.QLabel(self)
        self.patologia_riscontrata_mod = QtWidgets.QLabel(self)
        self.tabella_da_modificare = QtWidgets.QScrollArea(self)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.nome = QtWidgets.QLabel(self)
        self.ambulatorio = QtWidgets.QLabel(self)
        self.attivita_ambulatoriale = QtWidgets.QLabel(self)
        self.data_e_ora = QtWidgets.QLabel(self)
        self.patologia_riscontrata = QtWidgets.QLabel(self)
        self.setup_ui(self)

        self.menu_a_tendina = MenuATendinaPersonaleMedico(self)

        self.controller_lista_pazienti_visitati = ControllerListaPazientiVisitati(self)

        self.tool_pazienti_da_modificare = ToolPazientiDaModificare(self, self.tabella_da_modificare,
                                                                    self.scrollAreaWidgetContents,
                                                                    self.controller_lista_pazienti_visitati.
                                                                    model_lista_pazienti_visitati)

        self.tool_pazienti_modificati = ToolPazientiModificati(self, self.tabella_modificata,
                                                               self.scrollAreaWidgetContents_mod,
                                                               self.controller_lista_pazienti_visitati.
                                                               model_lista_pazienti_visitati)

        ridimensiona_widget.ridimensiona_view(self)

    def setup_ui(self, i_miei_pazienti_personale_medico):
        """
        Funzione che crea e determina le caratteristiche degli oggetti della ViewListaPazientiVisitati

        :param i_miei_pazienti_personale_medico: Oggetto della view che rappresenta la view stessa
        :type i_miei_pazienti_personale_medico: ViewListaPazientiVisitati
        """
        i_miei_pazienti_personale_medico.setObjectName("i_miei_pazienti_personale_medico")
        i_miei_pazienti_personale_medico.move(0, 0)
        i_miei_pazienti_personale_medico.resize(1920, 1080)
        i_miei_pazienti_personale_medico.setMinimumSize(QtCore.QSize(1920, 1080))
        i_miei_pazienti_personale_medico.setMaximumSize(QtCore.QSize(1920, 1080))
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
        i_miei_pazienti_personale_medico.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Immagini/logo_casa_alfredo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        i_miei_pazienti_personale_medico.setWindowIcon(icon)
        i_miei_pazienti_personale_medico.setStyleSheet("")
        self.i_miei_pazienti.setGeometry(QtCore.QRect(530, 20, 981, 131))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.i_miei_pazienti.setFont(font)
        self.i_miei_pazienti.setStyleSheet("color: rgb(84, 149, 223);")
        self.i_miei_pazienti.setObjectName("i_miei_pazienti")
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
        self.da_modificare.setGeometry(QtCore.QRect(30, 160, 190, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.da_modificare.setFont(font)
        self.da_modificare.setStyleSheet("color: rgb(33, 97, 171)")
        self.da_modificare.setObjectName("da_modificare")
        self.modificato.setGeometry(QtCore.QRect(30, 630, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.modificato.setFont(font)
        self.modificato.setStyleSheet("color: rgb(33, 97, 171)")
        self.modificato.setObjectName("modificato")
        self.tabella_modificata.setGeometry(QtCore.QRect(30, 670, 1811, 400))
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
        self.tabella_modificata.setPalette(palette)
        self.tabella_modificata.setStyleSheet("border: 0px solid;\n"
                                              "background-color: rgb(255, 255, 255);")
        self.tabella_modificata.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tabella_modificata.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tabella_modificata.setObjectName("tabella_modificata")
        self.scrollAreaWidgetContents_mod.setGeometry(QtCore.QRect(0, 0, 1811, 400))
        self.scrollAreaWidgetContents_mod.setObjectName("scrollAreaWidgetContents_mod")
        self.nome_mod.setGeometry(QtCore.QRect(30, 670, 325, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.nome_mod.setFont(font)
        self.nome_mod.setStyleSheet("background-color: rgb(13, 41, 73);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border: 2px solid;")
        self.nome_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.nome_mod.setObjectName("nome_mod")
        self.ambulatorio_mod.setGeometry(QtCore.QRect(353, 670, 400, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.ambulatorio_mod.setFont(font)
        self.ambulatorio_mod.setStyleSheet("background-color: rgb(13, 41, 73);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border: 2px solid;")
        self.ambulatorio_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.ambulatorio_mod.setObjectName("ambulatorio_mod")
        self.attivita_ambulatoriale_mod.setGeometry(QtCore.QRect(751, 670, 400, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.attivita_ambulatoriale_mod.setFont(font)
        self.attivita_ambulatoriale_mod.setStyleSheet("background-color: rgb(13, 41, 73);\n"
                                                      "color: rgb(255, 255, 255);\n"
                                                      "border: 2px solid;")
        self.attivita_ambulatoriale_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.attivita_ambulatoriale_mod.setObjectName("attivita_ambulatoriale_mod")
        self.data_e_ora_mod.setGeometry(QtCore.QRect(1149, 670, 400, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.data_e_ora_mod.setFont(font)
        self.data_e_ora_mod.setStyleSheet("background-color: rgb(13, 41, 73);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border: 2px solid;")
        self.data_e_ora_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.data_e_ora_mod.setObjectName("data_e_ora_mod")
        self.patologia_riscontrata_mod.setGeometry(QtCore.QRect(1547, 670, 273, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.patologia_riscontrata_mod.setFont(font)
        self.patologia_riscontrata_mod.setStyleSheet("background-color: rgb(13, 41, 73);\n"
                                                     "color: rgb(255, 255, 255);\n"
                                                     "border: 2px solid;")
        self.patologia_riscontrata_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.patologia_riscontrata_mod.setObjectName("patologia_riscontrata_mod")
        self.tabella_modificata.setWidget(self.scrollAreaWidgetContents_mod)
        self.tabella_da_modificare.setGeometry(QtCore.QRect(30, 200, 1811, 400))
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
        self.tabella_da_modificare.setPalette(palette)
        self.tabella_da_modificare.setStyleSheet("border: 0px solid;\n"
                                                 "background-color: rgb(255, 255, 255);")
        self.tabella_da_modificare.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tabella_da_modificare.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tabella_da_modificare.setObjectName("tabella_da_modificare")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.nome.setGeometry(QtCore.QRect(30, 200, 325, 25))
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
        self.ambulatorio.setGeometry(QtCore.QRect(353, 200, 400, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.ambulatorio.setFont(font)
        self.ambulatorio.setStyleSheet("background-color: rgb(13, 41, 73);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border: 2px solid;")
        self.ambulatorio.setAlignment(QtCore.Qt.AlignCenter)
        self.ambulatorio.setObjectName("ambulatorio")
        self.attivita_ambulatoriale.setGeometry(QtCore.QRect(751, 200, 400, 25))
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
        self.data_e_ora.setGeometry(QtCore.QRect(1149, 200, 400, 25))
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
        self.patologia_riscontrata.setGeometry(QtCore.QRect(1547, 200, 273, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.patologia_riscontrata.setFont(font)
        self.patologia_riscontrata.setStyleSheet("background-color: rgb(13, 41, 73);\n"
                                                 "color: rgb(255, 255, 255);\n"
                                                 "border: 2px solid;")
        self.patologia_riscontrata.setAlignment(QtCore.Qt.AlignCenter)
        self.patologia_riscontrata.setObjectName("patologia_riscontrata")

        self.retranslate_ui(i_miei_pazienti_personale_medico)
        QtCore.QMetaObject.connectSlotsByName(i_miei_pazienti_personale_medico)

    def retranslate_ui(self, i_miei_pazienti_personale_medico):
        """
        Funzione che formatta il testo degli oggetti creati all'interno della view

        :param i_miei_pazienti_personale_medico: Oggetto della view che rappresenta la view stessa
        :type i_miei_pazienti_personale_medico: ViewListaPazientiVisitati
        """
        _translate = QtCore.QCoreApplication.translate
        i_miei_pazienti_personale_medico.setWindowTitle(
            _translate("i_miei_pazienti_personale_medico", "Clinica Casa Alfredo"))
        self.i_miei_pazienti.setText(_translate("i_miei_pazienti_personale_medico", "I Miei Pazienti"))
        self.da_modificare.setText(_translate("i_miei_pazienti_personale_medico", "Da modificare:"))
        self.modificato.setText(_translate("i_miei_pazienti_personale_medico", "Modificato:"))
        self.nome_mod.setText(_translate("i_miei_pazienti_personale_medico", "Nome"))
        self.ambulatorio_mod.setText(_translate("i_miei_pazienti_personale_medico", "Ambulatorio"))
        self.attivita_ambulatoriale_mod.setText(
            _translate("i_miei_pazienti_personale_medico", "Attività ambulatoriale"))
        self.data_e_ora_mod.setText(_translate("i_miei_pazienti_personale_medico", "Data e Ora"))
        self.patologia_riscontrata_mod.setText(_translate("i_miei_pazienti_personale_medico", "Patologia riscontrata"))
        self.nome.setText(_translate("i_miei_pazienti_personale_medico", "Nome"))
        self.ambulatorio.setText(_translate("i_miei_pazienti_personale_medico", "Ambulatorio"))
        self.attivita_ambulatoriale.setText(_translate("i_miei_pazienti_personale_medico", "Attività ambulatoriale"))
        self.data_e_ora.setText(_translate("i_miei_pazienti_personale_medico", "Data e Ora"))
        self.patologia_riscontrata.setText(_translate("i_miei_pazienti_personale_medico", "Patologia riscontrata"))
