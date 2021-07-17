from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox

from personale_medico.login_personale_medico.view import view_login_personale_medico
from personale_medico.view import view_lista_pazienti_visitati
from personale_medico.view.view_dati_personali_personale_medico import ViewPersonaleMedico
from personale_medico.view import view_prenotazioni_personale_medico


class ControllerPersonaleMedico:

    def __init__(self, widget):
        """
        Costruttore della classe ControllerPersonaleMedoco, il quale crea le variabili di istanza e connette i
        button alle rispettive funzioni a seconda dell'istanza alla quale questi appartengono

        :param widget: Corrisponde alla ViewPersonaleMedico o alla ViewHomePersonaleMedico, nelle
                        quali viene creata un'istanza di questo controller
        :type widget: QWidget
        """
        self.widget = widget
        self.model_personale_medico = widget.personale_medico

        if isinstance(self.widget, ViewPersonaleMedico):

            widget.occhiello_button.clicked.connect(widget.occhiello_button_pressed)

            widget.occhiello_barrato_button.clicked.connect(widget.occhiello_barrato_button_pressed)

            widget.modifica_password.clicked.connect(self.modifica_password_button_pressed)

            widget.annulla_modifica_password.clicked.connect(self.annulla_modifica_password_button_pressed)

            # recupero dati personale_medico
            # conversione datetime in stringa setText accetta solo stringhe e non datetime
            date_time_to_str = self.widget.personale_medico.data_di_nascita.strftime("%d/%m/%Y")
            # conversione int in stringa perchè setText accetta solo stringhe e non interi
            converted_eta = str(self.widget.personale_medico.eta)

            widget.nome_label.setText(widget.personale_medico.nome)
            widget.cognome_label.setText(widget.personale_medico.cognome)
            widget.data_di_nascita_label.setText(date_time_to_str)
            widget.eta_label.setText(converted_eta)
            widget.sesso_label.setText(widget.personale_medico.sesso)
            widget.provincia_label.setText(widget.personale_medico.provincia_di_nascita)
            widget.citta_di_nascita_label.setText(widget.personale_medico.citta_di_nascita)
            widget.email_label.setText(widget.personale_medico.email)
            widget.codice_fiscale_label.setText(widget.personale_medico.codice_fiscale)
            widget.ambulatorio_label.setText(widget.personale_medico.ambulatorio)
            widget.codice_id_label.setText(widget.personale_medico.codice_identificativo)
            widget.password_line_edit.setText(widget.personale_medico.password)

            widget.conferma_button.clicked.connect(self.go_modifica_password)

            widget.conferma_password_line_edit.returnPressed.connect(self.go_modifica_password)

        # DATI PERSONALI personale_medico
        # pulsante che, se premuto, permette di aprire la schermata dati personali del personale_medico
        widget.menu_a_tendina.dati_button.clicked.connect(self.go_dati_personali_personale_medico)

        # Non sono un folle come Kevin e col caBBo che commento
        widget.menu_a_tendina.prenotazioni_button.clicked.connect(self.go_lista_prenotazioni_personale_medico)

        # Stessa cosa di sopra
        widget.menu_a_tendina.pazienti_button.clicked.connect(self.go_lista_pazienti_visitati)

        # LOGIN personale_medico
        # pulsante che, se premuto, permette di tornare alla schermata login personale_medico
        widget.menu_a_tendina.logout_button.clicked.connect(self.go_login_personale_medico)

    def go_dati_personali_personale_medico(self):
        """
        Funzione che consente di passare alla ViewPersonaleMedico dalla view attuale
        """
        dati_personali = ViewPersonaleMedico(self.model_personale_medico)
        dati_personali.show()
        self.widget.hide()

    def go_lista_prenotazioni_personale_medico(self):
        """
        Funzione che consente di passare alla ViewPrenotazioniPersonaleMedico dalla view attuale
        """
        vista_prenotazioni_personale_medico =\
            view_prenotazioni_personale_medico.ViewPrenotazioniPersonaleMedico(self.model_personale_medico)
        lista_prenotazioni = vista_prenotazioni_personale_medico.controller_prenotazioni_personale_medico.\
            model_lista_prenotazioni_personale_medico.lista_prenotazioni_personale_medico
        lista_prenotazioni_personale_medico = []

        for prenotazione in lista_prenotazioni:
            if self.model_personale_medico.id_personale_medico == prenotazione.id_personale_medico:
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
        lista_pazienti_visitati = view_lista_pazienti_visitati.ViewListaPazientiVisitati(self.model_personale_medico)

        if not lista_pazienti_visitati.controller_lista_pazienti_visitati.model_lista_pazienti_visitati. \
                lista_pazienti_da_modificare and not lista_pazienti_visitati.controller_lista_pazienti_visitati. \
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

    def go_modifica_password(self):
        """
        Funzione che rimanda l'utente alla ViewLoginPersonaleMedico dopo che è stata modificata la password dalla
        ViewPersonaleMedico
        """
        if (not self.widget.vecchia_password_line_edit.text()
                or not self.widget.nuova_password_line_edit.text()
                or not self.widget.conferma_password_line_edit.text()):
            popup = QMessageBox()
            icona = QIcon()
            icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
            popup.setWindowIcon(icona)
            popup.setWindowTitle('Attenzione')
            popup.setIcon(QMessageBox.Warning)
            popup.setText('Riempire accuratamente tutti i campi!')
            popup.exec_()
        else:

            if self.model_personale_medico.set_password_personale_medico(self.widget.nuova_password_line_edit.text(),
                                                                         self.widget.conferma_password_line_edit.text(),
                                                                         self.widget.vecchia_password_line_edit.text()):
                self.go_login_personale_medico()

    def modifica_password_button_pressed(self):
        """
        Funzione che rende visibile la sezione di modifica password nel momento in cui viene premuto l'apposito button
        """
        self.widget.modifica_password.setVisible(False)
        self.widget.annulla_modifica_password.setVisible(True)
        self.widget.modifica_password_label.setVisible(True)
        self.widget.vecchia_password.setVisible(True)
        self.widget.nuova_password.setVisible(True)
        self.widget.confema_password.setVisible(True)
        self.widget.vecchia_password_line_edit.setVisible(True)
        self.widget.nuova_password_line_edit.setVisible(True)
        self.widget.conferma_password_line_edit.setVisible(True)
        self.widget.scritta.setVisible(True)
        self.widget.conferma_button.setVisible(True)

        self.widget.animazioni.animazione_fade_in_totale.clear()

        self.widget.animazioni.animazione_fade_in(self.widget.modifica_password_label)
        self.widget.animazioni.animazione_fade_in(self.widget.vecchia_password)
        self.widget.animazioni.animazione_fade_in(self.widget.nuova_password)
        self.widget.animazioni.animazione_fade_in(self.widget.confema_password)
        self.widget.animazioni.animazione_fade_in(self.widget.vecchia_password_line_edit)
        self.widget.animazioni.animazione_fade_in(self.widget.nuova_password_line_edit)
        self.widget.animazioni.animazione_fade_in(self.widget.conferma_password_line_edit)
        self.widget.animazioni.animazione_fade_in(self.widget.scritta)
        self.widget.animazioni.animazione_fade_in(self.widget.conferma_button)

        self.widget.animazioni.animazione_fade_in_totale.start()

    def annulla_modifica_password_button_pressed(self):
        """
        Funzione che nasconde la sezione di modifica password nel momento in cui viene premuto l'apposito button
        """
        self.widget.modifica_password.setVisible(True)
        self.widget.annulla_modifica_password.setVisible(False)

        self.widget.animazioni.animazione_fade_out_totale.clear()

        self.widget.animazioni.animazione_fade_out(self.widget.modifica_password_label)
        self.widget.animazioni.animazione_fade_out(self.widget.vecchia_password)
        self.widget.animazioni.animazione_fade_out(self.widget.nuova_password)
        self.widget.animazioni.animazione_fade_out(self.widget.confema_password)
        self.widget.animazioni.animazione_fade_out(self.widget.vecchia_password_line_edit)
        self.widget.animazioni.animazione_fade_out(self.widget.nuova_password_line_edit)
        self.widget.animazioni.animazione_fade_out(self.widget.conferma_password_line_edit)
        self.widget.animazioni.animazione_fade_out(self.widget.scritta)
        self.widget.animazioni.animazione_fade_out(self.widget.conferma_button)

        self.widget.animazioni.animazione_fade_out_totale.start()
