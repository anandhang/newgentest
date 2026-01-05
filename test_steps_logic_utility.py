from logic.alarm_logic import AlarmLogic

class TestStepsLogicUtility:
    """
    Central Logic Utility.
    Aggregates all feature-specific logic modules for easy access in tests.
    """
    def __init__(self):
        self.alarm = AlarmLogic()
        # self.co_explorer = COExplorerLogic()
