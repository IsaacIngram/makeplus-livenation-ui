from PyQt6 import uic
from PyQt6.QtWidgets import QStackedWidget
from navigation import Navigation
from control_screen import ControlScreen

from dim_screen import DimScreen

class MainWidget(QStackedWidget):

    screen_select: Navigation

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Load UI
        uic.loadUi('mainWindow.ui', self)

        # Create navigation
        self.screen_select = Navigation(self)

        # Add pages to navigation
        dim_screen = DimScreen(self.screen_select)
        control_screen = ControlScreen(self.screen_select, dim_screen)
        dim_screen.set_control_screen(control_screen)
        self.screen_select.add_page(control_screen)
        self.screen_select.add_page(dim_screen)
        self.screen_select.switch_to_page(0)

