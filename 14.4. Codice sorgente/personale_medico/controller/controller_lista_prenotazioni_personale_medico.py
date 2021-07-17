import pickle

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox

from personale_medico.login_personale_medico.view import view_login_personale_medico
from personale_medico.model.model_lista_prenotazioni_personale_medico import ListaPrenotazioniPersonaleMedico
from personale_medico.view.view_dati_personali_personale_medico import ViewPersonaleMedico
from personale_medico.view import view_prenotazioni_personale_medico
from personale_medico.view import view_lista_pazienti_visitati


class ControllerListaPrenotazioniPersonaleMedico:

    def __init__(self, widget):
        """
        Costruttore della classe ControllerListaPrenotazioniPersonaleMedico, il quale crea le variabili di istanza e
        connette i button alle rispettive funzioni

        :param widget: Corrisponde alla ViewPrenotazioniPersonaleMedico, nella quale viene creata un'istanza di
                        questo controller
        :type widget: QWidget
        """
        self.widget = widget
        self.personale_medico = widget.personale_medico
        self.model_lista_prenotazioni_personale_medico = ListaPrenotazioniPersonaleMedico(self.personale_medico)

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
        vista_prenotazioni_personale_medico.show()
        self.widget.hide()

    def go_lista_pazienti_visitati(self):
        """
        Funzione che consente di passare alla ViewListaPazientiVisitati dalla view attuale
        """
        lista_pazienti_visitati = view_lista_pazienti_visitati.ViewListaPazientiVisitati(self.personale_medico)

        if not lista_pazienti_visitati.controller_lista_pazienti_visitati.model_lista_pazienti_visitati.\
                lista_pazienti_da_modificare and not lista_pazienti_visitati.controller_lista_pazienti_visitati.\
                model_lista_pazienti_visitati.lista_pazienti_modificati:
            popup = QMessageBox()
            icona = QIcon()
            icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
            popup.setWindowIcon(icona)
            popup.setWindowTitle('Attenzione')
            popup.setIcon(QMessageBox.Warning)
            popup.setText('Non è stato visitato ancora nessun paziente!')
            popup.exec_()
        else:
            lista_pazienti_visitati.show()
            self.widget.hide()

    def go_login_personale_medico(self):
        """
        Funzione che consente di passare alla ViewLoginPersonaleMedico dalla view attuale
        """
        login_personale_medico = view_login_personale_medico.ViewLoginPersonaleMedico()
        login_personale_medico.show()
        self.widget.hide()

    @staticmethod
    def get_paziente_by_id(prenotazione):
        """
        Funzione che legge da file 'pazienti.pickle' e salva in una lista i pazienti, per poi confrontare l'id di ogni
        paziente della lista con quello presente nella prenotazione passata come parametro alla funzione stessa

        :param prenotazione: Parametro che rappresenta un oggetto della classe Prenotazione
        :type prenotazione: Prenotazione
        :return: La funzione ritorna tutti i pazienti che hanno l'id_paziente corrispondente a quello della prenotazione
                 passata come parametro in ingresso
        :rtype: Paziente
        """
        with open('paziente/login_paziente/data/pazienti.pickle', 'rb') as pazienti:
            lista_pazienti = pickle.load(pazienti)
        for paziente in lista_pazienti:
            if paziente.id_paziente == prenotazione.id_paziente:
                return paziente
