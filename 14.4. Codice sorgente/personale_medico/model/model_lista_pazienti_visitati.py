import datetime
import os.path
import pickle


class ListaPazientiVisitati:
    def __init__(self, personale_medico):
        """
        Costruttore della classe ListaPazientiVisitati, nella quale vengono istanziate delle variabili e
        richiamate le funzioni successivamente dichiarate e definite all'interno della stessa classe

        :param personale_medico: Variabile d'istanza che rappresenta un oggetto della classe PersonaleMedico
        :type personale_medico: PersonaleMedico
        """
        self.personale_medico = personale_medico
        self.lista_pazienti_da_modificare = []
        self.lista_pazienti_modificati = []
        self.lista_pazienti_modificati_personale_medico = []

        self.elimina_prenotazioni_passate()

        self.recupera_pazienti_da_modificare()
        self.recupera_pazienti_modificati()
        self.recupera_pazienti_modificati_personale_medico()

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

        lista_prenotazioni = []

        if os.path.isfile('paziente/data/prenotazioni.pickle'):
            with open('paziente/data/prenotazioni.pickle', 'rb') as prenotazioni:
                lista_prenotazioni = pickle.load(prenotazioni)

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

    def recupera_pazienti_da_modificare(self):
        """
        Funzione che, se esiste, legge dal database del personale medico, salvando in una lista tutti i pazienti per i
        quali dev'essere modificata la descizione della patologia riscontrata
        """
        if os.path.isfile(f'personale_medico/data/{self.personale_medico.id_personale_medico}.pickle'):
            with open(f'personale_medico/data/{self.personale_medico.id_personale_medico}.pickle', "rb")\
                    as lista_pazienti_da_modificare:
                self.lista_pazienti_da_modificare = pickle.load(lista_pazienti_da_modificare)

    def recupera_pazienti_modificati(self):
        """
        Funzione che, se esiste, legge dal database del personale medico, salvando in una lista tutti i pazienti per i
        quali è già stata modificata la descizione della patologia riscontrata
        """
        if os.path.isfile('paziente/data/prenotazioni_avvenute.pickle'):
            with open('paziente/data/prenotazioni_avvenute.pickle', 'rb') as lista_pazienti_modificati:
                self.lista_pazienti_modificati = pickle.load(lista_pazienti_modificati)

    def recupera_pazienti_modificati_personale_medico(self):
        """
        Funzione che, tramite un controllo di id_personale_medico, assegna i pazienti per i quali è già stata modificata
        la descrizione della patologia riscontrata al medico con cui si è svolta la visita, inserendo i pazienti in una
        lista apposita
        """
        self.lista_pazienti_modificati_personale_medico =\
            [x for x in self.lista_pazienti_modificati
             if x.id_personale_medico == self.personale_medico.id_personale_medico]

    def salva_pazienti_da_modificare(self):
        """
        Funzione che scrive sul database del personale medico la lista_pazienti_da_modificare, salvando, di fatto,
        i pazienti per i quali deve essere modificata la descrizione della patologia riscontrata nel database
        """
        with open(f'personale_medico/data/{self.personale_medico.id_personale_medico}.pickle', "wb") \
                as lista_pazienti_da_modificare:
            pickle.dump(self.lista_pazienti_da_modificare, lista_pazienti_da_modificare, pickle.HIGHEST_PROTOCOL)

    def salva_pazienti_modificati(self):
        """
        Funzione che scrive su file 'prenotazioni_avvenute.pickle' la lista_pazienti_modificati, salvando, di fatto,
        i pazienti per i quali è già stata modificata la descrizione della patologia riscontrata nel database
        """
        with open('paziente/data/prenotazioni_avvenute.pickle', 'wb') as lista_pazienti_modificati:
            pickle.dump(self.lista_pazienti_modificati, lista_pazienti_modificati, pickle.HIGHEST_PROTOCOL)

    def modifica_descrizione_patologia(self, prenotazione, descrizione_patologia):
        """
        Funzione che sposta la prenotazione effettuata dal paziente dalla lista dei pazienti per i quali dev'essere
        modificata la descrizione della patologia riscontrata alla lista dei pazienti per i quali tale descrizione è già
        stata modificata

        :param prenotazione: Parametro che rappresenta un oggetto della classe Prenotazione
        :type prenotazione: Prenotazione
        :param descrizione_patologia: Parametro che rappresenta la descrizione della patologia riscontrata,
                                       dapprima inserita quando la prenotazione risulta ancora da modificare, poi
                                       visualizzata nell'apposita label una volta che la prenotazione viene spostata tra
                                       le già modificate
        :type descrizione_patologia: str
        """
        self.lista_pazienti_da_modificare.remove(prenotazione)

        prenotazione.descrizione_patologia = descrizione_patologia

        self.lista_pazienti_modificati.append(prenotazione)

        self.salva_pazienti_da_modificare()
        self.salva_pazienti_modificati()
