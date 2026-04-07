import yaml
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, path: str = "config/default.yaml"):
        self.path = path
        with open(path, 'r') as f:
            self.config = yaml.safe_load(f)

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)
