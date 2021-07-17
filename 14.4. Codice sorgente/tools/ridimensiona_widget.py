from PyQt5.QtCore import QSize, QRect
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton


def ridimensiona_view(widget):
    """
    Funzione che stabilisce una dimensione unitaria per tutte le view del software, andando a ridimensionare la
    dimensione stessa della view e, di conseguenza, quella di tutti gli oggetti al suo interno

    :param widget: Parametro che rappresenta tutte le view del software nelle quali è necessario il ridimensionamento
    :type widget: QWidget
    """
    screen = widget.screen()

    width = widget.width()
    height = widget.height()

    x = screen.availableGeometry().width()
    y = screen.availableGeometry().height()

    # print(x, y)

    rapporto_x = x / 1920
    rapporto_y = y / 1080

    widget.setMinimumSize(QSize(width * rapporto_x, height * rapporto_y))
    widget.setMaximumSize(QSize(width * rapporto_x, height * rapporto_y))

    for oggetto in widget.__dict__.values():
        if isinstance(oggetto, QWidget):
            x_oggetto = oggetto.pos().x() * rapporto_x
            y_oggetto = oggetto.pos().y() * rapporto_y
            larghezza_oggetto = oggetto.width() * rapporto_x
            altezza_oggetto = oggetto.height() * rapporto_y

            oggetto.setGeometry(QRect(x_oggetto, y_oggetto, larghezza_oggetto, altezza_oggetto))

        if isinstance(oggetto, QLabel) or isinstance(oggetto, QPushButton) or isinstance(oggetto, QLineEdit):
            font = oggetto.font()
            # print(font.pixelSize(), font.pixelSize() * ((rapporto_x + rapporto_y) / 2))
            font.setPixelSize(font.pixelSize() * ((rapporto_x + rapporto_y) / 2))
            oggetto.setFont(font)
            # print(font.pixelSize(), rapporto_x, rapporto_y, (rapporto_x + rapporto_y) / 2)
            # print(oggetto.text(), '\n')

    if hasattr(widget, 'menu_a_tendina'):
        for attr, valore in zip(widget.menu_a_tendina.__dict__.keys(), widget.menu_a_tendina.__dict__.values()):
            if isinstance(valore, QWidget):
                x_oggetto = valore.pos().x() * rapporto_x
                y_oggetto = valore.pos().y() * rapporto_y
                larghezza_oggetto = valore.width() * rapporto_x
                altezza_oggetto = valore.height() * rapporto_y

                valore.setGeometry(QRect(x_oggetto, y_oggetto, larghezza_oggetto, altezza_oggetto))

                if attr == 'tendina_button':
                    widget.menu_a_tendina.tendina_button.setIconSize(QSize(larghezza_oggetto, altezza_oggetto))

                if attr == 'tendina_aperta_button':
                    widget.menu_a_tendina.tendina_aperta_button.setIconSize(QSize(larghezza_oggetto, altezza_oggetto))

            if isinstance(valore, QLabel) or isinstance(valore, QPushButton) or isinstance(valore, QLineEdit):
                font = valore.font()
                # print(font.pixelSize(), font.pixelSize() * ((rapporto_x + rapporto_y) / 2))
                font.setPixelSize(font.pixelSize() * ((rapporto_x + rapporto_y) / 2) + 1)
                valore.setFont(font)
                # print(font.pixelSize(), rapporto_x, rapporto_y, (rapporto_x + rapporto_y) / 2)
                # print(valore.text(), '\n')


def ridimensiona_tool(tool):
    """
    Funzione che stabilisce una dimensione unitaria per tutti i tool del software, andando a ridimensionare la
    dimensione degli oggetti dei tool per i quali è prevista la GUI

    :param tool: Parametro che rappresenta tutti i tool del software nelle quali è necessario il ridimensionamento
    :type tool:  ToolCartellaClinicaPaziente, LabelPrenotazioni, ToolPazientiDaModificare, ToolPazientiModificati,
                 ToolPrenotazioniPersonaleMedico, PulsantePrenotazioni
    """
    screen = tool.widget.screen()

    x = screen.availableGeometry().width()
    y = screen.availableGeometry().height()

    # print(x, y)

    rapporto_x = x / 1920
    rapporto_y = y / 1080

    for oggetto in tool.__dict__.values():
        if isinstance(oggetto, QWidget) and not isinstance(oggetto, type(tool.widget)):
            x_oggetto = oggetto.pos().x() * rapporto_x
            y_oggetto = oggetto.pos().y() * rapporto_y
            larghezza_oggetto = oggetto.width() * rapporto_x
            altezza_oggetto = oggetto.height() * rapporto_y

            oggetto.setGeometry(QRect(x_oggetto, y_oggetto, larghezza_oggetto, altezza_oggetto))

        if isinstance(oggetto, QLabel) or isinstance(oggetto, QPushButton):
            font = oggetto.font()
            font.setPixelSize(font.pixelSize() * ((rapporto_x + rapporto_y) / 2) + 1)
            oggetto.setFont(font)


def ridimensiona_singolo_oggetto(widget, oggetto):
    """
    Funzione utile al ridimensionamento dei singoli oggetti in relazione alle dimensioni della view o del tool nei quali
    sono inseriti

    :param widget: Corrisponde alla view o al tool nei quali è presente l'oggetto da ridimensionare
    :type widget: QWidget
    :param oggetto: Parametro che rappresenta l'oggetto da ridimensionare
    :type oggetto: QWidget
    """
    screen = widget.screen()

    x = screen.availableGeometry().width()
    y = screen.availableGeometry().height()

    # print(x, y)

    rapporto_x = x / 1920
    rapporto_y = y / 1080

    x_oggetto = oggetto.pos().x() * rapporto_x
    y_oggetto = oggetto.pos().y() * rapporto_y
    larghezza_oggetto = oggetto.width() * rapporto_x
    altezza_oggetto = oggetto.height() * rapporto_y

    oggetto.setGeometry(QRect(x_oggetto, y_oggetto, larghezza_oggetto, altezza_oggetto))

    if isinstance(oggetto, QLabel) or isinstance(oggetto, QPushButton):
        font = oggetto.font()
        font.setPixelSize(font.pixelSize() * ((rapporto_x + rapporto_y) / 2) + 1)
        oggetto.setFont(font)
