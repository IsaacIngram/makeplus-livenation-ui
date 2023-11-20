import sys

from PyQt6 import QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("lightControlWindow.ui", self)

        self.openDiffuse.clicked.connect(self.open_diffuse_callback)
        self.closeDiffuse.clicked.connect(self.close_diffuse_callback)
        self.openBlackout.clicked.connect(self.open_blackout_callback)
        self.closeBlackout.clicked.connect(self.close_blackout_callback)
        self.slideDiffuse.valueChanged.connect(self.diffuse_changed_callback)
        self.slideBlackout.valueChanged.connect(self.blackout_changed_callback)

    def open_diffuse_callback(self):
        set_diffuse(0)

    def close_diffuse_callback(self):
        set_diffuse(100)

    def open_blackout_callback(self):
        set_blackout(0)

    def close_blackout_callback(self):
        set_blackout(100)

    def diffuse_changed_callback(self, value):
        set_diffuse(value)

    def blackout_changed_callback(self, value):
        set_blackout(value)


def set_blackout(value):
    print("Set blackout to: %s" % str(value))

def set_diffuse(value):
    print("Set diffuse to %s" % str(value))

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()