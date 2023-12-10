from PyQt6 import uic

from PyQt6.QtWidgets import QWidget, QApplication
from switch_widget import SwitchWidget, Position
from svg_button_widget import SvgButtonWidget
from svg_slider import SvgSlider
from dim_screen import DimScreen

class ControlWidget(QWidget):

    id: int
    dim_screen: DimScreen
    blackout_switch_widget: SwitchWidget
    filter_switch_widget: SwitchWidget

    def __init__(self, skylight_id: int, dim_screen: DimScreen, *args, **kwargs):
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
        self.dim_screen = dim_screen

        # Create switches
        self.blackout_switch_widget = SwitchWidget(Position.CLOSED, self.blackoutSwitch, self)
        self.filter_switch_widget = SwitchWidget(Position.CLOSED, self.filterSwitch, self)
        self.blackout_switch_widget.clicked.connect(self.blackout_switch_callback)
        self.filter_switch_widget.clicked.connect(self.filter_switch_callback)

        # Create buttons
        self.dim_button = SvgButtonWidget('images/dim-icon.svg', self.dimButton, 100, 100, self)
        self.settings_button = SvgButtonWidget('images/settings-icon.svg', self.settingsButton, 100, 100, self)
        self.dim_button.clicked.connect(self.dim_screen_callback)

        # Create sliders
        blackout_slider = SvgSlider(self.blackoutSlider, parent=self)
        filter_slider = SvgSlider(self.filterSlider, parent=self)

        self.show()

    def blackout_switch_callback(self):
        """
        Callback function for when the blackout switch is clicked
        """
        if self.blackout_switch_widget.checkbox.isChecked():
            # Uncheck
            self.blackout_switch_widget.checkbox.setChecked(False)
            print("Blackout switch unchecked")
        else:
            # Check
            self.blackout_switch_widget.checkbox.setChecked(True)
            print("Blackout switch checked")

    def filter_switch_callback(self):
        """
        Callback function for when the filter switch is clicked
        """
        if self.filter_switch_widget.checkbox.isChecked():
            # Uncheck
            self.filter_switch_widget.checkbox.setChecked(False)
            print("Filter switch unchecked")
        else:
            # Check
            self.filter_switch_widget.checkbox.setChecked(True)
            print("Filter switch checked")

    def dim_screen_callback(self):
        self.dim_screen.set_screen_dim()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = ControlWidget(0)
    w.show()
    sys.exit(app.exec())