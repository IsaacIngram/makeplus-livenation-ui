import typing
from PyQt6 import QtGui
from PyQt6.QtWidgets import QWidget, QCheckBox, QVBoxLayout
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt, pyqtSignal


class SwitchWidget(QWidget):
    
    clicked = pyqtSignal()
    svg_widget: QSvgWidget
    checkbox: QCheckBox
    original_x: int
    original_y: int

    def __init__(self, svg_path, checkbox: QCheckBox, parent=None):
        super().__init__(parent)

        # Load SVG image
        self.svg_widget = QSvgWidget(self)
        self.svg_widget.load(svg_path)

        # Create switch
        self.checkbox = checkbox
        self.checkbox.stateChanged.connect(self.on_state_changed)

        self.checkbox.hide()

        layout = QVBoxLayout(self)
        layout.addWidget(self.svg_widget, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.checkbox, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addStretch()

        self.original_x = self.checkbox.pos().x()
        self.original_y = self.checkbox.pos().y()

        self.setGeometry(self.original_x, self.original_y, 174, 133)

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

        #TODO remove temporary border drawing
        border_pen = QPen(QColor(255, 0, 0), 2)
        painter.setPen(border_pen)
        painter.drawRect(self.svg_widget.geometry())
        #END border drawing

        # Draw the SVG image as the background
        self.svg_widget.render(painter)

        # Draw a circle based on the switch state
        if self.checkbox.isEnabled():
            painter.setBrush(QColor(255, 0, 0))
            painter.drawEllipse(100, 100, 20, 20)
        else:
            painter.setBrush(QColor(255, 0, 0))
            painter.drawEllipse(100, 100, 20, 20)