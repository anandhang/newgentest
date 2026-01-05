from .common_grid_page_object import CommonGridPageObject
from controls.button import Button
from controls.textbox import TextBox

class AlarmPageObject(CommonGridPageObject):
    """
    Page Object for the Alarm Screen.
    Inherits grid capabilities from CommonGridPageObject.
    """
    def __init__(self, page):
        super().__init__(page, grid_selector="#alarm-table")
        self.acknowledge_btn = Button(page, "#ack-btn", "Acknowledge Button")
        self.search_box = TextBox(page, "#search-input", "Alarm Search Box")

    def search_alarm(self, query: str):
        self.search_box.fill(query)
        self.search_box.type_text("\n") # Press enter

    def acknowledge_selected(self):
        self.acknowledge_btn.click()
