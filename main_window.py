from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

from light_control_widget import LightControlWidget
from homescreen_widget import HomescreenWidget
from navigation import Navigation

class MainWindow(QMainWindow):

    navigation: Navigation

    def __init__(self):
        super().__init__()
        # Load UI file
        uic.loadUi('mainWindow.ui', self)

        # Create navigation with stacked widget
        self.navigation = Navigation(self.mainWidget)

        # Create homescreen widget
        homescreen_widget = HomescreenWidget(self.navigation)
        self.navigation.add_page(homescreen_widget, "homescreen")

        # Create light control widget
        light_control_widget = LightControlWidget(self.navigation)
        self.navigation.add_page(light_control_widget, "control")


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()