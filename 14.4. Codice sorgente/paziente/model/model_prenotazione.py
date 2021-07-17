class Prenotazione:

    def __init__(self, ultimo_id_prenotazione, id_paziente, nome_paziente, cognome_paziente, ambulatorio,
                 attivita_ambulatoriale, id_personale_medico, nome_personale_medico, cognome_personale_medico,
                 sesso_personale_medico, data_ora_prenotazione, data_ora_visita, prezzo,
                 durata, descrizione_patologia):
        """
        Costruttore della classe Prenotazione, nella quale vengono istanziate le variabili che definiscono gli oggetti
        della stessa classe

        :param ultimo_id_prenotazione: Parametro che rappresenta l'ultimo id generato per una prenotazione relativo alla
                                        prenotazione stessa
        :type ultimo_id_prenotazione: str
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
        :param data_ora_prenotazione: Parametro che rappresenta la data e l'ora al momento dell'effettuazione della
                                       prenotazione
        :type data_ora_prenotazione: datetime.datetime
        :param data_ora_visita: Parametro che rappresenta la data e l'ora della visita relative alla prenotazione
        :type data_ora_visita: datetime.datetime
        :param prezzo: Parametro che rappresenta il prezzo della visita relativo alla prenotazione
        :type prezzo: str
        :param durata: Parametro che rappresenta la durata della visita relativa alla prenotazione
        :type durata: int
        :param descrizione_patologia: Parametro che rappresenta la descrizione della patologia relativa alla
                                       prenotazione
        :type descrizione_patologia: str
        """
        ultimo_id_numero = int(ultimo_id_prenotazione[4:])
        nuovo_id = str(ultimo_id_numero + 1)

        while len(nuovo_id) < 4:
            nuovo_id = '0' + nuovo_id

        self.id_prenotazione = 'pren' + nuovo_id
        self.id_paziente = id_paziente
        self.nome_paziente = nome_paziente
        self.cognome_paziente = cognome_paziente
        self.ambulatorio = ambulatorio
        self.attivita_ambulatoriale = attivita_ambulatoriale
        self.id_personale_medico = id_personale_medico
        self.nome_personale_medico = nome_personale_medico
        self.cognome_personale_medico = cognome_personale_medico
        self.sesso_personale_medico = sesso_personale_medico
        self.data_ora_prenotazione = data_ora_prenotazione
        self.data_ora_visita = data_ora_visita
        self.prezzo = prezzo
        self.durata = durata
        self.descrizione_patologia = descrizione_patologia
