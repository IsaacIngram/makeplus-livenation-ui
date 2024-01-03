from PyQt6.QtWidgets import QHBoxLayout, QStackedWidget, QWidget
from navigation import Navigation
from tab_button import TabButton

class TabBar():

    navigation: Navigation
    stackedWidget: QStackedWidget
    tabs: QHBoxLayout

    def __init__(self, tabLayout: QHBoxLayout, stackedWidget: QStackedWidget):
        """
        Initialize the tab bar

        Params:
        tabLayout (QHBoxLayout): Layout to store all tab buttons
        stackedWidget (QStackedWidget): Stacked widget this bar navigates
        """
        self.stackedWidget = stackedWidget
        
        # Clear all widgets
        for i in range(self.stackedWidget.count()):
            widget = self.stackedWidget.widget(i)
            self.stackedWidget.removeWidget(widget)
            if widget:
                widget.deleteLater()
        
        self.tabs = tabLayout
        
        # Clear all tabs
        while self.tabs.count():
            item = self.tabs.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        self.navigation = Navigation(stackedWidget)

    def add_tab(self, id: int, widget: QWidget, name: str):
        """
        Add a tab to the tab bar

        Params:
        widget (QWidget): Widget for this tab
        name (str): Name on the tab
        """
        new_button = TabButton(name)
        self.tabs.addWidget(new_button)
        self.navigation.add_page(widget)
        new_button.clicked.connect(lambda: self.switch_to_tab(id, widget))
        
    def clear_tabs(self):
        """
        Clear all tabs
        """
        self.navigation.remove_all()
        while self.tabs.count():
            item = self.tabs.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            

    def switch_to_tab(self, id: int, widget: QWidget):
        """
        Callback function to switch tabs

        Params:
        id (int): id of the tab to switch to
        widget (QWidget): the widget the tab switches to
        """
        # Set the style of all tabs
        for i in range(self.tabs.count()):
            item = self.tabs.itemAt(i).widget()
            # Only set one tab to the active style
            if i == id and isinstance(item, TabButton):
                item.set_active_style()
            elif isinstance(item, TabButton):
                item.set_inactive_style()
        # Switch to the widget
        self.navigation.switch_to_page_widget(widget)


