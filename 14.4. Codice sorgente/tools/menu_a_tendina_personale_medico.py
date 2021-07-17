from PyQt5 import QtCore, QtGui, QtWidgets

from personale_medico.view import view_home_personale_medico

from tools.animazioni import Animazioni


class MenuATendinaPersonaleMedico:

    def __init__(self, widget):
        """
        Costruttore della classe MenuATendinaPersonaleMedico, nella quale vengono creati e regolamentati tutti gli
        oggetti che formano il menù a tendina del personale medico

        :param widget: Parametro che rappresenta tutte le view del personale medico nelle quali è possibile utilizzare
                        il menù a tendina
        :type widget: QWidget
        """
        self.menu_tendina = QtWidgets.QLabel(widget)
        self.tendina_button = QtWidgets.QPushButton(widget)
        self.tendina_aperta_button = QtWidgets.QPushButton(widget)
        self.dati_button = QtWidgets.QPushButton(widget)
        self.prenotazioni_button = QtWidgets.QPushButton(widget)
        self.logout_button = QtWidgets.QPushButton(widget)
        self.ciao = QtWidgets.QLabel(widget)
        self.pazienti_button = QtWidgets.QPushButton(widget)
        self.setup_menu_a_tendina(widget)

        self.animazioni = Animazioni()

    def setup_menu_a_tendina(self, widget):
        """
        Funzione che crea e determina le caratteristiche degli oggetti del menù a tendina del personale medico

        :param widget: Parametro che rappresenta tutte le view del personale medico nelle quali è possibile utilizzare
                        il menù a tendina
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
        font.setPixelSize(32)
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
        self.ciao.setGeometry(QtCore.QRect(1585, 110, 301, 111))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(27)
        self.ciao.setFont(font)
        self.ciao.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ciao.setStyleSheet("color: rgb(33, 97, 171);")
        self.ciao.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.ciao.setText(
            f'<p>Ciao,<p style="color: white; font-weight: bold; font-size: 30px">'
            f'{widget.personale_medico.nome}</p></p>')
        self.ciao.setObjectName("ciao")
        self.ciao.setVisible(False)
        self.pazienti_button.setGeometry(QtCore.QRect(1490, 531, 430, 120))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(37)
        font.setBold(True)
        font.setWeight(75)
        self.pazienti_button.setFont(font)
        self.pazienti_button.setStyleSheet("QPushButton#pazienti_button {\n"
                                           "background-color: rgb(0, 0, 0, 0);\n"
                                           "color: rgb(33, 97, 171);\n"
                                           "border: 3px solid;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#pazienti_button:pressed {\n"
                                           "background-color: rgb(33, 97, 171);\n"
                                           "color: rgb(13, 41, 73);\n"
                                           "}")
        self.pazienti_button.setObjectName("pazienti_button")
        self.pazienti_button.setVisible(False)

        self.retranslate_menu_a_tendina()

    def retranslate_menu_a_tendina(self):
        """
        Funzione che formatta il testo degli oggetti creati all'interno del menù a tendina del personale medico
        """
        _translate = QtCore.QCoreApplication.translate
        self.dati_button.setText(_translate("widget", "DATI PERSONALI"))
        self.prenotazioni_button.setText(_translate("widget", "LISTA PRENOTAZIONI"))
        self.logout_button.setText(_translate("widget", "LOGOUT"))
        self.pazienti_button.setText(_translate("widget", "I MIEI PAZIENTI"))

    def tendina_button_pressed(self, widget):
        """
        Funzione che mostra il menù a tendina del personale medico nel momento in cui viene premuto l'apposito button

        :param widget: Parametro che rappresenta tutte le view del personale medico nelle quali è possibile utilizzare
                        il menù a tendina
        :type widget: QWidget
        """
        self.menu_tendina.setVisible(True)
        self.tendina_button.setVisible(False)
        self.tendina_aperta_button.setVisible(True)
        self.ciao.setVisible(True)
        self.dati_button.setVisible(True)
        self.prenotazioni_button.setVisible(True)
        self.pazienti_button.setVisible(True)
        self.logout_button.setVisible(True)

        self.animazioni.animazione_fade_in_totale.clear()

        self.animazioni.animazione_fade_in(self.menu_tendina)
        self.animazioni.animazione_fade_in(self.tendina_aperta_button)
        self.animazioni.animazione_fade_in(self.ciao)
        self.animazioni.animazione_fade_in(self.dati_button)
        self.animazioni.animazione_fade_in(self.prenotazioni_button)
        self.animazioni.animazione_fade_in(self.pazienti_button)
        self.animazioni.animazione_fade_in(self.logout_button)

        if isinstance(widget, view_home_personale_medico.ViewHomePersonaleMedico):

            self.animazioni.animazione_slide_totale.clear()

            self.animazioni.animazione_slide(widget.logo)
            self.animazioni.animazione_slide(widget.titolo)
            self.animazioni.animazione_slide(widget.scritta)

            self.animazioni.animazione_slide_totale.start()

        self.animazioni.animazione_fade_in_totale.start()

    def tendina_button_pressed_reverse(self, widget):
        """
        Funzione che nasconde il menù a tendina del paziente nel momento in cui viene premuto l'apposito button

        :param widget: Parametro che rappresenta tutte le view del personale medico nelle quali è possibile utilizzare
                        il menù a tendina
        :type widget: QWidget
        """
        self.tendina_aperta_button.setVisible(False)
        self.tendina_button.setVisible(True)

        self.animazioni.animazione_fade_out_totale.clear()

        self.animazioni.animazione_fade_out(self.menu_tendina)
        self.animazioni.animazione_fade_out(self.ciao)
        self.animazioni.animazione_fade_out(self.logout_button)
        self.animazioni.animazione_fade_out(self.dati_button)
        self.animazioni.animazione_fade_out(self.prenotazioni_button)
        self.animazioni.animazione_fade_out(self.pazienti_button)

        if isinstance(widget, view_home_personale_medico.ViewHomePersonaleMedico):

            self.animazioni.animazione_slide_reverse_totale.clear()

            self.animazioni.animazione_slide_reverse(widget.logo)
            self.animazioni.animazione_slide_reverse(widget.titolo)
            self.animazioni.animazione_slide_reverse(widget.scritta)

            self.animazioni.animazione_slide_reverse_totale.start()

        self.animazioni.animazione_fade_out_totale.start()

        self.animazioni.animazione_fade_out_totale.finished.connect(self.chiudi_tutto)

    def chiudi_tutto(self):
        """
        Funzione che nasconde tutti gli oggetti del menù a tendina del personale medico
        """
        self.menu_tendina.setVisible(False)
        self.tendina_button.setVisible(True)
        self.tendina_aperta_button.setVisible(False)
        self.ciao.setVisible(False)
        self.dati_button.setVisible(False)
        self.prenotazioni_button.setVisible(False)
        self.logout_button.setVisible(False)
        self.pazienti_button.setVisible(False)
