from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_data(self): pass

class Actuator(ABC):
    @abstractmethod
    def set_value(self, val): pass
