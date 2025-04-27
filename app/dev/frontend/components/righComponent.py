
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd



from dev.frontend.style import componentSectionStyle, sideComponentsStyles

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

rightcomponent = Dash()

rightcomponent = html.Div(
    style=sideComponentsStyles,
    children=[
            html.Div(
                style=componentSectionStyle
            ),
            html.Div(
                style=componentSectionStyle
            ),
        ]
)


# @callback(
#     Output('graph-content', 'figure'),
#     Input('dropdown-selection', 'value')
# )



def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')


