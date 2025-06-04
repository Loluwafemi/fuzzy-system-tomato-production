from .temperatureToYield import Temperature
from .humidityToYield import Humidity
from .soilMoistureToYield import SoilMoisture
from .pestIncidentToYield import PestIncident
from .spacingToYield import Spacing
from .fertilizerToYield import Fertilizer
from .suface_temp_smoist_yield import TSMYSurface
from .suface_temp_humidity_yield import THYSurface
from .timeSeriesToYield import TimeSeries
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

"""
setup each linguistinc varibles and terms for all the parameters and pick them 
all by each class of the inference system.
Variables                               Type
1. All                                  Timeline
2. Humidity, Temperature, Yield         Surface Graph
3. Temperature vs Yield                 ------------
4. Pest Incidents vs Yield              ------------
5. Fertilizer vs Yield                  Line and Bar Chart
6. 

"""

