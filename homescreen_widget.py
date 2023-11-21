from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from navigation import Navigation

class HomescreenWidget(QWidget):

    navigation: Navigation

    def __init__(self, navigation: Navigation, *args, **kwargs):
        """
        Initialize the homescreen widget. Call __init__() for the superclass
        and bind all buttons.

        Params:
        navigation (Navigation): Navigation to use
        """
        super().__init__(*args, **kwargs)
        uic.loadUi('homescreenWidget.ui', self)
        self.navigation = navigation

        # Bind buttons
        self.light1Button.clicked.connect(lambda: self.navigation.switch_to_page_alias("control"))
        