from ui_objects import UIObjects

class AlarmLogic:
    """
    Logic/Workflow layer for Alarm-related features.
    Encapsulates business steps using Page Objects.
    """
    def __init__(self):
        # We access UIObjects via singleton
        self.ui = UIObjects.get()

    def filter_and_acknowledge_alarm(self, alarm_name: str):
        """
        High-level workflow: Search for an alarm and acknowledge it.
        """
        print(f"Logic: Filtering for alarm '{alarm_name}' and acknowledging.")
        self.ui.alarm_page.search_alarm(alarm_name)
        # Add verification logic here if needed, or row selection
        self.ui.alarm_page.acknowledge_selected()
