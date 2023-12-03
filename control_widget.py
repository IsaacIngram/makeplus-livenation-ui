from PyQt6 import uic

from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QApplication
from PyQt6.QtGui import QColor
from switch import Switch

class ControlWidget(QWidget):

    id: int

    def __init__(self, skylight_id: int, *args, **kwargs):
        """
        Create a new control widget

        Params:
        skylight_id (int): The id of the skylight to control
        """
        super().__init__(*args, **kwargs)

        # Load ui
        uic.loadUi('control_widget.ui', self)
        
        # Set local variables
        self.id = skylight_id

        print(self.styleSheet())

        self.show()

        # Create switch
        # test_switch = Switch()
        # test_switch.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = ControlWidget(0)
    w.show()
    sys.exit(app.exec())