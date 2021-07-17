from PyQt5 import QtCore, QtGui, QtWidgets

from paziente.view import view_home_paziente

from tools.animazioni import Animazioni


class MenuATendinaPaziente:

    def __init__(self, widget):
        """
        Costruttore della classe MenuATendinaPaziente, nella quale vengono creati e regolamentati tutti gli oggetti che
        formano il menù a tendina del paziente

        :param widget: Parametro che rappresenta tutte le view del paziente nelle quali è possibile utilizzare il menù
                        a tendina
        :type widget: QWidget
        """
        self.menu_tendina = QtWidgets.QLabel(widget)
        self.tendina_button = QtWidgets.QPushButton(widget)
        self.tendina_aperta_button = QtWidgets.QPushButton(widget)
        self.ciao = QtWidgets.QLabel(widget)
        self.profilo_button = QtWidgets.QPushButton(widget)
        self.prenota_button = QtWidgets.QPushButton(widget)
        self.logout_button = QtWidgets.QPushButton(widget)
        self.dati_button = QtWidgets.QPushButton(widget)
        self.prenotazioni_button = QtWidgets.QPushButton(widget)
        self.cartella_clinica_button = QtWidgets.QPushButton(widget)
        self.indietro_button = QtWidgets.QPushButton(widget)
        self.setup_menu_a_tendina(widget)

        self.animazioni = Animazioni()

    def setup_menu_a_tendina(self, widget):
        """
        Funzione che crea e determina le caratteristiche degli oggetti del menù a tendina del paziente

        :param widget: Parametro che rappresenta tutte le view del paziente nelle quali è possibile utilizzare il menù
                        a tendina
        :type widget: QWidget
        """
        self.menu_tendina.setGeometry(QtCore.QRect(1490, 0, 430, 1080))
        self.menu_tendina.setStyleSheet("background-color: rgb(13, 41, 73);\n"
                                        "border: 3px solid")
        self.menu_tendina.setText("")
        self.menu_tendina.setObjectName("menu_tendina")
        self.menu_tendina.setVisible(False)

        self.tendina_button.setGeometry(QtCore.QRect(1820, 20, 70, 70))
        self.tendina_button.setStyleSheet("QPushButton#tendina_button:pressed {\n"
                                          "background-color: rgb(0, 0, 0, 0);\n"
                                          "}")
        self.tendina_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Immagini/tendina_chiusa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tendina_button.setIcon(icon1)
        self.tendina_button.setIconSize(QtCore.QSize(70, 70))
        self.tendina_button.setFlat(True)
        self.tendina_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tendina_button.setObjectName("tendina_button")

        # bottone che, se premuto, permette di aprire la tendina dall'apposito pulsantino
        self.tendina_button.clicked.connect(lambda: self.tendina_button_pressed(widget))

        self.tendina_aperta_button.setGeometry(QtCore.QRect(1495, 5, 70, 70))
        self.tendina_aperta_button.setStyleSheet("QPushButton#tendina_aperta_button:pressed {\n"
                                                 "background-color: rgb(0, 0, 0, 0);\n"
                                                 "}")
        self.tendina_aperta_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Immagini/tendina_aperta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tendina_aperta_button.setIcon(icon2)
        self.tendina_aperta_button.setIconSize(QtCore.QSize(70, 70))
        self.tendina_aperta_button.setFlat(True)
        self.tendina_aperta_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # pulsante che consente di chiudere il menù a tendina
        self.tendina_aperta_button.clicked.connect(lambda: self.tendina_button_pressed_reverse(widget))

        self.tendina_aperta_button.setObjectName("tendina_aperta_button")
        self.tendina_aperta_button.setVisible(False)

        self.ciao.setGeometry(QtCore.QRect(1585, 130, 301, 111))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(27)
        self.ciao.setFont(font)
        self.ciao.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ciao.setStyleSheet("color: rgb(33, 97, 171);")
        self.ciao.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.ciao.setText(
            f'<p>Ciao,<p style="color: white; font-weight: bold; font-size: 30px">{widget.paziente.nome}</p></p>')
        self.ciao.setObjectName("ciao")
        self.ciao.setVisible(False)

        self.profilo_button.setGeometry(QtCore.QRect(1490, 297, 430, 120))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.profilo_button.setFont(font)
        self.profilo_button.setStyleSheet("QPushButton#profilo_button {\n"
                                          "background-color: rgb(0, 0, 0, 0);\n"
                                          "color: rgb(33, 97, 171);\n"
                                          "border: 3px solid;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton#profilo_button:pressed {\n"
                                          "background-color: rgb(33, 97, 171);\n"
                                          "color: rgb(13, 41, 73);\n"
                                          "}")
        self.profilo_button.setObjectName("profilo_button")
        self.profilo_button.setVisible(False)

        self.prenota_button.setGeometry(QtCore.QRect(1490, 414, 430, 120))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.prenota_button.setFont(font)
        self.prenota_button.setStyleSheet("QPushButton#prenota_button {\n"
                                          "background-color: rgb(0, 0, 0, 0);\n"
                                          "color: rgb(33, 97, 171);\n"
                                          "border: 3px solid;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton#prenota_button:pressed {\n"
                                          "background-color: rgb(33, 97, 171);\n"
                                          "color: rgb(13, 41, 73);\n"
                                          "}")
        self.prenota_button.setObjectName("prenota_button")
        self.prenota_button.setVisible(False)

        self.logout_button.setGeometry(QtCore.QRect(1490, 920, 430, 120))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.logout_button.setFont(font)
        self.logout_button.setStyleSheet("QPushButton#logout_button {\n"
                                         "background-color: rgb(0, 0, 0, 0);\n"
                                         "color: rgb(33, 97, 171);\n"
                                         "border: 3px solid;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton#logout_button:pressed {\n"
                                         "background-color: rgb(33, 97, 171);\n"
                                         "color: rgb(13, 41, 73);\n"
                                         "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Immagini/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_button.setIcon(icon2)
        self.logout_button.setIconSize(QtCore.QSize(50, 50))
        self.logout_button.setObjectName("logout_button")
        self.logout_button.setVisible(False)

        self.dati_button.setGeometry(QtCore.QRect(1490, 297, 430, 120))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.dati_button.setFont(font)
        self.dati_button.setStyleSheet("QPushButton#dati_button {\n"
                                       "background-color: rgb(0, 0, 0, 0);\n"
                                       "color: rgb(33, 97, 171);\n"
                                       "border: 3px solid;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#dati_button:pressed {\n"
                                       "background-color: rgb(33, 97, 171);\n"
                                       "color: rgb(13, 41, 73);\n"
                                       "}")
        self.dati_button.setObjectName("dati_button")
        self.dati_button.setVisible(False)

        self.prenotazioni_button.setGeometry(QtCore.QRect(1490, 414, 430, 120))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.prenotazioni_button.setFont(font)
        self.prenotazioni_button.setStyleSheet("QPushButton#prenotazioni_button {\n"
                                               "background-color: rgb(0, 0, 0, 0);\n"
                                               "color: rgb(33, 97, 171);\n"
                                               "border: 3px solid;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton#prenotazioni_button:pressed {\n"
                                               "background-color: rgb(33, 97, 171);\n"
                                               "color: rgb(13, 41, 73);\n"
                                               "}")
        self.prenotazioni_button.setObjectName("prenotazioni_button")
        self.prenotazioni_button.setVisible(False)

        self.cartella_clinica_button.setGeometry(QtCore.QRect(1490, 531, 430, 120))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(37)
        font.setBold(True)
        font.setWeight(75)
        self.cartella_clinica_button.setFont(font)
        self.cartella_clinica_button.setStyleSheet("QPushButton#cartella_clinica_button {\n"
                                                   "background-color: rgb(0, 0, 0, 0);\n"
                                                   "color: rgb(33, 97, 171);\n"
                                                   "border: 3px solid;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton#cartella_clinica_button:pressed {\n"
                                                   "background-color: rgb(33, 97, 171);\n"
                                                   "color: rgb(13, 41, 73);\n"
                                                   "}")
        self.cartella_clinica_button.setObjectName("cartella_clinica_button")
        self.cartella_clinica_button.setVisible(False)

        self.indietro_button.setGeometry(QtCore.QRect(1490, 648, 430, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.indietro_button.setFont(font)
        self.indietro_button.setStyleSheet("QPushButton#indietro_button {\n"
                                           "background-color: rgb(0, 0, 0, 0);\n"
                                           "color: rgb(33, 97, 171);\n"
                                           "border: 3px solid;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#indietro_button:pressed {\n"
                                           "background-color: rgb(33, 97, 171);\n"
                                           "color: rgb(13, 41, 73);\n"
                                           "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Immagini/torna_indietro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.indietro_button.setIcon(icon3)
        self.indietro_button.setObjectName("indietro_button")
        self.indietro_button.setVisible(False)

        self.profilo_button.clicked.connect(self.profilo_button_pressed)
        self.indietro_button.clicked.connect(self.indietro_button_pressed)

        self.retranslate_menu_a_tendina()

    def retranslate_menu_a_tendina(self):
        """
        Funzione che formatta il testo degli oggetti creati all'interno del menù a tendina del paziente
        """
        _translate = QtCore.QCoreApplication.translate
        self.profilo_button.setText(_translate("homePazienteAperto", "IL MIO PROFILO"))
        self.prenota_button.setText(_translate("homePazienteAperto", "PRENOTA ORA"))
        self.logout_button.setText(_translate("homePazienteAperto", "LOGOUT"))
        self.dati_button.setText(_translate("homePazienteApertoProfilo", "DATI PERSONALI"))
        self.prenotazioni_button.setText(_translate("homePazienteApertoProfilo", "LE MIE PRENOTAZIONI"))
        self.cartella_clinica_button.setText(_translate("homePazienteApertoProfilo", "CARTELLA CLINICA"))
        self.indietro_button.setText(_translate("homePazienteApertoProfilo", "Indietro"))

    def tendina_button_pressed(self, widget):
        """
        Funzione che mostra il menù a tendina del paziente nel momento in cui viene premuto l'apposito button

        :param widget: Parametro che rappresenta tutte le view del paziente nelle quali è possibile utilizzare il menù
                        a tendina
        :type widget: QWidget
        """
        self.menu_tendina.setVisible(True)
        self.tendina_button.setVisible(False)
        self.tendina_aperta_button.setVisible(True)
        self.ciao.setVisible(True)
        self.profilo_button.setVisible(True)
        self.prenota_button.setVisible(True)
        self.logout_button.setVisible(True)

        self.animazioni.animazione_fade_in_totale.clear()

        self.animazioni.animazione_fade_in(self.menu_tendina)
        self.animazioni.animazione_fade_in(self.tendina_aperta_button)
        self.animazioni.animazione_fade_in(self.ciao)
        self.animazioni.animazione_fade_in(self.profilo_button)
        self.animazioni.animazione_fade_in(self.prenota_button)
        self.animazioni.animazione_fade_in(self.logout_button)
        self.animazioni.animazione_fade_in(self.dati_button)
        self.animazioni.animazione_fade_in(self.prenotazioni_button)
        self.animazioni.animazione_fade_in(self.cartella_clinica_button)
        self.animazioni.animazione_fade_in(self.indietro_button)

        if isinstance(widget, view_home_paziente.ViewHomePaziente):

            self.animazioni.animazione_slide_totale.clear()

            self.animazioni.animazione_slide(widget.logo)
            self.animazioni.animazione_slide(widget.titolo)
            self.animazioni.animazione_slide(widget.scritta)

            self.animazioni.animazione_slide_totale.start()

        self.animazioni.animazione_fade_in_totale.start()

    def tendina_button_pressed_reverse(self, widget):
        """
        Funzione che nasconde il menù a tendina del paziente nel momento in cui viene premuto l'apposito button

        :param widget: Parametro che rappresenta tutte le view del paziente nelle quali è possibile utilizzare il menù
                        a tendina
        :type widget: QWidget
        """
        self.tendina_aperta_button.setVisible(False)
        self.tendina_button.setVisible(True)

        self.animazioni.animazione_fade_out_totale.clear()

        self.animazioni.animazione_fade_out(self.menu_tendina)
        self.animazioni.animazione_fade_out(self.ciao)
        self.animazioni.animazione_fade_out(self.logout_button)

        if self.profilo_button.isVisible():
            self.animazioni.animazione_fade_out(self.profilo_button)
            self.animazioni.animazione_fade_out(self.prenota_button)
        else:
            self.animazioni.animazione_fade_out(self.dati_button)
            self.animazioni.animazione_fade_out(self.prenotazioni_button)
            self.animazioni.animazione_fade_out(self.cartella_clinica_button)
            self.animazioni.animazione_fade_out(self.indietro_button)

        if isinstance(widget, view_home_paziente.ViewHomePaziente):

            self.animazioni.animazione_slide_reverse_totale.clear()

            self.animazioni.animazione_slide_reverse(widget.logo)
            self.animazioni.animazione_slide_reverse(widget.titolo)
            self.animazioni.animazione_slide_reverse(widget.scritta)

            self.animazioni.animazione_slide_reverse_totale.start()

        self.animazioni.animazione_fade_out_totale.start()

        self.animazioni.animazione_fade_out_totale.finished.connect(self.chiudi_tutto)

    def chiudi_tutto(self):
        """
        Funzione che nasconde tutti gli oggetti del menù a tendina del paziente
        """
        self.menu_tendina.setVisible(False)
        self.tendina_button.setVisible(True)
        self.tendina_aperta_button.setVisible(False)
        self.ciao.setVisible(False)
        self.profilo_button.setVisible(False)
        self.prenota_button.setVisible(False)
        self.logout_button.setVisible(False)
        self.dati_button.setVisible(False)
        self.prenotazioni_button.setVisible(False)
        self.cartella_clinica_button.setVisible(False)
        self.indietro_button.setVisible(False)

    def profilo_button_pressed(self):
        """
        Funzione che permette di passare alla nuova sezione del menù a tendina del paziente nel momento in cui viene
        premuto il button 'Il mio profilo'
        """
        self.dati_button.setVisible(True)
        self.prenotazioni_button.setVisible(True)
        self.cartella_clinica_button.setVisible(True)
        self.indietro_button.setVisible(True)
        self.profilo_button.setVisible(False)
        self.prenota_button.setVisible(False)

    def indietro_button_pressed(self):
        """
        Funzione che permette di tornare indeitro dalla nuova sezione del menù a tendina del paziente nel momento in cui
        viene premuto il button 'Indietro'
        """
        self.dati_button.setVisible(False)
        self.prenotazioni_button.setVisible(False)
        self.cartella_clinica_button.setVisible(False)
        self.indietro_button.setVisible(False)
        self.profilo_button.setVisible(True)
        self.prenota_button.setVisible(True)
