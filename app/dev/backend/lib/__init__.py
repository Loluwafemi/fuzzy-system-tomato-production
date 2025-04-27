from abc import ABCMeta, abstractmethod
"""
Interface to be used by all parameters

1. must define membership function
2. must have same output structure
3. can be updated
4. others
"""

class ParameterClassInterface(metaclass=ABCMeta):

    @abstractmethod
    def __inference(self):
        pass

    @abstractmethod
    def __FuzzySystem(self, parameter) -> dict:
        pass

    @abstractmethod
    def __updateGraph(self):
        pass
