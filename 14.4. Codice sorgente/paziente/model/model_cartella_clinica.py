import os.path
import pickle


class ListaPrenotazioniCartellaClinica:

    def __init__(self, paziente):
        """
        Costruttore della classe ListaPrenotazioniCartellaClinica, nella quale vengono istanziate delle variabili e
        richiamate le funzioni successivamente dichiarate e definite all'interno della stessa classe

        :param paziente: Variabile d'istanza che rappresenta un oggetto della classe Paziente
        :type paziente: Paziente
        """
        self.paziente = paziente
        self.lista_prenotazioni_cartella_clinica = []

        self.popola_descrizione_cartella_clinica()
        self.ordinamento_lista_per_data()

    def popola_descrizione_cartella_clinica(self):
        """
        Funzione che legge da file 'prenotazioni_avvenute.pickle', per poi confrontare l'id del paziente delle
        prenotazioni lette dal file con quello del paziente istanziato, per, infine, popolare la lista contenente
        le prenotazioni relative al paziente
        """
        prenotazioni_cartella_clinica = []

        if os.path.isfile('paziente/data/prenotazioni_avvenute.pickle'):
            with open('paziente/data/prenotazioni_avvenute.pickle', 'rb') as prenotazioni_avvenute:
                prenotazioni_cartella_clinica = pickle.load(prenotazioni_avvenute)

        for prenotazione in prenotazioni_cartella_clinica:
            if prenotazione.id_paziente == self.paziente.id_paziente:
                self.lista_prenotazioni_cartella_clinica.append(prenotazione)

    def ordinamento_lista_per_data(self):
        """
        Funzione che ordina la lista delle prenotazioni relative al paziente a seconda della data di quest'ultime
        """
        scambiati = True

        while scambiati:
            scambiati = False
            for i in range(len(self.lista_prenotazioni_cartella_clinica) - 1):
                if self.lista_prenotazioni_cartella_clinica[i].data_ora_visita >\
                        self.lista_prenotazioni_cartella_clinica[i + 1].data_ora_visita:
                    temp = self.lista_prenotazioni_cartella_clinica[i]
                    self.lista_prenotazioni_cartella_clinica[i] = self.lista_prenotazioni_cartella_clinica[i + 1]
                    self.lista_prenotazioni_cartella_clinica[i + 1] = temp
                    scambiati = True
