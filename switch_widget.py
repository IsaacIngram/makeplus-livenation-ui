import typing
from PyQt6 import QtGui
from PyQt6.QtWidgets import QWidget, QCheckBox, QVBoxLayout
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, pyqtSignal


class SwitchWidget(QWidget):
    
    clicked = pyqtSignal()
    svg_widget: QSvgWidget
    switch: QCheckBox

    def __init__(self, svg_path, parent=None):
        super().__init__(parent)

        # Load SVG image
        self.svg_widget = QSvgWidget(self)
        self.svg_widget.load(svg_path)

        # Create switch
        self.switch = QCheckBox(self)
        self.switch.stateChanged.connect(self.on_state_changed)

        self.switch.hide()

        layout = QVBoxLayout(self)
        layout.addWidget(self.svg_widget, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.switch, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addStretch()


    def on_state_changed(self, state):
        """
        Callback function for when the switch state is changed
        """
        print("Switch clicked")
        self.update()

    def mousePressEvent(self, event):
        # Emit the signal when the svg is clicked
        if self.svg_widget.geometry().contains(event.pos()):
            self.clicked.emit()

    def paintEvent(self, event):
        painter = QPainter(self)

        # Draw the SVG image as the background
        self.svg_widget.render(painter)

        # Draw a circle based on the switch state
        if self.switch.isEnabled():
            painter.setBrush(QColor(255, 0, 0))
            painter.drawEllipse(100, 100, 20, 20)
        else:
            painter.setBrush(QColor(255, 0, 0))
            painter.drawEllipse(150, 150, 20, 20)