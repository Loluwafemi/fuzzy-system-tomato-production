import numpy as np
import pandas as pd
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash

# Define the growth phases
growth_phases = [
    "Germination", 
    "Vegetative Growth",
    "Flowering", 
    "Fruit Set", 
    "Green Fruit", 
    "Mature Green", 
    "Color Breaker", 
    "Half Ripe", 
    "Full Ripe"
]

# Define approximate days for each phase (cumulative)
phase_days = [0, 15, 45, 60, 75, 95, 105, 115, 125]

# Create time series data for a complete growth cycle
days = np.arange(130)
phases_data = {}

# Generate data for each phase with fuzzy transitions
for i, phase in enumerate(growth_phases):
    # Calculate fuzzy membership for this phase
    if i == 0:
        start = 0
    else:
        start = phase_days[i-1]
    
    end = phase_days[i] if i < len(phase_days) else days[-1]
    next_end = phase_days[i+1] if i+1 < len(phase_days) else days[-1]
    
    # Create a trapezoidal membership function for each phase
    x = np.array([max(0, start-5), start, end, min(days[-1], next_end)])
    phases_data[phase] = fuzz.trapmf(days, x)

# Define key growing parameters that affect tomato development
parameters = {
    "Temperature": {
        "Germination": [20, 30],           # Optimal range in °C
        "Vegetative Growth": [18, 26],
        "Flowering": [18, 24],
        "Fruit Set": [18, 24],
        "Green Fruit": [18, 24],
        "Mature Green": [16, 22],
        "Color Breaker": [16, 22],
        "Half Ripe": [16, 22],
        "Full Ripe": [16, 22]
    },
    "Water": {
        "Germination": [80, 90],           # % of field capacity
        "Vegetative Growth": [70, 80],
        "Flowering": [70, 90],
        "Fruit Set": [80, 90],
        "Green Fruit": [70, 85],
        "Mature Green": [60, 75],
        "Color Breaker": [50, 70],
        "Half Ripe": [50, 65],
        "Full Ripe": [40, 60]
    },
    "Nitrogen": {
        "Germination": [0, 30],            # % of total required
        "Vegetative Growth": [70, 100],
        "Flowering": [40, 60],
        "Fruit Set": [30, 50],
        "Green Fruit": [30, 50],
        "Mature Green": [20, 40],
        "Color Breaker": [10, 30],
        "Half Ripe": [5, 15],
        "Full Ripe": [0, 10]
    },
    "Phosphorus": {
        "Germination": [40, 60],           # % of total required
        "Vegetative Growth": [40, 60],
        "Flowering": [70, 100],
        "Fruit Set": [70, 100],
        "Green Fruit": [50, 80],
        "Mature Green": [40, 60],
        "Color Breaker": [30, 50],
        "Half Ripe": [20, 40],
        "Full Ripe": [10, 30]
    },
    "Potassium": {
        "Germination": [20, 40],           # % of total required
        "Vegetative Growth": [40, 60],
        "Flowering": [60, 80],
        "Fruit Set": [70, 90],
        "Green Fruit": [80, 100],
        "Mature Green": [70, 90],
        "Color Breaker": [60, 80],
        "Half Ripe": [50, 70],
        "Full Ripe": [40, 60]
    },
    "Light": {
        "Germination": [0, 20],            # % of max light requirement
        "Vegetative Growth": [80, 100],
        "Flowering": [90, 100],
        "Fruit Set": [90, 100],
        "Green Fruit": [80, 100],
        "Mature Green": [80, 100],
        "Color Breaker": [80, 100],
        "Half Ripe": [70, 90],
        "Full Ripe": [70, 90]
    }
}

