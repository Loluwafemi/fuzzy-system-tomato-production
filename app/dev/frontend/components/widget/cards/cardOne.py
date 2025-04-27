
from dev.frontend.style import standardTopWidget, widgetLayout, defaultCardStyle, figureStyle
from dash import html, dcc
import plotly.express as px
import pandas as pd
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
    def __init__(self, figure=None, active=False) -> None:
        self.figure = figure
        self.active = active




    def output(self):
        defaultData = []

        figure = dcc.Graph(
        # id='basic-interactions',
            figure={
                "data": self.figure if self.active else defaultData,
                # 'layout': widgetLayout
                },
            style=figureStyle
            )


        return html.Div([
                html.Div(
                style=standardTopWidget,
                children=[
                    figure
                ]
                    )
                        ]
)
    



