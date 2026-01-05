import pytest
from playwright.sync_api import Page
from typing import Optional

class TestContextBase:
    """
    Base class for specific test contexts.
    Manages the page fixture and other common test utilities.
    """
    # __init__ removed to avoid pytest collection warning

    def setup(self):
        """Optional setup steps for the context."""
        pass

    def teardown(self):
        """Optional teardown steps for the context."""
        pass
