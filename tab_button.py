from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont


class TabButton(QPushButton):

    def __init__(self, name: str, *args, **kwargs):
        """
        Create a new tab button
        """
        super().__init__(name, *args, **kwargs)
        self.setFont(QFont("Live Nation Regular"))
        self.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF;
                color: black;
                border: 1px solid #FFFFFF;
                border-radius: 20px;
                padding: 20px;
            }
        """)

    def set_active_style(self):
        self.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF;
                color: black;
                border: 1px solid #FFFFFF;
                border-radius: 20px;
                padding: 20px;
            }
        """)
        self.raise_()

    def set_inactive_style(self):
        self.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: black;
                border: 1px solid transparent;
                border-radius: 20px;
                padding: 20px;
            }
        """)