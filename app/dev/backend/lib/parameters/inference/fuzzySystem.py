"""
    Create a function for each inference which takes the:
        - universal discourse
        - memebership function
    which is used to create rules for each of those function and takes in
    input which help return a fuzzy output that is a x, y dictionary
    Functions are:
        - Temperature vs Yield: dict(x and y)
        - Humidity vs Yield: dict(x and y)
        - PestIncidents vs Yield: dict(x and y)
        - SoilMoisture vs Yield: dict(x and y)
        - Spacing vs Yield: dict(x and y)
        - Fertilizer vs Yield: dict(elements)

        each function must define the following for itself:
            - membership function
            - universal discourse
            - rules

    Using Interpolation to get the degree of effect on Input on Membership function
"""

# from .universal_discourse import temp_membership_function, temp_universe_discourse, humidity_membership_function, humidity_universe_discourse, moisture_membership_function, moisture_universe_discourse, pestIncident_membership_function, pestIncident_universe_discourse, plantSpacing_membership_function, plantSpacing_universe_discourse
from .universal_discourse import *
from .universal_discourse import crop_universe_discourse, crop_membership_function
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as FCtrl
import time
import matplotlib.pyplot as plt
import random


def findYinMF(universe, mf, param):
    percentageYield = fuzz.interp_membership(universe, mf, param)
    return percentageYield * 100


def temperatureVsYield(param:float|None = 0) -> dict:
    if not param: 
        # print("Parameter not found at temp")
        return {"output": param}

    # find the degree of mf in x
    degree = findYinMF(universe=temp_universe_discourse, mf=temp_membership_function, param=param)
    # print(f'Temp: {param} ->  Yield: {degree}')
    return dict(input=param, output=degree)


def humidityVsYield(param:float|int = 0)->dict:
    if not param: 
        # print(f"Parameter not found at Humid: {param}")
        return {"output": param}
    
    membership_function = humidity_membership_function
    universe_discourse = humidity_universe_discourse
    degree = findYinMF(universe=universe_discourse, mf=membership_function, param=param)
    # print(f'Humidity: {param} ->  Yield: {degree}')
    return dict(input=param, output=degree)


def pestIncidentsVsYield(param:float|int=0)->dict:
    membership_function = pestIncident_membership_function
    universe_discourse = pestIncident_universe_discourse
    degree = findYinMF(universe=universe_discourse, mf=membership_function, param=param)
    # print(f'Pest Incident: {param} ->  Yield: {degree}')
    return dict(input=param, output=degree)

def soilMoistureVsYield(param:float|int=0)->dict:
    if not param: 
        print(f"Parameter not found at Smoiture: {param}")
        return {"output": param}
    membership_function = moisture_membership_function
    universe_discourse = moisture_universe_discourse
    degree = findYinMF(universe=universe_discourse, mf=membership_function, param=param)
    # print(f'Soil Moisture: {param} ->  Yield: {degree}')
    return dict(input=param, output=degree)

def spacingVsYield(param:list)->dict:
    if not param: 
        print("Parameter not found at Spacing")
        return {"output": param}
    membership_function = plantSpacing_membership_function
    universe_discourse = plantSpacing_universe_discourse
    # use the following to find yield
    area = int(param[0]) * int(param[1])
    plantYield = 100000000 / (area)
    degree = findYinMF(universe=universe_discourse, mf=membership_function, param=area)
    # print(f'Spacing: {param} ->  Yield: {degree}')
    return dict(input=plantYield, output=degree)

def fertilizerVsYield()->dict:

    return {}


