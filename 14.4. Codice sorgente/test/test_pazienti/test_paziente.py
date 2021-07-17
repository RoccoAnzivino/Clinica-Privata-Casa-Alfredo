import datetime
from unittest import TestCase

from paziente.model.model_paziente import Paziente


class TestPaziente(TestCase):
    def test_controllo_credenziali_paziente(self):
        email = 'alfredo.sansovini@finta.com'
        password = 'alfredoS90.'

        data_di_nascita = datetime.date(1990, 5, 14)
        paziente = Paziente('p0000', 'Alfredo', 'Sansovini', data_di_nascita, 35, 'M', 'Foggia', 'Lucera',
                            'SNSLRD90E14D643Y', 'alfredo.sansovini@finta.com', 'alfredoS90.')

        self.assertTrue(paziente.controllo_credenziali_paziente(email, password))

    def test_controllo_sicurezza_password(self):
        password = 'alfredoS90.'
        self.assertTrue(Paziente.controllo_sicurezza_password(password))
