import typing
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QSlider, QStyleOptionSlider, QStyle, QWidget, QVBoxLayout
from PyQt6.QtGui import QPainter, QPixmap
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtCore import Qt, QRectF, QSize

handle_path = 'images/slider/handle.svg'
track_path = 'images/slider/slider.svg'
slider_max: int = 100
slider_min: int = 0

class SvgSlider(QSlider):

    track_svg_renderer: QSvgRenderer
    handle_svg_renderer: QSvgRenderer
    temp_value: int

    def __init__(self, default_value: int = 0, parent=None):
        super().__init__(parent)

        self.setMinimum(0)
        self.setMaximum(100)

        self.track_svg_renderer = QSvgRenderer(track_path)
        self.handle_svg_renderer = QSvgRenderer(handle_path)

        self.temp_value = default_value

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw track
        track_rect = QRectF(0, self.height() / 2 - 2, self.width(), 30)
        self.track_svg_renderer.render(painter, track_rect)
        
        handle_rect = QRectF((self.temp_value/100) * self.width() - 8, self.height() / 2 -8, 16, 16)
        self.handle_svg_renderer.render(painter, handle_rect)

    def sizeHint(self):
        return QSize(600, 90)  # Set a reasonable default size
    
    def mousePressEvent(self, event):
        """
        Called when the mouse is clicked. Updates handle position but not the
        slider value.
        """
        # Calculate position
        self.temp_value = round((event.pos().x() / self.width()) * 100)
        # Normalize between bounds
        if self.temp_value > slider_max:
            self.temp_value = slider_max
        elif self.temp_value < slider_min:
            self.temp_value = slider_min
        self.update()
        
    def mouseMoveEvent(self, event):
        """
        Called when mouse is clicked and moved. Updates handle position but
        not the slider value.
        """
        # Calulcate position
        self.temp_value = round((event.pos().x() / self.width()) * 100)
        # Normalize between bounds
        if self.temp_value > slider_max:
            self.temp_value = slider_max
        elif self.temp_value < slider_min:
            self.temp_value = slider_min 
        self.update()

    def mouseReleaseEvent(self, event):
        """
        Called when mouse is released. Updates handle position and slider value
        """
        # Calculate position
        self.temp_value = round((event.pos().x() / self.width()) * 100)
        # Normalize between bounds
        if self.temp_value > slider_max:
            self.temp_value = slider_max
        elif self.temp_value < slider_min:
            self.temp_value = slider_min
        # Set values
        self.setValue(self.temp_value)
        self.update()
        print(self.temp_value)

if __name__ == '__main__':
    app = QApplication([])

    window = QWidget()
    layout = QVBoxLayout(window)
    slider = SvgSlider()
    layout.addWidget(slider)
    window.show()

    app.exec()