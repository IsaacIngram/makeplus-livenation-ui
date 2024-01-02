from PyQt6.QtWidgets import QWidget, QCheckBox, QVBoxLayout
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtGui import QPainter, QColor, QPen, QTransform
from PyQt6.QtCore import Qt, pyqtSignal, QPoint
from enum import Enum

class Position(Enum):
    OPEN = 1
    CLOSED = 2
    DISABLED_OPEN = 3
    DISABLED_CLOSED = 4

open_path = 'images/switch/open.svg'
closed_path = 'images/switch/closed.svg'
open_disabled_path = 'images/switch/open-disabled.svg'
closed_disabled_path = 'images/switch/closed-disabled.svg'

class SwitchWidget(QWidget):
    
    clicked = pyqtSignal()
    main_svg: QSvgWidget
    checkbox: QCheckBox
    disabled: bool

    def __init__(self, default_position: Position, checkbox: QCheckBox, parent=None):
        """
        Create new SwitchWidget

        Params:
        default_position (Position): The position to set the switch to by default
        checkbox (QCheckBox): QCheckBox this SwitchWidget is replacing
        parent: Parent widget
        """
        super().__init__(parent)

        # Load SVG based on provided default
        self.main_svg = QSvgWidget(self)
        if default_position == Position.OPEN:
            self.main_svg.load(open_path)
            self.disabled = False
        elif default_position == Position.CLOSED:
            self.main_svg.load(closed_path)
            self.disabled = False
        elif default_position == Position.DISABLED_OPEN:
            self.main_svg.load(open_disabled_path)
            self.disabled = True
        elif default_position == Position.DISABLED_CLOSED:
            self.main_svg.load(closed_disabled_path)
            self.disabled = True

        # Create switch
        self.checkbox = checkbox
        self.checkbox.stateChanged.connect(self.on_clicked) # Connect to action
        self.checkbox.hide() # Hide because we replace with SVG

        # Lay out SVG
        layout = QVBoxLayout(self)
        layout.addWidget(self.main_svg, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.checkbox, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addStretch()

        self.original_pos = self.checkbox.pos()

        print(f"original {self.original_pos.x()}, {self.original_pos.y()}")
        print(f"new {self.mapFromParent(self.original_pos).x()}, {self.mapFromParent(self.original_pos).y()}")


        self.setGeometry(
            self.mapFromParent(self.original_pos).x(), 
            self.mapFromParent(self.original_pos).y(),
            300, 300)

    def on_clicked(self, state):
        """
        Callback function for when the switch state is changed
        """
        self.disabled = False
        if self.checkbox.isChecked():
            self.main_svg.load(open_path)
        else:
            self.main_svg.load(closed_path)
        self.update()

    def mousePressEvent(self, event):
        # Emit the signal when the svg is clicked
        if self.main_svg.geometry().contains(event.pos()):
            self.clicked.emit()

    def paintEvent(self, event):
        painter = QPainter(self)
        
        #TODO remove temporary border drawing
        # border_pen = QPen(QColor(255, 0, 0), 2)
        # painter.setPen(border_pen)
        # painter.drawRect(self.main_svg.geometry())
        #END border drawing

        # Draw the main SVG as the background
        self.main_svg.render(painter)

    def disable(self):
        """
        Set this button to disabled. Should be called when another control feature
        is interacted with that causes the last input of this switch to be irrelevant,
        such as interacting with the slider.
        """
        self.disabled = True
        # Make call to state changed callback
        if self.checkbox.isChecked():
            self.main_svg.load(open_disabled_path)
        else:
            self.main_svg.load(closed_disabled_path)
        self.update()

    def set_open(self):
        """
        Set this switch to open.
        """
        self.disabled = False
        self.checkbox.setChecked(True)
        self.main_svg.load(open_path)
        self.update()

    def set_closed(self):
        """
        Set this switch to closed.
        """
        self.disabled = False
        self.checkbox.setChecked(False)
        self.main_svg.load(closed_path)
        self.update()

