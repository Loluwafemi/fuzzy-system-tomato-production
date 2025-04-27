"""
Model that helps connect the controller and the parameters
Everything from library is only implemented here which is used by the model only
Entry to the parameters in the library

Model can trigger the parameters which in turn update the screen with graphs data
"""
from dev.backend.lib.parameters import Temperature, Humidity, SoilMoisture, PestIncident, Spacing, Fertilizer


class FuzzyModel:
    payload: dict | bool
    def __init__(self, payload:dict, tunable=False):
        self.payload = payload
        self.tunable = tunable

    def performOperation(self) -> list | bool:
        if self.payload == False or self.payload is None:
            return self.catchException(self.payload)
        else: 
            return [
                "time-series",
                Humidity(self.payload, tune_humidity=self.tunable).inference(),
                Temperature(self.payload, tune_temp=self.tunable).inference(),
                SoilMoisture(self.payload, tune_smoisture=self.tunable).inference(),
                PestIncident(self.payload, tune_pinsident=self.tunable).inference(),
                Spacing(self.payload, tune_spacing=self.tunable).inference(),
                Fertilizer(self.payload, tune_fertilizer=self.tunable).inference(),
                ]
    
    def catchException(self, payload):
        return payload
    

class FuzzyTuning(FuzzyModel):
    def __init__(self) -> None:
        # makes use of fuzzymodel and its payload and then use all priviledge to overide data
        pass

