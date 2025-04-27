from .. import ParameterClassInterface
import plotly.express as plt
import plotly.graph_objects as go
import pandas as pd
import numpy as np

from .inference.universal_discourse import humidity_universe_discourse, humidity_membership_function
from .inference.fuzzySystem import humidityVsYield

class Humidity():
    parameterValue: float
    def __init__(self, humidity, tune_humidity=False) -> None:
        self.parameterValue = humidity
        self.tune = tune_humidity

    """
    A graphs takes in a universal_discourse[] and then takes in membershipfunction[]
    which both is an array.

    """
    def inference(self) -> any:

        df = pd.DataFrame(
            {
                "Humidity": humidity_universe_discourse,
                "Yield": humidity_membership_function
            }
        )

        df["index"] = df.index
        trace = plt.area(
            data_frame=df,
            x=humidity_universe_discourse, 
            y=humidity_membership_function, 
            title="Humidity - Yield Effect",
            hover_data=["Yield", "Humidity"]
            
            )
        
        trace.update_layout(
            xaxis_title="Humidity Level",
            yaxis_title="Yield Effect",
            autosize=True,
            overwrite=True
        )

        # from the fuzzy result. Use it to generate the points for both axis
        fuzzyResult = humidityVsYield(self.parameterValue["Humidity"])
        fuzzyResultHumidity = [fuzzyResult["input"]]
        fuzzyResultYield = [fuzzyResult["output"]]
        # print(fuzzyResultHumidity)
        # fuzzyResult = np.unique(np.random.randint(0, len(df), 1))
        fuzzydf2 = df.iloc[fuzzyResultHumidity]

        
        trace.add_traces(
            go.Scatter(
                x=fuzzydf2["Humidity"], 
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
        x=fuzzydf2["Humidity"].values[0], 
        y=fuzzydf2["Yield"].values[0], 
        text=f'Yield Predicted: {int(fuzzydf2["Yield"].values[0] * 100)}%',
        showarrow=True,
        arrowcolor="red",
        bordercolor="green",
        bgcolor="blue",
        font=dict(color="white")
        )

        if self.tune and self.tune["Tune_Humidity"] :
            fuzzyResultTune = humidityVsYield(self.tune["Tune_Humidity"])
            fuzzyResultHumidityTune = [fuzzyResultTune["input"]]
            fuzzyResultYieldTune = [fuzzyResultTune["output"]]
            fuzzydfTune = df.iloc[fuzzyResultHumidityTune]

            trace.add_traces(
                go.Scatter(
                    x=fuzzydfTune["Humidity"], 
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
                x=fuzzydfTune["Humidity"].values[0], 
                y=fuzzydfTune["Yield"].values[0], 
                text=f'Yield Predicted Tune: {int(fuzzydfTune["Yield"].values[0] * 100)}%',
                showarrow=True,
                arrowcolor="green",
                bordercolor="green",
                bgcolor="green",
                font=dict(color="white")
            )

        return trace
    
    
    async def updateGraph(self):
        pass







