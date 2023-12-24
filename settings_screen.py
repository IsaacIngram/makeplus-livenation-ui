from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor
from navigation import Navigation
from svg_button_widget import SvgButtonWidget

class SettingsScreen(QWidget):

    screen_select: Navigation

    def __init__(self, screen_select: Navigation, *args, **kwargs):
        """
        Initialize the settings screen
        """
        super().__init__(*args, **kwargs)
        # Load the UI elements
        uic.loadUi('settings_screen.ui', self)

        self.screen_select = screen_select

        # Apply shadow effect to the right and bottom edges
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(50)
        shadow_effect.setColor(QColor(75, 75, 75, 80))
        shadow_effect.setOffset(15, 15)
        self.settingsWidget.setGraphicsEffect(shadow_effect)

        # Create buttons
        self.close_button = SvgButtonWidget('images/close-icon.svg', self.closeButton, 50, 50, self)
        self.close_button.clicked.connect(lambda: self.control_screen.switch_to())

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

