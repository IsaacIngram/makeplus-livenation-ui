from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

from main_widget import MainWidget
from navigation import Navigation

class MainWindow(QMainWindow):

    navigation: Navigation

    def __init__(self):
        super().__init__()
        # Load UI file
        uic.loadUi('mainWindow.ui', self)

        main_widget = MainWidget()
        self.setCentralWidget(main_widget)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()