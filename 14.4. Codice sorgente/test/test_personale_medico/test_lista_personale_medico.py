import datetime
from unittest import TestCase

from personale_medico.login_personale_medico.model.model_lista_personale_medico import ListaPersonaleMedico


class TestListaPersonaleMedico(TestCase):
    def test_calcolo_eta(self):
        data_di_nascita = datetime.date(1970, 3, 21)
        eta_calcolata = ListaPersonaleMedico.calcolo_eta(data_di_nascita)
        self.assertEqual(eta_calcolata, 51)

    def test_controllo_sicurezza_password(self):
        password = 'SonoUnMedicoEvvai0.'
        self.assertTrue(ListaPersonaleMedico.controllo_sicurezza_password(password))
