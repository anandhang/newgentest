from .abstract_page_object import AbstractPageObject
from playwright.sync_api import Locator

class CommonGridPageObject(AbstractPageObject):
    """
    Base Page Object for screens containing a common grid/table structure.
    """
    def __init__(self, page, grid_selector: str = "table"):
        super().__init__(page)
        self.grid_selector = grid_selector
        self.grid_locator = self.page.locator(grid_selector)

    def get_row_count(self) -> int:
        return self.grid_locator.locator("tr").count()

    def get_cell_text(self, row_index: int, col_index: int) -> str:
        """
        Gets text from a specific cell (0-indexed).
        Assumes standard table structure (tr > td).
        """
        return self.grid_locator.locator("tr").nth(row_index).locator("td").nth(col_index).inner_text()

    def click_row(self, row_index: int):
        self.grid_locator.locator("tr").nth(row_index).click()
        
    def get_headers(self) -> list[str]:
        return self.grid_locator.locator("th").all_inner_texts()
