from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont


class TabButton(QPushButton):

    def __init__(self, name: str, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        self.setFont(QFont("Live Nation Regular"))
        self.setMinimumHeight(50)
        self.setMaximumHeight(50)
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
                padding-top: 8px;
                font-size: 14px;
                font-family: "Live Nation";
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
                padding-top: 8px;
                font-size: 14px;
                font-family: "Live Nation";
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
                padding-top: 8px;
                font-size: 14px;
                font-family: "Live Nation";
            }
        """)