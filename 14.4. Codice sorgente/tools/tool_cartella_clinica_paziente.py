from PyQt5 import QtCore, QtWidgets, QtGui

from tools import ridimensiona_widget


class ToolCartellaClinicaPaziente:

    def __init__(self, widget, scroll_area, widget_scroll_area, lista_prenotazioni):
        """
        Costruttore della classe ToolCartellaClinicaPaziente, nella quale vengono creati e gestiti tutti gli oggetti
        della Graphical User Interface (GUI) relativi alla scroll area della cartella clinica del paziente

        :param widget: Parametro che rappresenta un oggetto della classe ViewCartellaClinica
        :type widget: ViewCartellaClinica
        :param scroll_area: Parametro che rappresenta la scroll area
        :type scroll_area: QScrollArea
        :param widget_scroll_area: Parametro che rappresenta il contenuto della scroll area, nella quale sono inseriti
                                    i diversi oggetti delle prenotazioni all'interno della cartella clinica del paziente
        :type widget_scroll_area: QWidget
        :param lista_prenotazioni: Parametro che rappresenta la lista contenente tutte le prenotazioni effettuate dal
                                    paziente
        :type lista_prenotazioni: list
        """
        self.widget = widget
        self.lista_prenotazioni = lista_prenotazioni
        self.altezza = -1

        self.patologia_label = None
        self.patologia_label_2 = None

        self.moltiplicazione_del_pane_e_delle_label(widget_scroll_area)

        widget_scroll_area.setGeometry(QtCore.QRect(0, 0, 1771, self.altezza))
        scroll_area.setWidget(widget_scroll_area)

    def crea_label(self, widget_scroll_area, y, prenotazioni):
        """
        Funzione che crea e determina le caratteristiche degli oggetti all'interno della widget_scroll_area

        :param widget_scroll_area: Parametro che rappresenta il contenuto della scroll area, nella quale sono inseriti
                                    i diversi oggetti delle prenotazioni all'interno della cartella clinica del paziente
        :type widget_scroll_area: QWidget
        :param y: Parametro che rappresenta l'altezza di ogni singola label contenente le prenotazioni
        :type y: int
        :param prenotazioni: Parametro che rappresenta la lista di tutte le prenotazioni effettuate dal paziente
        :type prenotazioni: list
        """
        self.patologia_label = QtWidgets.QLabel(widget_scroll_area)
        self.patologia_label.setGeometry(QtCore.QRect(0, y, 875, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(18)
        self.patologia_label.setFont(font)
        self.patologia_label.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                           "border: 2px solid")
        self.patologia_label.setText(prenotazioni[0].attivita_ambulatoriale + ', ' +
                                     prenotazioni[0].data_ora_visita.strftime("%d/%m/%Y, %H:%M") + ', ' +
                                     prenotazioni[0].descrizione_patologia)
        self.patologia_label.setObjectName("patologia_label")
        self.patologia_label_2 = QtWidgets.QLabel(widget_scroll_area)
        self.patologia_label_2.setGeometry(QtCore.QRect(873, y, 877, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(18)
        self.patologia_label_2.setFont(font)
        self.patologia_label_2.setStyleSheet("background-color: rgb(169, 202, 239);\n"
                                             "border: 2px solid")
        if len(prenotazioni) > 1:
            self.patologia_label_2.setText(prenotazioni[1].attivita_ambulatoriale + ', ' +
                                           prenotazioni[1].data_ora_visita.strftime("%d/%m/%Y, %H:%M") + ', ' +
                                           prenotazioni[1].descrizione_patologia)
        self.patologia_label_2.setObjectName("patologia_label_2")

        ridimensiona_widget.ridimensiona_tool(self)

    def moltiplicazione_del_pane_e_delle_label(self, widget_scroll_area):
        """
        Funzione che calcola dinamicamente la dimensione e la posizione di ogni nuova label che si viene a creare nel
        momento in cui si aggiunge una visita effettuata nella cartella clinica del paziente

        :param widget_scroll_area: Parametro che rappresenta il contenuto della scroll area, nella quale sono inseriti
                                    i diversi oggetti delle prenotazioni all'interno della cartella clinica del paziente
        :type widget_scroll_area: QWidget
        """
        y = -1

        for i in range(len(self.lista_prenotazioni))[::2]:
            self.crea_label(widget_scroll_area, y + (29 * i), self.lista_prenotazioni[i: i + 2])
            self.altezza += 60
