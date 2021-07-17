import datetime
from unittest import TestCase

from paziente.model.model_cartella_clinica import ListaPrenotazioniCartellaClinica
from paziente.model.model_paziente import Paziente
from paziente.model.model_prenotazione import Prenotazione


class TestCartellaClinica(TestCase):
    def test_ordinamento_lista_per_data(self):
        data_di_nascita = datetime.date(1990, 5, 14)
        paziente = Paziente('p0000', 'Alfredo', 'Sansovini', data_di_nascita, 35, 'M', 'Foggia', 'Lucera',
                            'SNSLRD90E14D643Y', 'alfredo.sansovini@finta.com', 'alfredoS90.')

        data_ora_prenotazione1 = datetime.datetime(2021, 6, 30, 17, 45)
        data_ora_visita_prenotazione1 = datetime.datetime(2021, 7, 6, 8, 50)
        prenotazione1 = Prenotazione('pren0000', paziente.id_paziente, paziente.nome, paziente.cognome,
                                     'Endocrinologia', 'Visita endocrinologica', 'pm0004', 'Lara', 'Ghiando', 'F',
                                     data_ora_prenotazione1, data_ora_visita_prenotazione1, '€130', 40, 'Infiammazione')

        data_ora_prenotazione2 = datetime.datetime(2021, 7, 20, 17, 45)
        data_ora_visita_prenotazione2 = datetime.datetime(2021, 7, 22, 10, 40)
        prenotazione2 = Prenotazione(prenotazione1.id_prenotazione, paziente.id_paziente, paziente.nome,
                                     paziente.cognome, 'Endocrinologia', 'Visita endocrinologica', 'pm0004', 'Lara',
                                     'Ghiando', 'F', data_ora_prenotazione2, data_ora_visita_prenotazione2, '€130', 40,
                                     'Infiammazione')

        data_ora_prenotazione3 = datetime.datetime(2021, 7, 25, 17, 45)
        data_ora_visita_prenotazione3 = datetime.datetime(2021, 7, 27, 9, 45)
        prenotazione3 = Prenotazione(prenotazione2.id_prenotazione, paziente.id_paziente, paziente.nome,
                                     paziente.cognome, 'Endocrinologia', 'Visita endocrinologica', 'pm0004', 'Lara',
                                     'Ghiando', 'F', data_ora_prenotazione3, data_ora_visita_prenotazione3, '€130', 40,
                                     'Infiammazione')

        data_ora_prenotazione4 = datetime.datetime(2021, 7, 29, 17, 45)
        data_ora_visita_prenotazione4 = datetime.datetime(2021, 7, 31, 15, 55)
        prenotazione4 = Prenotazione(prenotazione3.id_prenotazione, paziente.id_paziente, paziente.nome,
                                     paziente.cognome, 'Endocrinologia', 'Visita endocrinologica', 'pm0004', 'Lara',
                                     'Ghiando', 'F', data_ora_prenotazione4, data_ora_visita_prenotazione4, '€130', 40,
                                     'Infiammazione')

        lista_ordinata = [prenotazione1, prenotazione2, prenotazione3, prenotazione4]
        lista_disordinata = [prenotazione3, prenotazione4, prenotazione2, prenotazione1]

        model_cartella_clinica = ListaPrenotazioniCartellaClinica(paziente)
        model_cartella_clinica.lista_prenotazioni_cartella_clinica.clear()
        model_cartella_clinica.lista_prenotazioni_cartella_clinica.extend(lista_disordinata)

        model_cartella_clinica.ordinamento_lista_per_data()

        for prenotazione_ord, prenotazione_model in zip(lista_ordinata,
                                                        model_cartella_clinica.lista_prenotazioni_cartella_clinica):
            for val1, val2 in zip(prenotazione_ord.__dict__.values(), prenotazione_model.__dict__.values()):
                self.assertEqual(val1, val2)
