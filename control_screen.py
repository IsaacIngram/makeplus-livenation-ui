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

        # Create tab bar
        self.tab_bar = TabBar(self.tabBar, self.stackedWidget)

        # Apply shadow effect to the right and bottom edges
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(50)
        shadow_effect.setColor(QColor(75, 75, 75, 80))
        shadow_effect.setOffset(15, 15)
        self.stackedWidget.setGraphicsEffect(shadow_effect)

        self.add_skylight(0, dim_screen, settings_screen, "All")
        self.add_skylight(1, dim_screen, settings_screen, "Skylight 1")
        self.add_skylight(2, dim_screen, settings_screen, "Skylight 2")
        self.add_skylight(3, dim_screen, settings_screen, "Skylight 3")
        self.add_skylight(4, dim_screen, settings_screen, "Skylight 4")
        self.add_skylight(5, dim_screen, settings_screen, "Skylight 5")

    def add_skylight(self, id, dim_screen, settings_screen, name):
        """
        Add a skylight to be controlled
        """
        new_skylight: ControlWidget = ControlWidget(id, dim_screen, settings_screen)
        self.tab_bar.add_tab(id, new_skylight, name)
        model.add_skylight(name, 0, 0)

    def clear_skylights(self):
        """
        Remove all skylights
        """
        #TODO implement
        pass

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
        