from PyQt6.QtWidgets import QPushButton, QWidget, QVBoxLayout
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt

class SvgButtonWidget(QWidget):

    svg_widget: QSvgWidget
    button: QPushButton
    original_x: int
    original_y: int
    width: int
    height: int

    def __init__(self, svg_path, button: QPushButton, width: int, height: int, parent=None):
        super().__init__(parent)

        self.width = width
        self.height = height

        # Load SVG image
        self.svg_widget = QSvgWidget(self)
        self.svg_widget.load(svg_path)

        # Create button
        self.button = button
        self.button.clicked.connect(self.on_click)

        self.button.hide()

        layout = QVBoxLayout(self)
        layout.addWidget(self.svg_widget, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addStretch()

        self.original_x = self.button.pos().x()
        self.original_y = self.button.pos().y()

        self.setGeometry(self.original_x, self.original_y, self.width, self.height)

    def on_click():
        #TODO add callback function. Probably lambda passed in via constructor
        print("Button clicked")

    def paintEvent(self, event):
        painter = QPainter(self)

        #TODO remove temporary border drawing
        border_pen = QPen(QColor(255, 0, 0), 2)
        painter.setPen(border_pen)
        painter.drawRect(self.svg_widget.geometry())
        #END border drawing

        # Draw the SVG image as the background
        self.svg_widget.render(painter)
