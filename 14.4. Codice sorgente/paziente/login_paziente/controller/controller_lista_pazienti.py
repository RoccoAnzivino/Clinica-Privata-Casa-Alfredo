import datetime

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon, QPixmap

from utente import view_home_utente

from paziente.login_paziente.view import view_login_paziente, view_registrazione_paziente
from paziente.view.view_home_paziente import ViewHomePaziente
from paziente.login_paziente.model.model_lista_pazienti import ListaPazienti

from tools.codice_fiscale import CodiceFiscale


class ControllerListaPazienti:

    def __init__(self, widget):
        """
        Costruttore della classe ControllerListaPazienti, il quale crea le variabili di istanza e connette i button
        alle rispettive funzioni a seconda dell'istanza alla quale questi appartengono

        :param widget: Corrisponde alla ViewLoginPaziente o alla ViewRegistrazionePaziente, nelle quali viene
                        creata un'istanza di questo controller
        :type widget: QWidget
        """
        self.widget = widget
        self.model_lista_pazienti = ListaPazienti()

        if isinstance(widget, view_login_paziente.ViewLoginPaziente):
            utente = view_home_utente.ViewHomeUtente()
            self.widget.torna_indietro.clicked.connect(lambda: self.go_home_utente(utente))
            self.widget.registrati.clicked.connect(self.go_registrazione_paziente)
            self.widget.login_button.clicked.connect(self.go_home_paziente)
            self.widget.password.returnPressed.connect(self.go_home_paziente)
        else:
            self.widget.provincia_combo_box.activated.connect(lambda:
                                                              widget.lista_comuni(
                                                                  widget.provincia_combo_box.currentText()))
            self.widget.torna_indietro.clicked.connect(self.go_login_paziente)
            self.widget.registrati_button.clicked.connect(self.registrazione_paziente)

        # pulsante che consente di visualizzare/nascondere la password
        self.widget.occhiello_barrato_button.clicked.connect(self.widget.occhiello_barrato_button_pressed)
        self.widget.occhiello_button.clicked.connect(self.widget.occhiello_button_pressed)

    def go_home_utente(self, utente):
        """
        Funzione che consente di passare alla ViewHomeUtente dalla view attuale

        :param utente: Parametro che rappresenta un oggetto della classe ViewHomeUtente, il quale viene utilizzato per
                        mostrare la view relativa
        :type utente: ViewHomeUtente
        """
        utente.show()
        self.widget.hide()

    def go_registrazione_paziente(self):
        """
        Funzione che consente di passare alla ViewRegistrazionePaziente dalla view attuale
        """
        registrazione = view_registrazione_paziente.ViewRegistrazionePaziente()
        registrazione.show()
        self.widget.hide()

    def go_login_paziente(self):
        """
        Funzione che consente di passare alla ViewLoginPaziente dalla view attuale
        """
        paziente = view_login_paziente.ViewLoginPaziente()
        paziente.show()
        self.widget.hide()

    def go_home_paziente(self):
        """
        Funzione che consente di passare alla ViewHomePaziente dalla view attuale
        """
        popup = QMessageBox()
        icona = QIcon()
        icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
        popup.setWindowIcon(icona)
        paziente = self.model_lista_pazienti.controlla_credenziali(self.widget.email.text(),
                                                                   self.widget.password.text())

        if paziente is not None:
            popup.setWindowTitle('Accesso completato')
            popup.setIcon(QMessageBox.Information)
            popup.setText('Il login è stato effettuato con successo!')
            popup.exec_()

            home_paziente = ViewHomePaziente(paziente)
            home_paziente.show()
            self.widget.hide()
        else:
            popup.setWindowTitle('Accesso negato')
            popup.setIcon(QMessageBox.Critical)
            popup.setText('Le credenziali sono errate!')
            popup.exec_()

    def registrazione_paziente(self):
        """
        Funzione che registra un paziente secondo le informazioni inserite e richieste, effettuando anche diversi
        controlli

        :return: La funzione ritorna None e, dunque, si interrompe nel momento in cui fallisce un controllo, in
                  particolare se viene lasciato un campo vuoto tra quelli richiesti, se il codice fiscale non
                  corrisponde a quello calcolato tramite l'apposita funzione di controllo, se l'email non è nel formato
                  corretto, se è già presente un paziente registrato con la stessa email inserita o, infine, se la
                  password non rispetta i parametri di sicurezza
        :rtype: None
        """
        popup = QMessageBox()
        icona = QIcon()
        icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
        popup.setWindowIcon(icona)

        data_di_nascita = datetime.date(self.widget.data_di_nascita_date_edit.date().toPyDate().year,
                                        self.widget.data_di_nascita_date_edit.date().toPyDate().month,
                                        self.widget.data_di_nascita_date_edit.date().toPyDate().day)

        if (not self.widget.nome_line_edit.text() or not self.widget.cognome_line_edit.text()
                or self.widget.provincia_combo_box.currentText() == 'Seleziona una provincia'
                or not self.widget.codice_fiscale_line_edit.text() or not self.widget.email_line_edit.text()
                or not self.widget.password_line_edit.text()):

            popup.setWindowTitle('Attenzione')
            popup.setIcon(QMessageBox.Warning)
            popup.setText('Riempire accuratamente tutti i campi!')
            popup.exec_()
            return

        codice_fiscale = CodiceFiscale(self.widget.nome_line_edit.text(), self.widget.cognome_line_edit.text(),
                                       data_di_nascita, self.widget.sesso_combo_box.currentText(),
                                       self.widget.citta_di_nascita_combo_box.currentText())

        if not codice_fiscale.controllo_codice_fiscale(self.widget.codice_fiscale_line_edit.text().upper()):
            popup.setWindowTitle('Attenzione')
            popup.setIcon(QMessageBox.Warning)
            popup.setText('Il codice fiscale non corrisponde ai dati immessi!')
            popup.exec_()
            return

        if not self.model_lista_pazienti.controllo_email(self.widget.email_line_edit.text()):
            popup.setWindowTitle('Attenzione')
            popup.setIcon(QMessageBox.Warning)
            popup.setText("L'email digitata non rispetta il formato standard!\nEs.: nomeutente@dominio.it")
            popup.exec_()
            return

        if self.model_lista_pazienti.controllo_email_gia_registrata(self.widget.email_line_edit.text()):
            popup.setWindowTitle('Errore')
            popup.setIcon(QMessageBox.Critical)
            popup.setText('La mail scelta è già associata ad un altro utente!\nInserire una nuova mail.')
            popup.exec_()
            return

        if self.model_lista_pazienti.controllo_sicurezza_password(self.widget.password_line_edit.text()) is False:
            popup.setWindowTitle('Attenzione')
            popup.setIcon(QMessageBox.Warning)
            popup.setText('La password non è sicura! Seguire le indicazioni.')
            popup.exec_()
            return

        nome = self.widget.nome_line_edit.text()[0:1].upper() + self.widget.nome_line_edit.text()[1:].lower()
        cognome = self.widget.cognome_line_edit.text()[0:1].upper() + self.widget.cognome_line_edit.text()[1:].lower()

        self.model_lista_pazienti.registrazione_paziente(nome, cognome, data_di_nascita,
                                                         self.model_lista_pazienti.calcolo_eta(data_di_nascita),
                                                         self.widget.sesso_combo_box.currentText(),
                                                         self.widget.provincia_combo_box.currentText(),
                                                         self.widget.citta_di_nascita_combo_box.currentText(),
                                                         self.widget.codice_fiscale_line_edit.text(),
                                                         self.widget.email_line_edit.text().lower(),
                                                         self.widget.password_line_edit.text())

        popup.setWindowTitle('Registrazione effettuata')
        popup.setIcon(QMessageBox.Information)
        popup.setText('La registrazione è andata a buon fine!')
        popup.exec_()

        self.go_login_paziente()
