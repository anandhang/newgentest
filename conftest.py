import pytest
import os
from datetime import datetime
from variables import config

# Ensure variables are loaded
config.load()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Override browser context arguments if needed.
    """
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080}
    }

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshot on failure.
    """
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = f"screenshots/{item.name}_{timestamp}.png"
            # Ensure directory exists
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
            
            # Attach extra html if using pytest-html
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(screenshot_path))
                rep.extra = extra
