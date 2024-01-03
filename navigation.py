from PyQt6.QtWidgets import QStackedWidget, QWidget

class Navigation():

    stackedWidget: QStackedWidget

    def __init__(self, stackedWidget: QStackedWidget) -> None:
        """
        Initialize the navigation

        Params:
        stackedWidget (QStackedWidget): The stacked widget used for navigation
        """
        self.stackedWidget = stackedWidget

    def switch_to_page(self, page_index: int) -> None:
        """
        Switch to a page

        Params:
        page_index (int): The index of the page to switch to
        """
        self.stackedWidget.setCurrentIndex(page_index)

    def switch_to_page_widget(self, widget: QWidget) -> None:
        """
        Switch to a page

        Params:
        widget (QWidget): The widget object to switch to. 
        """
        self.stackedWidget.setCurrentWidget(widget)

    def add_page(self, page: QWidget) -> int:
        """
        Add a page to navigation

        Params:
        page (QWidget): Widget (or "page") to add

        Returns:
        int: Index of the new page
        """
        return self.stackedWidget.addWidget(page)
    
    def remove_all(self):
        """
        Remove all widgets from the stacked widget and delete them from memory.
        """
        all_widgets = [self.stackedWidget.widget(i) for i in range(2, self.stackedWidget.count())]
        for widget in all_widgets:
            self.stackedWidget.removeWidget(widget)
            widget.deleteLater()

        