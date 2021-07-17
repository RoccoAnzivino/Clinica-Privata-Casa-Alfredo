import datetime

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox

from paziente.login_paziente.view import view_login_paziente
from paziente.view import view_prenota_ora, view_home_paziente, view_prenotazioni_paziente, view_disdetta_prenotazione
from paziente.view import view_cartella_clinica_paziente
from paziente.view.view_dati_personali_paziente import ViewPaziente

from tools.pdf_generator import PrenotazionePDF


class ControllerPrenotazione:

    def __init__(self, widget):
        """
        Costruttore della classe ControllerPrenotazione, il quale crea le variabili di istanza e connette i button
        alle rispettive funzioni

        :param widget: Corrisponde alla ViewPrenotazione, nella quale viene creata un'istanza di questo controller
        :type widget: QWidget
        """
        self.widget = widget
        self.model_prenotazione = widget.prenotazione

        widget.nome_label.setText(widget.paziente.nome)
        widget.cognome_label.setText(widget.paziente.cognome)
        widget.ambulatorio_label.setText(self.model_prenotazione.ambulatorio)
        widget.attivita_ambulatoriale_label.setText(self.model_prenotazione.attivita_ambulatoriale)
        widget.medico_label.setText(self.model_prenotazione.cognome_personale_medico + ' ' +
                                    self.model_prenotazione.nome_personale_medico)
        widget.data_e_ora_label.setText(self.model_prenotazione.data_ora_visita.strftime("%d/%m/%Y, %H:%M"))
        widget.prezzo_label.setText(self.model_prenotazione.prezzo)
        widget.data_e_ora_prenotazione_label.setText(self.model_prenotazione.data_ora_prenotazione.
                                                     strftime("%d/%m/%Y, %H:%M:%S"))

        self.pdf_prenotazione = None

        # pulsanthe che, se premuto, permette di aprire la voce "il mio profilo" del menù a tendina
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

        widget.torna_indietro.clicked.connect(self.go_lista_prenotazioni)

        # DOWNLOAD PDF
        # pulsante che, se premuto, permette di scaricare il pdf relativo alla propria prenotazione
        widget.download_pdf.clicked.connect(self.go_scarica_prenotazione)

        widget.disdici.clicked.connect(self.go_disdici_prenotazione)

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
        dati_personali = ViewPaziente(self.widget.paziente)
        dati_personali.show()
        self.widget.hide()

    def go_cartella_clinica_paziente(self):
        """
        Funzione che consente di passare alla ViewCartellaClinica dalla view attuale
        """
        cartella_clinica_paziente = view_cartella_clinica_paziente.ViewCartellaClinica(self.widget.paziente)
        lista_prenotazioni_cartella_clinica = cartella_clinica_paziente.controller_cartella_clinica. \
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
        prenota_ora = view_prenota_ora.ViewPrenotaOra(self.widget.paziente)
        prenota_ora.show()
        self.widget.hide()

    def go_lista_prenotazioni(self):
        """
        Funzione che consente di passare alla ViewListaPrenotazioni dalla view attuale
        """
        vista_prenotazioni_paziente = view_prenotazioni_paziente.ViewListaPrenotazioni(self.widget.paziente)
        lista_prenotazioni = self.widget.lista_prenotazioni
        lista_prenotazioni_paziente = []

        for prenotazione in lista_prenotazioni:
            if self.widget.paziente.id_paziente == prenotazione.id_paziente:
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

    def go_home_paziente(self):
        """
        Funzione che consente di passare alla ViewHomePaziente dalla view attuale
        """
        home_paziente = view_home_paziente.ViewHomePaziente(self.widget.paziente)
        home_paziente.show()
        self.widget.hide()

    def go_scarica_prenotazione(self):
        """
        Funzione che consente di scaricare il pdf relativo alla prenotazione nella cartella scelta dall'utente
        """
        self.pdf_prenotazione = PrenotazionePDF(self.model_prenotazione.id_prenotazione,
                                                self.model_prenotazione.data_ora_prenotazione,
                                                self.model_prenotazione.nome_paziente,
                                                self.model_prenotazione.cognome_paziente,
                                                self.widget.paziente.sesso,
                                                self.widget.paziente.data_di_nascita,
                                                self.widget.paziente.provincia_di_nascita,
                                                self.widget.paziente.citta_di_nascita,
                                                self.model_prenotazione.ambulatorio,
                                                self.model_prenotazione.nome_personale_medico,
                                                self.model_prenotazione.cognome_personale_medico,
                                                self.model_prenotazione.sesso_personale_medico,
                                                self.model_prenotazione.data_ora_visita,
                                                self.model_prenotazione.attivita_ambulatoriale)
        self.pdf_prenotazione.set_font('times', 'B', 11)
        self.pdf_prenotazione.genera_pdf()

    def go_disdici_prenotazione(self):
        """
        Funzione che consente di passare alla ViewDisdettaPrenotazione dalla view attuale
        """
        vincolo = datetime.datetime.now() + datetime.timedelta(hours=24)

        if vincolo < self.model_prenotazione.data_ora_visita:
            view_disdetta_prenotazione.ViewDisdettaPrenotazione(self.widget, self.model_prenotazione)
        else:
            popup = QMessageBox()
            icona = QIcon()
            icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
            popup.setWindowIcon(icona)
            popup.setWindowTitle('Errore')
            popup.setIcon(QMessageBox.Critical)
            popup.setText("Non è possibile disdire la prenotazione a meno\ndi 24 ore dall'appuntamento con il medico!")
            popup.exec_()
