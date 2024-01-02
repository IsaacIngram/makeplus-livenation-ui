import typing
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QSlider, QStyleOptionSlider, QStyle, QWidget, QVBoxLayout
from PyQt6.QtGui import QPainter, QPixmap
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtCore import Qt, QRectF, QSize

from typing import Callable

handle_path = 'images/slider/handle.svg'
track_path = 'images/slider/slider.svg'
slider_max_val: int = 100
slider_min_val: int = 0

class SvgSlider(QSlider):

    track_svg_renderer: QSvgRenderer
    handle_svg_renderer: QSvgRenderer
    temp_value: int
    adj_width: int
    left_pad: int = 5
    right_pad: int = 21
    value_update_callback: Callable[[], None]

    def __init__(self, slider: QSlider = None, default_value: int = 0, value_update_callback: Callable[[int], None] = None, parent=None):
        """
        Created new SVG Slider

        Params:
        slider (QSlider): Optional slider to get geometric data from
        default_value (int): Optional starting value for this slider
        value_update_callback (Callable[[ControlWidget, int], None]): Optional callback 
        function for when the value of this slider is updated. Must have a controlwidget
        to modify and an integer value as the parameters.
        parent: Optional parent of this widget
        """
        super().__init__(parent)

        if slider is not None:
            pos_x = slider.pos().x()
            pos_y = slider.pos().y()
            width = slider.width()
            height = slider.height()
            slider.hide()
        else:
            pos_x = 0
            pos_y = 0
            width = 280
            height = 100
            
        self.setMinimum(slider_min_val)
        self.setMaximum(slider_max_val)

        self.track_svg_renderer = QSvgRenderer(track_path)
        self.handle_svg_renderer = QSvgRenderer(handle_path)
        
        self.value_update_callback = value_update_callback

        self.temp_value = default_value
        self.setGeometry(pos_x, pos_y, width + 10, height)
        self.adj_width = self.width() - (self.left_pad + self.right_pad)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw track
        track_rect = QRectF(0, self.height() / 2 - 2, self.width(), 16)
        self.track_svg_renderer.render(painter, track_rect)
        
        # Draw handle
        handle_rect = QRectF(self.left_pad + ((self.temp_value/100) * self.adj_width) - 8, self.height() / 2 - 14, 32, 40)
        self.handle_svg_renderer.render(painter, handle_rect)

    def sizeHint(self):
        return QSize(600, 90)  # Set a reasonable default size
    
    def _normalize_pos(self, pos: int) -> int:
        """
        Normalize the mouse position

        Params:
        pos (int): Position of the mouse on the X axis
        """
        normalized_val = round((pos / self.adj_width) * 100)

        # Check that it's between the normalized range specified
        if normalized_val > slider_max_val:
            normalized_val = slider_max_val
        elif normalized_val < slider_min_val:
            normalized_val = slider_min_val

        return normalized_val
        
    
    def mousePressEvent(self, event):
        """
        Called when the mouse is clicked. Updates handle position but not the
        slider value.
        """
        # Calculate position
        self.temp_value = self._normalize_pos(event.pos().x())
        self.update()
        
    def mouseMoveEvent(self, event):
        """
        Called when mouse is clicked and moved. Updates handle position but
        not the slider value.
        """
        # Calculate position
        self.temp_value = self._normalize_pos(event.pos().x())
        self.update()

    def mouseReleaseEvent(self, event):
        """
        Called when mouse is released. Updates handle position and slider value
        """
        # Calculate position
        self.temp_value = self._normalize_pos(event.pos().x())
        self.setValue(self.temp_value)
        self.update()
        self.on_value_changed(self.temp_value)

    def on_value_changed(self, new_value: int):
        """
        Call the value update callback function provided in the constructor
        if it exists.
        
        Params:
        new_value (int): New value to pass to the function
        """
        if self.value_update_callback is not None:
            self.value_update_callback(new_value)

if __name__ == '__main__':
    app = QApplication([])

    window = QWidget()
    layout = QVBoxLayout(window)
    slider = SvgSlider()
    layout.addWidget(slider)
    window.show()

    app.exec()