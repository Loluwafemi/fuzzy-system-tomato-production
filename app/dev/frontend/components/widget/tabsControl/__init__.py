


from dash import dcc, html
from dev.frontend.style import tabsStyle, tabChildrenStyle
from .tab import parameter
from .tunetab import tunableparameter

inputTab = html.Div(
    [
    dcc.Tabs([
        dcc.Tab(label='Input Data', style=tabChildrenStyle, children=parameter),
        dcc.Tab(label='Tune Result', style=tabChildrenStyle, children=tunableparameter)
    ]
    )
],
style=tabsStyle
)