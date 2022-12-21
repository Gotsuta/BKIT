from abc import ABC, abstractmethod

class Figure(ABC):

    @classmethod
    def get_figure_type(cls):
        return cls.FigureType

    @abstractmethod
    def square(self):
        pass
