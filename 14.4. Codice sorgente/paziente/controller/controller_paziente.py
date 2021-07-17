from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox

from paziente.login_paziente.view import view_login_paziente
from paziente.view.view_cartella_clinica_paziente import ViewCartellaClinica
from paziente.view.view_dati_personali_paziente import ViewPaziente
from paziente.view.view_prenota_ora import ViewPrenotaOra
from paziente.view.view_prenotazioni_paziente import ViewListaPrenotazioni


class ControllerPaziente:

    def __init__(self, widget):
        """
        Costruttore della classe ControllerPaziente, il quale crea le variabili di istanza e connette i button
        alle rispettive funzioni a seconda dell'istanza alla quale questi appartengono

        :param widget: Corrisponde alla ViewPaziente o alla ViewHomePaziente, nelle quali viene
                        creata un'istanza di questo controller
        :type widget: QWidget
        """
        self.widget = widget
        self.model_paziente = widget.paziente

        if isinstance(widget, ViewPaziente):

            widget.occhiello_button.clicked.connect(widget.occhiello_button_pressed)

            widget.occhiello_barrato_button.clicked.connect(widget.occhiello_barrato_button_pressed)

            # pulsante che permette di aprire la schermata modifica password nella schermata dati paziente
            widget.modifica_password.clicked.connect(self.modifica_password_button_pressed)
            # pulsante che permette di chiudere la schermata modifica password nella schermata dati paziente
            widget.annulla_modifica_password.clicked.connect(self.annulla_modifica_password_button_pressed)

            # recupero dati paziente
            # conversione datetime in stringa setText accetta solo stringhe e non datetime
            date_time_to_str = self.model_paziente.data_di_nascita.strftime("%d/%m/%Y")
            # conversione int in stringa perchè setText accetta solo stringhe e non interi
            converted_eta = str(self.model_paziente.eta)

            widget.nome_label.setText(self.model_paziente.nome)
            widget.cognome_label.setText(self.model_paziente.cognome)
            widget.data_di_nascita_label.setText(date_time_to_str)
            widget.eta_label.setText(converted_eta)
            widget.sesso_label.setText(self.model_paziente.sesso)
            widget.provincia_label.setText(self.model_paziente.provincia_di_nascita)
            widget.citta_di_nascita_label.setText(self.model_paziente.citta_di_nascita)
            widget.codice_fiscale_label.setText(self.model_paziente.codice_fiscale)
            widget.email_label.setText(self.model_paziente.email)
            widget.password_line_edit.setText(self.model_paziente.password)

            widget.conferma_button.clicked.connect(self.go_modifica_password)

            widget.conferma_password_line_edit.returnPressed.connect(self.go_modifica_password)

        # pulsanthe alla pesca che, se premuto, permette di aprire la voce "il mio profilo" del menù a tendina
        # che contiene "i miei dati", "le mie prenotazioni" e "cartella clinica"
        widget.menu_a_tendina.profilo_button.clicked.connect(self.go_il_mio_profilo)

        # pulsante che, se premuto, permette di tornare al menù a tendina principale, ovvero quello contenente
        # le voci "il mio profilo" e "prenota ora"
        widget.menu_a_tendina.indietro_button.clicked.connect(self.go_indietro)

        # DATI PERSONALI PAZIENTE
        # pulsante che, se premuto, permette di aprire la schermata dati personali del paziente
        widget.menu_a_tendina.dati_button.clicked.connect(self.go_dati_personali_paziente)

        # CARTELLA CLINICA PAZIENTE
        # pulsante che, se premuto, permette di aprire la schermata cartella clinica del paziente
        widget.menu_a_tendina.cartella_clinica_button.clicked.connect(self.go_cartella_clinica_paziente)

        # LOGIN PAZIENTE
        # pulsante che, se premuto, permette di tornare alla schermata login paziente
        widget.menu_a_tendina.logout_button.clicked.connect(self.go_login_paziente)

        # LISTA PRENOTAZIONI PAZIENTE
        # pulsante che, se premuto, permette di andare alla schermata lista prenotazioni paziente
        widget.menu_a_tendina.prenotazioni_button.clicked.connect(self.go_lista_prenotazioni)

        # PRENOTA ORA PAZIENTE
        # pulsante che, se premuto, permette di andare alla schermata lista prenotazioni paziente
        widget.menu_a_tendina.prenota_button.clicked.connect(self.go_prenota_ora)

    def go_il_mio_profilo(self):
        """
        Funzione che consente di andare all'interno della sezione 'Il mio profilo' nel menù a tendina
        """
        self.widget.menu_a_tendina.profilo_button_pressed()

    def go_indietro(self):
        """
        Funzione che permette di tornare indietro dalla sezione 'Il mio profilo' del menù a tendina
        """
        self.widget.menu_a_tendina.indietro_button_pressed()

    def go_dati_personali_paziente(self):
        """
        Funzione che consente di passare alla ViewPaziente dalla view attuale
        """
        dati_personali = ViewPaziente(self.model_paziente)
        dati_personali.show()
        self.widget.hide()

    def go_cartella_clinica_paziente(self):
        """
        Funzione che consente di passare alla ViewCartellaClinica dalla view attuale
        """
        cartella_clinica_paziente = ViewCartellaClinica(self.model_paziente)
        lista_prenotazioni_cartella_clinica = cartella_clinica_paziente.controller_cartella_clinica.\
            model_cartella_clinica.lista_prenotazioni_cartella_clinica

        if not lista_prenotazioni_cartella_clinica:
            popup = QMessageBox()
            icona = QIcon()
            icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
            popup.setWindowIcon(icona)
            popup.setWindowTitle('Attenzione')
            popup.setIcon(QMessageBox.Warning)
            popup.setText('Non hai mai effettuato visite nei nostri ambulatori!')
            popup.exec_()
        else:
            cartella_clinica_paziente.show()
            cartella_clinica_paziente.controller_cartella_clinica.set_labels_text()
            self.widget.hide()

    def go_login_paziente(self):
        """
        Funzione che consente di passare alla ViewLoginPaziente dalla view attuale tramite 'Logout'
        """
        login_paziente = view_login_paziente.ViewLoginPaziente()
        login_paziente.show()
        self.widget.hide()

    def go_prenota_ora(self):
        """
        Funzione che consente di passare alla ViewPrenotaOra dalla view attuale
        """
        prenota_ora = ViewPrenotaOra(self.model_paziente)
        prenota_ora.show()
        self.widget.hide()

    def go_lista_prenotazioni(self):
        """
        Funzione che consente di passare alla ViewListaPrenotazioni dalla view attuale
        """
        vista_prenotazioni_paziente = ViewListaPrenotazioni(self.model_paziente)
        lista_prenotazioni = \
            vista_prenotazioni_paziente.controller_prenotazioni.model_lista_prenotazioni.lista_prenotazioni
        lista_prenotazioni_paziente = []

        for prenotazione in lista_prenotazioni:
            if self.model_paziente.id_paziente == prenotazione.id_paziente:
                lista_prenotazioni_paziente.append(prenotazione)

        if not lista_prenotazioni_paziente:
            popup = QMessageBox()
            icona = QIcon()
            icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
            popup.setWindowIcon(icona)
            popup.setWindowTitle('Attenzione')
            popup.setIcon(QMessageBox.Warning)
            popup.setText('Non hai effettuato nessuna prenotazione!')
            popup.exec_()
        else:
            vista_prenotazioni_paziente.show()
            self.widget.hide()

    def go_modifica_password(self):
        """
        Funzione che rimanda l'utente alla ViewLoginPaziente dopo che è stata modificata la password dalla ViewPaziente
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

            if self.model_paziente.set_password_paziente(self.widget.nuova_password_line_edit.text(),
                                                         self.widget.conferma_password_line_edit.text(),
                                                         self.widget.vecchia_password_line_edit.text()):
                self.go_login_paziente()

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

    # per Kevin. prima si chiamava modifica_password_button_pressed_reverse. cancella questo commento
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
