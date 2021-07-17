from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox

from paziente.login_paziente.view import view_login_paziente
from paziente.model import model_cartella_clinica
from paziente.view import view_prenota_ora, view_cartella_clinica_paziente
from paziente.view.view_dati_personali_paziente import ViewPaziente
from paziente.view.view_prenotazioni_paziente import ViewListaPrenotazioni

from personale_medico.login_personale_medico.view import view_login_personale_medico
from personale_medico.view import view_cartella_clinica_personale_medico, view_dati_personali_personale_medico
from personale_medico.view import view_lista_pazienti_visitati, view_prenotazioni_personale_medico


class ControllerCartellaClinica:

    def __init__(self, widget):
        """
        Costruttore della classe ControllerCartellaClinica, il quale crea le variabili di istanza e connette i button
        alle rispettive funzioni a seconda che questi siano istanze di ViewCartellaClinica o di
        ViewCartellaClinicaPersonaleMedico

        :param widget: Corrisponde alla ViewCartellaClinica o alla ViewCartellaClinicaPersonaleMedico,
                        nelle quali viene creata un'istanza di questo controller
        :type widget: QWidget
        """
        self.widget = widget
        self.model_cartella_clinica = model_cartella_clinica.ListaPrenotazioniCartellaClinica(self.widget.paziente)

        self.lista_operatori_medici = []

        if isinstance(self.widget, view_cartella_clinica_paziente.ViewCartellaClinica):
            # MENU A TENDINA

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

        elif isinstance(self.widget, view_cartella_clinica_personale_medico.ViewCartellaClinicaPersonaleMedico):
            widget.torna_indietro.clicked.connect(self.go_lista_prenotazioni_personale_medico)
            widget.menu_a_tendina.dati_button.clicked.connect(self.go_dati_personali_personale_medico)
            widget.menu_a_tendina.prenotazioni_button.clicked.connect(self.go_lista_prenotazioni_personale_medico)
            widget.menu_a_tendina.pazienti_button.clicked.connect(self.go_lista_pazienti_visitati)
            widget.menu_a_tendina.logout_button.clicked.connect(self.go_login_personale_medico)

    def set_labels_text(self):
        """
        Funzione che formatta il testo all'interno delle label della cartella clinica
        """
        self.widget.nome_label.setText("Nome: " + self.widget.paziente.nome)
        self.widget.cognome_label.setText("Cognome: " + self.widget.paziente.cognome)
        self.widget.data_di_nascita_label.setText("Data di nascita: " + self.widget.paziente.data_di_nascita.
                                                  strftime("%d/%m/%Y"))
        self.widget.eta_label.setText("Età: " + str(self.widget.paziente.eta))
        self.widget.sesso_label.setText("Sesso: " + self.widget.paziente.sesso)
        self.widget.provincia_label.setText("Provincia: " + self.widget.paziente.provincia_di_nascita)
        self.widget.citta_di_nascita_label.setText("Città di nascita: " + self.widget.paziente.citta_di_nascita)
        self.widget.codice_fiscale_label.setText("Codice fiscale: " + self.widget.paziente.codice_fiscale)
        self.widget.data_emissione.setText('Data emissione: ' + self.model_cartella_clinica.
                                           lista_prenotazioni_cartella_clinica[0].
                                           data_ora_visita.strftime("%d/%m/%Y"))
        self.set_text_operatori_medici_label()

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
        Funzione che consente di passare alla ViewPaziente dalla ViewCartellaClinica
        """
        dati_personali = ViewPaziente(self.widget.paziente)
        dati_personali.show()
        self.widget.hide()

    def go_cartella_clinica_paziente(self):
        """
        Funzione che consente di passare alla ViewCartellaClinica dalla ViewCartellaClinica
        """
        cartella_clinica_paziente = view_cartella_clinica_paziente.ViewCartellaClinica(self.widget.paziente)
        cartella_clinica_paziente.show()
        cartella_clinica_paziente.controller_cartella_clinica.set_labels_text()
        self.widget.hide()

    def go_login_paziente(self):
        """
        Funzione che consente di passare alla ViewLoginPaziente dalla ViewCartellaClinica tramite 'Logout'
        """
        login_paziente = view_login_paziente.ViewLoginPaziente()
        login_paziente.show()
        self.widget.hide()

    def go_prenota_ora(self):
        """
        Funzione che consente di passare alla ViewPrenotaOra dalla ViewCartellaClinica
        """
        prenota_ora = view_prenota_ora.ViewPrenotaOra(self.widget.paziente)
        prenota_ora.show()
        self.widget.hide()

    def go_lista_prenotazioni(self):
        """
        Funzione che consente di passare alla ViewListaPrenotazioni dalla ViewCartellaClinica
        """
        vista_prenotazioni_paziente = ViewListaPrenotazioni(self.widget.paziente)
        lista_prenotazioni =\
            vista_prenotazioni_paziente.controller_prenotazioni.model_lista_prenotazioni.lista_prenotazioni
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

    def go_dati_personali_personale_medico(self):
        """
        Funzione che consente di passare alla ViewPersonaleMedico dalla ViewCartellaClinicaPersonaleMedico
        """
        dati_personali = view_dati_personali_personale_medico.ViewPersonaleMedico(self.widget.personale_medico)
        dati_personali.show()
        self.widget.hide()

    def go_lista_prenotazioni_personale_medico(self):
        """
        Funzione che consente di passare alla ViewPrenotazioniPersonaleMedico dalla
        ViewCartellaClinicaPersonaleMedico
        """
        vista_lista_prenotazioni_personale_medico = view_prenotazioni_personale_medico.\
            ViewPrenotazioniPersonaleMedico(self.widget.personale_medico)
        vista_lista_prenotazioni_personale_medico.show()
        self.widget.hide()

    def go_lista_pazienti_visitati(self):
        """
        Funzione che consente di passare alla ViewListaPazientiVisitati dalla ViewCartellaClinicaPersonaleMedico
        """
        lista_pazienti_visitati = view_lista_pazienti_visitati.ViewListaPazientiVisitati(self.widget.personale_medico)
        lista_pazienti_visitati.show()
        self.widget.hide()

    def go_login_personale_medico(self):
        """
        Funzione che consente di passare alla ViewLoginPersonaleMedico dalla ViewCartellaClinicaPersonaleMedico
        tramite 'Logout'
        """
        login_personale_medico = view_login_personale_medico.ViewLoginPersonaleMedico()
        login_personale_medico.show()
        self.widget.hide()

    def popola_operatori_medici(self):
        """
        Funzione che inserisce e ordina all'interno di una lista gli operatori medici che hanno visitato il paziente,
        il tutto in base alle prenotazioni effettuate dallo stesso paziente
        """
        for prenotazione in self.model_cartella_clinica.lista_prenotazioni_cartella_clinica:
            medico = prenotazione.cognome_personale_medico + ' ' + prenotazione.nome_personale_medico
            if medico not in self.lista_operatori_medici:
                self.lista_operatori_medici.append(medico)

        self.lista_operatori_medici.sort()

    def set_text_operatori_medici_label(self):
        """
        Funzione che formatta il testo all'interno di operatori_medici_label nella cartella clinica
        """
        self.popola_operatori_medici()
        operatori_medici = ''
        for medico in self.lista_operatori_medici:
            if medico is self.lista_operatori_medici[-1]:
                operatori_medici += medico
            else:
                operatori_medici += medico + ', '
        self.widget.operatori_medici_label.setText(operatori_medici)
