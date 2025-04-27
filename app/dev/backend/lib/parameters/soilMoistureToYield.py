from .. import ParameterClassInterface
import plotly.express as plt
import plotly.graph_objects as go
import pandas as pd
import numpy as np

from .inference.universal_discourse import moisture_universe_discourse, moisture_membership_function
from .inference.fuzzySystem import soilMoistureVsYield

class SoilMoisture():
    parameterValue: float
    def __init__(self, smoisture, tune_smoisture) -> None:
        self.parameterValue = smoisture
        self.tune = tune_smoisture

    """
    A graphs takes in a universal_discourse[] and then takes in membershipfunction[]
    which both is an array.

    """
    def inference(self) -> any:
        df = pd.DataFrame(
            {
                "Soil Moisture": moisture_universe_discourse,
                "Yield": moisture_membership_function
            }
        )

        df["index"] = df.index
        trace = plt.area(
            data_frame=df,
            x=moisture_universe_discourse, 
            y=moisture_membership_function, 
            title="Soil Moisture - Yield Effect",
            hover_data=["Yield", "Soil Moisture"]
            
            )
        
        trace.update_layout(
            xaxis_title="Soil Moisture",
            yaxis_title="Yield Effect",
            autosize=True,
            overwrite=True
        )

        # from the fuzzy result. Use it to generate the points for both axis
        # fuzzyResult = np.unique(np.random.randint(0, len(df), 1))
        
        fuzzyResult = soilMoistureVsYield(param=self.parameterValue["Soil Moisture"])
        fuzzyResultInput = [fuzzyResult['input']]
        fuzzyResulYield = fuzzyResult['output']
        fuzzydf2 = df.iloc[fuzzyResultInput]

        trace.add_traces(
            go.Scatter(
                x=fuzzydf2["Soil Moisture"], 
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
        x=fuzzydf2["Soil Moisture"].values[0], 
        y=fuzzydf2["Yield"].values[0], 
        text=f'Yield Predicted: {int(fuzzydf2["Yield"].values[0] * 100)}%',
        showarrow=True,
        arrowcolor="red",
        bordercolor="green",
        bgcolor="gray",
        font=dict(color="white")
        )


        if self.tune and self.tune["Tune_Soil_Moisture"]:
            fuzzyResultTune = soilMoistureVsYield(param=self.tune["Tune_Soil_Moisture"])
            fuzzyResultResultTune = [fuzzyResultTune['input']]
            fuzzyResultYieldTune = fuzzyResultTune['output']

            # fuzzyResult = np.unique(np.random.randint(0, len(df), 1))
            fuzzydfTune = df.iloc[fuzzyResultResultTune]

            trace.add_traces(
                go.Scatter(
                    x=fuzzydfTune["Soil Moisture"], 
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
                x=fuzzydfTune['Soil Moisture'].values[0], 
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







