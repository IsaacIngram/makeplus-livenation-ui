from PyQt6 import uic

from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtSvgWidgets import QSvgWidget
from switch_widget import SwitchWidget
import xml.etree.ElementTree as ET

class ControlWidget(QWidget):

    id: int
    switch_widget: SwitchWidget

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

        # Create switch
        self.switch_widget = SwitchWidget('images/switch-icon.svg', self.blackoutSwitch, self)
        self.switch_widget.clicked.connect(self.handle_svg_click)

        self.show()

    def handle_svg_click(self):
        self.switch_widget.checkbox.setChecked(not self.switch_widget.checkbox.isChecked())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = ControlWidget(0)
    w.show()
    sys.exit(app.exec())