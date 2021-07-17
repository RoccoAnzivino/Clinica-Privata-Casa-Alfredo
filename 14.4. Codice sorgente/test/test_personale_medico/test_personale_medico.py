import datetime
from unittest import TestCase

from personale_medico.model.model_personale_medico import PersonaleMedico


class TestPersonaleMedico(TestCase):
    def test_controllo_credenziali_personale_medico(self):
        codice_identificativo = 'CCAMGCpm0001'
        password = 'SonoUnMedicoEvvai0.'

        data_di_nascita = datetime.date(1970, 12, 12)
        personale_medico = PersonaleMedico('pm0000', 'Mario', 'Rossi', data_di_nascita, 50, 'M', 'Pescara', 'Popoli',
                                           'RSSMRA70T12G878Q', 'Medicina Generale Cardiologica',
                                           'mario.rossi@casa.alfredo.com', 'CCAMGCpm0001', 'SonoUnMedicoEvvai0.')

        self.assertTrue(personale_medico.controllo_credenziali_personale_medico(codice_identificativo, password))

    def test_controllo_sicurezza_password(self):
        password = 'SonoUnMedicoEvvai0.'
        self.assertTrue(PersonaleMedico.controllo_sicurezza_password(password))
