from .. import ParameterClassInterface
import plotly.express as plt
import numpy as np
import plotly.graph_objects as go
import pandas as pd

from .inference.universal_discourse import plantSpacing_universe_discourse, plantSpacing_membership_function
from .inference.fuzzySystem import spacingVsYield

class Spacing():
    parameterValue: float
    def __init__(self, spacing, tune_spacing=False) -> None:
        self.parameterValue = spacing
        self.tune = tune_spacing


    """
    A graphs takes in a universal_discourse[] and then takes in membershipfunction[]
    which both is an array.

    """
    def inference(self) -> any:
        df = pd.DataFrame(
            {
                "Plant Spacing": plantSpacing_universe_discourse,
                "Yield": plantSpacing_membership_function
            }
        )
        df["index"] = df.index
        trace = plt.area(
            data_frame=df,
            x=plantSpacing_universe_discourse, 
            y=plantSpacing_membership_function, 
            title="Plant Spacing - Yield Effect",
            hover_data=["Yield", "Plant Spacing"]
            
            )

        trace.update_layout(
            xaxis_title="Plant Spacing (Area - row x plantspace)",
            yaxis_title="Yield Effect",
            autosize=True,
            overwrite=True
        )

        # from the fuzzy result. Use it to generate the points for both axis
        # fuzzyResult = np.unique(np.random.randint(0, len(df), 1))
        fuzzyResult = spacingVsYield(param=[self.parameterValue["plant"], self.parameterValue["row"]])
        fuzzyResultInput = [fuzzyResult['input']]
        fuzzyResultOutput = fuzzyResult['output']
        # print(f'Input: {fuzzyResultInput}, output: {fuzzyResultOutput}')

        # fuzzydf2 = df.iloc[[300]]
        fuzzydf2 = df.iloc[fuzzyResultInput]

        trace.add_traces(
            go.Scatter(
                x=fuzzydf2["Plant Spacing"], 
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
                x=fuzzydf2["Plant Spacing"].values[0], 
                y=fuzzydf2["Yield"].values[0], 
                text=f'Yield Predicted: {int(fuzzydf2["Yield"].values[0] * 100)}%',
                showarrow=True,
                arrowcolor="red",
                bordercolor="green",
                bgcolor="green",
                font=dict(color="white")
        )

        if self.tune and (self.tune['Tune_row'] or self.tune['Tune_plant']):
            splant = self.tune['Tune_plant'] if self.tune['Tune_plant'] else self.parameterValue["plant"]
            rplant = self.tune['Tune_row'] if self.tune['Tune_row'] else self.parameterValue["row"]
            fuzzyResultTune = spacingVsYield(param=(splant, rplant))
            fuzzyResultSpacing = [fuzzyResultTune['input']]
            fuzzyResultYieldTune = fuzzyResultTune['output']

            # fuzzyResult = np.unique(np.random.randint(0, len(df), 1))
            fuzzydfTune = df.iloc[fuzzyResultSpacing]

            trace.add_traces(
                go.Scatter(
                    x=fuzzydfTune["Plant Spacing"], 
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
                x=fuzzydfTune['Plant Spacing'].values[0], 
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







