from playwright.sync_api import Page, Locator
from abc import ABC

class AbstractPageObject(ABC):
    """
    Base class for all Page Objects.
    Provides common functionality for page interactions.
    """
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        print(f"Navigating to {url}")
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def get_url(self) -> str:
        return self.page.url

    def reload(self):
        self.page.reload()

    def wait_for_load_state(self, state="load"):
        self.page.wait_for_load_state(state)
    
    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"screenshots/{name}.png")
