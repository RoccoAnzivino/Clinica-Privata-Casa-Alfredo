import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget

from paziente.controller import controller_lista_prenotazioni_pazienti

from tools.menu_a_tendina_paziente import MenuATendinaPaziente
from tools import ridimensiona_widget


class ViewPrenotaOra(QWidget):

    def __init__(self, paziente):
        """
        Costruttore della classe ViewPrenotaOra, nella quale vengono creati e mostrati tutti gli oggetti della
        Graphical User Interface (GUI) relativi alla suddetta view

        :param paziente: Variabile d'istanza che rappresenta un oggetto della classe Paziente
        :type paziente: Paziente
        """
        super().__init__()

        self.paziente = paziente

        self.orario_apertura_mattina = None
        self.orario_chiusura_mattina = None
        self.orario_apertura_pomeriggio = None
        self.orario_chiusura_pomeriggio = None
        self.prezzo = ""
        self.durata = 0
        self.lista_orari_attivita_ambulatoriale = []
        self.lista_orari_da_sottrarre = []
        self.lista_orari_medici = []
        self.lista_medici_disponibili = []
        self.lista_pulsanti = []
        self.specializzazioni = []

        self.prenota_ora = QtWidgets.QLabel(self)
        self.logo = QtWidgets.QLabel(self)
        self.titolo = QtWidgets.QLabel(self)
        self.ambulatorio_label = QtWidgets.QLabel(self)
        self.attivita_ambulatoriale_label = QtWidgets.QLabel(self)
        self.data_e_ora_label = QtWidgets.QLabel(self)
        self.riepilogo_label = QtWidgets.QLabel(self)
        self.freccia_1 = QtWidgets.QLabel(self)
        self.freccia_2 = QtWidgets.QLabel(self)
        self.calendarWidget = QtWidgets.QCalendarWidget(self)
        self.medicina_generale_cardiologica = QtWidgets.QPushButton(self)
        self.endocrinologia = QtWidgets.QPushButton(self)
        self.urologia_andrologia = QtWidgets.QPushButton(self)
        self.oculistica = QtWidgets.QPushButton(self)
        self.ortopedia = QtWidgets.QPushButton(self)
        self.dermatologia = QtWidgets.QPushButton(self)
        self.selezionato_ambulatorio = QtWidgets.QLabel(self)
        self.attivita_ambulatoriale_button_1 = QtWidgets.QPushButton(self)
        self.selezionato_attivita_ambulatoriale = QtWidgets.QLabel(self)
        self.selezionato_data_e_ora = QtWidgets.QLabel(self)
        self.ora_combo_box = QtWidgets.QComboBox(self)
        self.prenota_ora_button = QtWidgets.QPushButton(self)
        self.lunedi = QtWidgets.QLabel(self)
        self.martedi = QtWidgets.QLabel(self)
        self.mercoledi = QtWidgets.QLabel(self)
        self.giovedi = QtWidgets.QLabel(self)
        self.venerdi = QtWidgets.QLabel(self)
        self.sabato = QtWidgets.QLabel(self)
        self.domenica = QtWidgets.QLabel(self)
        self.setup_ui(self)

        self.menu_a_tendina = MenuATendinaPaziente(self)

        self.controller_prenotazioni = controller_lista_prenotazioni_pazienti.ControllerListaPrenotazioniPazienti(self)

        ridimensiona_widget.ridimensiona_view(self)

    def setup_ui(self, prenota_ora_paziente):
        """
        Funzione che crea e determina le caratteristiche degli oggetti della ViewPrenotaOra

        :param prenota_ora_paziente: Oggetto della view che rappresenta la view stessa
        :type prenota_ora_paziente: ViewPrenotaOra
        """
        prenota_ora_paziente.setObjectName("prenota_ora_paziente")
        prenota_ora_paziente.move(0, 0)
        prenota_ora_paziente.resize(1920, 1080)
        prenota_ora_paziente.setMinimumSize(QtCore.QSize(1920, 1080))
        prenota_ora_paziente.setMaximumSize(QtCore.QSize(1920, 1080))
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
        prenota_ora_paziente.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Immagini/logo_casa_alfredo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        prenota_ora_paziente.setWindowIcon(icon)
        prenota_ora_paziente.setStyleSheet("")
        self.prenota_ora.setGeometry(QtCore.QRect(530, 20, 981, 131))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.prenota_ora.setFont(font)
        self.prenota_ora.setStyleSheet("color: rgb(84, 149, 223);")
        self.prenota_ora.setObjectName("prenota_ora")
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
        self.ambulatorio_label.setGeometry(QtCore.QRect(70, 170, 400, 700))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.ambulatorio_label.setFont(font)
        self.ambulatorio_label.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                             "border-radius: 20px solid;\n"
                                             "border: 3px solid;\n"
                                             "border-color: rgb(33, 97, 171);\n"
                                             "color: rgb(33, 97, 171);")
        self.ambulatorio_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.ambulatorio_label.setObjectName("ambulatorio_label")
        self.attivita_ambulatoriale_label.setGeometry(QtCore.QRect(670, 170, 400, 700))
        self.attivita_ambulatoriale_label.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.attivita_ambulatoriale_label.setFont(font)
        self.attivita_ambulatoriale_label.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                                        "border-radius: 20px solid;\n"
                                                        "border: 3px solid;\n"
                                                        "border-color: rgb(33, 97, 171);\n"
                                                        "color: rgb(33, 97, 171);\n"
                                                        "padding-top: 5px;")
        self.attivita_ambulatoriale_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.attivita_ambulatoriale_label.setObjectName("attivita_ambulatoriale_label")
        self.data_e_ora_label.setGeometry(QtCore.QRect(1270, 170, 500, 600))
        self.data_e_ora_label.setVisible(False)
        self.data_e_ora_label.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                            "border-radius: 20px solid;\n"
                                            "border: 3px solid;\n"
                                            "border-color: rgb(33, 97, 171);")
        self.data_e_ora_label.setText("")
        self.data_e_ora_label.setObjectName("data_e_ora_label")
        self.riepilogo_label.setGeometry(QtCore.QRect(1270, 775, 500, 189))
        self.riepilogo_label.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.riepilogo_label.setFont(font)
        self.riepilogo_label.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                           "border-radius: 20px solid;\n"
                                           "border: 3px solid;\n"
                                           "border-color: rgb(33, 97, 171);\n"
                                           "color: rgb(33, 97, 171);")
        self.riepilogo_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.riepilogo_label.setObjectName("riepilogo_label")
        self.freccia_1.setGeometry(QtCore.QRect(485, 470, 180, 100))
        self.freccia_1.setText("")
        self.freccia_1.setVisible(False)
        self.freccia_1.setPixmap(QtGui.QPixmap("Immagini/freccia.png"))
        self.freccia_1.setScaledContents(True)
        self.freccia_1.setObjectName("freccia_1")
        self.freccia_2.setGeometry(QtCore.QRect(1085, 470, 180, 100))
        self.freccia_2.setText("")
        self.freccia_2.setVisible(False)
        self.freccia_2.setPixmap(QtGui.QPixmap("Immagini/freccia.png"))
        self.freccia_2.setScaledContents(True)
        self.freccia_2.setObjectName("freccia_2")
        self.calendarWidget.setGeometry(QtCore.QRect(1273, 173, 494, 440))
        self.calendarWidget.setVisible(False)
        self.calendarWidget.setStyleSheet("border-radius: 20px solid;")
        self.calendarWidget.setObjectName("calendarWidget")

        # calcolo limite massimo di un anno a partire dalla data di prenotazione
        data_oggi = datetime.date.today()
        shift_24_ore = datetime.timedelta(hours=24)
        data_domani = data_oggi + shift_24_ore
        self.calendarWidget.setMinimumDate(QDate(data_domani.year, data_domani.month, data_domani.day))
        self.calendarWidget.setMaximumDate(QDate(data_oggi.year + 1, data_oggi.month, data_oggi.day))

        self.medicina_generale_cardiologica.setGeometry(QtCore.QRect(90, 250, 360, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.medicina_generale_cardiologica.setFont(font)
        self.medicina_generale_cardiologica.setStyleSheet("QPushButton#medicina_generale_cardiologica {\n"
                                                          "background-color: rgb(33, 97, 171);\n"
                                                          "border: 1px solid;\n"
                                                          "border-color: rgb(13, 41, 73);\n"
                                                          "border-radius: 10px;\n"
                                                          "color: rgb(255, 255, 255);\n"
                                                          "}\n"
                                                          "QPushButton#medicina_generale_cardiologica:pressed {\n"
                                                          "background-color: rgb(13, 41, 73);\n"
                                                          "border-color: rgb(33, 97, 171);\n"
                                                          "color: rgb(200, 200, 200);\n"
                                                          "}")
        self.medicina_generale_cardiologica.setObjectName("medicina_generale_cardiologica")
        self.medicina_generale_cardiologica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.endocrinologia.setGeometry(QtCore.QRect(90, 330, 360, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.endocrinologia.setFont(font)
        self.endocrinologia.setStyleSheet("QPushButton#endocrinologia {\n"
                                          "background-color: rgb(33, 97, 171);\n"
                                          "border: 1px solid;\n"
                                          "border-color: rgb(13, 41, 73);\n"
                                          "border-radius: 10px;\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "}\n"
                                          "QPushButton#endocrinologia:pressed {\n"
                                          "background-color: rgb(13, 41, 73);\n"
                                          "border-color: rgb(33, 97, 171);\n"
                                          "color: rgb(200, 200, 200);\n"
                                          "}")
        self.endocrinologia.setObjectName("endocrinologia")
        self.endocrinologia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.urologia_andrologia.setGeometry(QtCore.QRect(90, 410, 360, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.urologia_andrologia.setFont(font)
        self.urologia_andrologia.setStyleSheet("QPushButton#urologia_andrologia {\n"
                                               "background-color: rgb(33, 97, 171);\n"
                                               "border: 1px solid;\n"
                                               "border-color: rgb(13, 41, 73);\n"
                                               "border-radius: 10px;\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "}\n"
                                               "QPushButton#urologia_andrologia:pressed {\n"
                                               "background-color: rgb(13, 41, 73);\n"
                                               "border-color: rgb(33, 97, 171);\n"
                                               "color: rgb(200, 200, 200);\n"
                                               "}")
        self.urologia_andrologia.setObjectName("urologia_andrologia")
        self.urologia_andrologia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.oculistica.setGeometry(QtCore.QRect(90, 490, 360, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.oculistica.setFont(font)
        self.oculistica.setStyleSheet("QPushButton#oculistica {\n"
                                      "background-color: rgb(33, 97, 171);\n"
                                      "border: 1px solid;\n"
                                      "border-color: rgb(13, 41, 73);\n"
                                      "border-radius: 10px;\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QPushButton#oculistica:pressed {\n"
                                      "background-color: rgb(13, 41, 73);\n"
                                      "border-color: rgb(33, 97, 171);\n"
                                      "color: rgb(200, 200, 200);\n"
                                      "}")
        self.oculistica.setObjectName("oculistica")
        self.oculistica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ortopedia.setGeometry(QtCore.QRect(90, 570, 360, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.ortopedia.setFont(font)
        self.ortopedia.setStyleSheet("QPushButton#ortopedia {\n"
                                     "background-color: rgb(33, 97, 171);\n"
                                     "border: 1px solid;\n"
                                     "border-color: rgb(13, 41, 73);\n"
                                     "border-radius: 10px;\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "}\n"
                                     "QPushButton#ortopedia:pressed {\n"
                                     "background-color: rgb(13, 41, 73);\n"
                                     "border-color: rgb(33, 97, 171);\n"
                                     "color: rgb(200, 200, 200);\n"
                                     "}")
        self.ortopedia.setObjectName("ortopedia")
        self.ortopedia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dermatologia.setGeometry(QtCore.QRect(90, 650, 360, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dermatologia.setFont(font)
        self.dermatologia.setStyleSheet("QPushButton#dermatologia {\n"
                                        "background-color: rgb(33, 97, 171);\n"
                                        "border: 1px solid;\n"
                                        "border-color: rgb(13, 41, 73);\n"
                                        "border-radius: 10px;\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "QPushButton#dermatologia:pressed {\n"
                                        "background-color: rgb(13, 41, 73);\n"
                                        "border-color: rgb(33, 97, 171);\n"
                                        "color: rgb(200, 200, 200);\n"
                                        "}")
        self.dermatologia.setObjectName("dermatologia")
        self.dermatologia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selezionato_ambulatorio.setGeometry(QtCore.QRect(90, 790, 360, 90))
        self.selezionato_ambulatorio.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.selezionato_ambulatorio.setFont(font)
        self.selezionato_ambulatorio.setStyleSheet("color: rgb(33, 97, 171);")
        self.selezionato_ambulatorio.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.selezionato_ambulatorio.setObjectName("selezionato_ambulatorio")
        self.attivita_ambulatoriale_button_1.setGeometry(QtCore.QRect(690, 250, 360, 45))
        self.attivita_ambulatoriale_button_1.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.attivita_ambulatoriale_button_1.setFont(font)
        self.attivita_ambulatoriale_button_1.setStyleSheet("QPushButton#attivita_ambulatoriale_button_1{\n"
                                                           "background-color: rgb(33, 97, 171);\n"
                                                           "border: 1px solid;\n"
                                                           "border-color: rgb(13, 41, 73);\n"
                                                           "border-radius: 10px;\n"
                                                           "color: rgb(255, 255, 255);\n"
                                                           "}\n"
                                                           "QPushButton#attivita_ambulatoriale_button_1:pressed {\n"
                                                           "background-color: rgb(13, 41, 73);\n"
                                                           "border-color: rgb(33, 97, 171);\n"
                                                           "color: rgb(200, 200, 200);\n"
                                                           "}")
        self.attivita_ambulatoriale_button_1.setText("")
        self.attivita_ambulatoriale_button_1.setObjectName("attivita_ambulatoriale_button_1")
        self.selezionato_attivita_ambulatoriale.setGeometry(QtCore.QRect(690, 740, 360, 200))
        self.selezionato_attivita_ambulatoriale.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.selezionato_attivita_ambulatoriale.setFont(font)
        self.selezionato_attivita_ambulatoriale.setStyleSheet("color: rgb(33, 97, 171);")
        self.selezionato_attivita_ambulatoriale.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.selezionato_attivita_ambulatoriale.setObjectName("selezionato_attivita_ambulatoriale")
        self.selezionato_data_e_ora.setGeometry(QtCore.QRect(1290, 660, 460, 90))
        self.selezionato_data_e_ora.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.selezionato_data_e_ora.setFont(font)
        self.selezionato_data_e_ora.setStyleSheet("color: rgb(33, 97, 171);")
        self.selezionato_data_e_ora.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.selezionato_data_e_ora.setObjectName("selezionato_data_e_ora")

        self.ora_combo_box.setGeometry(QtCore.QRect(1510, 663, 231, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.ora_combo_box.setFont(font)
        self.ora_combo_box.setStyleSheet("QComboBox#comboBox {\n"
                                         "    border-bottom-right-radius: 10px;\n"
                                         "    border-bottom-left-radius: 10px;\n"
                                         "    border-top-left-radius: 10px;\n"
                                         "    border-top-right-radius: 10px;\n"
                                         "    background-color: rgb(169, 202, 239);\n"
                                         "    border: 2px solid;\n"
                                         "    border-color: rgb(33, 97, 171);\n"
                                         "    color: rgb(33, 97, 171);\n"
                                         "}\n"
                                         "QComboBox QAbstractItemView {\n"
                                         "    background-color: rgb(169, 202, 239);\n"
                                         "    border: 2px solid;\n"
                                         "    border-color: rgb(33, 97, 171);\n"
                                         "    color: rgb(33, 97, 171);\n"
                                         "}\n"
                                         "QComboBox#comboBox::drop-down:button{\n"
                                         "    border: 0px;\n"
                                         "}\n"
                                         "QComboBox#comboBox::down-arrow {\n"
                                         "    image: url(Immagini/freccia_combo_box.png);\n"
                                         "    width: 20px;\n"
                                         "    height: 20px;\n"
                                         "    padding-right: 10px;\n"
                                         "}\n"
                                         "QComboBox#comboBox::down-arrow:on {\n"
                                         "    image: url(Immagini/freccia_combo_box_capovolta.png);\n"
                                         "}")
        self.ora_combo_box.setObjectName("comboBox")
        self.ora_combo_box.addItem('')

        self.ora_combo_box.setVisible(False)

        self.prenota_ora_button.setGeometry(QtCore.QRect(1430, 915, 180, 40))
        self.prenota_ora_button.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.prenota_ora_button.setFont(font)
        self.prenota_ora_button.setStyleSheet("QPushButton#prenota_ora_button {\n"
                                              "background-color: rgb(33, 97, 171);\n"
                                              "border: 1px solid;\n"
                                              "border-color: rgb(13, 41, 73);\n"
                                              "border-radius: 10px;\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "}\n"
                                              "QPushButton#prenota_ora_button:pressed {\n"
                                              "background-color: rgb(13, 41, 73);\n"
                                              "border-color: rgb(33, 97, 171);\n"
                                              "color: rgb(200, 200, 200);\n"
                                              "}")
        self.prenota_ora_button.setObjectName("prenota_ora_button")

        # Label per i giorni del calendar widget
        # Esse diventano visibili in base ai giorni di apertura dei vari ambulatori
        self.lunedi.setGeometry(QtCore.QRect(1335, 256, 62, 357))
        self.lunedi.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.lunedi.setStyleSheet("background-color: white")
        self.lunedi.setText("")
        self.lunedi.setObjectName("lunedi")
        self.lunedi.setVisible(False)

        self.martedi.setGeometry(QtCore.QRect(1397, 256, 62, 357))
        self.martedi.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.martedi.setStyleSheet("background-color: white")
        self.martedi.setText("")
        self.martedi.setObjectName("martedi")
        self.martedi.setVisible(False)

        self.mercoledi.setGeometry(QtCore.QRect(1459, 256, 62, 357))
        self.mercoledi.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.mercoledi.setStyleSheet("background-color: white")
        self.mercoledi.setText("")
        self.mercoledi.setObjectName("mercoledi")
        self.mercoledi.setVisible(False)

        self.giovedi.setGeometry(QtCore.QRect(1521, 256, 62, 357))
        self.giovedi.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.giovedi.setStyleSheet("background-color: white")
        self.giovedi.setText("")
        self.giovedi.setObjectName("giovedi")
        self.giovedi.setVisible(False)

        self.venerdi.setGeometry(QtCore.QRect(1583, 256, 62, 357))
        self.venerdi.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.venerdi.setStyleSheet("background-color: white")
        self.venerdi.setText("")
        self.venerdi.setObjectName("venerdi")
        self.venerdi.setVisible(False)

        self.sabato.setGeometry(QtCore.QRect(1645, 256, 62, 357))
        self.sabato.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.sabato.setStyleSheet("background-color: white")
        self.sabato.setText("")
        self.sabato.setObjectName("sabato")
        self.sabato.setVisible(False)

        self.domenica.setGeometry(QtCore.QRect(1707, 256, 60, 357))
        self.domenica.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.domenica.setStyleSheet("background-color: white")
        self.domenica.setText("")
        self.domenica.setObjectName("domenica")
        self.domenica.setVisible(False)

        self.retranslate_ui(prenota_ora_paziente)
        QtCore.QMetaObject.connectSlotsByName(prenota_ora_paziente)

    def retranslate_ui(self, prenota_ora_paziente):
        """
        Funzione che formatta il testo degli oggetti creati all'interno della view

        :param prenota_ora_paziente: Oggetto della view che rappresenta la view stessa
        :type prenota_ora_paziente: ViewPrenotaOra
        """
        _translate = QtCore.QCoreApplication.translate
        prenota_ora_paziente.setWindowTitle(_translate("prenota_ora_paziente", "Clinica Casa Alfredo"))
        self.prenota_ora.setText(_translate("prenota_ora_paziente", "- Prenota Ora"))
        self.ambulatorio_label.setText(_translate("prenota_ora_paziente", "AMBULATORIO"))
        self.attivita_ambulatoriale_label.setText(_translate("prenota_ora_paziente", "ATTIVITA\' AMBULATORIALE"))
        self.riepilogo_label.setText(_translate("prenota_ora_paziente", "RIEPILOGO\n"))
        self.medicina_generale_cardiologica.setText(
            _translate("prenota_ora_paziente", "Medicina Generale Cardiologica"))
        self.endocrinologia.setText(_translate("prenota_ora_paziente", "Endocrinologia"))
        self.urologia_andrologia.setText(_translate("prenota_ora_paziente", "Urologia/Andrologia"))
        self.oculistica.setText(_translate("prenota_ora_paziente", "Oculistica"))
        self.ortopedia.setText(_translate("prenota_ora_paziente", "Ortopedia"))
        self.dermatologia.setText(_translate("prenota_ora_paziente", "Dermatologia"))
        self.selezionato_ambulatorio.setText(_translate("prenota_ora_paziente", "Selezionato:"))
        self.selezionato_attivita_ambulatoriale.setText(_translate("prenota_ora_paziente", "Selezionato:"))
        self.selezionato_data_e_ora.setText(_translate("prenota_ora_paziente", "Selezionato:"))
        self.ora_combo_box.setItemText(0, _translate("prenota_ora_paziente", "Scegli ora:"))
        self.prenota_ora_button.setText(_translate("prenota_ora_paziente", "PRENOTA ORA"))
