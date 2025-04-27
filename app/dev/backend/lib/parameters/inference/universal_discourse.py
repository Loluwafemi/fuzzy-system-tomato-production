import numpy as np
import skfuzzy as fuzz


"""
Each Parameter is defined:
    The Universal Discourse (X)
    The membership function (Y)
every x and y axis is made public
"""

crop_universe_discourse = np.arange(0, 100, 1)
crop_membership_function = fuzz.trimf(x=crop_universe_discourse, abc=[0, 1, 10])

temp_universe_discourse = np.arange(0, 100, 1)
temp_membership_function = fuzz.gaussmf(temp_universe_discourse, 28.0, 6)


humidity_universe_discourse = np.arange(-30, 150, 10)
humidity_membership_function = fuzz.gaussmf(humidity_universe_discourse, mean=60, sigma=30)


moisture_universe_discourse = np.arange(1, 120, 10)
moisture_membership_function = fuzz.gaussmf(moisture_universe_discourse, mean=70, sigma=10)


pestIncident_universe_discourse = np.arange(0, 7, 1)
pestIncident_membership_function = fuzz.trimf(x=pestIncident_universe_discourse, abc=[0, 0, 7])


plantSpacing_universe_discourse = np.arange(0, 35000, 1)
plantSpacing_membership_function = fuzz.trimf(x=plantSpacing_universe_discourse, abc=[100, 35000, 35000])