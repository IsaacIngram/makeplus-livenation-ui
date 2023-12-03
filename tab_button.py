from PyQt6.QtWidgets import QPushButton, QGraphicsDropShadowEffect
from PyQt6.QtCore import QRect
from PyQt6.QtGui import QFont


class TabButton(QPushButton):

    def __init__(self, name: str, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        self.setFont(QFont("Live Nation Regular"))
        self.setMinimumHeight(100)
        self.setMaximumHeight(100)
        self.setMinimumWidth(100)
        self.setMaximumWidth(951)
        self.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: black;
                border: 1px solid transparent;
                border-top-left-radius: 0px;
                border-top-right-radius: 0px;
                border-bottom-left-radius: 20px;
                border-bottom-right-radius: 20px;
                padding: 20px;
            }
        """)

    def set_active_style(self):
        self.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF;
                color: black;
                border: 1px solid #FFFFFF;
                border-top-left-radius: 0px;
                border-top-right-radius: 0px;
                border-bottom-left-radius: 20px;
                border-bottom-right-radius: 20px;
                padding: 20px;
            }
        """)

    def set_inactive_style(self):
        self.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: black;
                border: 1px solid transparent;
                border-top-left-radius: 0px;
                border-top-right-radius: 0px;
                border-bottom-left-radius: 20px;
                border-bottom-right-radius: 20px;
                padding: 20px;
            }
        """)