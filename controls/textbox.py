from .base_control import BaseControl

class TextBox(BaseControl):
    """
    Control representing a Text Input field.
    """
    def __init__(self, page, selector, name="TextBox"):
        super().__init__(page, selector, name)

    def fill(self, value: str):
        print(f"Filling {self.name} with '{value}'")
        self.locator.fill(value)

    def type_text(self, value: str, delay: int = 0):
        print(f"Typing '{value}' into {self.name}")
        self.locator.type(value, delay=delay)
    
    def clear(self):
        print(f"Clearing {self.name}")
        self.locator.fill("")

    def get_value(self) -> str:
        return self.locator.input_value()
