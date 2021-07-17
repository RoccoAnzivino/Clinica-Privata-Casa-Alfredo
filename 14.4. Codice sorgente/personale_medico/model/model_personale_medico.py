import pickle
import re

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox


class PersonaleMedico:

    def __init__(self, ultimo_id, nome, cognome, data_di_nascita, eta, sesso, provincia_di_nascita, citta_di_nascita,
                 codice_fiscale, ambulatorio, email, codice_identificativo, password):
        """
        Costruttore della classe PersonaleMedico, nella quale vengono istanziate le variabili che definiscono gli
        oggetti della stessa classe

        :param ultimo_id: Parametro che rappresenta l'ultimo id generato per un personale medico relativo al personale
                           medico stesso
        :type ultimo_id: str
        :param nome: Parametro che rappresenta il nome del personale medico relativo al personale medico stesso
        :type nome: str
        :param cognome: Parametro che rappresenta il cognome del personale medico relativo al personale medico stesso
        :type cognome: str
        :param data_di_nascita: Parametro che rappresenta la data di mascita del personale medico relativa al personale
                                 medico stesso
        :type data_di_nascita: date
        :param eta: Parametro che rappresenta l'età del personale medico relativa al personale medico stesso
        :type eta: int
        :param sesso: Parametro che rappresenta il sesso del personale medico relativo al personale medico stesso
        :type sesso: str
        :param provincia_di_nascita: Parametro che rappresenta la provincia di nascita del personale medico relativa al
                                      personale medico stesso
        :type provincia_di_nascita: str
        :param citta_di_nascita: Parametro che rappresenta la cittò di nascita del personale medico relativa al
                                  personale medico stesso
        :type citta_di_nascita: str
        :param codice_fiscale: Parametro che rappresenta il codice fiscale del personale medico relativo al personale
                                medico stesso
        :type codice_fiscale: str
        :param ambulatorio: Parametro che rappresenta l'ambulatorio del personale medico relativo al personale medico
                             stesso
        :type ambulatorio: str
        :param email: Parametro che rappresenta l'email del personale medico relativa al personale medico stesso
        :type email: str
        :param codice_identificativo: Parametro che rappresenta il codice identificativo del personale medico relativo
                                       al personale medico stesso
        :type codice_identificativo: str
        :param password: Parametro che rappresenta la password del personale medico relativa al personale medico stesso
        :type password: str
        """
        ultimo_id_numero = int(ultimo_id[2:])
        nuovo_id = str(ultimo_id_numero + 1)

        while len(nuovo_id) < 4:
            nuovo_id = '0' + nuovo_id

        self.id_personale_medico = 'pm' + nuovo_id
        self.nome = nome
        self.cognome = cognome
        self.data_di_nascita = data_di_nascita
        self.eta = eta
        self.sesso = sesso
        self.provincia_di_nascita = provincia_di_nascita
        self.citta_di_nascita = citta_di_nascita
        self.codice_fiscale = codice_fiscale
        self.ambulatorio = ambulatorio
        self.email = email
        self.codice_identificativo = codice_identificativo
        self.password = password

    def controllo_credenziali_personale_medico(self, codice_identificativo, password):
        """
        Funzione che confronta il codice identificativo e la password inserite, ovvero quelle passate alla stessa
        funzione come parametri, con il codice identificativo e la password salvate come variabili d'istanza
        dell'oggetto stesso

        :param codice_identificativo: Parametro che rappresenta il codice identificativo inserito, che verrà
                                       successivamente confrontato con la variabile d'istanza relativa
        :type codice_identificativo: str
        :param password: Parametro che rappresenta la password inserita, che verrà successivamente confrontata con la
                          variabile d'istanza relativa
        :type password: str
        :return: La funzione ritorna True quando i codici identificativi e le password coincidono, altrimenti
                  ritorna False
        :rtype: bool
        """
        if codice_identificativo == self.codice_identificativo and password == self.password:
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

    def salva_nuova_password_personale_medico(self):
        """
        Funzione che scrive sul database relativo la nuova password che è stata creata
        """
        percorso_personale_medico = 'personale_medico/login_personale_medico/data'

        with open(f'{percorso_personale_medico}/{self.id_personale_medico}.pickle', 'wb') as new_password:
            personale_medico_nuova_password = PersonaleMedico(self.id_personale_medico, self.nome, self.cognome,
                                                              self.data_di_nascita, self.eta, self.sesso,
                                                              self.provincia_di_nascita, self.citta_di_nascita,
                                                              self.codice_fiscale, self.ambulatorio, self.email,
                                                              self.codice_identificativo, self.password)
            pickle.dump(personale_medico_nuova_password, new_password, pickle.HIGHEST_PROTOCOL)

    def set_password_personale_medico(self, new_password, ripeti_password, vecchia_password):
        """
        Fuzione che permette di modificare la password relativa al personale medico, tramite l'inserimento della vecchia
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
                        self.salva_nuova_password_personale_medico()
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
