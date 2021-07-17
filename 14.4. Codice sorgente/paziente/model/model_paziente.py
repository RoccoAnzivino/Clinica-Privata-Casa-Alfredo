import pickle
import re

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox


class Paziente:

    def __init__(self, ultimo_id, nome, cognome, data_di_nascita, eta, sesso, provincia_di_nascita, citta_di_nascita,
                 codice_fiscale, email, password):
        """
        Costruttore della classe Paziente, nella quale vengono istanziate le variabili che definiscono gli oggetti della
        stessa classe

        :param ultimo_id: Parametro che rappresenta l'ultimo id generato per un paziente relativo al paziente stesso
        :type ultimo_id: str
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
        :param provincia_di_nascita: Parametro che rappresenta la provincia di nascita del paziente relativa al
                                      paziente stesso
        :type provincia_di_nascita: str
        :param citta_di_nascita: Parametro che rappresenta la città di nascita del paziente relativa al paziente stesso
        :type citta_di_nascita: str
        :param codice_fiscale: Parametro che rappresenta il codice fiscale del paziente relativo al paziente stesso
        :type codice_fiscale: str
        :param email: Parametro che rappresenta l'email del paziente relativa al paziente stesso
        :type email: str
        :param password: Parametro che rappresenta la password del paziente relativa al paziente stesso
        :type password: str
        """
        ultimo_id_numero = int(ultimo_id[1:])
        nuovo_id = str(ultimo_id_numero + 1)

        while len(nuovo_id) < 4:
            nuovo_id = '0' + nuovo_id

        self.id_paziente = 'p' + nuovo_id
        self.nome = nome
        self.cognome = cognome
        self.data_di_nascita = data_di_nascita
        self.eta = eta
        self.sesso = sesso
        self.provincia_di_nascita = provincia_di_nascita
        self.citta_di_nascita = citta_di_nascita
        self.codice_fiscale = codice_fiscale
        self.email = email
        self.password = password

    def controllo_credenziali_paziente(self, email, password):
        """
        Funzione che confronta l'email e la password inserite, ovvero quelle passate alla stessa funzione come
        parametri, con l'email e la password salvate come variabili d'istanza dell'oggetto stesso

        :param email: Parametro che rappresenta l'email inserita, che verrà successivamente confrontata con la variabile
                      d'istanza relativa
        :type email: str
        :param password: Parametro che rappresenta la password inserita, che verrà successivamente confrontata con la
                          variabile d'istanza relativa
        :type password: str
        :return: La funzione ritorna True quando le email e le password coincidono, altrimenti ritorna False
        :rtype: bool
        """
        if email == self.email and password == self.password:
            return True
        else:
            return False

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

    def salva_nuova_password_paziente(self):
        """
        Funzione che scrive sul database relativo la nuova password che è stata creata
        """
        with open(f'paziente/login_paziente/data/{self.id_paziente}.pickle', 'wb') as new_password:
            pickle.dump(self, new_password, pickle.HIGHEST_PROTOCOL)

    def set_password_paziente(self, new_password, ripeti_password, vecchia_password):
        """
        Fuzione che permette di modificare la password relativa al paziente, tramite l'inserimento della vecchia
        password (o password attuale) e della nuova password ripetuta due volte

        :param new_password: Parametro che rappresenta la nuova password che si vuole inserire nella modifica
        :type new_password: str
        :param ripeti_password: Parametro che rappresenta la nuova password inserita nuovamente, al fine di controllare
                                 che questa risulti uguale alla nuova password inserita, per evitare errori
        :type ripeti_password: str
        :param vecchia_password: Parametro che rappresenta la password attuale che si intende modificare
        :type vecchia_password: str
        :return: La funzione ritorna True se la modifica della password va a buon fine, altrimenti ritorna False
        :rtype: bool
        """
        popup = QMessageBox()
        icona = QIcon()
        icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
        popup.setWindowIcon(icona)

        if self.password == vecchia_password:
            if self.password == new_password:
                popup.setWindowTitle('Attenzione')
                popup.setIcon(QMessageBox.Warning)
                popup.setText('La nuova password deve essere diversa dalla vecchia password!')
                popup.exec_()
            else:
                if new_password == ripeti_password:
                    if self.controllo_sicurezza_password(new_password):
                        self.password = new_password
                        self.salva_nuova_password_paziente()
                        popup.setWindowTitle('Attenzione')
                        popup.setIcon(QMessageBox.Information)
                        popup.setText('Password aggiornata con successo!')
                        popup.exec_()
                        return True
                    else:
                        popup.setWindowTitle('Attenzione')
                        popup.setIcon(QMessageBox.Warning)
                        popup.setText('La password non è sicura! Seguire le indicazioni.')
                        popup.exec_()
                else:
                    popup.setWindowTitle('Attenzione')
                    popup.setIcon(QMessageBox.Warning)
                    popup.setText('La nuova password inserita e la sua conferma non coincidono!')
                    popup.exec_()
        else:
            popup.setWindowTitle('Attenzione')
            popup.setIcon(QMessageBox.Warning)
            popup.setText('La vecchia password inserita non è corretta')
            popup.exec_()

        return False
