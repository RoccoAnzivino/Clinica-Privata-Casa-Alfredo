import datetime
import json

from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox

from paziente.login_paziente.view import view_login_paziente
from paziente.model.model_lista_prenotazioni_pazienti import ListaPrenotazioniPazienti
from paziente.view import view_cartella_clinica_paziente, view_disdetta_prenotazione
from paziente.view.view_dati_personali_paziente import ViewPaziente
from paziente.view import view_prenota_ora
from paziente.view import view_home_paziente
from paziente.view import view_prenotazioni_paziente

from tools.tool_pulsante_prenotazioni import PulsantePrenotazioni


class ControllerListaPrenotazioniPazienti:

    def __init__(self, widget):
        """
        Costruttore della classe ControllerListaPrenotazioniPazienti, il quale crea le variabili di istanza e connette
        i button alle rispettive funzioni a seconda dell'istanza alla quale questi appartengono

        :param widget: Corrisponde alla ViewDisdettaPrenotazione o alla ViewPrenotaOra o alla
                        ViewListaPrenotazioni, nelle quali viene creata un'istanza di questo controller
        :type widget: QWidget
        """
        self.widget = widget
        self.model_lista_prenotazioni = ListaPrenotazioniPazienti()

        self.lista_ambulatori_prenotazioni = {}
        self.medicina_generale_cardiologica = {}
        self.endocrinologia = {}
        self.urologia_andrologia = {}
        self.oculistica = {}
        self.ortopedia = {}
        self.dermatologia = {}

        self.get_ambulatori_e_specializzazioni()

        self.lista_prenotazioni_paziente = []

        if isinstance(self.widget, view_prenota_ora.ViewPrenotaOra):
            # VISUALIZZA SECONDA SLIDE PRENOTAZIONI
            # pulsante che, se premuto, permette di andare alla seconda slide della generazione nuova prenotazione
            self.widget.medicina_generale_cardiologica.clicked.connect(lambda: self.visualizza_seconda_slide(
                self.widget.medicina_generale_cardiologica, self.medicina_generale_cardiologica))

            # pulsante che, se premuto, permette di andare alla seconda slide della generazione nuova prenotazione
            self.widget.endocrinologia.clicked.connect(lambda: self.visualizza_seconda_slide(
                self.widget.endocrinologia, self.endocrinologia))

            # pulsante che, se premuto, permette di andare alla seconda slide della generazione nuova prenotazione
            self.widget.urologia_andrologia.clicked.connect(lambda: self.visualizza_seconda_slide(
                self.widget.urologia_andrologia, self.urologia_andrologia))

            # pulsante che, se premuto, permette di andare alla seconda slide della generazione nuova prenotazione
            self.widget.oculistica.clicked.connect(lambda: self.visualizza_seconda_slide(
                self.widget.oculistica, self.oculistica))

            # pulsante che, se premuto, permette di andare alla seconda slide della generazione nuova prenotazione
            self.widget.ortopedia.clicked.connect(lambda: self.visualizza_seconda_slide(
                self.widget.ortopedia, self.ortopedia))

            # pulsante che, se premuto, permette di andare alla seconda slide della generazione nuova prenotazione
            self.widget.dermatologia.clicked.connect(lambda: self.visualizza_seconda_slide(
                self.widget.dermatologia, self.dermatologia))

            # pulsante che, se premuto, visualizza la data selezionata e visualizza la combobox che permette
            # la scelta dell'ora
            self.widget.calendarWidget.clicked.connect(lambda: self.visualizza_quarta_slide(
                self.widget.calendarWidget.selectedDate().toString("dd'/'MM'/'yyyy")))

            # quando si sceglie un'ora nella relativa combobox, appare il riepilogo della prenotazione
            # e la possibilità di poterla effettuare
            self.widget.ora_combo_box.activated.connect(self.visualizza_quinta_slide)

            self.widget.prenota_ora_button.clicked.connect(self.effettua_prenotazione)

        elif isinstance(self.widget, view_disdetta_prenotazione.ViewDisdettaPrenotazione):
            self.widget.popup.buttonClicked.connect(self.disdici_prenotazione_paziente)

        else:
            self.get_prenotazioni_specifiche()

        if not isinstance(self.widget, view_disdetta_prenotazione.ViewDisdettaPrenotazione):
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
        lista_prenotazioni = self.model_lista_prenotazioni.lista_prenotazioni
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

    def get_ambulatori_e_specializzazioni(self):
        """
        Funzione che legge da file 'ambulatori_specializzazioni.json, salvando i dati in una lista, per poi asegnare gli
        ambulatori alle rispettive variabili d'istanza
        """
        with open('database/ambulatori_specializzazioni.json', 'rb') as ambulatori_prenotazioni:
            self.lista_ambulatori_prenotazioni = json.load(ambulatori_prenotazioni)

            for ambulatorio in self.lista_ambulatori_prenotazioni:
                if ambulatorio.get('ambulatorio') == "Medicina generale cardiologica":
                    self.medicina_generale_cardiologica = ambulatorio
                elif ambulatorio.get('ambulatorio') == "Endocrinologia":
                    self.endocrinologia = ambulatorio
                elif ambulatorio.get('ambulatorio') == "Urologia/Andrologia":
                    self.urologia_andrologia = ambulatorio
                elif ambulatorio.get('ambulatorio') == "Oculistica":
                    self.oculistica = ambulatorio
                elif ambulatorio.get('ambulatorio') == "Ortopedia":
                    self.ortopedia = ambulatorio
                elif ambulatorio.get('ambulatorio') == "Dermatologia":
                    self.dermatologia = ambulatorio

    def visualizza_seconda_slide(self, bottone, ambulatorio):
        """
        Funzione che gestisce la comparsa della seconda slide all'interno della ViewPrenotaOra, la quale sarà
        differente a seconda dell'ambulatorio selezionato all'interno della prima slide

        :param bottone: Parametro che rappresenta il button con l'ambulatorio selezionato nella prima slide
        :type bottone: QPushButton
        :param ambulatorio: Parametro che rappresenta l'ambulatorio associato a bottone
        :type ambulatorio: dict
        """
        self.widget.freccia_1.setVisible(True)
        self.widget.freccia_2.setVisible(False)
        self.widget.attivita_ambulatoriale_label.setVisible(True)
        self.widget.selezionato_ambulatorio.setVisible(True)
        self.widget.selezionato_attivita_ambulatoriale.setVisible(False)
        self.widget.calendarWidget.setVisible(False)
        oggi = datetime.date.today()
        date = QDate(oggi.year, oggi.month, oggi.day - 1)
        self.widget.calendarWidget.setSelectedDate(date)
        self.widget.lunedi.setVisible(False)
        self.widget.martedi.setVisible(False)
        self.widget.mercoledi.setVisible(False)
        self.widget.giovedi.setVisible(False)
        self.widget.venerdi.setVisible(False)
        self.widget.sabato.setVisible(False)
        self.widget.domenica.setVisible(False)
        self.widget.data_e_ora_label.setVisible(False)
        self.widget.selezionato_data_e_ora.setVisible(False)
        self.widget.ora_combo_box.setVisible(False)
        self.widget.riepilogo_label.setVisible(False)
        self.widget.prenota_ora_button.setVisible(False)
        self.widget.attivita_ambulatoriale_label.setText("ATTIVITA\' AMBULATORIALE")
        self.widget.selezionato_ambulatorio.setText("Selezionato: \n" + bottone.text())

        for pulsante_prenotazione in self.widget.lista_pulsanti:
            pulsante_prenotazione.pulsante.hide()

        self.widget.lista_pulsanti.clear()

        if ambulatorio.get('ambulatorio') == "Medicina generale cardiologica":
            self.widget.attivita_ambulatoriale_label.setText("SPECIALIZZAZIONI")
            posizione = 250
            for specializzazione in ambulatorio['lista_specializzazioni']:
                self.widget.lista_pulsanti.append(
                    PulsantePrenotazioni(posizione, self.widget, specializzazione, ambulatorio['ambulatorio']))
                posizione += 60

        elif ambulatorio.get('ambulatorio') == "Endocrinologia":
            posizione = 250
            for attivita_ambulatoriale in ambulatorio['lista_attivita_ambulatoriali']:
                self.widget.lista_pulsanti.append(
                    PulsantePrenotazioni(posizione, self.widget, attivita_ambulatoriale, ambulatorio['ambulatorio']))
                posizione += 60

            self.widget.lista_pulsanti[0].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[0]))
            self.widget.lista_pulsanti[1].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[1]))

        elif ambulatorio.get('ambulatorio') == "Urologia/Andrologia":
            posizione = 250
            for attivita_ambulatoriale in ambulatorio['lista_attivita_ambulatoriali']:
                self.widget.lista_pulsanti.append(
                    PulsantePrenotazioni(posizione, self.widget, attivita_ambulatoriale, ambulatorio['ambulatorio']))
                posizione += 60

            self.widget.lista_pulsanti[0].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[0]))
            self.widget.lista_pulsanti[1].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[1]))
            self.widget.lista_pulsanti[2].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[2]))
            self.widget.lista_pulsanti[3].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[3]))
            self.widget.lista_pulsanti[4].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[4]))
            self.widget.lista_pulsanti[5].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[5]))

        elif ambulatorio.get('ambulatorio') == "Oculistica":
            posizione = 250
            for attivita_ambulatoriale in ambulatorio['lista_attivita_ambulatoriali']:
                self.widget.lista_pulsanti.append(
                    PulsantePrenotazioni(posizione, self.widget, attivita_ambulatoriale, ambulatorio['ambulatorio']))
                posizione += 60

            self.widget.lista_pulsanti[0].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[0]))
            self.widget.lista_pulsanti[1].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[1]))
            self.widget.lista_pulsanti[2].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[2]))
            self.widget.lista_pulsanti[3].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[3]))
            self.widget.lista_pulsanti[4].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[4]))
            self.widget.lista_pulsanti[5].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[5]))

        elif ambulatorio.get('ambulatorio') == "Ortopedia":
            posizione = 250
            for attivita_ambulatoriale in ambulatorio['lista_attivita_ambulatoriali']:
                self.widget.lista_pulsanti.append(
                    PulsantePrenotazioni(posizione, self.widget, attivita_ambulatoriale, ambulatorio['ambulatorio']))
                posizione += 60

            self.widget.lista_pulsanti[0].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[0]))
            self.widget.lista_pulsanti[1].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[1]))
            self.widget.lista_pulsanti[2].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[2]))

        elif ambulatorio.get('ambulatorio') == "Dermatologia":
            posizione = 250
            for attivita_ambulatoriale in ambulatorio['lista_attivita_ambulatoriali']:
                self.widget.lista_pulsanti.append(
                    PulsantePrenotazioni(posizione, self.widget, attivita_ambulatoriale, ambulatorio['ambulatorio']))
                posizione += 60

            self.widget.lista_pulsanti[0].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[0]))
            self.widget.lista_pulsanti[1].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[1]))
            self.widget.lista_pulsanti[2].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[2]))
            self.widget.lista_pulsanti[3].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[3]))
            self.widget.lista_pulsanti[4].pulsante.clicked.connect(
                lambda: self.visualizza_terza_slide(self.widget.lista_pulsanti[4]))

    def visualizza_terza_slide(self, pulsante_attivita_ambulatoriale):
        """
        Funzione che gestisce la comparsa della terza slide all'interno della ViewPrenotaOra, la quale sarà
        differente a seconda dell'attività ambulatoriale selezionata all'interno della seconda slide

        :param pulsante_attivita_ambulatoriale: Parametro che rappresenta il button con l'attività ambulatoriale
                                                 selezionata nella seconda slide
        :type pulsante_attivita_ambulatoriale: PulsantePrenotazioni
        """
        self.widget.prezzo = pulsante_attivita_ambulatoriale.dizionario['prezzo']
        self.widget.durata = pulsante_attivita_ambulatoriale.dizionario['durata']

        self.widget.freccia_2.setVisible(True)
        self.widget.data_e_ora_label.setVisible(True)
        self.widget.selezionato_attivita_ambulatoriale.setVisible(True)
        self.widget.selezionato_attivita_ambulatoriale.setText(
            f'Selezionato:'
            f'\n{pulsante_attivita_ambulatoriale.pulsante.text()}'
            f'\nPrezzo: {self.widget.prezzo}'
            f'\nDurata: {self.widget.durata} minuti')
        self.widget.calendarWidget.setVisible(True)
        oggi = datetime.date.today()
        date = QDate(oggi.year, oggi.month, oggi.day - 1)
        self.widget.calendarWidget.setSelectedDate(date)
        self.widget.selezionato_data_e_ora.setVisible(False)
        self.widget.ora_combo_box.setVisible(False)
        self.widget.riepilogo_label.setVisible(False)
        self.widget.prenota_ora_button.setVisible(False)

        ambulatorio = None

        for ambulatorio in self.lista_ambulatori_prenotazioni:
            if ambulatorio['ambulatorio'] == pulsante_attivita_ambulatoriale.ambulatorio:
                break

        if ambulatorio.get('giorni_apertura') is not None:
            giorni_apertura = ambulatorio['giorni_apertura']

            if 'lunedì' not in giorni_apertura:
                self.widget.lunedi.setVisible(True)
            if 'martedì' not in giorni_apertura:
                self.widget.martedi.setVisible(True)
            if 'mercoledì' not in giorni_apertura:
                self.widget.mercoledi.setVisible(True)
            if 'giovedì' not in giorni_apertura:
                self.widget.giovedi.setVisible(True)
            if 'venerdì' not in giorni_apertura:
                self.widget.venerdi.setVisible(True)
            if 'sabato' not in giorni_apertura:
                self.widget.sabato.setVisible(True)

        self.widget.domenica.setVisible(True)

        self.widget.orario_apertura_mattina = datetime.datetime(1, 1, 1, hour=ambulatorio['orario_apertura_mattina'])
        self.widget.orario_chiusura_mattina = datetime.datetime(1, 1, 1, hour=ambulatorio['orario_chiusura_mattina'])
        self.widget.orario_apertura_pomeriggio = datetime.datetime(1, 1, 1,
                                                                   hour=ambulatorio['orario_apertura_pomeriggio'])
        self.widget.orario_chiusura_pomeriggio = datetime.datetime(1, 1, 1,
                                                                   hour=ambulatorio['orario_chiusura_pomeriggio'])
        self.widget.lista_medici_disponibili = ambulatorio['medici_operanti']

    def calcolo_orari_ambulatorio(self):
        """
        Funzione che calcola gli orari disponibili per ogni ambulatorio e attività ambulatoriale selezionati
        """
        pausa = 15

        ora_da_aggiungere = self.widget.orario_apertura_mattina
        while ora_da_aggiungere < self.widget.orario_chiusura_mattina:
            self.widget.lista_orari_attivita_ambulatoriale.append(ora_da_aggiungere.strftime("%H:%M"))
            durata_piu_pausa = datetime.timedelta(minutes=self.widget.durata + pausa)
            ora_da_aggiungere += durata_piu_pausa

        ora_da_aggiungere = self.widget.orario_apertura_pomeriggio
        while ora_da_aggiungere < self.widget.orario_chiusura_pomeriggio:
            self.widget.lista_orari_attivita_ambulatoriale.append(ora_da_aggiungere.strftime("%H:%M"))
            durata_piu_pausa = datetime.timedelta(minutes=self.widget.durata + pausa)
            ora_da_aggiungere += durata_piu_pausa

    def popola_lista_orari_medici(self):
        """
        Funzione che popola una lista di orari in base alla disponibilità dei medici attinenti a ogni attività
        ambulatoriale
        """
        for orario in self.widget.lista_orari_attivita_ambulatoriale:
            temp = dict()
            temp['orario'] = orario
            lista_temp = []
            for medico in self.widget.lista_medici_disponibili:
                lista_temp.append(medico)
            temp['lista_medici_disponibili'] = lista_temp
            self.widget.lista_orari_medici.append(temp)

        print('Orari medici prima: ', self.widget.lista_orari_medici)

    def calcolo_orari_disponibili(self):
        """
        Funzione che calcola gli orari disponibili e selezionabili nella quarta slide, tenendo conto degli orari di
        apertura e chiusura dell'ambulatorio selezionato, degli orari dei medici dispobibili per lo stesso ambulatorio
        e delle prenotazioni già effettuate
        """
        lista_prenotazioni = self.widget.controller_prenotazioni.model_lista_prenotazioni.lista_prenotazioni

        self.popola_lista_orari_medici()

        pausa = 15

        print('Lista iniziale: ', self.widget.lista_orari_attivita_ambulatoriale)

        for prenotazione in lista_prenotazioni:
            if prenotazione.ambulatorio == self.widget.selezionato_ambulatorio.text().replace("Selezionato: \n", ""):
                if prenotazione.data_ora_visita.strftime('%d/%m/%Y') == self.widget.selezionato_data_e_ora.text(). \
                        replace("Selezionato: \n", ""):
                    for ora in self.widget.lista_orari_attivita_ambulatoriale:
                        ora_min_cb = int(ora[:2]) * 60 + int(ora[-2:])
                        ora_pren = prenotazione.data_ora_visita.strftime("%H:%M")
                        ora_min_pren = int(ora_pren[:2]) * 60 + int(ora_pren[-2:])
                        if ora_min_cb < ora_min_pren:
                            ora_min_cb_completa = ora_min_cb + self.widget.durata + pausa
                            if ora_min_cb_completa > ora_min_pren:
                                print('Rimossa prima: ', ora)
                                self.widget.lista_orari_da_sottrarre.append(ora)
                        elif ora_min_cb > ora_min_pren:
                            ora_min_pren_completa = ora_min_pren + prenotazione.durata + pausa
                            if ora_min_pren_completa > ora_min_cb:
                                print('Rimossa dopo: ', ora)
                                self.widget.lista_orari_da_sottrarre.append(ora)
                        else:
                            print('Rimossa uguale: ', ora)
                            self.widget.lista_orari_da_sottrarre.append(ora)

        for ora in self.widget.lista_orari_da_sottrarre:
            for orario in self.widget.lista_orari_medici:
                if orario['orario'] == ora:
                    print('\n', orario['lista_medici_disponibili'][0], orario['orario'], '\n')
                    orario['lista_medici_disponibili'].pop(0)
                    if not orario['lista_medici_disponibili']:
                        print('Rimossa definitivamente: ', ora)
                        self.widget.lista_orari_attivita_ambulatoriale.remove(ora)

        print('Lista finale: ', self.widget.lista_orari_attivita_ambulatoriale)
        print('Orari medici dopo: ', self.widget.lista_orari_medici)

    def visualizza_quarta_slide(self, data):
        """
        Funzione che gestisce la comparsa della quarta slide all'interno della ViewPrenotaOra, la quale conterrà una
        lista di orari differente a seconda della data selezionata all'interno della terza slide

        :param data: Parametro rappresentante la data, convertita in stringa, selezionata
        :type data: str
        """
        self.widget.selezionato_data_e_ora.setVisible(True)
        self.widget.selezionato_data_e_ora.setText("Selezionato: \n" + data)
        self.widget.ora_combo_box.clear()
        self.widget.ora_combo_box.addItem('Scegli ora:')
        self.widget.ora_combo_box.setCurrentIndex(0)
        self.widget.lista_orari_attivita_ambulatoriale.clear()
        self.widget.lista_orari_da_sottrarre.clear()
        self.widget.lista_orari_medici.clear()
        self.calcolo_orari_ambulatorio()
        self.calcolo_orari_disponibili()
        self.widget.ora_combo_box.addItems(self.widget.lista_orari_attivita_ambulatoriale)
        self.widget.ora_combo_box.setVisible(True)

    def visualizza_quinta_slide(self):
        """
        Funzione che gestisce la comparsa della quinta slide all'interno della ViewPrenotaOra, la quale sarà
        differente a seconda di tutte le selezioni effettuate all'interno delle precedenti slide
        """
        self.widget.riepilogo_label.setVisible(True)

        selezionato_attivita_ambulatoriale = \
            self.widget.selezionato_attivita_ambulatoriale.text().replace("Selezionato:\n", "")
        attivita_ambulatoriale = selezionato_attivita_ambulatoriale[:selezionato_attivita_ambulatoriale.index('\n')]
        prezzo_durata = \
            (selezionato_attivita_ambulatoriale.replace(attivita_ambulatoriale + '\n', '')).replace('\n', ', ')

        self.widget.riepilogo_label.setText("Riepilogo: \n\nAmbulatorio: " +
                                            self.widget.selezionato_ambulatorio.text().replace("Selezionato: \n", "") +
                                            '\nAttività ambulatoriale: ' + attivita_ambulatoriale +
                                            '\n' + prezzo_durata + '\nData: ' +
                                            self.widget.selezionato_data_e_ora.text().replace("Selezionato: \n", "") +
                                            ' ' + self.widget.ora_combo_box.currentText())

        self.widget.prenota_ora_button.setVisible(True)

    def effettua_prenotazione(self):
        """
        Funzione che inserisce la prenotazione richiesta trammite la ViewPrenotaOra all'interno di
        model_lista_prenotazioni, prenotazione caratterizzata da tutte le selezioni fatte nella view e dai dati del
        paziente che effettua la stessa prenotazione

        :return: La funzione ritorna None, interrompendo la prenotazione, nel momento in cui non viene specificato alcun
        orario della visita all'interno della prenotazione stessa
        :rtype: None
        """
        id_personale_medico = ''
        nome_personale_medico = ''
        cognome_personale_medico = ''
        sesso_personale_medico = ''

        popup = QMessageBox()
        icona = QIcon()
        icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
        popup.setWindowIcon(icona)

        att_ambulatoriale_widget = self.widget.selezionato_attivita_ambulatoriale.text().replace('Selezionato:\n', '')
        attivita_ambulatoriale = att_ambulatoriale_widget[:att_ambulatoriale_widget.index('\n')]

        if self.widget.ora_combo_box.currentText() == 'Scegli ora:':
            popup.setWindowTitle('Attenzione')
            popup.setIcon(QMessageBox.Warning)
            popup.setText("Selezionare l'orario della visita!")
            popup.exec_()
            return

        data_prenotazione = datetime.datetime(self.widget.calendarWidget.selectedDate().year(),
                                              self.widget.calendarWidget.selectedDate().month(),
                                              self.widget.calendarWidget.selectedDate().day(),
                                              int(self.widget.ora_combo_box.currentText()[:2]),
                                              int(self.widget.ora_combo_box.currentText()[-2:]))

        for orario in self.widget.lista_orari_medici:
            if orario['orario'] == self.widget.ora_combo_box.currentText():
                lista_medici_disponibili = orario['lista_medici_disponibili']
                id_personale_medico = lista_medici_disponibili[0]['id']
                nome_personale_medico = lista_medici_disponibili[0]['nome']
                cognome_personale_medico = lista_medici_disponibili[0]['cognome']
                sesso_personale_medico = lista_medici_disponibili[0]['sesso']

        if self.model_lista_prenotazioni.aggiungi_prenotazione(
                self.widget.paziente.id_paziente, self.widget.paziente.nome, self.widget.paziente.cognome,
                self.widget.selezionato_ambulatorio.text().replace("Selezionato: \n", ""), attivita_ambulatoriale,
                id_personale_medico, nome_personale_medico, cognome_personale_medico, sesso_personale_medico,
                datetime.datetime.now(), data_prenotazione, self.widget.prezzo, self.widget.durata):
            popup.setWindowTitle('Prenotazione effettuata')
            popup.setIcon(QMessageBox.Information)
            popup.setText('La informiamo che la prenotazione è andata a buon fine!')
            popup.exec_()

            self.go_home_paziente()

    def get_prenotazioni_specifiche(self):
        """
        Funzione che inserisce all'interno di una lista le prenotazioni relative al paziente specifico, analizzando
        tutte le prenotazioni presenti nella lista_prenotazioni del model_lista_prenotazioni e confrontandone gli
        id_paziente con l'id del paziente specifico
        """
        lista_prenotazioni = self.model_lista_prenotazioni.lista_prenotazioni

        for prenotazione in lista_prenotazioni:
            if self.widget.paziente.id_paziente == prenotazione.id_paziente:
                self.lista_prenotazioni_paziente.append(prenotazione)

    def disdici_prenotazione_paziente(self):
        """
        Funzione che rimuove la prenotazione selezionata dalla lista_prenotazioni nel model_lista_prenotazioni
        """
        if self.widget.popup.clickedButton() == self.widget.popup.button(QMessageBox.Yes):
            self.widget.popup.hide()

            popup = QMessageBox()
            icona = QIcon()
            icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
            popup.setWindowIcon(icona)
            popup.setWindowTitle('Informazione')
            popup.setIcon(QMessageBox.Information)
            popup.setText('La prenotazione è stata disdetta!')
            popup.exec_()

            self.model_lista_prenotazioni.disdici_prenotazione(self.widget.prenotazione)

            self.get_prenotazioni_specifiche()

            if self.lista_prenotazioni_paziente:
                vista_lista_prenotazioni_pazienti = \
                    view_prenotazioni_paziente.ViewListaPrenotazioni(self.widget.paziente)
                vista_lista_prenotazioni_pazienti.show()
            else:
                vista_home_paziente = view_home_paziente.ViewHomePaziente(self.widget.paziente)
                vista_home_paziente.show()

            self.widget.widget_prenotazione.hide()
