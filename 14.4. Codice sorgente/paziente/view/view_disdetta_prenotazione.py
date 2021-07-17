from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox

from paziente.controller import controller_lista_prenotazioni_pazienti


class ViewDisdettaPrenotazione:

    def __init__(self, widget_prenotazione, prenotazione):
        """
        Costruttore della classe ViewDisdettaPrenotazione, nella quale vengono creati e mostrati tutti gli oggetti della
        Graphical User Interface (GUI) relativi alla suddetta view

        :param widget_prenotazione: Variabile d'istanza che rappresenta un oggetto della classe ViewPrenotazione
        :type widget_prenotazione: ViewPrenotazione
        :param prenotazione: Variabile d'istanza che rappresenta un oggetto della classe Prenotazione
        :type prenotazione: Prenotazione
        """
        self.widget_prenotazione = widget_prenotazione
        self.prenotazione = prenotazione
        self.paziente = widget_prenotazione.paziente
        self.popup = None

        self.crea_popup()

        self.controller_lista_prenotazioni_pazienti = controller_lista_prenotazioni_pazienti.\
            ControllerListaPrenotazioniPazienti(self)

        self.esegui_popup()

    def crea_popup(self):
        """
        Funzione che crea l'oggetto popup, il quale viene visualizzato nel momento in cui si vuole disdire una
        prenotazione tramite l'apposito button
        """
        self.popup = QMessageBox()
        icona = QIcon()
        icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
        self.popup.setWindowIcon(icona)
        self.popup.setWindowTitle('Conferma')
        self.popup.setIcon(QMessageBox.Question)
        self.popup.setText('Vuoi davvero disdire la prenotazione?')
        self.popup.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        self.popup.button(QMessageBox.Yes).setText('Sì')
        self.popup.button(QMessageBox.No).setText('No')

    def esegui_popup(self):
        """
        Funzione che esegue l'oggetto popup creato con la funzione 'crea_popup'
        """
        self.popup.exec_()