# time series functions dependencies

    """
    every method have the ability to update self.payload
    {
        'Crop Type': 'Indeterminate fresh', 
        'Crop SubType': 'Long Shelf Life', 
        'Crop Size': 'large', 
        'Temperature': [10, 27], 
        'plant': 42.2, 
        'row': 192, 
        'Humidity': 2.2, 
        'Soil Moisture': 7.2, 
        'Fertilizer': None, 
        'Acidity': 8, 
        'Sun Light': 4.5, 
        'Ethylene': None, 
        'Pest Incident': 1.1
        }

        and 
        {
            'Tune_Temperature': [10, 24.4], 
            'Tune_plant': None, 
            'Tune_row': None, 
            'Tune_Humidity': None, 
            'Tune_Soil_Moisture': None, 
            'Tune_Fertilizer': None, 
            'Tune_Acidity': None, 
            'Tune_Sun_Light': None, 
            'Tune_Ethylene': None, 
            'Tune_Pest_Incident': None, 
            'Tune_Nitrogen': None, 
            'Tune_Potatium': None, 
            'Tune_Magnisium': None, 
            'Tune_Phosphorus': None, 
            'Tune_Calcium': None, 
            'Tune_Sodium': 132
        }

        use input against payload and return a % value 
        using the expectation output
        both input and ratio are percentage
        output = % of output

        OPERATION:
        -> find parameter from payload as u
        -> subtract ratio from u
        -> update payload
        -> return the % of the ratio

        Note: some ratio are constant and won't change during process.
        examples are:
        Soil Moisture
        Humidity
        Sunlight
        Spacing
        Temperature
    """

class TimeSeriesInference:
    payload: any

    def __init__(self, payload, tune) -> dict:
        self.payload = payload
        self.tune = tune

    def getTemperature(self, output, inputValue=0):
        tempLow, tempHigh = self.payload['Temperature'][0], self.payload['Temperature'][1]
        ratioOutput = inputValue * 100

        match output:
            case 'soil':
                return random.randint(0, 30)
            case 'env':
                return random.randint(0, 30)
            case 'day':
                return random.randint(0, 30)
            case 'night':
                return random.randint(0, 30)
            
        return random.randint(0, 30)


    def getFertilizer(self, output, inputValue=0):
        if self.tune:
            Nitrogen = self.tune['Tune_Nitrogen'] if self.tune['Tune_Nitrogen'] else 0
            Potasium = self.tune['Tune_Potatium'] if self.tune['Tune_Potatium'] else 0
            Magnisium = self.tune['Tune_Magnisium'] if self.tune['Tune_Magnisium'] else 0
            Phosphorus = self.tune['Tune_Phosphorus'] if self.tune['Tune_Phosphorus'] else 0
            Calcium = self.tune['Tune_Calcium'] if self.tune['Tune_Calcium'] else 0
            Sodium = self.tune['Tune_Sodium'] if self.tune['Tune_Sodium'] else 0
            Acidity = Sodium

        match output:
            case 'pH':
                return random.randint(0, 30)
            case 'nutrient':
                return random.randint(0, 30)
            case 'env':
                return random.randint(0, 30)
        
        return random.randint(0, 30)


    def getSoilMoisture(self, output, inputValue=0):
        soilMoisture = self.payload['Soil Moisture']

        match output:
            case 'soil':
                return random.randint(0, 30)
            case 'irrigation':
                return random.randint(0, 30)
        
        return random.randint(0, 30)

    def getpestIncident(self, output, inputValue=0):
        pestIncident = self.payload['Pest Incident']

        match output:
            case 'null':
                return random.randint(0, 30)
        
        return random.randint(0, 30)

    def getHumidity(self, output, inputValue=0):
        if self.tune:
            humidity = self.payload['Humidity'] if self.payload['Humidity'] else 0

        match output:
            case 'null':
                return random.randint(0, 30)
            
        
        return random.randint(0, 30)

    def getSunlight(self, output, inputValue=0):
        sunLight = self.payload['Sun Light']

        match output:
            case 'null':
                return random.randint(0, 30)
        
        return random.randint(0, 30)

    def getSpacing(self, output, inputValue=0):
        plantSpacing = [self.payload['plant'], self.payload['row']]
        plantColSpace, plantRowSpace = plantSpacing[0], plantSpacing[1] 

        match output:
            case 'null':
                return random.randint(0, 30)
        
        return random.randint(0, 30)
    
    def getEthylene(self, output, inputValue=0):
        if self.tune:
            ethylene = self.tune['Tune_Ethylene'] if self.tune['Tune_Ethylene'] else 0
        
        match output:
            case 'null':
                return random.randint(0, 30)
        
    
        return random.randint(0, 30)