# Create a fuzzy control system for tomato growth
def create_fuzzy_system():
    # Input variables
    temperature = ctrl.Antecedent(np.arange(10, 40, 1), 'temperature')
    water = ctrl.Antecedent(np.arange(0, 101, 1), 'water')
    nitrogen = ctrl.Antecedent(np.arange(0, 101, 1), 'nitrogen')
    phosphorus = ctrl.Antecedent(np.arange(0, 101, 1), 'phosphorus')
    potassium = ctrl.Antecedent(np.arange(0, 101, 1), 'potassium')
    light = ctrl.Antecedent(np.arange(0, 101, 1), 'light')
    
    # Output variable
    growth_quality = ctrl.Consequent(np.arange(0, 101, 1), 'growth_quality')
    
    # Membership functions for temperature
    temperature['low'] = fuzz.trimf(temperature.universe, [10, 15, 18])
    temperature['optimal'] = fuzz.trimf(temperature.universe, [18, 24, 26])
    temperature['high'] = fuzz.trimf(temperature.universe, [26, 30, 40])
    
    # Membership functions for water
    water['low'] = fuzz.trimf(water.universe, [0, 30, 50])
    water['medium'] = fuzz.trimf(water.universe, [40, 60, 80])
    water['high'] = fuzz.trimf(water.universe, [70, 85, 100])
    
    # Membership functions for nutrients
    for nutrient in [nitrogen, phosphorus, potassium]:
        nutrient['low'] = fuzz.trimf(nutrient.universe, [0, 0, 50])
        nutrient['medium'] = fuzz.trimf(nutrient.universe, [30, 50, 70])
        nutrient['high'] = fuzz.trimf(nutrient.universe, [60, 100, 100])
    
    # Membership functions for light
    light['low'] = fuzz.trimf(light.universe, [0, 0, 60])
    light['medium'] = fuzz.trimf(light.universe, [40, 70, 90])
    light['high'] = fuzz.trimf(light.universe, [80, 100, 100])
    
    # Membership functions for growth quality
    growth_quality['poor'] = fuzz.trimf(growth_quality.universe, [0, 0, 40])
    growth_quality['average'] = fuzz.trimf(growth_quality.universe, [30, 50, 70])
    growth_quality['good'] = fuzz.trimf(growth_quality.universe, [60, 80, 90])
    growth_quality['excellent'] = fuzz.trimf(growth_quality.universe, [80, 100, 100])
    
    # Define rules for the fuzzy system
    rule1 = ctrl.Rule(temperature['optimal'] & water['medium'], growth_quality['good'])
    rule2 = ctrl.Rule(temperature['optimal'] & water['high'] & light['high'], growth_quality['excellent'])
    rule3 = ctrl.Rule(temperature['low'] | water['low'], growth_quality['poor'])
    rule4 = ctrl.Rule(nitrogen['high'] & phosphorus['medium'] & potassium['medium'], growth_quality['good'])
    rule5 = ctrl.Rule(nitrogen['high'] & phosphorus['high'] & potassium['high'] & temperature['optimal'], growth_quality['excellent'])
    rule6 = ctrl.Rule(light['low'], growth_quality['poor'])
    rule7 = ctrl.Rule(temperature['high'] & water['low'], growth_quality['poor'])
    rule8 = ctrl.Rule(temperature['optimal'] & water['medium'] & nitrogen['medium'] & phosphorus['medium'] & potassium['medium'] & light['medium'], growth_quality['good'])
    
    # Create and return the control system
    growth_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])
    return ctrl.ControlSystemSimulation(growth_ctrl)

# Calculate parameter requirements over time
def calculate_parameter_values():
    parameter_values = {}
    
    for param in parameters:
        param_values = np.zeros(len(days))
        
        for day in days:
            # Find which phase has the highest membership at this day
            phase_memberships = [(phase, phases_data[phase][day]) for phase in growth_phases]
            phase_memberships.sort(key=lambda x: x[1], reverse=True)
            
            # Weight parameter values by membership in each relevant phase
            weighted_value = 0
            weight_sum = 0
            
            for phase, membership in phase_memberships:
                if membership > 0:
                    # Get the min and max for this parameter in this phase
                    param_min, param_max = parameters[param][phase]
                    # Use the mean as the representative value
                    param_value = (param_min + param_max) / 2
                    weighted_value += membership * param_value
                    weight_sum += membership
            
            if weight_sum > 0:
                param_values[day] = weighted_value / weight_sum
        
        parameter_values[param] = param_values
    
    return parameter_values
