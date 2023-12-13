from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt

from main_widget import MainWidget
from navigation import Navigation

import platform

class MainWindow(QMainWindow):

    navigation: Navigation

    def __init__(self):
        super().__init__()
        # Load UI file
        uic.loadUi('mainWindow.ui', self)

        main_widget = MainWidget()
        self.setCentralWidget(main_widget)

        # Run frameless and fullscreen if on raspberry pi
        if platform.system() == "Linux" and "raspberry" in platform.uname().release:
            self.setWindowFlag(Qt.WindowType.Window, True)
            self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
            self.showFullScreen()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()