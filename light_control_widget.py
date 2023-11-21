from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from control_api import light_control

class LightControlWidget(QWidget):

    light_id: int

    def __init__(self, *args, **kwargs):
        self.light_id = 1
        """
        Initialize the light control widget. Call __init__() for the
        superclass and bind all buttons and all dynamic text elements.
        """
        super().__init__(*args, **kwargs)
        uic.loadUi("lightControlWidget.ui", self)

        # Bind all buttons
        self.openDiffuse.clicked.connect(self.open_diffuse_callback)
        self.closeDiffuse.clicked.connect(self.close_diffuse_callback)
        self.openBlackout.clicked.connect(self.open_blackout_callback)
        self.closeBlackout.clicked.connect(self.close_blackout_callback)
        self.slideDiffuse.valueChanged.connect(self.diffuse_changed_callback)
        self.slideBlackout.valueChanged.connect(self.blackout_changed_callback)

    def open_diffuse_callback(self):
        """
        Callback for diffuse open button
        """
        self.slideDiffuse.setValue(0)

    def close_diffuse_callback(self):
        """
        Callback for diffuse close button
        """
        self.slideDiffuse.setValue(100)

    def open_blackout_callback(self):
        """
        Callback for blackout open button
        """
        self.slideBlackout.setValue(0)

    def close_blackout_callback(self):
        """
        Callback for blackout close button
        """
        self.slideBlackout.setValue(100)

    def diffuse_changed_callback(self, value: int):
        """
        Callback for when the diffuse slider is changed

        Params:
        value (int): Value to set the diffuse to (0 - 100)
        """
        light_control.set_diffuse(self.light_id, value)

    def blackout_changed_callback(self, value: int):
        """
        Callback for when the blackout slider is changed

        Params:
        value (int): Value to set the blackout to (0 - 100)
        """
        light_control.set_blackout(self.light_id, value)


