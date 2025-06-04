from .. import ParameterClassInterface
import numpy as np
import plotly.express as plt
import plotly.graph_objects as go
import pandas as pd
from .inference.universal_discourse import temp_membership_function, temp_universe_discourse
from .inference.fuzzySystem import temperatureVsYield, TimeSeriesInference

"""
Time Series


"""



class TimeSeries():
    parameterValue: float
    def __init__(self, data, tune_data=None) -> None:
        self.parameterValue = data
        self.tune = tune_data

    """
    A graphs takes in a universal_discourse[] and then takes in membershipfunction[]
    which both is an array.

    """
    def inference(self) -> any:
        print("calling INFERENCE SYSTEM")
        phases = dict(
                    Germination={
                        "getTemperature.soil": 20,
                        "getFertilizer.pH": 60,
                        "getSoilMoisture.soil": 30,
                        "getpestIncident.null": 10
                    },
                    Vegetation = {
                        "getTemperature.env": 60,
                        "getFertilizer.env": 20,
                        "getHumidity.null": 10,
                        "getSunlight.null": 30,
                    },
                    Flowering = {
                        "getTemperature.night": 10,
                        "getTemperature.day": 20,
                        "getFertilizer.nutrient": 40,
                        "getHumidity.null": 30,
                    },
                    Fruit_Set = {
                        "getSoilMoisture.irrigation": 60,
                        "getpestIncident.null": 60,
                    },
                    Green_Fruit = {
                        "getFertilizer.nutrient": 30,
                        "getSoilMoisture.soil": 50,
                    },
                    Mature_Green = {
                        "getSoilMoisture.soil": 10,
                        "getEthylene.null": 40,
                    },
                    Color_Breaker = {
                        "getTemperature.env": 40,
                        "getSunlight.null": 40
                    },
                    Half_Ripe = {
                        "getpestIncident.null": 20,
                        "getSpacing.null": 40,
                    },
                    Full_Ripe = {},
                )
        
        defaultparameters = [ 'getTemperature',
                              'getFertilizer', 
                              'getSoilMoisture', 
                              'getpestIncident', 
                              'getHumidity', 
                              'getSunlight', 
                              'getEthylene', 
                              'getSpacing' ]


        dfPhase = {
            "Temperature" :[x for x in range(9)],
            "Fertilizer" :[x for x in range(9)],
            "Soil Moisture": [x for x in range(9)],
            "Pest Incident" :[x for x in range(9)],
            "Humidity": [x for x in range(9)],
            "Sunlight": [x for x in range(9)],
            "Ethylene": [x for x in range(9)],
            "Crop Spacing": [x for x in range(9)]
        }

        dataframe = pd.DataFrame(data=dfPhase)

        dataframe.index = list(phases.keys())
        
        InferenceData = self.parameterValue
        TimeSeriesInstance = TimeSeriesInference(InferenceData, tune=self.tune)
        for phase in phases:
            composite = list()
            phaseFunctionsUntouched = phases[phase]
            phaseFunctions = list(phaseFunctionsUntouched.keys())
            phaseSplitFunction = [x.split('.')[0] for x in phaseFunctions]
            phaseOperations = [x.split('.')[1] for x in phaseFunctions]

            for defaultFunc in defaultparameters:
                if defaultFunc in phaseSplitFunction:
                    # get phaseSplitFunction index
                    phaseSplitFunctionIndex = phaseSplitFunction.index(defaultFunc)
                    phaseFunctionOutput = phaseOperations[phaseSplitFunctionIndex]
                    phaseFunctionRatioValue = phaseFunctionsUntouched[f'{defaultFunc}.{phaseFunctionOutput}']
                    """
                        Perform function operation on each
                        Use the detected default funtion to call the method
                        Use the detected default function operator to decide output
                    """
                    output = 0
                    try:
                        callableObj = getattr(TimeSeriesInstance, defaultFunc)
                        response = callableObj(phaseFunctionOutput, phaseFunctionRatioValue)
                        output = response
                    except Exception:
                        print(f'Error: {Exception} on the fg: func: {defaultFunc} and ops: {phaseFunctionOutput}')


                    composite.append(output)
                else:
                    composite.append(0)


            phaseIndex = list(phases.keys()).index(phase)
            dataframe.iloc[phaseIndex] = composite


        data = [
            go.Bar(x=dataframe.index, y=dataframe['Temperature'], name="Temperature", text="Temperature"),
            go.Bar(x=dataframe.index, y=dataframe["Fertilizer"], name="Fertilizer", text="Fertilizer"),
            go.Bar(x=dataframe.index, y=dataframe["Soil Moisture"], name="Soil Moisture", text="Soil Moisture"),
            go.Bar(x=dataframe.index, y=dataframe["Pest Incident"], name="Pest Incident", text="Pest Incident"),
            go.Bar(x=dataframe.index, y=dataframe["Humidity"], name="Humidity", text="Humidity"),
            go.Bar(x=dataframe.index, y=dataframe["Sunlight"], name="Sunlight", text="Sunlight"),
            go.Bar(x=dataframe.index, y=dataframe["Ethylene"], name="Ethylene", text="Ethylene"),
            go.Bar(x=dataframe.index, y=dataframe["Crop Spacing"], name="Crop Spacing", text="Crop Spacing"),
        ]
        
        figure = go.Figure(
            data=data,
            layout=dict(
                barcornerradius=15,
                showlegend=True
            )
        )

        # Lower Usage Annotation
        figure.add_annotation(
            x=0,
            y=0.5,
            text="Low Usage",
            showarrow=False,
            yshift=5
        )
        figure.add_hline(y=0.5)

        # Average Usage Annotation
        figure.add_annotation(
            x=0,
            y=1.5,
            text="Average Usage",
            showarrow=False,
            yshift=5
        )
        figure.add_hline(y=1.5)

        # High Usage Annotation
        figure.add_annotation(
            x=0,
            y=3,
            text="Maximum Usage",
            showarrow=False,
            yshift=5
        )
        figure.add_hline(y=3)

        return figure

"""
        the phase object is:
        first used to populate the dataframe, using the days as index
        secondly used to upgrade the plot annotation

        dataframe for the line graph starts on fruit set. Meaning when iteration gets to Fruit set [3] 
            a function is called to populate the 2nd dataframe.
            Note before fuit set. Data is sent to dataframe but its 0-0

        Plot Hierarchy
        Bar Plot Top
            + annotations
            + bar per parameter
        Line Plot Child
            + annotion at the end to show percentage

        
        
"""