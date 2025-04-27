from dash import Dash, html, dcc, callback, Output, Input


from dev.frontend.components.widget.tabsControl import inputTab
from dev.frontend.style import componentSectionStyle, sideComponentsStyles

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

leftcomponent = Dash()

leftcomponent = html.Div(
    style=sideComponentsStyles,
    children=[
            html.Div(
                style=componentSectionStyle,
                children=inputTab
            ),
            html.Div(
                style=componentSectionStyle,
                children="Download Reports"
            )
        ]
)


