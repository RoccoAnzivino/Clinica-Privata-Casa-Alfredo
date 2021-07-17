import datetime
import os.path
import pickle


class ListaPrenotazioniPersonaleMedico:

    def __init__(self, personale_medico):
        """
        Costruttore della classe ListaPrenotazioniPersonaleMedico, nella quale vengono istanziate delle variabili e
        richiamate le funzioni successivamente dichiarate e definite all'interno della stessa classe

        :param personale_medico: Variabile d'istanza che rappresenta un oggetto della classe PersonaleMedico
        :type personale_medico: PersonaleMedico
        """
        self.personale_medico = personale_medico
        self.lista_prenotazioni_personale_medico = []

        self.recupera_prenotazioni_personale_medico()

    def recupera_prenotazioni_personale_medico(self):
        """
        Funzione che, se esiste, legge da file 'prenotazioni.pickle' e inserisce in una lista le prenotazioni, per poi
        eliminare le prenotazioni passate e inserire le prenotazioni relative al personale medico designato in una
        lista apposita, tramite un controllo sull'id_personale medico della prenotazione, che deve coincidere con quello
        del personale medico
        """
        lista_prenotazioni = []

        if os.path.isfile('paziente/data/prenotazioni.pickle'):
            with open('paziente/data/prenotazioni.pickle', 'rb') as prenotazioni:
                lista_prenotazioni = pickle.load(prenotazioni)

        lista_prenotazioni = self.elimina_prenotazioni_passate(lista_prenotazioni)

        for prenotazione in lista_prenotazioni:
            if prenotazione.id_personale_medico == self.personale_medico.id_personale_medico:
                self.lista_prenotazioni_personale_medico.append(prenotazione)

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

    def elimina_prenotazioni_passate(self, lista_prenotazioni):
        """
        Funzione che pulisce la lista_prenotazioni, per poi popolarla nuovamente con le prenotazioni le cui date sono
        posteriori alla data attuale, aggiornando, infine, i database tramite le apposite funzioni

        :param lista_prenotazioni: Parametro che rappresenta la lista di tutte le prenotazioni effettuate
        :type lista_prenotazioni: list
        :return: La funzione ritorna una lista contenente solo le prenotazioni posteriori alla data attuale
        :rtype: list
        """
        oggi = datetime.datetime.now()
        # oggi = datetime.datetime(2021, 6, 29)
        lista_prenotazioni_presenti = []

        for prenotazione in lista_prenotazioni:
            if prenotazione.data_ora_visita > oggi:
                lista_prenotazioni_presenti.append(prenotazione)
            else:
                print('Eliminata la prenotazione del:', prenotazione.data_ora_visita.strftime("%d/%m/%Y"))
                print('Medico:', prenotazione.id_personale_medico, prenotazione.nome_personale_medico,
                      prenotazione.cognome_personale_medico)
                self.aggiorna_database_medici(prenotazione)

        self.salva_prenotazioni(lista_prenotazioni_presenti)

        return lista_prenotazioni_presenti

    @staticmethod
    def salva_prenotazioni(lista_prenotazioni_presenti):
        """
        Funzione che scrive su file 'prenotazioni.pickle' la lista_prenotazioni, salvando, di fatto, le prenotazioni
        effettuate nel database

        :param lista_prenotazioni_presenti: Parametro che rappresenta la lista delle prenotazioni presenti su cui
                                             salvare le prenotazioni
        :type lista_prenotazioni_presenti: list
        """
        with open('paziente/data/prenotazioni.pickle', 'wb') as prenotazioni_effettuate:
            pickle.dump(lista_prenotazioni_presenti, prenotazioni_effettuate, pickle.HIGHEST_PROTOCOL)
