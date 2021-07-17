from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from fpdf import FPDF


class PrenotazionePDF(FPDF):

    def __init__(self, id_prenotazione, data_prenotazione, nome, cognome, sesso, data_di_nascita, provincia, citta,
                 ambulatorio, nome_medico, cognome_medico, sesso_medico, data_visita, tipo_visita):
        """
        Costruttore della classe PrenotazionePDF, nella quale, a partire dalle informazioni ottenute tramite le stesse
        variabili d'istanza, viene generato il file .pdf relativo alla singola prenotazione effettuata dal paziente

        :param id_prenotazione: Parametro che rappresenta l'id della prenotazione relativo alla prenotazione stessa
        :type id_prenotazione: str
        :param data_prenotazione: Parametro che rappresenta la data dell'effettuazione della prenotazione relativa alla
                                   prenotazione stessa
        :type data_prenotazione: datetime.datetime
        :param nome: Parametro che rappresenta il nome del paziente relativo alla prenotazione
        :type nome: str
        :param cognome: Parametro che rappresenta il cognome del paziente relativo alla prenotazione
        :type cognome: str
        :param sesso: Parametro che rappresenta il sesso del paziente relativo alla prenotazione
        :type sesso: str
        :param data_di_nascita: Parametro che rappresenta la data di nascita del paziente relativa alla prenotazione
        :type data_di_nascita: datetime.date
        :param provincia: Parametro che rappresenta la provincia di nascita del paziente relativa alla prenotazione
        :type provincia: str
        :param citta: Parametro che rappresenta la città di nascita del paziente relativa alla prenotazione
        :type citta: str
        :param ambulatorio: Parametro che rappresenta l'ambulatorio relativo alla prenotazione
        :type ambulatorio: str
        :param nome_medico: Parametro che rappresenta il nome del personale medico relativo alla prenotazione
        :type nome_medico: str
        :param cognome_medico: Parametro che rappresenta il cognome del personale medico relativo alla prenotazione
        :type cognome_medico: str
        :param sesso_medico: Parametro che rappresenta il sesso del personale medico relativo alla prenotazione
        :type sesso_medico: str
        :param data_visita: Parametro che rappresenta la data della visita relativa alla prenotazione
        :type data_visita: datetime.datetime
        :param tipo_visita: Parametro che rappresenta il tipo di visita relativo alla prenotazione
        :type tipo_visita: str
        """
        super().__init__()

        self.id_prenotazione = id_prenotazione
        self.data_prenotazione = data_prenotazione
        self.nome = nome
        self.cognome = cognome
        self.sesso = sesso
        self.data_di_nascita = data_di_nascita
        self.provincia = provincia
        self.citta = citta
        self.ambulatorio = ambulatorio
        self.nome_medico = nome_medico
        self.cognome_medico = cognome_medico
        self.sesso_doc = sesso_medico
        self.data_visita = data_visita
        self.tipo_visita = tipo_visita

    def header(self):
        """
        Funzione che genera l'header del pdf
        """
        # add logo
        # coordinate: x = 10, y = 8
        # width = 25
        # fonts('times', 'courier', 'helvetica', 'symbol')
        self.image('Immagini/logo_casa_alfredo - pdf.png', 100, 8, 20)
        self.set_font('times', 'B', 20)

        # line break
        self.ln(40)

        # add title
        # align = 'C' mette il testo a centro pagina
        self.cell(0, 10, 'Clinica Casa Alfredo', ln=True, align='C')

    def mi_dia_del_lei(self):
        """
        Funzione che stabilisce, in base al sesso del paziente, se nel pdf debba essere definito come 'il Signor' oppure
        'la Signora'

        :return: La funzione ritorna 'il Signor' se il sesso del paziente è 'M', altrimenti ritorna 'la Signora' se il
                  sesso del paziente è 'F'
        :rtype: str
        """
        if self.sesso == "M":
            return "il Signor"
        else:
            return "la Signora"

    def nato_nata(self):
        """
        Funzione che stabilisce, in base al sesso del paziente, se nel pdf debba essere inserito 'nato il' oppure
        'nata il'

        :return: La funzione ritorna 'nato il' se il sesso del paziente è 'M', altrimenti ritorna 'nata il' se il
                  sesso del paziente è 'F'
        :rtype: str
        """
        if self.sesso == "M":
            return "nato il"
        else:
            return "nata il"

    def mi_dia_del_lei_doc(self):
        """
        Funzione che stabilisce, in base al sesso del personale medico, se nel pdf debba essere definito come
        'dal Dottor' oppure 'dalla Dott.ssa'

        :return: La funzione ritorna 'dal Dottor' se il sesso del personale medico è 'M', altrimenti ritorna
                  'dalla Dott.ssa' se il sesso del personale medico è 'F'
        :rtype: str
        """
        if self.sesso_doc == "M":
            return "dal Dottor"
        else:
            return "dalla Dott.ssa"

    def genera_pdf(self):
        """
        Funzione che genera il pdf, settando il testo e richiamando tutte le funzioni presenti in questa classe, per poi
        salvare il file .pdf
        """

        dir_path = QFileDialog.getExistingDirectory(caption='Scegli la cartella in cui scaricare la prenotazione')

        if not dir_path:
            return

        self.add_page()
        self.cell(0, 10, 'Rilascio attestato di avvenuta prenotazione', ln=True, align='C')
        self.ln(15)
        self.set_font('times', '', 11)
        self.cell(0, 10, 'Si certifica che', ln=True, align='C')
        self.cell(0, 10, 'in data ' + self.data_prenotazione.strftime("%d/%m/%Y") + ', alle ore ' +
                  self.data_prenotazione.strftime("%H:%M") + ', ' + self.mi_dia_del_lei() + ' ' + self.cognome + ' ' +
                  self.nome + ', ' + self.nato_nata() + ' ' + self.data_di_nascita.strftime("%d/%m/%Y") + ' a ' +
                  self.citta + ', in provincia di ' + self.provincia + ', ', ln=True)
        self.cell(0, 0, 'ha effettuato una prenotazione presso l\'ambulatorio ' + self.ambulatorio + ', presieduto ' +
                  self.mi_dia_del_lei_doc() + ' ' + self.cognome_medico + ' ' + self.nome_medico + ', ', ln=True)
        self.cell(0, 10, 'che avrà luogo il giorno ' + self.data_visita.strftime("%d/%m/%Y") + ' alle ore ' +
                  self.data_visita.strftime("%H:%M") + '.', ln=True)
        self.cell(0, 10, 'Il motivo della visita è: ' + self.tipo_visita + '.', ln=True)
        self.ln(15)
        self.set_font('times', 'B', 11)
        self.cell(0, 10, 'Clinica Casa Alfredo', align='R')
        self.image('Immagini/firma - pdf.png', 180, 148, 20)
        self.set_auto_page_break(auto=True, margin=15)
        path = dir_path + f'/prenotazione_del_{self.data_visita.strftime("%d-%m-%Y")}_{self.nome}_{self.cognome}.pdf'
        self.output(path, 'F')
        popup = QMessageBox()
        icona = QIcon()
        icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
        popup.setWindowIcon(icona)
        popup.setWindowTitle('Prenotazione effettuata')
        popup.setIcon(QMessageBox.Information)
        popup.setText('Download eseguito!               ')
        popup.exec_()
