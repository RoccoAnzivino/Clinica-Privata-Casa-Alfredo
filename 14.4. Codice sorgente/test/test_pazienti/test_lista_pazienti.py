import datetime
from unittest import TestCase
from paziente.login_paziente.model.model_lista_pazienti import ListaPazienti


class TestListaPazienti(TestCase):
    def test_calcolo_eta(self):
        data_di_nascita = datetime.date(1990, 5, 14)
        eta_calcolata = ListaPazienti.calcolo_eta(data_di_nascita)
        self.assertEqual(eta_calcolata, 31)

    def test_controllo_sicurezza_password(self):
        password = 'alfredoS90.'
        self.assertTrue(ListaPazienti.controllo_sicurezza_password(password))
