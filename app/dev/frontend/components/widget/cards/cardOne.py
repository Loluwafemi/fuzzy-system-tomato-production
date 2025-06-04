
from dev.frontend.style import standardTopWidget, widgetLayout, defaultCardStyle, figureStyle
from dash import html, dcc
import plotly.express as px
import pandas as pd
import numpy as np
# from dev.backend.lib.parameters.inference.universal_discourse import temperatureAxis




"""
Rule Surfaces
3D Surface Plots: Show interactions between 2 inputs and output (e.g., Temperature vs. Sunlight → Production).
"""

class MetricAnalyzier():
    data: dict
    def __init__(self, data=None):
        self.data = data

    
    def figure(self):
                
        if(not self.data):
            return self.demonstration()
           
        print("showing processed figure")

        df = pd.DataFrame({
            "x": [1,2,1,2],
            "y": [1,2,3,4],
            "customdata": [1,2,3,4],
            "fruit": ["apple", "apple", "orange", "orange"]
        })


        figure = px.scatter(df, x="x", y="y", color="fruit", custom_data=["customdata"])

        figure.update_layout(clickmode='event+select')

        figure.update_traces(marker_size=20)
        return figure.data
    
    def demonstration(self):
        print("showing demonstration")
        df = pd.DataFrame({
            "x": [1,2,1,2],
            "y": [1,2,3,4],
            "customdata": [1,2,3,4],
            "fruit": ["apple", "apple", "orange", "orange"]
        })


        figure = px.scatter(df, x="x", y="y", color="fruit", custom_data=["customdata"])

        figure.update_layout(clickmode='event+select')

        figure.update_traces(marker_size=20)
        return figure.data


figureObject = MetricAnalyzier()

# just a card that takes in the type of 
class cardOne:
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
            figure=self.figure if self.figure else emptyFigure,
            style=figureStyle
            )

        screenOutput = self.message if self.message else figure
        return html.Div([
                html.Div(
                style=standardTopWidget,
                children=[
                    screenOutput
                ]
                    )
                        ]
)
    



