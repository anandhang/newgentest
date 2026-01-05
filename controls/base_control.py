from playwright.sync_api import Locator, Page, expect

class BaseControl:
    """
    Base class for all UI controls. 
    Wraps Playwright Locator and provides common interaction methods.
    """
    def __init__(self, page: Page, selector: str, name: str = "Control"):
        self.page = page
        self.selector = selector
        self.name = name
        self.locator: Locator = self.page.locator(selector)

    def click(self, **kwargs):
        print(f"Clicking {self.name}")
        self.locator.click(**kwargs)

    def is_visible(self) -> bool:
        return self.locator.is_visible()

    def is_enabled(self) -> bool:
        return self.locator.is_enabled()

    def get_text(self) -> str:
        return self.locator.inner_text()
        
    def wait_for_visible(self, timeout: int = None):
        self.locator.wait_for(state="visible", timeout=timeout)
