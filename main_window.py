from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

from light_control_widget import LightControlWidget
from homescreen_widget import HomescreenWidget

class MainWindow(QMainWindow):

    # Create all widgets used in stacked widget
    light_control_widget: LightControlWidget
    homescreen_widget: HomescreenWidget

    def __init__(self):
        super().__init__()
        # Load UI file
        uic.loadUi('mainWindow.ui', self)
        # Add homescreen widget
        self.homescreen_widget = HomescreenWidget()
        self.mainWidget.addWidget(self.homescreen_widget)

        # Add light control widget
        self.light_control_widget = LightControlWidget()
        self.mainWidget.addWidget(self.light_control_widget)

        # Set callback functions
        self.homescreen_widget.skylight1Button.clicked.connect(self.go_to_control)
        self.light_control_widget.backButton.clicked.connect(self.go_home)

    def go_home(self):
        self.mainWidget.setCurrentIndex(0)

    def go_to_control(self):
        self.mainWidget.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()