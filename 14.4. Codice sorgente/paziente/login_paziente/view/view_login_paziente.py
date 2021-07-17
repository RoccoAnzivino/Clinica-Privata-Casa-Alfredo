from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

from paziente.login_paziente.controller.controller_lista_pazienti import ControllerListaPazienti


class ViewLoginPaziente(QWidget):

    def __init__(self):
        """
        Costruttore della classe ViewLoginPaziente, nella quale vengono creati e mostrati tutti gli oggetti della
        Graphical User Interface (GUI) relativi alla suddetta view
        """
        super().__init__()

        self.logo = QtWidgets.QLabel(self)
        self.titolo = QtWidgets.QLabel(self)
        self.scritta = QtWidgets.QLabel(self)
        self.login_button = QtWidgets.QPushButton(self)
        self.banner = QtWidgets.QLabel(self)
        self.torna_indietro = QtWidgets.QPushButton(self)
        self.email = QtWidgets.QLineEdit(self)
        self.password = QtWidgets.QLineEdit(self)
        self.registrati = QtWidgets.QPushButton(self)
        self.occhiello_barrato_button = QtWidgets.QPushButton(self)
        self.occhiello_button = QtWidgets.QPushButton(self)
        self.setup_ui(self)

        self.controller_lista_pazienti = ControllerListaPazienti(self)

    def occhiello_button_pressed(self):
        """
        Funzione che rende visibile il testo inserito nella line edit delle password nel momento in cui si preme
        l'apposito button
        """
        # non fa vedere la password digitata
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.occhiello_barrato_button.setVisible(True)
        self.occhiello_button.setVisible(False)

    def occhiello_barrato_button_pressed(self):
        """
        Funzione che nasconde l testo inserito nella line edit delle password nel momento in cui si preme l'apposito
        button
        """
        # fa vedere la password digitata
        self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.occhiello_button.setVisible(True)
        self.occhiello_barrato_button.setVisible(False)

    def setup_ui(self, login_paziente):
        """
        Funzione che crea e determina le caratteristiche degli oggetti della ViewLoginPaziente

        :param login_paziente: Oggetto della view che rappresenta la view stessa
        :type login_paziente: ViewLoginPaziente
        """
        login_paziente.setObjectName("login_paziente")
        login_paziente.resize(900, 600)
        login_paziente.setMinimumSize(QtCore.QSize(900, 600))
        login_paziente.setMaximumSize(QtCore.QSize(900, 600))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        login_paziente.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        login_paziente.setFont(font)
        login_paziente.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Immagini/logo_casa_alfredo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login_paziente.setWindowIcon(icon)
        self.logo.setGeometry(QtCore.QRect(60, 30, 141, 161))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Immagini/logo_casa_alfredo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.titolo.setGeometry(QtCore.QRect(200, 50, 641, 131))
        self.titolo.setText("")
        self.titolo.setPixmap(QtGui.QPixmap("Immagini/titolo_casa_alfredo.png"))
        self.titolo.setScaledContents(True)
        self.titolo.setObjectName("titolo")
        self.scritta.setGeometry(QtCore.QRect(310, 340, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.scritta.setFont(font)
        self.scritta.setObjectName("scritta")
        self.login_button.setGeometry(QtCore.QRect(316, 447, 265, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 97, 171))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 97, 171))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 97, 171))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 97, 171))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 97, 171))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 97, 171))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 97, 171))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 97, 171))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 97, 171))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.login_button.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.login_button.setFont(font)
        self.login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_button.setStyleSheet("QPushButton#login_button {\n"
                                        "background-color: rgb(33, 97, 171);\n"
                                        "border: 1px solid;\n"
                                        "border-color: rgb(13, 41, 73);\n"
                                        "border-radius: 10px;\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "QPushButton#login_button:pressed {\n"
                                        "background-color: rgb(13, 41, 73);\n"
                                        "border-color: rgb(33, 97, 171);\n"
                                        "color: rgb(200, 200, 200);\n"
                                        "}")
        self.login_button.setObjectName("login_button")
        self.banner.setGeometry(QtCore.QRect(0, 560, 901, 41))
        self.banner.setStyleSheet("background-color: rgb(13, 41, 73);")
        self.banner.setText("")
        self.banner.setObjectName("banner")
        self.torna_indietro.setGeometry(QtCore.QRect(730, 565, 171, 31))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
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
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.torna_indietro.setFont(font)
        self.torna_indietro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.torna_indietro.setStyleSheet("QPushButton#torna_indietro {\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton#torna_indietro:pressed {\n"
                                          "background-color: rgb(0, 0, 0, 0);\n"
                                          "color: rgb(200, 200, 200);\n"
                                          "}")
        self.torna_indietro.setFlat(True)
        self.torna_indietro.setObjectName("torna_indietro")
        self.email.setGeometry(QtCore.QRect(300, 220, 293, 36))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.email.setFont(font)
        self.email.setStyleSheet("QLineEdit#email {\n"
                                 "border: 1px solid;\n"
                                 "border-radius: 18px;\n"
                                 "padding-left: 8px;\n"
                                 "padding-right: 8px;\n"
                                 "}")
        self.email.setObjectName("email")
        self.password.setGeometry(QtCore.QRect(300, 296, 293, 36))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.password.setFont(font)
        self.password.setStyleSheet("QLineEdit#password {\n"
                                    "border: 1px solid;\n"
                                    "border-radius: 18px;\n"
                                    "padding-left: 8px;\n"
                                    "padding-right: 8px;\n"
                                    "}")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")

        self.registrati.setGeometry(QtCore.QRect(304, 364, 101, 31))
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
        self.registrati.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.registrati.setFont(font)
        self.registrati.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registrati.setStyleSheet("QPushButton#registrati {\n"
                                      "color: rgb(0, 0, 255);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton#registrati:pressed {\n"
                                      "background-color: rgb(0, 0, 0, 0);\n"
                                      "    color: rgb(0, 0, 180);\n"
                                      "}")
        self.registrati.setFlat(True)
        self.registrati.setObjectName("registrati")

        self.occhiello_barrato_button.setGeometry(QtCore.QRect(600, 295, 40, 40))
        self.occhiello_barrato_button.setStyleSheet("QPushButton#occhiello_barrato_button:pressed {\n"
                                                    "background-color: rgb(0, 0, 0, 0);\n"
                                                    "}")
        self.occhiello_barrato_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Immagini/occhiello_barrato_password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.occhiello_barrato_button.setIcon(icon1)
        self.occhiello_barrato_button.setIconSize(QtCore.QSize(30, 30))
        self.occhiello_barrato_button.setFlat(True)
        self.occhiello_barrato_button.setObjectName("occhiello_barrato_button")
        self.occhiello_barrato_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.occhiello_button.setGeometry(QtCore.QRect(600, 295, 40, 40))
        self.occhiello_button.setStyleSheet("QPushButton#occhiello_button:pressed {\n"
                                            "background-color: rgb(0, 0, 0, 0);\n"
                                            "}")
        self.occhiello_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Immagini/occhiello_password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.occhiello_button.setIcon(icon1)
        self.occhiello_button.setIconSize(QtCore.QSize(30, 30))
        self.occhiello_button.setFlat(True)
        self.occhiello_button.setObjectName("occhiello_button")
        self.occhiello_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.occhiello_button.setVisible(False)

        self.retranslate_ui(login_paziente)
        QtCore.QMetaObject.connectSlotsByName(login_paziente)

    def retranslate_ui(self, login_paziente):
        """
        Funzione che formatta il testo degli oggetti creati all'interno della view

        :param login_paziente: Oggetto della view che rappresenta la view stessa
        :type login_paziente: ViewLoginPaziente
        """
        _translate = QtCore.QCoreApplication.translate
        login_paziente.setWindowTitle(_translate("login_paziente", "Clinica Casa Alfredo"))
        self.scritta.setText(_translate("login_paziente", "Non hai un account?"))
        self.login_button.setText(_translate("login_paziente", "Login"))
        self.torna_indietro.setText(_translate("login_paziente", "Torna Indietro"))
        self.email.setPlaceholderText(_translate("login_paziente", "E-mail..."))
        self.password.setPlaceholderText(_translate("login_paziente", "Password..."))
        self.registrati.setText(_translate("login_paziente", "Registrati"))
