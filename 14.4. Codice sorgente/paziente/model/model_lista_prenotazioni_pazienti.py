import datetime
import json
import os.path
import pickle

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox

from paziente.model.model_prenotazione import Prenotazione


class ListaPrenotazioniPazienti:

    def __init__(self):
        """
        Costruttore della classe ListaPrenotazioniPazienti, nella quale vengono istanziate delle variabili e
        richiamate le funzioni successivamente dichiarate e definite all'interno della stessa classe
        """
        self.lista_prenotazioni = []

        self.recupera_prenotazioni()
        self.elimina_prenotazioni_passate()

    def recupera_prenotazioni(self):
        """
        Funzione che legge da file 'prenotazioni.pickle', salvando le prenotazioni effettuate in una lista
        """
        if os.path.isfile('paziente/data/prenotazioni.pickle'):
            with open('paziente/data/prenotazioni.pickle', 'rb') as prenotazioni_effetuate:
                self.lista_prenotazioni = pickle.load(prenotazioni_effetuate)

    @staticmethod
    def aggiorna_database_medici(prenotazione):
        """
        Funzione che legge dal database del personale medico d'interesse tramite l'id di quest'ultimo, inserisce i dati
        in una lista, aggiunge la prenotazione alla lista, per poi scrivere sul database le informazioni aggiornate

        :param prenotazione: Parametro che rappresenta un oggetto della classe Prenotazione
        :type prenotazione: Prenotazione
        """
        id_personale_medico = prenotazione.id_personale_medico

        lista_prenotazioni_da_aggiornare = []

        if os.path.isfile(f'personale_medico/data/{id_personale_medico}.pickle'):
            with open(f'personale_medico/data/{id_personale_medico}.pickle', 'rb') as prenotazioni_personale_medico:
                lista_prenotazioni_da_aggiornare = pickle.load(prenotazioni_personale_medico)

        lista_prenotazioni_da_aggiornare.append(prenotazione)

        with open(f'personale_medico/data/{id_personale_medico}.pickle', 'wb') as prenotazioni_personale_medico:
            pickle.dump(lista_prenotazioni_da_aggiornare, prenotazioni_personale_medico)

    def elimina_prenotazioni_passate(self):
        """
        Funzione che pulisce la lista_prenotazioni, per poi popolarla nuovamente con le prenotazioni le cui date sono
        posteriori alla data attuale, aggiornando, infine, i database tramite le apposite funzioni
        """
        oggi = datetime.datetime.now()
        # oggi = datetime.datetime(2021, 6, 27)
        lista_prenotazioni = [x for x in self.lista_prenotazioni]
        self.lista_prenotazioni.clear()

        for prenotazione in lista_prenotazioni:
            if prenotazione.data_ora_visita > oggi:
                self.lista_prenotazioni.append(prenotazione)
            else:
                print('Eliminata la prenotazione del:', prenotazione.data_ora_visita.strftime("%d/%m/%Y"))
                print('Medico:', prenotazione.id_personale_medico, prenotazione.nome_personale_medico,
                      prenotazione.cognome_personale_medico)
                self.aggiorna_database_medici(prenotazione)

        self.salva_prenotazioni()

    @staticmethod
    def aggiorna_storico_prenotazioni(prenotazione):
        """
        Funzione che legge da file 'storico_prenotazioni.json' e inserisce i dati in una lista, per poi aggiornare la
        lista tramite l'inserimento dei dati relativi alla prenotazione passata e reinserire il tutto sul file
        'storico_prenotazioni.json' in scrittura, di fatto aggiornando il file

        :param prenotazione: Parametro che rappresenta un oggetto della classe Prenotazione
        :type prenotazione: Prenotazione
        """
        with open('paziente/data/storico_prenotazioni.json', 'r') as storico_prenotazioni:
            lista_storico_prenotazioni = json.load(storico_prenotazioni)
        with open('paziente/data/storico_prenotazioni.json', 'w') as storico_prenotazioni:

            storico = dict()
            storico['id_prenotazione'] = prenotazione.id_prenotazione
            storico['id_paziente'] = prenotazione.id_paziente
            storico['nome_paziente'] = prenotazione.nome_paziente
            storico['cognome_paziente'] = prenotazione.cognome_paziente
            storico['ambulatorio'] = prenotazione.ambulatorio
            storico['attivita_ambulatoriale'] = prenotazione.attivita_ambulatoriale
            storico['id_personale_medico'] = prenotazione.id_personale_medico
            storico['nome_personale_medico'] = prenotazione.nome_personale_medico
            storico['cognome_personale_medico'] = prenotazione.cognome_personale_medico
            storico['sesso_personale_medico'] = prenotazione.sesso_personale_medico
            storico['data_ora_prenotazione'] = prenotazione.data_ora_prenotazione.strftime("%d/%m/%Y, %H:%M:%S")
            storico['data_ora_visita'] = prenotazione.data_ora_visita.strftime("%d/%m/%Y, %H:%M")
            storico['prezzo'] = prenotazione.prezzo
            storico['durata'] = prenotazione.durata

            lista_storico_prenotazioni.append(storico)
            json.dump(lista_storico_prenotazioni, storico_prenotazioni)

    def aggiungi_prenotazione(self, id_paziente, nome_paziente, cognome_paziente, ambulatorio, attivita_ambulatoriale,
                              id_personale_medico, nome_personale_medico, cognome_personale_medico,
                              sesso_personale_medico, data_ora_prenotazione, data_ora_visita, prezzo, durata):
        """
        Funzione che crea una prenotazione come oggetto della classe Prenotazione, per poi
        controllare se vi sono duplicati e aggiornare i database tramite le apposite funzioni

        :param id_paziente: Parametro che rappresenta l'id del paziente relativo alla prenotazione
        :type id_paziente: str
        :param nome_paziente: Parametro che rappresenta il nome del paziente relativo alla prenotazione
        :type nome_paziente: str
        :param cognome_paziente: Parametro che rappresenta il cognome del paziente relativo alla prenotazione
        :type cognome_paziente: str
        :param ambulatorio: Parametro che rappresenta l'ambulatorio relativo alla prenotazione
        :type ambulatorio: str
        :param attivita_ambulatoriale: Parametro che rappresenta l'attività ambulatoriale relativa alla prenotazione
        :type attivita_ambulatoriale: str
        :param id_personale_medico: Parametro che rappresenta l'id del personale medico relativo alla prenotazione
        :type id_personale_medico: str
        :param nome_personale_medico: Parametro che rappresenta il nome del personale medico relativo alla prenotazione
        :type nome_personale_medico: str
        :param cognome_personale_medico: Parametro che rappresenta il cognome del personale medico relativo alla
                                         prenotazione
        :type cognome_personale_medico: str
        :param sesso_personale_medico: Parametro che rappresenta il sesso del personale medico relativo alla
                                       prenotazione
        :type sesso_personale_medico: str
        :param data_ora_prenotazione: Parametro che rappresenta la data e l'ora al momento dell'effetuazione della
                                      prenotazione
        :type data_ora_prenotazione: datetime.datetime
        :param data_ora_visita: Parametro che rappresenta la data e l'ora della visita relative alla prenotazione
        :type data_ora_visita: datetime.datetime
        :param prezzo: Parametro che rappresenta il prezzo della visita relativo alla prenotazione
        :type prezzo: str
        :param durata: Parametro che rappresenta la durata della visita relativa alla prenotazione
        :type durata: int
        :return: La funzione ritorna False se il controllo dei duplicati fallisce, altrimenti ritorna True dopo aver
                  aggiornato i database con l'aggiunta della nuova prenotazione
        :rtype: bool
        """
        if not self.lista_prenotazioni:
            id_prenotazione = 'pren0000'
        else:
            id_prenotazione = self.lista_prenotazioni[-1].id_prenotazione
        prenotazione = Prenotazione(id_prenotazione, id_paziente, nome_paziente, cognome_paziente, ambulatorio,
                                    attivita_ambulatoriale, id_personale_medico, nome_personale_medico,
                                    cognome_personale_medico, sesso_personale_medico, data_ora_prenotazione,
                                    data_ora_visita, prezzo, durata, "")

        if self.controllo_duplicati(prenotazione):
            return False
        else:
            self.lista_prenotazioni.append(prenotazione)
            self.salva_prenotazioni()
            self.aggiorna_storico_prenotazioni(prenotazione)
            return True

    def salva_prenotazioni(self):
        """
        Funzione che scrive su file 'prenotazioni.pickle' la lista_prenotazioni, salvando, di fatto, le prenotazioni
        effettuate nel database
        """
        with open('paziente/data/prenotazioni.pickle', 'wb') as prenotazioni_effettuate:
            pickle.dump(self.lista_prenotazioni, prenotazioni_effettuate, pickle.HIGHEST_PROTOCOL)

    def controllo_duplicati(self, prenotazione):
        """
        Funzione che confronta la prenotazione passata come parametro d'ingresso alla stessa funzione con l'insieme di
        tutte prenotazioni all'interno di lista_prenotazioni, al fine di trovare eventuali duplicati

        :param prenotazione: Parametro che rappresenta un oggetto della classe Prenotazione
        :type prenotazione: Prenotazione
        :return: La funzione ritorna True nel momento in cui viene trovata una prenotazione in lista_prenotazioni che
                  coincide per attività ambulatoriale o per data e ora della visita con la prenotazione passata in
                  ingresso, altrimenti ritorna False se non viene trovato nessun duplicato
        :rtype: bool
        """
        popup = QMessageBox()
        icona = QIcon()
        icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
        popup.setWindowIcon(icona)

        for prenotazione_lista in self.lista_prenotazioni:
            # controllo id paziente
            if prenotazione_lista.id_paziente == prenotazione.id_paziente:
                # controllo attività ambulatoriale
                if prenotazione_lista.attivita_ambulatoriale == prenotazione.attivita_ambulatoriale:
                    popup.setWindowTitle('Attenzione')
                    popup.setIcon(QMessageBox.Warning)
                    popup.setText("La informiamo che è stata già effettuata una prenotazione relativa alla seguente "
                                  f"attività ambulatoriale: {prenotazione_lista.attivita_ambulatoriale}")
                    popup.exec_()
                    return True
                # controllo data visita
                if prenotazione_lista.data_ora_visita.strftime("%d/%m/%Y") == prenotazione.data_ora_visita.\
                        strftime("%d/%m/%Y"):
                    popup.setWindowTitle('Attenzione')
                    popup.setIcon(QMessageBox.Warning)
                    popup.setText("La informiamo che è stata già effettuata una prenotazione in "
                                  f"data {prenotazione_lista.data_ora_visita.strftime('%d/%m/%Y')}.\n Selezionare"
                                  f" un'altra data!")
                    popup.exec_()
                    return True
        return False

    def disdici_prenotazione(self, prenotazione):
        """
        Funzione che rimuove la prenotazione designata dalla lista di tutte le prenotazioni, per poi apportare la
        modifica al database

        :param prenotazione: Parametro che rappresenta un oggetto della classe Prenotazione
        :type prenotazione: Prenotazione
        """
        for pren in self.lista_prenotazioni:
            if pren.id_prenotazione == prenotazione.id_prenotazione:
                self.lista_prenotazioni.remove(pren)
                break

        self.salva_prenotazioni()
