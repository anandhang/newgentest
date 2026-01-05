import os
from dotenv import load_dotenv

class Variables:
    """
    Centralized configuration and test data management.
    Reads from environment variables (supported by .env files) and provides defaults.
    """
    
    _loaded = False

    @classmethod
    def load(cls):
        if not cls._loaded:
            load_dotenv()
            cls._loaded = True

    @classmethod
    def get(cls, key: str, default=None):
        cls.load()
        return os.getenv(key, default)

    # Pre-defined known variables for easy access
    @property
    def BASE_URL(cls):
        return cls.get("BASE_URL", "https://example.com")

    @property
    def HEADLESS(cls):
        return cls.get("HEADLESS", "True").lower() == "true"

    @property
    def BROWSER_TYPE(cls):
        return cls.get("BROWSER_TYPE", "chromium")

    @property
    def SLOW_MO(cls):
        return int(cls.get("SLOW_MO", "0"))

# Singleton instance access (optional, or just use class methods directly)
config = Variables()
