from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox

from personale_medico.login_personale_medico.view import view_login_personale_medico
from personale_medico.model.model_lista_pazienti_visitati import ListaPazientiVisitati
from personale_medico.view.view_dati_personali_personale_medico import ViewPersonaleMedico
from personale_medico.view import view_lista_pazienti_visitati
from personale_medico.view import view_prenotazioni_personale_medico


class ControllerListaPazientiVisitati:

    def __init__(self, widget):
        """
        Costruttore della classe ControllerListaPazientiVisitati, il quale crea le variabili di istanza e connette i
        button alle rispettive funzioni

        :param widget: Corrisponde alla ViewListaPazientiVisitati, nella quale viene creata un'istanza di questo
                        controller
        :type widget: QWidget
        """
        self.widget = widget
        self.personale_medico = widget.personale_medico
        self.model_lista_pazienti_visitati = ListaPazientiVisitati(self.personale_medico)

        widget.menu_a_tendina.dati_button.clicked.connect(self.go_dati_personali_personale_medico)
        widget.menu_a_tendina.prenotazioni_button.clicked.connect(self.go_lista_prenotazioni_personale_medico)
        widget.menu_a_tendina.pazienti_button.clicked.connect(self.go_lista_pazienti_visitati)
        widget.menu_a_tendina.logout_button.clicked.connect(self.go_login_personale_medico)

    def go_dati_personali_personale_medico(self):
        """
        Funzione che consente di passare alla ViewPersonaleMedico dalla view attuale
        """
        dati_personali = ViewPersonaleMedico(self.personale_medico)
        dati_personali.show()
        self.widget.hide()

    def go_lista_prenotazioni_personale_medico(self):
        """
        Funzione che consente di passare alla ViewPrenotazioniPersonaleMedico dalla view attuale
        """
        vista_prenotazioni_personale_medico = \
            view_prenotazioni_personale_medico.ViewPrenotazioniPersonaleMedico(self.personale_medico)
        lista_prenotazioni = vista_prenotazioni_personale_medico.controller_prenotazioni_personale_medico.\
            model_lista_prenotazioni_personale_medico.lista_prenotazioni_personale_medico
        lista_prenotazioni_personale_medico = []

        for prenotazione in lista_prenotazioni:
            if self.personale_medico.id_personale_medico == prenotazione.id_personale_medico:
                lista_prenotazioni_personale_medico.append(prenotazione)
        if not lista_prenotazioni_personale_medico:
            popup = QMessageBox()
            icona = QIcon()
            icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
            popup.setWindowIcon(icona)
            popup.setWindowTitle('Attenzione')
            popup.setIcon(QMessageBox.Warning)
            popup.setText('Non è presente alcuna prenotazione!')
            popup.exec_()
        else:
            vista_prenotazioni_personale_medico.show()
            self.widget.hide()

    def go_lista_pazienti_visitati(self):
        """
        Funzione che consente di passare alla ViewListaPazientiVisitati dalla view attuale
        """
        lista_pazienti_visitati = view_lista_pazienti_visitati.ViewListaPazientiVisitati(self.personale_medico)
        lista_pazienti_visitati.show()
        self.widget.hide()

    def go_login_personale_medico(self):
        """
        Funzione che consente di passare alla ViewLoginPersonaleMedico dalla view attuale
        """
        login_personale_medico = view_login_personale_medico.ViewLoginPersonaleMedico()
        login_personale_medico.show()
        self.widget.hide()
