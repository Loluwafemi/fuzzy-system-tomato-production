from .. import ParameterClassInterface
import plotly.express as plt
import plotly.graph_objects as go
import numpy as np
import pandas as pd

from .inference.universal_discourse import pestIncident_universe_discourse, pestIncident_membership_function
from .inference.fuzzySystem import pestIncidentsVsYield

class PestIncident():
    parameterValue: float
    def __init__(self, pinsident, tune_pinsident=False) -> None:
        self.parameterValue = pinsident
        self.tune = tune_pinsident


    """
    A graphs takes in a universal_discourse[] and then takes in membershipfunction[]
    which both is an array.

    """
    def inference(self) -> any:

        df = pd.DataFrame(
            {
                "Pest Incident": pestIncident_universe_discourse,
                "Yield": pestIncident_membership_function
            }
        )
        df["index"] = df.index
        trace = plt.area(
            data_frame=df,
            x=pestIncident_universe_discourse, 
            y=pestIncident_membership_function, 
            title="Pest Incident - Yield Effect",
            hover_data=["Yield", "Pest Incident"]
            
            )


        trace.update_layout(
            xaxis_title="Pest Incident [per week]",
            yaxis_title="Yield Effect",
            autosize=True,
            overwrite=True
        )

        # from the fuzzy result. Use it to generate the points for both axis
        fuzzyResult = pestIncidentsVsYield(self.parameterValue['Pest Incident'])
        fuzzyResulIncident = [fuzzyResult['input']]
        fuzzyResultYield = fuzzyResult['output']

        # fuzzyResult = np.unique(np.random.randint(0, len(df), 1))
        fuzzydf2 = df.iloc[fuzzyResulIncident]

        trace.add_traces(
            go.Scatter(
                x=fuzzydf2["Pest Incident"], 
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
        x=fuzzydf2["Pest Incident"].values[0], 
        y=fuzzydf2["Yield"].values[0], 
        text=f'Yield Predicted: {int(fuzzydf2["Yield"].values[0] * 100)}%',
        showarrow=True,
        arrowcolor="red",
        bordercolor="green",
        bgcolor="yellow",
        font=dict(color="black")
        )


        if self.tune and self.tune['Tune_Pest_Incident']:
            fuzzyResultTune = pestIncidentsVsYield(self.tune['Tune_Pest_Incident'])
            fuzzyResultHumidityTune = [fuzzyResultTune['input']]
            fuzzyResultYieldTune = fuzzyResultTune['output']

            # fuzzyResult = np.unique(np.random.randint(0, len(df), 1))
            fuzzydfTune = df.iloc[fuzzyResultHumidityTune]

            trace.add_traces(
                go.Scatter(
                    x=fuzzydfTune["Pest Incident"], 
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
                x=fuzzydfTune['Pest Incident'].values[0], 
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







