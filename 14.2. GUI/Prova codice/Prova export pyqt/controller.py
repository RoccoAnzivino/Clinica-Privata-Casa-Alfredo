import login_paziente
import schermata_utente


def go_vista_schermata_iniziale(paziente):
    utente = schermata_utente.Ui_schermataIniziale()
    utente.show()
    paziente.hide()


def go_vista_login_paziente(utente):
    paziente = login_paziente.Ui_loginPaziente()
    paziente.show()
    utente.hide()