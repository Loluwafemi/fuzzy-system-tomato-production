from .. import ParameterClassInterface
import numpy as np
import math
import plotly.express as plt
import plotly.graph_objects as go
import pandas as pd
from dev.frontend.style import widgetLayout
from .inference.universal_discourse import temp_universe_discourse, humidity_universe_discourse
from .inference.fuzzySystem import temperatureVsYield, humidityVsYield

class THYSurface():
    parameterValue: any
    def __init__(self, trace) -> None:
        self.parameterValue = trace

    """
    A graphs takes in a universal_discourse[] and then takes in membershipfunction[]
    which both is an array.

    """
    def inference(self) -> any:

        np.random.seed(1)
        dimensionData = tableBuildupForParamters()
        x = temp_universe_discourse
        y = humidity_universe_discourse
        z = dimensionData
        
        fig = go.Surface(
                            x=x, 
                            y=y, 
                            z=z,
                            # colorscale="Viridis",
                            # colorbar=dict(title="Yield (%)")
            )
        
        trace = go.Figure(fig)
        trace.update_layout(
            title = {
                "text": "TemperatureX - HumidityY - YieldZ",
            },
            scene = dict(
                xaxis_title="Temperature (°C)",
                yaxis_title="Humidity (%)",
                zaxis_title="Yield (%)",
                # xaxis=dict(range=[10, 35], nticks=6),
                # yaxis=dict(range=[20, 80], nticks=7),
                # zaxis=dict(range=[0, 120]),
                camera=dict(
                    eye=dict(
                        x=1.6,
                        y=-1.6,
                        z=0.9
                    )
                ),


            )
        )

        trace.add_annotation(
            go.layout.Annotation(
                x=0.06,
                y=1,
                # z=0.9,
                text=f'Parameter Output: --%',
                showarrow=False,
                arrowcolor="red",
                bordercolor="green",
                bgcolor="red",
                font=dict(color="white")
            )
        )
        return trace
    
    




def tableBuildupForParamters():
    temp_grid, humid_grid = np.meshgrid(temp_universe_discourse, humidity_universe_discourse)
    yield_grid = np.zeros_like(temp_grid)      # output
    # perform operation using the temp and moist fuzzy function and store result
    for temp_unit in range(len(temp_universe_discourse)):
        for humid_grid in range(len(humidity_universe_discourse)):
            temp = temp_universe_discourse[temp_unit]
            moist = humidity_universe_discourse[humid_grid]

            temp_factor = temperatureVsYield(temp)
            humid_factor = humidityVsYield(moist)

            yield_factor = temp_factor["output"] * humid_factor["output"] * 0.8 + temp_factor["output"] * 0.1 + humid_factor["output"] * 0.1

            yield_grid[humid_grid, temp_unit] = max(0, yield_factor * 120)

    return yield_grid