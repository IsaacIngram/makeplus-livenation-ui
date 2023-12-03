from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from tab_bar import TabBar
from control_widget import ControlWidget
from navigation import Navigation

class ControlScreen(QWidget):

    tab_bar: TabBar
    control_select: Navigation

    def __init__(self, screen_navigation: Navigation, *args, **kwargs):
        """
        Initialize the ControlScreen. 

        Params:
        screen_navigation (Navigation): Navigation controlling the main three
        screens (control screen, settings screen, and dim screen)
        """
        super().__init__(*args, **kwargs)
        uic.loadUi('control_screen.ui', self)
    
        self.tab_bar = TabBar(self.tabBar, self.stackedWidget)
        self.add_skylight(0, "All")
        self.add_skylight(1, "Skylight 1")


        # Create a bunch of control widgets, add them to the tab bar

    def add_skylight(self, id, name):
        """
        Add a skylight to be controlled
        """
        new_skylight: ControlWidget = ControlWidget(id)
        self.tab_bar.add_tab(new_skylight, name)

    def clear_skylights(self):
        """
        Remove all skylights
        """
        #TODO implement
        