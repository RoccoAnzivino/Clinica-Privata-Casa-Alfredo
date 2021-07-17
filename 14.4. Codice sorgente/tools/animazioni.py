from PyQt5 import QtWidgets, QtCore


class Animazioni:

    def __init__(self):
        """
        Costruttore della classe Animazioni, la quale aggiunge a diversi elementi della Graphic User Interface (GUI)
        l'animazione opportuna
        """
        self.animazione_fade_in_totale = QtCore.QParallelAnimationGroup()
        self.animazione_fade_out_totale = QtCore.QParallelAnimationGroup()
        self.animazione_slide_totale = QtCore.QParallelAnimationGroup()
        self.animazione_slide_reverse_totale = QtCore.QParallelAnimationGroup()

    def animazione_fade_in(self, widget):
        """
        Funzione che aggiunge agli elementi specificati l'animazione 'fade in'

        :param widget: Parametro che rappresenta tutti quegli elementi che utilizzano l'animazione specificata dalla
                        funzione, tra i quali QPushButton, QLineEdit e QLabel
        :type widget: QWidget
        """
        effect = QtWidgets.QGraphicsOpacityEffect()
        widget.setGraphicsEffect(effect)

        animatione = QtCore.QPropertyAnimation(effect, b"opacity", widget)
        animatione.setDuration(300)
        animatione.setStartValue(0)
        animatione.setEndValue(1)
        self.animazione_fade_in_totale.addAnimation(animatione)

    def animazione_fade_out(self, widget):
        """
        Funzione che aggiunge agli elementi specificati l'animazione 'fade out'

        :param widget: Parametro che rappresenta tutti quegli elementi che utilizzano l'animazione specificata dalla
                        funzione, tra i quali QPushButton, QLineEdit e QLabel
        :type widget: QWidget
        """
        effect = QtWidgets.QGraphicsOpacityEffect()
        widget.setGraphicsEffect(effect)

        animatione = QtCore.QPropertyAnimation(effect, b"opacity", widget)
        animatione.setDuration(150)
        animatione.setStartValue(1)
        animatione.setEndValue(0)
        self.animazione_fade_out_totale.addAnimation(animatione)

    def animazione_slide(self, widget):
        """
        Funzione che aggiunge agli elementi specificati l'animazione 'slide'

        :param widget: Parametro che rappresenta tutti quegli elementi che utilizzano l'animazione specificata dalla
                        funzione, ovvero gli elementi delle home (paziente e personale medico)
        :type widget: QLabel
        """
        x = widget.pos().x()
        y = widget.pos().y()

        animazione = QtCore.QPropertyAnimation(widget, b'pos')
        animazione.setDuration(150)
        animazione.setStartValue(QtCore.QPoint(x, y))
        animazione.setEndValue(QtCore.QPoint(x - 215, y))
        self.animazione_slide_totale.addAnimation(animazione)

    def animazione_slide_reverse(self, widget):
        """
        Funzione che aggiunge agli elementi specificati l'animazione 'slide reverse'

        :param widget: Parametro che rappresenta tutti quegli elementi che utilizzano l'animazione specificata dalla
                        funzione, ovvero gli elementi delle home (paziente e personale medico)
        :type widget: QLabel
        """
        x = widget.pos().x()
        y = widget.pos().y()

        animazione = QtCore.QPropertyAnimation(widget, b'pos')
        animazione.setDuration(150)
        animazione.setStartValue(QtCore.QPoint(x, y))
        animazione.setEndValue(QtCore.QPoint(x + 215, y))
        self.animazione_slide_reverse_totale.addAnimation(animazione)
