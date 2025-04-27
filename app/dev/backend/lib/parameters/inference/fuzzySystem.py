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
"""

# from .universal_discourse import temp_membership_function, temp_universe_discourse, humidity_membership_function, humidity_universe_discourse, moisture_membership_function, moisture_universe_discourse, pestIncident_membership_function, pestIncident_universe_discourse, plantSpacing_membership_function, plantSpacing_universe_discourse
from .universal_discourse import *
from .universal_discourse import crop_universe_discourse, crop_membership_function
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as FCtrl
import time
import matplotlib.pyplot as plt



def findYinMF(universe, mf, param):
    percentageYield = fuzz.interp_membership(universe, mf, param)
    return percentageYield * 100


def temperatureVsYield(param:float|None = 0) -> dict:
    if not param: 
        print("Parameter not found at temp")
        return
    # find the degree of mf in x
    degree = findYinMF(universe=temp_universe_discourse, mf=temp_membership_function, param=param)
    # print(f'Temp: {param} ->  Yield: {degree}')
    return dict(input=param, output=degree)


def humidityVsYield(param:float|int = 0)->dict:
    if not param: 
        print(f"Parameter not found at Humid: {param}")
        return
    
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
        return
    membership_function = moisture_membership_function
    universe_discourse = moisture_universe_discourse
    degree = findYinMF(universe=universe_discourse, mf=membership_function, param=param)
    # print(f'Soil Moisture: {param} ->  Yield: {degree}')
    return dict(input=param, output=degree)

def spacingVsYield(param:list)->dict:
    if not param: 
        print("Parameter not found at Spacing")
        return
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


# for ps in range(2, 50):
#     spacingVsYield(param=[ps*10, ps*2])
