from playwright.sync_api import Page
from page_objects.alarm_page_object import AlarmPageObject

class UIObjects:
    """
    Registry for all Page Objects.
    Provides a central access point for pages.
    """
    _instance = None

    def __init__(self, page: Page):
        self.page = page
        self.alarm_page = AlarmPageObject(page)
        # Add other pages here:
        # self.home_page = HomePageObject(page)

    @classmethod
    def init(cls, page: Page):
        cls._instance = UIObjects(page)
        return cls._instance

    @classmethod
    def get(cls):
        if cls._instance is None:
            raise Exception("UIObjects not initialized! Call init(page) first.")
        return cls._instance
