from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QApplication, QStackedWidget, QVBoxLayout
from PyQt6.QtGui import QColor

from tab_bar import TabBar
from control_widget import ControlWidget
from navigation import Navigation
from dim_screen import DimScreen
from settings_screen import SettingsScreen
import model

class ControlScreen(QWidget):

    tab_bar: TabBar
    screen_select: Navigation
    dim_screen: QWidget
    settings_screen: QWidget
    control_select: Navigation

    def __init__(self, screen_navigation: Navigation, dim_screen: DimScreen, settings_screen: SettingsScreen, *args, **kwargs):
        """
        Initialize the ControlScreen. 

        Params:
        screen_navigation (Navigation): Navigation controlling the main three
        screens (control screen, settings screen, and dim screen)
        """
        super().__init__(*args, **kwargs)
        # Load UI elements
        uic.loadUi('control_screen.ui', self)

        self.screen_select = screen_navigation
        self.dim_screen = dim_screen
        self.settings_screen = settings_screen

        # Create tab bar
        self.tab_bar = TabBar(self.tabBar, self.stackedWidget)

        # Apply shadow effect to the right and bottom edges
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(50)
        shadow_effect.setColor(QColor(75, 75, 75, 80))
        shadow_effect.setOffset(15, 15)
        self.stackedWidget.setGraphicsEffect(shadow_effect)

        model.model._ui_add_skylight_signal.connect(self.add_skylight)

    def add_skylight(self, id, name, skylight_model: model.Skylight):
        """
        Add a skylight to be controlled

        Params:
        id (int): Skylight id
        name (str): Skylight name
        skylight_model: Skylight object from the model. Used to set callback functions
        """
        # Add new skylight to model
        skylight_page: ControlWidget = ControlWidget(id, self.dim_screen, self.settings_screen)
        skylight_model.set_connected_func(skylight_page.hide_connection_indicator)
        skylight_model.set_not_connected_func(skylight_page.show_connection_indicator)
        self.tab_bar.add_tab(id, skylight_page, name)

    def switch_to(self):
        """
        Switch to the control screen (this screen)
        """
        self.screen_select.switch_to_page_widget(self)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    test = QStackedWidget()
    test_nav = Navigation(test)
    w = ControlScreen(test_nav)
    w.show()
    sys.exit(app.exec())
        