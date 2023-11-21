from PyQt6.QtWidgets import QStackedWidget, QWidget

class Navigation():

    stackedWidget: QStackedWidget
    alias_map: dict[str : QWidget]

    def __init__(self, stackedWidget: QStackedWidget) -> None:
        """
        Initialize the navigation

        Params:
        stackedWidget (QStackedWidget): The stacked widget used for navigation
        """
        self.stackedWidget = stackedWidget
        self.alias_map = dict()

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

    def switch_to_page_alias(self, alias: str) -> int:
        """
        Switch to a page that has this alias

        Returns:
        int: 0 if failure, 1 if success
        """
        if not alias in self.alias_map:
            print("ERROR HIT")
            return 1
        self.switch_to_page_widget(self.alias_map[alias])
        print("SHOULD BE SWITCHED")

    def add_page(self, page: QWidget) -> int:
        """
        Add a page to navigation

        Params:
        page (QWidget): Widget (or "page") to add

        Returns:
        int: Index of the new page
        """
        return self.stackedWidget.addWidget(page)
    
    def add_page(self, page: QWidget, alias: str) -> int:
        """
        Add page to navigation with an alias

        Params:
        page (QWidget): Widget (or "page") to add
        alias (str): Alias name for this page

        Returns:
        int: 0 if success, 1 if failure
        """
        if alias in self.alias_map:
            return 1
        self.stackedWidget.addWidget(page)
        self.alias_map[alias] = page
    