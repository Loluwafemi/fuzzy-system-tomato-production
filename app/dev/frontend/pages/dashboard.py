from dev.frontend.components.controllboard import controllboard
from dev.frontend.components.leftComponent import leftcomponent
from dev.frontend.components.righComponent import rightcomponent
from dash import Dash, html
from dev.frontend.style import layoutStyle
import dash

# render all components here

dashboard = Dash()


# Requires Dash 2.17.0 or later

dashboard = html.Div(
    style=layoutStyle,
    children=[
    leftcomponent,
    controllboard,
    # rightcomponent

]
)

