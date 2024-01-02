from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor
from navigation import Navigation
from svg_button_widget import SvgButtonWidget
from PyQt6.QtCore import Qt

import model

class SettingsScreen(QWidget):

    screen_select: Navigation
    settings_select: Navigation

    def __init__(self, screen_select: Navigation, *args, **kwargs):
        """
        Initialize the settings screen
        """
        super().__init__(*args, **kwargs)
        # Load the UI elements
        uic.loadUi('settings_screen.ui', self)

        self.screen_select = screen_select
        self.settings_select = Navigation(self.settingsWidget)

        # Apply shadow effect to the right and bottom edges
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(50)
        shadow_effect.setColor(QColor(75, 75, 75, 80))
        shadow_effect.setOffset(15, 15)
        self.settingsWidget.setGraphicsEffect(shadow_effect)

        # Create buttons
        self.close_button = SvgButtonWidget('images/close-icon.svg', self.closeButton, 50, 50, self)
        self.pairButton.clicked.connect(self.pair_button_callback)
        self.clearButton.clicked.connect(self.clear_button_callback)

        # Bind buttons
        self.close_button.clicked.connect(lambda: self.control_screen.switch_to())
        self.cancelPairingButton.clicked.connect(self.cancel_pairing_callback)
        self.clearToPairButton.clicked.connect(self.pair_button_callback)
        self.exitClearButton.clicked.connect(self.exit_clear_callback)

        # Add listener for stacked widget being changed
        self.settingsWidget.currentChanged.connect(self.stacked_widget_change_callback)

    def set_control_screen(self, control_screen):
        """
        Set the control screen the X on the settings screen switches to
        """
        self.control_screen = control_screen

    def switch_to(self):
        """
        Switch to the settings screen (this screen)
        """
        self.screen_select.switch_to_page_widget(self)

    def stacked_widget_change_callback(self, index):
        """
        Callback function for when the stacked widget index is changed

        Params:
        index (int): Index switched to
        """
        if index == 0:
            self.close_button.show()
        else:
            self.close_button.hide()

    def pair_button_callback(self):
        """
        Callback for when pair button is pressed
        """
        self.settings_select.switch_to_page(1)
        model.enter_pairing_mode()
        #TODO implement model

    def clear_button_callback(self):
        """
        Callback for when clear button is pressed
        """
        self.settings_select.switch_to_page(2)
        #TODO implement model
        pass

    def cancel_pairing_callback(self):
        """
        Callback function for when the cancel button is pressed
        """
        self.settings_select.switch_to_page(0)
        model.enter_normal_mode()
        #TODO implement model

    def exit_clear_callback(self):
        """
        Callback function for when the exit button on the clear page is pressed
        """
        self.settings_select.switch_to_page(0)

