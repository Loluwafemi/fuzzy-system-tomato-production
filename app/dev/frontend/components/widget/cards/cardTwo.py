from dash import html, dcc
import plotly.express as px
import pandas as pd
import numpy as np
from dev.frontend.style import standardWidget, widgetLayout, figureStyle, defaultCardStyle
# from dev.backend.lib.parameters.inference.universal_discourse import temp_membership_function




"""
Rule Surfaces
3D Surface Plots: Show interactions between 2 inputs and output (e.g., Temperature vs. Sunlight → Production).
"""

# just a card that takes in the type of 
class cardTwo:
    figure: any
    active: bool
    def __init__(self, message:str|bool = False,  figure=None, active=False) -> None:
        self.figure = figure
        self.active = active
        self.message = message



    def output(self):
        defaultData = np.arange(0, 1, 1)
        
        emptyFigure = px.line(x=defaultData, y=defaultData)
        emptyFigure.update_layout(
            width=10,
            autosize=True,
        )

        figure = dcc.Graph(
            # id='basic-interactions',
            figure=self.figure if self.figure else emptyFigure,
            style=figureStyle
            )

        screenOutput = self.message if self.message else figure

        return html.Div([
                html.Div(
                    style=standardWidget,
                    children=[
                        screenOutput
                    ]
                )
            ]
            )