from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox

from personale_medico.view import view_cartella_clinica_personale_medico

from tools import ridimensiona_widget


class ToolPrenotazioniPersonaleMedico:
    def __init__(self, widget, scroll_area, widget_scroll_area, lista_prenotazioni):
        """
        Costruttore della classe ToolPrenotazioniPersonaleMedico, nella quale vengono creati e gestiti tutti gli oggetti
        della Graphical User Interface (GUI) relativi alla scroll area dove sono inserite le prenotazioni effettuate dai
        pazienti relative al personale medico

        :param widget: Parametro che rappresenta un oggetto della classe ViewPrenotazioniPersonaleMedico
        :type widget: ViewPrenotazioniPersonaleMedico
        :param scroll_area: Parametro che rappresenta la scroll area
        :type scroll_area: QScrollArea
        :param widget_scroll_area: Parametro che rappresenta il contenuto della scroll area, nella quale sono inseriti
                                    i diversi oggetti delle prenotazioni
        :type widget_scroll_area: QWidget
        :param lista_prenotazioni: Parametro che rappresenta la lista contenente tutte le prenotazioni effettuate
        :type lista_prenotazioni: list
        """
        self.widget = widget
        self.lista_prenotazioni = lista_prenotazioni
        self.altezza = 23

        self.nome_label = None
        self.attivita_ambulatoriale_label = None
        self.data_e_ora_label = None
        self.visualizza_cartella_clinica_button = None

        self.moltiplicazione_del_pane_e_delle_label(widget_scroll_area)

        widget_scroll_area.setGeometry(QtCore.QRect(0, 0, 1755, self.altezza))
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
        self.nome_label = QtWidgets.QLabel(widget_scroll_area)
        self.nome_label.setGeometry(QtCore.QRect(0, y, 400, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        self.nome_label.setFont(font)
        self.nome_label.setStyleSheet("border: 2px solid;\n"
                                      "background-color: rgb(84, 149, 223);")
        self.nome_label.setText("")
        self.nome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.nome_label.setObjectName("nome_label")
        self.nome_label.setText(prenotazione.nome_paziente + ' ' + prenotazione.cognome_paziente)
        self.attivita_ambulatoriale_label = QtWidgets.QLabel(widget_scroll_area)
        self.attivita_ambulatoriale_label.setGeometry(QtCore.QRect(398, y, 500, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        self.attivita_ambulatoriale_label.setFont(font)
        self.attivita_ambulatoriale_label.setStyleSheet("border: 2px solid;\n"
                                                        "background-color: rgb(169, 202, 239);")
        self.attivita_ambulatoriale_label.setText("")
        self.attivita_ambulatoriale_label.setAlignment(QtCore.Qt.AlignCenter)
        self.attivita_ambulatoriale_label.setObjectName("attivita_ambulatoriale_label")
        self.attivita_ambulatoriale_label.setText(prenotazione.attivita_ambulatoriale)
        self.data_e_ora_label = QtWidgets.QLabel(widget_scroll_area)
        self.data_e_ora_label.setGeometry(QtCore.QRect(896, y, 500, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        self.data_e_ora_label.setFont(font)
        self.data_e_ora_label.setStyleSheet("border: 2px solid;\n"
                                            "background-color: rgb(84, 149, 223);")
        self.data_e_ora_label.setText("")
        self.data_e_ora_label.setAlignment(QtCore.Qt.AlignCenter)
        self.data_e_ora_label.setObjectName("data_e_ora_label")
        self.data_e_ora_label.setText(prenotazione.data_ora_visita.strftime("%d/%m/%Y, %H:%M"))
        self.visualizza_cartella_clinica_button = QtWidgets.QPushButton(widget_scroll_area)
        self.visualizza_cartella_clinica_button.setGeometry(QtCore.QRect(1394, y, 340, 90))
        self.visualizza_cartella_clinica_button.setStyleSheet("border: 2px solid;\n"
                                                              "background-color: rgb(169, 202, 239);")
        self.visualizza_cartella_clinica_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Immagini/apri.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("Immagini/apri.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap("Immagini/apri pressed.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("Immagini/apri pressed.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap("Immagini/apri.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.visualizza_cartella_clinica_button.setIcon(icon2)
        self.visualizza_cartella_clinica_button.setIconSize(QtCore.QSize(50, 50))
        self.visualizza_cartella_clinica_button.setObjectName("visualizza_cartella_clinica_button")
        self.visualizza_cartella_clinica_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.visualizza_cartella_clinica_button.clicked.connect(lambda:
                                                                self.go_cartella_clinica_personale_medico(prenotazione))

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

    def go_cartella_clinica_personale_medico(self, prenotazione):
        """
        Funzione che consente di passare alla ViewCartellaClinicaPersonaleMedico

        :param prenotazione: Parametro che rappresenta un oggetto della classe Prenotazione
        :type prenotazione: Prenotazione
        """
        cartella_clinica_personale_medico = \
            view_cartella_clinica_personale_medico.ViewCartellaClinicaPersonaleMedico(
                self.widget.controller_prenotazioni_personale_medico.get_paziente_by_id(prenotazione),
                self.widget.personale_medico)
        lista_prenotazioni_cartella_clinica = cartella_clinica_personale_medico.controller_cartella_clinica. \
            model_cartella_clinica.lista_prenotazioni_cartella_clinica

        if not lista_prenotazioni_cartella_clinica:
            popup = QMessageBox()
            icona = QIcon()
            icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
            popup.setWindowIcon(icona)
            popup.setWindowTitle('Attenzione')
            popup.setIcon(QMessageBox.Warning)
            popup.setText('Il paziente non ha mai effettuato visite nei nostri ambulatori!')
            popup.exec_()
        else:
            cartella_clinica_personale_medico.show()
            cartella_clinica_personale_medico.controller_cartella_clinica.set_labels_text()
            self.widget.hide()
