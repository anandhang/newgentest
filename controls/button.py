from .base_control import BaseControl

class Button(BaseControl):
    """
    Control representing a Button.
    """
    def __init__(self, page, selector, name="Button"):
        super().__init__(page, selector, name)

    # Add button-specific methods if any, usually click is enough
    # but could add double_click, etc.
