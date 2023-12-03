from PyQt6.QtWidgets import QPushButton


class TabButton(QPushButton):

    def __init__(self, name: str, *args, **kwargs):
        """
        Create a new tab button
        """
        super().__init__(name, *args, **kwargs)
        self.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF;
                color: black;
                border: 1px solid #FFFFFF;
                border-radius: 20px;
                padding: 6px;
            }
        """)

    def set_active_style(self):
        self.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF;
                color: black;
                border: 1px solid #FFFFFF;
                border-radius: 20px;
                padding: 6px;
            }
        """)

    def set_inactive_style(self):
        self.setStyleSheet("""
            QPushButton {
                background-color: #000000;
                color: white;
                border: 1px solid #000000;
                border-radius: 20px;
                padding: 6px;
            }
        """)