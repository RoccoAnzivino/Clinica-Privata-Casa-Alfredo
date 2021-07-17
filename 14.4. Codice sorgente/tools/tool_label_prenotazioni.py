from PyQt5 import QtGui, QtWidgets, QtCore

from paziente.view import view_prenotazione

from tools import ridimensiona_widget


class LabelPrenotazioni:

    def __init__(self, widget, scroll_area, paziente, widget_scroll_area, lista_prenotazioni):
        """
        Costruttore della classe LabelPrenotazioni, nella quale vengono creati e gestiti tutti gli oggetti
        della Graphical User Interface (GUI) relativi alla scroll area delle prenotazioni effettuate

        :param widget: Parametro che rappresenta un oggetto della classe ViewListaPrenotazioni
        :type widget: ViewListaPrenotazioni
        :param scroll_area: Parametro che rappresenta la scroll area
        :type scroll_area: QScrollArea
        :param paziente: Variabile d'istanza che rappresenta un oggetto della classe Paziente
        :type paziente: Paziente
        :param widget_scroll_area: Parametro che rappresenta il contenuto della scroll area, nella quale sono inseriti
                                    i diversi oggetti delle prenotazioni
        :type widget_scroll_area: QWidget
        :param lista_prenotazioni: Parametro che rappresenta la lista contenente tutte le prenotazioni effettuate
        :type lista_prenotazioni: list
        """
        self.widget = widget
        self.paziente = paziente
        self.lista_prenotazioni = lista_prenotazioni
        self.altezza = 23

        self.label_nome = None
        self.label_attivita = None
        self.label_medico = None
        self.label_data_e_ora = None
        self.visualizza_prenotazione_button = None

        self.moltiplicazione_del_pane_e_delle_label(widget_scroll_area)

        widget_scroll_area.setGeometry(QtCore.QRect(0, 0, 1790, self.altezza))
        scroll_area.setWidget(widget_scroll_area)

    def crea_label(self, widget_scroll_area, y, prenotazione):
        """
        Funzione che crea e determina le caratteristiche degli oggetti all'interno della widget_scroll_area

        :param widget_scroll_area: Parametro che rappresenta il contenuto della scroll area, nella quale sono inseriti
                                    i diversi oggetti delle prenotazioni
        :type widget_scroll_area: QWidget
        :param y: Parametro che rappresenta l'altezza di ogni singola label contenente le prenotazioni
        :type y: int
        :param prenotazione: Parametro che rappresenta un oggetto della classe Prenotazione
        :type prenotazione: Prenotazione
        """
        self.label_nome = QtWidgets.QLabel(widget_scroll_area)
        self.label_nome.setGeometry(QtCore.QRect(0, y, 280, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        self.label_nome.setFont(font)
        self.label_nome.setStyleSheet("border: 2px solid;\n"
                                      "background-color: rgb(169, 202, 239);")
        self.label_nome.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nome.setObjectName("label_nome")
        self.label_nome.setText(prenotazione.id_prenotazione[4:])

        self.label_attivita = QtWidgets.QLabel(widget_scroll_area)
        self.label_attivita.setGeometry(QtCore.QRect(278, y, 575, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        self.label_attivita.setFont(font)
        self.label_attivita.setStyleSheet("border: 2px solid;\n"
                                          "background-color: rgb(84, 149, 223);")
        self.label_attivita.setAlignment(QtCore.Qt.AlignCenter)
        self.label_attivita.setObjectName("label_attivita")
        self.label_attivita.setText(prenotazione.attivita_ambulatoriale)

        self.label_medico = QtWidgets.QLabel(widget_scroll_area)
        self.label_medico.setGeometry(QtCore.QRect(851, y, 353, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        self.label_medico.setFont(font)
        self.label_medico.setStyleSheet("border: 2px solid;\n"
                                        "background-color: rgb(169, 202, 239);")
        self.label_medico.setAlignment(QtCore.Qt.AlignCenter)
        self.label_medico.setObjectName("label_medico")
        self.label_medico.setText(prenotazione.cognome_personale_medico + ' ' + prenotazione.nome_personale_medico)

        self.label_data_e_ora = QtWidgets.QLabel(widget_scroll_area)
        self.label_data_e_ora.setGeometry(QtCore.QRect(1202, y, 500, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        self.label_data_e_ora.setFont(font)
        self.label_data_e_ora.setStyleSheet("border: 2px solid;\n"
                                            "background-color: rgb(84, 149, 223);")
        self.label_data_e_ora.setAlignment(QtCore.Qt.AlignCenter)
        self.label_data_e_ora.setObjectName("label_data_e_ora")
        self.label_data_e_ora.setText((prenotazione.data_ora_visita.strftime("%d/%m/%Y, %H:%M")))

        self.visualizza_prenotazione_button = QtWidgets.QPushButton(widget_scroll_area)
        self.visualizza_prenotazione_button.setGeometry(QtCore.QRect(1700, y, 90, 90))
        self.visualizza_prenotazione_button.setStyleSheet("border: 2px solid;\n"
                                                          "background-color: rgb(169, 202, 239);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Immagini/apri.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("Immagini/apri.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap("Immagini/apri pressed.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("Immagini/apri pressed.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap("Immagini/apri.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.visualizza_prenotazione_button.setIcon(icon2)
        self.visualizza_prenotazione_button.setIconSize(QtCore.QSize(50, 50))
        self.visualizza_prenotazione_button.setObjectName("visualizza_prenotazione_button")
        self.visualizza_prenotazione_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.visualizza_prenotazione_button.clicked.connect(lambda: self.go_prenotazione(prenotazione))

        ridimensiona_widget.ridimensiona_tool(self)

    def moltiplicazione_del_pane_e_delle_label(self, widget_scroll_area):
        """
        Funzione che calcola dinamicamente la dimensione e la posizione di ogni nuova label che si viene a creare nel
        momento in cui si aggiunge una prenotazione

        :param widget_scroll_area: Parametro che rappresenta il contenuto della scroll area, nella quale sono inseriti
                                    i diversi oggetti delle prenotazioni
        :type widget_scroll_area: QWidget
        """
        y = 23

        for prenotazione, i in zip(self.lista_prenotazioni, range(len(self.lista_prenotazioni))):
            self.crea_label(widget_scroll_area, y + (88 * i), prenotazione)
            self.altezza += 90

    def go_prenotazione(self, prenotazione):
        """
        Funzione che permette di passare alla ViewPrenotazione

        :param prenotazione: Parametro che rappresenta un oggetto della classe Prenotazione
        :type prenotazione: Prenotazione
        """
        prenotazione = view_prenotazione.ViewPrenotazione(self.paziente, prenotazione, self.lista_prenotazioni)
        prenotazione.show()
        self.widget.hide()
