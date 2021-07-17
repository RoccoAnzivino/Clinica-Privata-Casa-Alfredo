import datetime
import json
import os.path
import pickle
import re

from paziente.model.model_paziente import Paziente


class ListaPazienti:

    def __init__(self):
        """
        Costruttore della classe ListaPazienti, nella quale vengono istanziate delle variabili e richiamate le funzioni
        successivamente dichiarate e definite all'interno della stessa classe
        """
        self.lista_pazienti = []

        self.recupera_pazienti()
        self.aggiorna_password_paziente()

    def recupera_pazienti(self):
        """
        Funzione che, se esiste, legge da file 'pazienti.pickle', salvando i pazienti registrati in una lista,
        altrimenti legge da file 'pazienti.json', salvando i pazienti pre registrati in una lista e assegnando gli
        id_paziente agli elementi di quest'ultima, ovvero ai pazienti pre registrati
        """
        if os.path.isfile('paziente/login_paziente/data/pazienti.pickle'):
            with open('paziente/login_paziente/data/pazienti.pickle', 'rb') as pazienti_registrati:
                self.lista_pazienti = pickle.load(pazienti_registrati)
        else:
            with open('paziente/login_paziente/data/pazienti.json', 'r') as pazienti_pre_registrati:
                lista_pazienti_json = json.load(pazienti_pre_registrati)
            for paziente in lista_pazienti_json:
                if not self.lista_pazienti:
                    id_paziente = 'p0000'
                else:
                    id_paziente = self.lista_pazienti[-1].id_paziente
                data_di_nascita = datetime.date(paziente['anno_di_nascita'], paziente['mese_di_nascita'],
                                                paziente['giorno_di_nascita'])
                eta = self.calcolo_eta(data_di_nascita)
                self.lista_pazienti.append(Paziente(id_paziente, paziente['nome'], paziente['cognome'],
                                                    data_di_nascita, eta, paziente['sesso'],
                                                    paziente['provincia_di_nascita'], paziente['citta_di_nascita'],
                                                    paziente['codice_fiscale'], paziente['email'],
                                                    paziente['password']))

    def aggiorna_password_paziente(self):
        """
        Funzione che aggiorna la password del paziente, sostituendo nel database relativo allo stesso paziente la
        vecchia password con quella nuova
        """
        for paziente in self.lista_pazienti:
            if os.path.isfile(f'paziente/login_paziente/data/{paziente.id_paziente}.pickle'):
                with open(f'paziente/login_paziente/data/{paziente.id_paziente}.pickle', 'rb') as paz:
                    paziente_nuova_password = pickle.load(paz)
                self.lista_pazienti[int(paziente.id_paziente[1:])-1].password = paziente_nuova_password.password
                os.remove(f'paziente/login_paziente/data/{paziente.id_paziente}.pickle')
        self.salva_pazienti()

    def registrazione_paziente(self, nome, cognome, data_di_nascita, eta, sesso, citta_di_nascita, provincia_di_nascita,
                               codice_fiscale, email, password):
        """
        Funzione che crea un oggetto della classe Paziente, per poi inserire il paziente creato dapprima nella
        lista_pazienti, poi nel database tramite la relativa funzione

        :param nome: Parametro che rappresenta il nome del paziente relativo al paziente stesso
        :type nome: str
        :param cognome: Parametro che rappresenta il cognome del paziente relativo al paziente stesso
        :type cognome: str
        :param data_di_nascita: Parametro che rappresenta la data di nascita del paziente relativa al paziente stesso
        :type data_di_nascita: date
        :param eta: Parametro che rappresenta l'età del paziente relativa al paziente stesso
        :type eta: int
        :param sesso: Parametro che rappresenta il sesso del paziente relativo al paziente stesso
        :type sesso: str
        :param citta_di_nascita: Parametro che rappresenta la città di nascita del paziente relativa al paziente stesso
        :type citta_di_nascita: str
        :param provincia_di_nascita: Parametro che rappresenta la provincia di nascita del paziente relativa al paziente
                                      stesso
        :type provincia_di_nascita: str
        :param codice_fiscale: Parametro che rappresenta il codice fiscale del paziente relativo al paziente stesso
        :type codice_fiscale: str
        :param email: Parametro che rappresenta l'email del paziente relativa al paziente stesso
        :type email: str
        :param password: Parametro che rappresenta la password del paziente relativa al paziente stesso
        :type password: str
        """
        paziente = Paziente(self.lista_pazienti[-1].id_paziente, nome, cognome, data_di_nascita, eta, sesso,
                            provincia_di_nascita, citta_di_nascita, codice_fiscale, email, password)

        self.lista_pazienti.append(paziente)
        self.salva_pazienti()

    def controlla_credenziali(self, email, password):
        """
        Funzione che confronta l'email e la password inserite, ovvero quelle passate alla stessa funzione come
        parametri, con l'email e la password salvate come variabili d'istanza dell'oggetto stesso, il tutto richiamando
        l'apposita funzione

        :param email: Parametro che rappresenta l'email inserita, che verrà successivamente confrontata con la variabile
                      d'istanza relativa
        :type email: str
        :param password: Parametro che rappresenta la password inserita, che verrà successivamente confrontata con la
                          variabile d'istanza relativa
        :type password: str
        :return: La funzione ritorna Paziente se trova una corrispondenza nel database dei Pazienti,
                 altrimenti ritorna None
        :rtype: Paziente, None
        """
        for paziente in self.lista_pazienti:
            if paziente.controllo_credenziali_paziente(email, password):
                return paziente

        return None

    def salva_pazienti(self):
        """
        Funzione che scrive su file 'pazienti.pickle' la lista dei pazienti registrati
        """
        with open('paziente/login_paziente/data/pazienti.pickle', 'wb') as pazienti_registrati:
            pickle.dump(self.lista_pazienti, pazienti_registrati, pickle.HIGHEST_PROTOCOL)

    def controllo_email_gia_registrata(self, email):
        """
        Funzione che controlla l'eventuale presenza di una email già utilizzata da un altro paziente, evitando la
        possibilità di associare più account a una stessa email

        :param email: Parametro che rappresenta l'email inserita, che verrà successivamente confrontata con le email di
                       di tutti gli altri pazienti presenti nella lista_pazienti
        :type email: str
        :return: La funzione ritorna True se nella lista_pazienti esiste una email uguale a quella inserita, altrimenti
                  ritorna False
        :rtype: bool
        """
        for paziente in self.lista_pazienti:
            if paziente.email == email:
                return True

        return False

    @staticmethod
    def controllo_email(email):
        """
        Funzione che controlla la correttezza del formato dell'email inserita

        :param email: Parametro che rappresenta l'email inserita, della quale verrà controllata la correttezza del
                      formato
        :type email: str
        :return: La funzione ritorna False nel momento in cui non rispetta uno dei vincoli di formato imposto dalla
                  stessa funzione, altrimenti ritorna True quando il controllo va a buon fine
        :rtype: bool
        """
        if '@' not in email:
            return False

        pre_chiocciola = email[:email.index('@')]

        if not pre_chiocciola:
            return False

        post_chiocciola = email[email.index('@') + 1:]

        if not post_chiocciola:
            return False

        if '.' not in post_chiocciola:
            return False

        post_punto = email[email.index('.') + 1:]

        if not post_punto:
            return False

        return True

    @staticmethod
    def calcolo_eta(data_di_nascita):
        """
        Funzione che calcola l'età del paziente a partire dalla data di nascita di quest'ultimo

        :param data_di_nascita: Parametro che rappresenta la data di nascita del paziente relativa al paziente stesso
        :type data_di_nascita: date
        :return: La funzione ritorna l'età del paziente calcolata a partire dalla data di nascita del paziente
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
