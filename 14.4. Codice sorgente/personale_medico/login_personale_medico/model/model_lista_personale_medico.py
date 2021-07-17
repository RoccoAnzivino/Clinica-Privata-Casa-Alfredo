import datetime
import json
import os
import pickle
import re

from personale_medico.model.model_personale_medico import PersonaleMedico


class ListaPersonaleMedico:
    def __init__(self):
        """
        Costruttore della classe ListaPersonaleMedico, nella quale vengono istanziate delle variabili e richiamate le
        funzioni successivamente dichiarate e definite all'interno della stessa classe
        """
        self.lista_personale_medico = []

        self.recupera_personale_medico()
        self.aggiorna_password_personale_medico()

    def recupera_personale_medico(self):
        """
        Funzione che, se esiste, legge da file 'personale_medico.pickle', salvando i personale medico registrati in una
        lista, altrimenti legge da file 'personale_medico.json', salvando i personale_medico in una lista e assegnando
        gli id_personale_medico agli elementi di quest'ultima, ovvero al personale_medico
        """
        percorso_personale_medico = 'personale_medico/login_personale_medico/data'

        if os.path.isfile(f'{percorso_personale_medico}/personale_medico.pickle'):
            with open(f'{percorso_personale_medico}/personale_medico.pickle', 'rb') as personale_medico:
                self.lista_personale_medico = pickle.load(personale_medico)
        else:
            with open(f'{percorso_personale_medico}/personale_medico.json', 'r') as personale_medico:
                lista_personale_medico_json = json.load(personale_medico)

            for personale_medico in lista_personale_medico_json:
                if not self.lista_personale_medico:
                    id_personale_medico = 'pm0000'
                else:
                    id_personale_medico = self.lista_personale_medico[-1].id_personale_medico

                data_di_nascita = datetime.date(personale_medico['anno_di_nascita'],
                                                personale_medico['mese_di_nascita'],
                                                personale_medico['giorno_di_nascita'])

                eta = self.calcolo_eta(data_di_nascita)

                self.lista_personale_medico.append(PersonaleMedico(id_personale_medico, personale_medico['nome'],
                                                                   personale_medico['cognome'], data_di_nascita, eta,
                                                                   personale_medico['sesso'],
                                                                   personale_medico['provincia_di_nascita'],
                                                                   personale_medico['citta_di_nascita'],
                                                                   personale_medico['codice_fiscale'],
                                                                   personale_medico['ambulatorio'],
                                                                   personale_medico['email'],
                                                                   personale_medico['codice_identificativo'],
                                                                   personale_medico['password']))

    def aggiorna_password_personale_medico(self):
        """
        Funzione che aggiorna la password del personale medico, sostituendo nel database relativo allo stesso paziente
        la vecchia password con quella nuova
        """
        percorso_personale_medico = 'personale_medico/login_personale_medico/data'

        for personale_medico in self.lista_personale_medico:
            if os.path.isfile(f'{percorso_personale_medico}/{personale_medico.id_personale_medico}.pickle'):

                with open(f'{percorso_personale_medico}/{personale_medico.id_personale_medico}.pickle', 'rb') as pm:
                    personale_medico_nuova_password = pickle.load(pm)

                self.lista_personale_medico[int(personale_medico.id_personale_medico[2:]) - 1].password = \
                    personale_medico_nuova_password.password

                os.remove(f'personale_medico/login_personale_medico/data/{personale_medico.id_personale_medico}.pickle')

        self.salva_personale_medico()

    def controlla_credenziali(self, codice_identificativo, password):
        """
        Funzione che confronta il codice identificativo e la password inserite, ovvero quelle passate alla stessa
        funzione come parametri, con il codice identificativo e la password salvate come variabili d'istanza
        dell'oggetto stesso, il tutto richiamando l'apposita funzione

        :param codice_identificativo: Parametro che rappresenta il codice identificativo inserito, che verrà
                                       successivamente confrontato con la variabile d'istanza relativa
        :type codice_identificativo: str
        :param password: Parametro che rappresenta la password inserita, che verrà successivamente confrontata con la
                          variabile d'istanza relativa
        :type password: str
        :return: La funzione ritorna PersonaleMedico se trova una corrispondenza nel database del personale medico,
                 altrimenti ritorna None
        :rtype: PersonaleMedico, None
        """
        for personale_medico in self.lista_personale_medico:
            if personale_medico.controllo_credenziali_personale_medico(codice_identificativo, password):
                return personale_medico

        return None

    def salva_personale_medico(self):
        """
        Funzione che scrive su file 'personale_medico.pickle' la lista dei personale medico registrati
        """
        percorso_personale_medico = 'personale_medico/login_personale_medico/data'

        with open(f'{percorso_personale_medico}/personale_medico.pickle', 'wb') as personale_medico:
            pickle.dump(self.lista_personale_medico, personale_medico, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def calcolo_eta(data_di_nascita):
        """
        Funzione che calcola l'età del personale medico a partire dalla data di nascita di quest'ultimo

        :param data_di_nascita: Parametro che rappresenta la data di nascita del personale medico relativa al personale
                                 medico stesso
        :type data_di_nascita: date
        :return: La funzione ritorna l'età del personale medico calcolata a partire dalla data di nascita del personale
                  medico stesso
        :rtype: int
        """
        data_attuale = datetime.date.today()

        if data_attuale.month > data_di_nascita.month:
            eta = data_attuale.year - data_di_nascita.year
        elif data_attuale.month < data_di_nascita.month:
            eta = data_attuale.year - data_di_nascita.year - 1
        else:
            if data_attuale.day >= data_di_nascita.day:
                eta = data_attuale.year - data_di_nascita.year
            else:
                eta = data_attuale.year - data_di_nascita.year - 1

        return eta

    @staticmethod
    def controllo_sicurezza_password(password):
        """
        Funzione che analizza la password inserita, al fine di stabilire se quest'ultima sia sicura o meno, ovvero
        se rispetta i vincoli imposti per la generazione della password

        :param password: Parametro che rappresenta la password inserita, la quale andrà incontro al controllo di
                          sicurezza attuato dalla funzione stessa
        :type password: str
        :return: La funzione ritorna True se la password da controllare rispetta i vincoli imposti dal controllo,
                 altrimenti la funzione ritorna False
        :rtype: bool
        """
        conta_minimo_caratteri = 0
        maiuscola = 0
        numero = 0
        carattere_speciale = 0
        caratteri_speciali = re.compile('[@_!#$%^&*()<>?/\\\\|}{~:.,]')
        min_length = 0

        for c in password:
            conta_minimo_caratteri += 1
            if c.isupper():
                maiuscola += 1
            if c.isdigit():
                numero += 1
            if caratteri_speciali.search(c) is not None:
                carattere_speciale += 1
            if conta_minimo_caratteri >= 8:
                min_length = 1

        if maiuscola > 0 and numero > 0 and carattere_speciale > 0 and min_length == 1:
            return True
        else:
            return False
