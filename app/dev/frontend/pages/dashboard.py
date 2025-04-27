from dev.frontend.components.controllboard import controllboard
from dev.frontend.components.leftComponent import leftcomponent
from dev.frontend.components.righComponent import rightcomponent
from dash import Dash, html
from dev.frontend.style import layoutStyle

# render all components here
dashboard = Dash(__name__)


# Requires Dash 2.17.0 or later

dashboard.title = 'Tomato Production Fuzzy Base System'

dashboard.layout = html.Div(
    style=layoutStyle,
    children=[
    leftcomponent,
    controllboard,
    # rightcomponent

]
)

