from .. import ParameterClassInterface
import numpy as np
import math
import plotly.express as plt
import plotly.graph_objects as go
import pandas as pd
from dev.frontend.style import widgetLayout
from .inference.universal_discourse import temp_membership_function, temp_universe_discourse
from .inference.fuzzySystem import temperatureVsYield

class Temperature():
    parameterValue: float
    def __init__(self, temperature, tune_temp=False) -> None:
        self.parameterValue = temperature
        self.tune = tune_temp

    """
    A graphs takes in a universal_discourse[] and then takes in membershipfunction[]
    which both is an array.

    """
    def inference(self) -> any:
        
        df = pd.DataFrame(
            {
                "Temperature": temp_universe_discourse,
                "Yield": temp_membership_function
            }
        )
        df["index"] = df.index
        trace = plt.area(
            data_frame=df,
            x=temp_universe_discourse, 
            y=temp_membership_function, 
            title="Temperature - Yield Effect",
            hover_data=["Yield", "Temperature"],
            
            )
        
        trace.update_layout(
            xaxis_title="Temperature",
            yaxis_title="Yield Effect",
            autosize=True,
            overwrite=True
        )
        
        


        # from the fuzzy result. Use it to generate the points for both axis
        fuzzyResult = addTemperature(temperature=self.parameterValue["Temperature"])
        fuzzyResult = temperatureVsYield(param=fuzzyResult)
        fuzzyResultTemperature = [fuzzyResult["input"]]
        fuzzyResultYield = fuzzyResult["output"]
        fuzzydf2 = df.iloc[fuzzyResultTemperature]



        trace.add_traces(
            go.Scatter(
                x=fuzzydf2["Temperature"], 
                y=fuzzydf2["Yield"], 
                mode="markers",
                name=f'Yield Percentage: {int(fuzzydf2["Yield"].values[0] * 100)}%',
                hoverinfo="skip",
                showlegend=False,
                marker={
                    "size": 12,
                    "color": "red",
                    "opacity": 1
                }
                )
        )

        



        trace.add_annotation(
                x=fuzzydf2["Temperature"].values[0], 
                y=fuzzydf2["Yield"].values[0], 
                text=f'Yield Predicted: {int(fuzzydf2["Yield"].values[0] * 100)}%',
                showarrow=True,
                arrowcolor="red",
                bordercolor="green",
                bgcolor="red",
                font=dict(color="white")
        )

        # Tunning Data
        if self.tune:
            fuzzyResultTune = addTemperature(temperature=self.tune["Tune_Temperature"])
            fuzzyResultTune = temperatureVsYield(param=fuzzyResultTune)
            fuzzyResultTemperatureTune = [fuzzyResultTune["input"]]
            fuzzyResultYieldTune = fuzzyResultTune["output"]
            fuzzydfTune = df.iloc[fuzzyResultTemperatureTune]

            trace.add_traces(
                go.Scatter(
                    x=fuzzydfTune["Temperature"], 
                    y=fuzzydfTune["Yield"], 
                    mode="markers",
                    name=f'Yield Percentage: {int(fuzzydfTune["Yield"].values[0] * 100)}%',
                    hoverinfo="skip",
                    showlegend=False,
                    marker={
                        "size": 12,
                        "color": "green",
                        "opacity": 1
                    }
                    )
            )

            trace.add_annotation(
                x=fuzzydfTune["Temperature"].values[0], 
                y=fuzzydfTune["Yield"].values[0], 
                text=f'Yield Predicted Tune: {int(fuzzydfTune["Yield"].values[0] * 100)}%',
                showarrow=True,
                arrowcolor="green",
                bordercolor="green",
                bgcolor="green",
                font=dict(color="white")
            )
        
        return trace
    
    




def addTemperature(temperature: list=[]) -> float:
    coldTemp = temperature[0]
    hotTemp = temperature[1]

    return hotTemp - (coldTemp/2)