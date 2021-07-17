from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox

from utente import view_home_utente

from personale_medico.login_personale_medico.model.model_lista_personale_medico import ListaPersonaleMedico
from personale_medico.view.view_home_personale_medico import ViewHomePersonaleMedico


class ControllerListaPersonaleMedico:
    def __init__(self, widget):
        """
        Costruttore della classe ControllerListaPersonaleMedico, il quale crea le variabili di istanza e connette i
        button alle rispettive funzioni

        :param widget: Corrisponde alla ViewLoginPersonaleMedico, nella quale viene creata un'istanza di questo
                        controller
        :type widget: QWidget
        """
        self.widget = widget
        self.model_lista_personale_medico = ListaPersonaleMedico()

        utente = view_home_utente.ViewHomeUtente()
        self.widget.torna_indietro.clicked.connect(lambda: self.go_home_utente(utente))
        self.widget.login_button.clicked.connect(self.go_home_personale_medico)
        self.widget.password.returnPressed.connect(self.go_home_personale_medico)

        # pulsante che consente di visualizzare/nascondere la password
        self.widget.occhiello_barrato_button.clicked.connect(self.widget.occhiello_barrato_button_pressed)
        self.widget.occhiello_button.clicked.connect(self.widget.occhiello_button_pressed)

    def go_home_utente(self, utente):
        """
        Funzione che consente di passare alla ViewHomeUtente dalla view attuale

        :param utente: Parametro che rappresenta un oggetto della classe ViewHomeUtente, il quale
                        viene utilizzato per mostrare la view relativa
        :type utente: ViewHomeUtente
        """
        utente.show()
        self.widget.hide()

    def go_home_personale_medico(self):
        """
        Funzione che consente di passare alla ViewHomePersonaleMedico dalla view attuale
        """
        popup = QMessageBox()
        icona = QIcon()
        icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
        popup.setWindowIcon(icona)
        personale_medico = \
            self.model_lista_personale_medico.controlla_credenziali(self.widget.codice_identificativo.text(),
                                                                    self.widget.password.text())

        if personale_medico is not None:
            popup.setWindowTitle('Accesso completato')
            popup.setIcon(QMessageBox.Information)
            popup.setText('Il login è stato effettuato con successo!')
            popup.exec_()

            home_personale_medico = ViewHomePersonaleMedico(personale_medico)
            home_personale_medico.show()
            self.widget.hide()
        else:
            popup.setWindowTitle('Accesso negato')
            popup.setIcon(QMessageBox.Critical)
            popup.setText('Le credenziali sono errate!')
            popup.exec_()
