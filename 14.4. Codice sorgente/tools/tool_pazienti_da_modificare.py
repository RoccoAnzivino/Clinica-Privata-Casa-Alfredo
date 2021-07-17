from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox, QLineEdit

from personale_medico.view import view_lista_pazienti_visitati

from tools import ridimensiona_widget


class ToolPazientiDaModificare:

    def __init__(self, widget, scroll_area, widget_scroll_area, lista_pazienti_visitati):
        """
        Costruttore della classe ToolPazientiDaModificare, nella quale vengono creati e gestiti tutti gli oggetti
        della Graphical User Interface (GUI) relativi alla scroll area dove sono inserite le visite effettuate dal
        personale medico ai pazienti per le quali dev'essere ancora modificata la descrizione della patologia
        riscontrata

        :param widget: Parametro che rappresenta un oggetto della classe ViewListaPazientiVisitati
        :type widget: ViewListaPazientiVisitati
        :param scroll_area: Parametro che rappresenta la scroll area
        :type scroll_area: QScrollArea
        :param widget_scroll_area: Parametro che rappresenta il contenuto della scroll area, nella quale sono inseriti
                                    i diversi oggetti delle prenotazioni delle visite effettuate
        :type widget_scroll_area: QWidget
        :param lista_pazienti_visitati: Parametro che rappresenta un oggetto della classe ListaPazientiVisitati
        :type lista_pazienti_visitati: ListaPazientiVisitati
        """
        self.widget = widget
        self.lista_pazienti_visitati = lista_pazienti_visitati
        self.altezza = 23

        self.nome_label = None
        self.ambulatorio_label = None
        self.attivita_ambulatoriale_label = None
        self.data_e_ora_label = None
        self.patologia_riscontrata_button = None

        self.moltiplicazione_del_pane_e_delle_label(widget_scroll_area)

        widget_scroll_area.setGeometry(QtCore.QRect(0, 0, 1811, self.altezza))
        scroll_area.setWidget(widget_scroll_area)

    def crea_label(self, widget_scroll_area, y, prenotazione):
        """
        Funzione che crea e determina le caratteristiche degli oggetti all'interno della widget_scroll_area

        :param widget_scroll_area: Parametro che rappresenta il contenuto della scroll area, nella quale sono inseriti
                                    i diversi oggetti delle prenotazioni delle visite effettuate
        :type widget_scroll_area: QWidget
        :param y: Parametro che rappresenta l'altezza di ogni singola label contenente le prenotazioni
        :type y: int
        :param prenotazione: Parametro che rappresenta un oggetto della classe Prenotazione
        :type prenotazione: Prenotazione
        """
        self.nome_label = QtWidgets.QLabel(widget_scroll_area)
        self.nome_label.setGeometry(QtCore.QRect(0, y, 325, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        self.nome_label.setFont(font)
        self.nome_label.setStyleSheet("border: 2px solid;\n"
                                      "background-color: rgb(169, 202, 239);")
        self.nome_label.setText(prenotazione.nome_paziente + ' ' + prenotazione.cognome_paziente)
        self.nome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.nome_label.setObjectName("nome_label")
        self.ambulatorio_label = QtWidgets.QLabel(widget_scroll_area)
        self.ambulatorio_label.setGeometry(QtCore.QRect(323, y, 400, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        self.ambulatorio_label.setFont(font)
        self.ambulatorio_label.setStyleSheet("border: 2px solid;\n"
                                             "background-color: rgb(84, 149, 223);")
        self.ambulatorio_label.setText(prenotazione.ambulatorio)
        self.ambulatorio_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ambulatorio_label.setObjectName("ambulatorio_label")
        self.attivita_ambulatoriale_label = QtWidgets.QLabel(widget_scroll_area)
        self.attivita_ambulatoriale_label.setGeometry(QtCore.QRect(721, y, 400, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        self.attivita_ambulatoriale_label.setFont(font)
        self.attivita_ambulatoriale_label.setStyleSheet("border: 2px solid;\n"
                                                        "background-color: rgb(169, 202, 239);")
        self.attivita_ambulatoriale_label.setText(prenotazione.attivita_ambulatoriale)
        self.attivita_ambulatoriale_label.setAlignment(QtCore.Qt.AlignCenter)
        self.attivita_ambulatoriale_label.setObjectName("attivita_ambulatoriale_label")
        self.data_e_ora_label = QtWidgets.QLabel(widget_scroll_area)
        self.data_e_ora_label.setGeometry(QtCore.QRect(1119, y, 400, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        self.data_e_ora_label.setFont(font)
        self.data_e_ora_label.setStyleSheet("border: 2px solid;\n"
                                            "background-color: rgb(84, 149, 223);")
        self.data_e_ora_label.setText(prenotazione.data_ora_visita.strftime("%d/%m/%Y, %H:%M"))
        self.data_e_ora_label.setAlignment(QtCore.Qt.AlignCenter)
        self.data_e_ora_label.setObjectName("data_e_ora_label")
        self.patologia_riscontrata_button = QtWidgets.QPushButton(widget_scroll_area)
        self.patologia_riscontrata_button.setGeometry(QtCore.QRect(1517, y, 273, 90))
        self.patologia_riscontrata_button.setText('Modifica')
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPixelSize(19)
        font.setItalic(True)
        font.setUnderline(True)
        self.patologia_riscontrata_button.setFont(font)
        self.patologia_riscontrata_button.setStyleSheet("QPushButton#patologia_riscontrata_button {\n"
                                                        "color: rgb(0, 0, 255);\n"
                                                        "border: 2px solid;\n"
                                                        "background-color: rgb(169, 202, 239);\n"
                                                        "}\n"
                                                        "\n"
                                                        "QPushButton#patologia_riscontrata_button:pressed {\n"
                                                        "color: rgb(0, 0, 180);\n"
                                                        "}")
        self.patologia_riscontrata_button.setIconSize(QtCore.QSize(50, 50))
        self.patologia_riscontrata_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.patologia_riscontrata_button.setObjectName("patologia_riscontrata_button")
        self.patologia_riscontrata_button.clicked.connect(lambda: self.modifica_patologia_riscontrata(prenotazione))

        ridimensiona_widget.ridimensiona_tool(self)

    def moltiplicazione_del_pane_e_delle_label(self, widget_scroll_area):
        """
        Funzione che calcola dinamicamente la dimensione e la posizione di ogni nuova label che si viene a creare nel
        momento in cui si aggiunge una prenotazione di una visita effettuata

        :param widget_scroll_area: Parametro che rappresenta il contenuto della scroll area, nella quale sono inseriti
                                    i diversi oggetti delle prenotazioni delle visite effettuate
        :type widget_scroll_area: QWidget
        """
        y = 23

        for prenotazione, i in zip(self.lista_pazienti_visitati.lista_pazienti_da_modificare,
                                   range(len(self.lista_pazienti_visitati.lista_pazienti_da_modificare))):
            self.crea_label(widget_scroll_area, y + (88 * i), prenotazione)
            self.altezza += 90

    def modifica_patologia_riscontrata(self, prenotazione):
        """
        Funzione che consente di inserire la patologia riscontrata nell'apposito campo di una prenotazione

        :param prenotazione: Parametro che rappresenta un oggetto della classe Prenotazione
        :type prenotazione: Prenotazione
        """
        popup = QMessageBox()
        icona = QIcon()
        testo = QLineEdit(popup)
        icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
        popup.setWindowIcon(icona)
        popup.setText("                                                                            ")
        popup.setWindowTitle('Patologia')
        popup.setIcon(QMessageBox.Question)
        popup.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        popup.buttonClicked.connect(lambda: self.registra_patologia_riscontrata(popup, testo.text(), prenotazione))
        testo.setGeometry(70, 18, 300, 30)
        testo.setPlaceholderText("Inserire patologia riscontrata...")
        ridimensiona_widget.ridimensiona_singolo_oggetto(self.widget, testo)
        popup.exec_()

    def registra_patologia_riscontrata(self, popup, descrizione_patologia, prenotazione):
        """
        Funzione che salva la descrizione della patologia riscontrata per una determinata prenotazione e la registra

        :param popup: Parametro che rappresente la QMessageBox che permette di modificare la patologia riscontrata
        :type popup: QMesssageBox
        :param descrizione_patologia: Parametro che rappresenta la patologia riscontrata inserita
        :type descrizione_patologia: str
        :param prenotazione: Parametro che rappresenta un oggetto della classe Prenotazione
        :type prenotazione: Prenotazione
        """
        if popup.clickedButton().text() == "OK":
            if descrizione_patologia:
                popup.hide()
                popup2 = QMessageBox()
                icona = QIcon()
                icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
                popup2.setWindowIcon(icona)
                popup2.setWindowTitle('Informazione')
                popup2.setIcon(QMessageBox.Information)
                popup2.setText('La patologia è stata registrata!')
                popup2.exec_()
                self.lista_pazienti_visitati.modifica_descrizione_patologia(prenotazione,
                                                                            self.testo_a_capo(descrizione_patologia))
                nuova_view_lista_pazienti_visitati = \
                    view_lista_pazienti_visitati.ViewListaPazientiVisitati(self.widget.personale_medico)
                nuova_view_lista_pazienti_visitati.show()
                self.widget.hide()
            else:
                popup3 = QMessageBox()
                icona = QIcon()
                icona.addPixmap(QPixmap("Immagini/logo_casa_alfredo.png"), QIcon.Normal, QIcon.Off)
                popup3.setWindowIcon(icona)
                popup3.setWindowTitle('Attenzione')
                popup3.setIcon(QMessageBox.Warning)
                popup3.setText('Nessuna patologia inserita!')
                popup3.exec_()

    @staticmethod
    def testo_a_capo(testo):
        """
        Funzione che formatta il testo della descrizione della patologia riscontrata, al fine di evitare errori grafici

        :param testo: Parametro che rappresenta il testo della descrizione della patologia riscontrata
        :type testo: str
        :return: La funzione ritorna il testo della descrizione della patologia riscontrata formattato
        :rtype: str
        """
        if len(testo) > 17:
            testo_a_capo = testo[10:]
            testo_piu_righe = testo[:10] + testo_a_capo.replace(' ', '\n')
            return testo_piu_righe

        return testo
