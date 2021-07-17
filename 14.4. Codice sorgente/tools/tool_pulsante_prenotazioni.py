from PyQt5 import QtGui, QtWidgets, QtCore

from tools import ridimensiona_widget


class PulsantePrenotazioni:
    def __init__(self, posizione, widget, dizionario, ambulatorio):
        """
        Costruttore della classe PulsantePrenotazioni, nella quale vengono creati e regolati i button relativi alle
        attività ambulatoriali in base all'ambulatorio scelto

        :param posizione: Parametro che rappresenta la posizione dei button dove sono inserite le attività ambulatoriali
        :type posizione: int
        :param widget: Parametro che rappresenta un oggetto della classe ViewPrenotaOra
        :type widget: ViewPrenotaOra
        :param dizionario: Parametro che rappresenta un oggetto di tipo dict, nel quale verrano inserite le attività
                            ambulatoriali
        :type dizionario: dict
        :param ambulatorio: Parametro che rappresenta l'ambulatorio selezionato dal paziente in fase di prenotazione
        :type ambulatorio: str
        """
        self.posizione = posizione
        self.widget = widget
        self.dizionario = dizionario
        self.ambulatorio = ambulatorio

        self.pulsante = QtWidgets.QPushButton()

        self.crea_pulsante()

    def crea_pulsante(self):
        """
        Funzione che crea e determina le caratteristiche dei button relativi alle attività ambulatoriali
        """
        self.pulsante = QtWidgets.QPushButton(self.widget)
        self.pulsante.setGeometry(QtCore.QRect(690, self.posizione, 360, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pulsante.setFont(font)
        self.pulsante.setStyleSheet("QPushButton#pulsante {\n"
                                    "background-color: rgb(33, 97, 171);\n"
                                    "border: 1px solid;\n"
                                    "border-color: rgb(13, 41, 73);\n"
                                    "border-radius: 10px;\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "QPushButton#pulsante:pressed {\n"
                                    "background-color: rgb(13, 41, 73);\n"
                                    "border-color: rgb(33, 97, 171);\n"
                                    "color: rgb(200, 200, 200);\n"
                                    "}")
        self.pulsante.setObjectName("pulsante")
        self.pulsante.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        if self.dizionario.get('specializzazione') is not None:
            self.pulsante.setText(self.dizionario['specializzazione'])
            self.pulsante.clicked.connect(self.attivita_ambulatoriali_specializzazione)
        else:
            self.pulsante.setText(self.dizionario['attivita_ambulatoriale'])
        self.pulsante.show()

        ridimensiona_widget.ridimensiona_tool(self)

    def attivita_ambulatoriali_specializzazione(self):
        """
        Funzione che regola i button delle attività ambulatoriali nel caso in cui queste facciano parte dell'ambulatorio
        di 'Medicina Generale Cardiologica', per il quale le attività ambulatoriali sono suddivise in 4 ulteriori
        sezioni, ovvero le specializzazioni
        """
        self.widget.attivita_ambulatoriale_label.setText("ATTIVITA' AMBULATORIALE")
        for pulsante_prenotazione in self.widget.lista_pulsanti:
            pulsante_prenotazione.pulsante.hide()
        self.widget.lista_pulsanti.clear()
        posizione = 250
        for attivita_ambulatoriale in self.dizionario['lista_attivita_ambulatoriali']:
            self.widget.lista_pulsanti.append(PulsantePrenotazioni(posizione, self.widget, attivita_ambulatoriale,
                                                                   self.ambulatorio))
            posizione += 60
            # for pulsante_prenotazione in self.widget.lista_pulsanti:
            #    pulsante_prenotazione.pulsante.clicked.connect(self.widget.visualizza_terza_slide)

        if self.dizionario.get('specializzazione') == "Cardiovascolari":
            self.widget.lista_pulsanti[0].pulsante.clicked.connect(
                lambda: self.widget.controller_prenotazioni.visualizza_terza_slide(self.widget.lista_pulsanti[0]))
            self.widget.lista_pulsanti[1].pulsante.clicked.connect(
                lambda: self.widget.controller_prenotazioni.visualizza_terza_slide(self.widget.lista_pulsanti[1]))
            self.widget.lista_pulsanti[2].pulsante.clicked.connect(
                lambda: self.widget.controller_prenotazioni.visualizza_terza_slide(self.widget.lista_pulsanti[2]))
            self.widget.lista_pulsanti[3].pulsante.clicked.connect(
                lambda: self.widget.controller_prenotazioni.visualizza_terza_slide(self.widget.lista_pulsanti[3]))
            self.widget.lista_pulsanti[4].pulsante.clicked.connect(
                lambda: self.widget.controller_prenotazioni.visualizza_terza_slide(self.widget.lista_pulsanti[4]))
            self.widget.lista_pulsanti[5].pulsante.clicked.connect(
                lambda: self.widget.controller_prenotazioni.visualizza_terza_slide(self.widget.lista_pulsanti[5]))

        elif self.dizionario.get('specializzazione') == "Pneumologia":
            self.widget.lista_pulsanti[0].pulsante.clicked.connect(
                lambda: self.widget.controller_prenotazioni.visualizza_terza_slide(self.widget.lista_pulsanti[0]))

        elif self.dizionario.get('specializzazione') == "Gastroenterologia":
            self.widget.lista_pulsanti[0].pulsante.clicked.connect(
                lambda: self.widget.controller_prenotazioni.visualizza_terza_slide(self.widget.lista_pulsanti[0]))
            self.widget.lista_pulsanti[1].pulsante.clicked.connect(
                lambda: self.widget.controller_prenotazioni.visualizza_terza_slide(self.widget.lista_pulsanti[1]))
            self.widget.lista_pulsanti[2].pulsante.clicked.connect(
                lambda: self.widget.controller_prenotazioni.visualizza_terza_slide(self.widget.lista_pulsanti[2]))

        elif self.dizionario.get('specializzazione') == "Neurologia":
            self.widget.lista_pulsanti[0].pulsante.clicked.connect(
                lambda: self.widget.controller_prenotazioni.visualizza_terza_slide(self.widget.lista_pulsanti[0]))
