from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QEvent
from PyQt6 import uic
from navigation import Navigation

import subprocess

class DimScreen(QWidget):
    
    control_screen: QWidget
    screen_select: Navigation

    def __init__(self, screen_select: Navigation, *args, **kwargs):
        """
        Initialize the dim screen

        Params:
        control_screen_i (int): Index of control screen in screen navigation
        """
        super().__init__(*args, **kwargs)

        self.screen_select = screen_select

        # Load UI elements
        uic.loadUi('dim_screen.ui', self)

    def set_control_screen(self, control_screen: QWidget):
        """
        Set the control screen. This must be called after init and before 
        using this screen.
        """
        self.control_screen = control_screen
        self.set_screen_wake()

    def set_screen_dim(self):
        """
        Dim the screen
        """
        print("Dim screen")
        # Switch to dim screen
        self.screen_select.switch_to_page_widget(self)
        # Set display brightness
        subprocess.run(["ddcutil", "setvcp", "10", "0", "--bus", "21"])


    def set_screen_wake(self):
        """
        Wake the screen
        """
        print("Wake screen")
        # Set display brightness
        subprocess.run(["ddcutil", "setvcp", "10", "30", "--bus", "21"])

        # Switch to control screen
        self.screen_select.switch_to_page_widget(self.control_screen)

    def event(self, event):
        # Check if the screen was touched
        if event.type() == QEvent.Type.MouseButtonRelease:
            self.set_screen_wake()

        return super().event(event)