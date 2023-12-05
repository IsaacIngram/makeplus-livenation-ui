from PyQt6 import uic

from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtSvgWidgets import QSvgWidget
from switch_widget import SwitchWidget
import xml.etree.ElementTree as ET

def get_svg_dimensions(file_path):
    try:
        # Parse the SVG file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Extract width and height attributes from the root <svg> element
        width = root.get('width')
        height = root.get('height')

        return width, height

    except Exception as e:
        print(f"Error: {e}")
        return None, None

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
        print(get_svg_dimensions('images/switch-icon.svg'))
        self.switch_widget = SwitchWidget('images/switch-icon.svg', self)
        self.switch_widget.setGeometry(100, 100, 174, 133)
        self.switch_widget.clicked.connect(self.handle_svg_click)

        self.show()

    def handle_svg_click(self):
        self.switch_widget.switch.setChecked(not self.switch_widget.switch.isChecked())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = ControlWidget(0)
    w.show()
    sys.exit(app.exec())