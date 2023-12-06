from PyQt6.QtWidgets import QWidget, QCheckBox, QVBoxLayout
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtGui import QPainter, QColor, QPen, QTransform
from PyQt6.QtCore import Qt, pyqtSignal, QPoint


class SwitchWidget(QWidget):
    
    clicked = pyqtSignal()
    main_svg: QSvgWidget
    indicator_svg: QSvgWidget
    checkbox: QCheckBox
    original_x: int
    original_y: int

    def __init__(self, main_svg_path: str, indicator_svg_path: str, checkbox: QCheckBox, parent=None):
        """
        Create new SwitchWidget

        Params:
        main_svg_path (str): Path to main SVG
        indicator_svg_path (str): Path to the indicator SVG
        checkbox (QCheckBox): QCheckBox this SwitchWidget is replacing
        parent: Parent widget
        """
        super().__init__(parent)

        # Load SVGs
        self.main_svg = QSvgWidget(self)
        self.main_svg.load(main_svg_path)
        self.indicator_svg = QSvgWidget(self)
        self.indicator_svg.load(indicator_svg_path)

        # Create switch
        self.checkbox = checkbox
        self.checkbox.stateChanged.connect(self.on_state_changed) # Connect to action
        self.checkbox.hide() # Hide because we replace with SVG

        # Lay out SVG
        layout = QVBoxLayout(self)
        layout.addWidget(self.main_svg, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.indicator_svg, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.checkbox, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addStretch()

        self.original_x = self.checkbox.pos().x()
        self.original_y = self.checkbox.pos().y()

        self.setGeometry(self.original_x, self.original_y, 300, 300)

    def on_state_changed(self, state):
        """
        Callback function for when the switch state is changed
        """
        print("Switch clicked")
        self.update()

    def mousePressEvent(self, event):
        # Emit the signal when the svg is clicked
        if self.main_svg.geometry().contains(event.pos()):
            self.clicked.emit()

    def paintEvent(self, event):
        painter = QPainter(self)
        
        #TODO remove temporary border drawing
        border_pen = QPen(QColor(255, 0, 0), 2)
        painter.setPen(border_pen)
        painter.drawRect(self.main_svg.geometry())
        #END border drawing

        # Draw the main SVG as the background
        self.main_svg.render(painter)

        # Draw the indicator SVG
        if self.checkbox.isChecked():
            # Switch to close/off
            indicator_pos = QPoint(self.original_x - 120, self.original_y - 166)
        else:
            # Switch to open/on
            indicator_pos = QPoint(self.original_x - 140, self.original_y - 166)
        
        self.indicator_svg.setGeometry(indicator_pos.x(), indicator_pos.y(), 37, 20)

        return