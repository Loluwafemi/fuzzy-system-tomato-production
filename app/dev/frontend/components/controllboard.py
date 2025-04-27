from dash import html
from dev.frontend.components.widget.cards import cardOne
from dev.frontend.components.widget.cards import cardTwo
from dev.frontend.style import centerComponentStyle, sectionThreeStyle
from dev.backend.app import FuzzyModel
""" 
The following are displayed after data is processed:

1. Input/Output Membership Functions
Triangular/Trapezoidal Plots: Visualize MFs for each parameter (e.g., temperature vs. membership degree).

2. Rule Surfaces
3D Surface Plots: Show interactions between 2 inputs and output (e.g., Temperature vs. Sunlight → Production).

3. Validation Graphs
Predicted vs. Actual: Line/scatter plots comparing model predictions with historical data.
Sensitivity Analysis: Heatmaps to show parameter impact on production.

4. Dynamic Monitoring
Time-Series Plots: Track input parameters (e.g., soil moisture) over a growing season.


"""




class DisplayGraph:
    processData: None | list
    def __init__(self, processedData=None) -> None:
        self.processData = processedData

    
    def display(self, message=None, tune=False):
        if (self.processData is None or message):
            return self.defaulDisplay(message=message)
        else:
            return self.manageDispay(self.processData, tunable=tune)
        


    def defaulDisplay(self, message):
        
        return [
            html.Div(
                children=[cardOne(figure=message).output()], 
            style={
            "display": "block",
            "width": "100%",
            "margin": "2px"

            
            }),
            html.Div(children=[
                cardTwo(message=message).output(), 
                cardTwo(message=message).output(), 
                cardTwo(message=message).output(), 
                cardTwo(message=message).output(), 
                cardTwo(message=message).output(), 
                cardTwo(message=message).output(), 
                cardTwo(message=message).output(), 
                cardTwo(message=message).output()
            ], style={
                "display": "grid",
                "gap": 8,
                "gridTemplateColumns": "50% 50%",
                "border": "solid 0px white",
                "height": "0",
                "width": "inherit"
            })
        ]
    

    def manageDispay(self, processData: list, tunable=False):
        inferenceSpaceForAllParameter = FuzzyModel(payload=processData, tunable=tunable)
        inference = inferenceSpaceForAllParameter.performOperation()

        return [
            html.Div(
                children=[cardOne(figure=inference, active=True).output()], 
            style={
            "display": "block",
            "width": "100%",
            "margin": "2px"
            }),
            html.Div(children=[
                cardTwo(figure=inference[1], active=True).output(),
                cardTwo(figure=inference[2], active=True).output(), 
                cardTwo(figure=inference[3], active=True).output(), 
                cardTwo(figure=inference[4], active=True).output(), 
                cardTwo(figure=inference[5], active=True).output(), 
                cardTwo(figure=inference[6], active=True).output(),
                cardTwo(figure=inference).output(),
                cardTwo(figure=inference).output()
            ], style={
                "display": "grid",
                "gap": 8,
                "gridTemplateColumns": "50% 50%",
                "border": "solid 0px white",
                "height": "0",
                "width": "inherit"
            })
        ]



controllboard = html.Div(
    id='control-section',
    style=centerComponentStyle,
    children=[
            html.Div(
                style=sectionThreeStyle,
                children= DisplayGraph().display()
            )
        ]
)

# should contain a row with two column in a row. c1 contains a single container. 



