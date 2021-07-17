from PyQt5 import QtWidgets, QtCore, QtGui

from tools import ridimensiona_widget


class ToolPazientiModificati:
    def __init__(self, widget, scroll_area, widget_scroll_area, lista_pazienti_visitati):
        """
        Costruttore della classe ToolPazientiModificati, nella quale vengono creati e gestiti tutti gli oggetti
        della Graphical User Interface (GUI) relativi alla scroll area dove sono inserite le visite effettuate dal
        personale medico ai pazienti per le quali è già stata modificata la descrizione della patologia
        riscontrata

        :param widget: Parametro che rappresenta un oggetto della classe ViewListaPazientiVisitati
        :type widget: ViewListaPazientiVisitati
        :param scroll_area: Parametro che rappresenta la scroll area
        :type scroll_area: QScrollArea
        :param widget_scroll_area: Parametro che rappresenta il contenuto della scroll area, nella quale sono inseriti
                                    i diversi oggetti delle prenotazioni delle visite effettuate
        :type widget_scroll_area: QWidget
        :param lista_pazienti_visitati: Parametro che rappresenta un oggetto della classe ListaPazientiVisitati
        :type lista_pazienti_visitati: ListaPazientiVisitati
        """
        self.widget = widget
        self.lista_pazienti_visitati = lista_pazienti_visitati
        self.altezza = 23

        self.nome_label_mod = None
        self.ambulatorio_label_mod = None
        self.attivita_ambulatoriale_label_mod = None
        self.data_e_ora_label_mod = None
        self.patologia_riscontrata_label_mod = None

        self.moltiplicazione_del_pane_e_delle_label(widget_scroll_area)

        widget_scroll_area.setGeometry(QtCore.QRect(0, 0, 1811, self.altezza))
        scroll_area.setWidget(widget_scroll_area)

    def crea_label(self, widget_scroll_area, y, prenotazione):
        """
        Funzione che crea e determina le caratteristiche degli oggetti all'interno della widget_scroll_area

        :param widget_scroll_area: Parametro che rappresenta il contenuto della scroll area, nella quale sono inseriti
                                    i diversi oggetti delle prenotazioni delle visite effettuate
        :type widget_scroll_area: QWidget
        :param y: Parametro che rappresenta l'altezza di ogni singola label contenente le prenotazioni
        :type y: int
        :param prenotazione: Parametro che rappresenta un oggetto della classe Prenotazione
        :type prenotazione: Prenotazione
        """
        self.nome_label_mod = QtWidgets.QLabel(widget_scroll_area)
        self.nome_label_mod.setGeometry(QtCore.QRect(0, y, 325, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        self.nome_label_mod.setFont(font)
        self.nome_label_mod.setStyleSheet("border: 2px solid;\n"
                                          "background-color: rgb(169, 202, 239);")
        self.nome_label_mod.setText("")
        self.nome_label_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.nome_label_mod.setObjectName("nome_label_mod")
        self.nome_label_mod.setText(prenotazione.nome_paziente + ' ' + prenotazione.cognome_paziente)

        self.ambulatorio_label_mod = QtWidgets.QLabel(widget_scroll_area)
        self.ambulatorio_label_mod.setGeometry(QtCore.QRect(323, y, 400, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        self.ambulatorio_label_mod.setFont(font)
        self.ambulatorio_label_mod.setStyleSheet("border: 2px solid;\n"
                                                 "background-color: rgb(84, 149, 223);")
        self.ambulatorio_label_mod.setText("")
        self.ambulatorio_label_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.ambulatorio_label_mod.setObjectName("ambulatorio_label_mod")
        self.ambulatorio_label_mod.setText(prenotazione.ambulatorio)

        self.attivita_ambulatoriale_label_mod = QtWidgets.QLabel(widget_scroll_area)
        self.attivita_ambulatoriale_label_mod.setGeometry(QtCore.QRect(721, y, 400, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        self.attivita_ambulatoriale_label_mod.setFont(font)
        self.attivita_ambulatoriale_label_mod.setStyleSheet("border: 2px solid;\n"
                                                            "background-color: rgb(169, 202, 239);")
        self.attivita_ambulatoriale_label_mod.setText("")
        self.attivita_ambulatoriale_label_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.attivita_ambulatoriale_label_mod.setObjectName("attivita_ambulatoriale_label_mod")
        self.attivita_ambulatoriale_label_mod.setText(prenotazione.attivita_ambulatoriale)

        self.data_e_ora_label_mod = QtWidgets.QLabel(widget_scroll_area)
        self.data_e_ora_label_mod.setGeometry(QtCore.QRect(1119, y, 400, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        self.data_e_ora_label_mod.setFont(font)
        self.data_e_ora_label_mod.setStyleSheet("border: 2px solid;\n"
                                                "background-color: rgb(84, 149, 223);")
        self.data_e_ora_label_mod.setText("")
        self.data_e_ora_label_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.data_e_ora_label_mod.setObjectName("data_e_ora_label_mod")
        self.data_e_ora_label_mod.setText(prenotazione.data_ora_visita.strftime("%d/%m/%Y, %H:%M"))

        self.patologia_riscontrata_label_mod = QtWidgets.QLabel(widget_scroll_area)
        self.patologia_riscontrata_label_mod.setGeometry(QtCore.QRect(1517, y, 273, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        self.patologia_riscontrata_label_mod.setFont(font)
        self.patologia_riscontrata_label_mod.setStyleSheet("border: 2px solid;\n"
                                                           "background-color: rgb(169, 202, 239);")
        self.patologia_riscontrata_label_mod.setText("")
        self.patologia_riscontrata_label_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.patologia_riscontrata_label_mod.setObjectName("patologia_riscontrata_label_mod")
        self.patologia_riscontrata_label_mod.setText(prenotazione.descrizione_patologia)

        ridimensiona_widget.ridimensiona_tool(self)

    def moltiplicazione_del_pane_e_delle_label(self, widget_scroll_area):
        """
        Funzione che calcola dinamicamente la dimensione e la posizione di ogni nuova label che si viene a creare nel
        momento in cui si aggiunge una prenotazione di una visita effettuata

        :param widget_scroll_area: Parametro che rappresenta il contenuto della scroll area, nella quale sono inseriti
                                    i diversi oggetti delle prenotazioni delle visite effettuate
        :type widget_scroll_area: QWidget
        """
        y = 23

        for prenotazione, i in zip(self.lista_pazienti_visitati.lista_pazienti_modificati_personale_medico,
                                   range(len(self.lista_pazienti_visitati.lista_pazienti_modificati))):
            self.crea_label(widget_scroll_area, y + (88 * i), prenotazione)
            self.altezza += 90
