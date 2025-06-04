from dash import Dash, html, dcc, callback, Input, Output
from dev.frontend.style import onboard, onboard_nav, onboard_section, onboard_nav_items, onboard_content, onboard_tab_styling, onboard_tab_item_style, tab_selected_style
from dev.frontend.components.onboard_contents import welcome, about, manual, report
# render all components here





onboarding = Dash()



onboarding.title = "Tomato Production Fuzzy Base System"
# Requires Dash 2.17.0 or later
onboarding = html.Section(
    style=onboard,
    children=[
        html.Div(
            style=onboard_nav,
            children=[
                html.Div(children="Header"),
                html.Div(children=[
                    html.Div(
                        style=onboard_nav_items,
                        children=[
                        dcc.Tabs(
                            id="section_tab",
                            style=onboard_tab_styling,
                            children=[
                                dcc.Tab(style=onboard_tab_item_style, selected_style= tab_selected_style, label="Welcome", value='welcome'),
                                dcc.Tab(style=onboard_tab_item_style, selected_style= tab_selected_style, label="About", value='about'),
                                dcc.Tab(style=onboard_tab_item_style, selected_style= tab_selected_style, label="Manual", value="manual"),
                                dcc.Tab(style=onboard_tab_item_style, selected_style= tab_selected_style, label="Report Bug", value="report"),

                        ])
                    ])
                ]),
                html.Div(
                    style={
                        "display": "flex",
                        "justify-content": 'center'

                    },
                    children=[
                    dcc.Link('Start', href='/dashboard', style={
                        "text": "black",
                        "backgroundColor": "white",
                        "padding": "10px",
                        "textAlign": "center",
                        "marginBottom": "10px",
                        "textDecoration": "none",
                        "display": "flex",
                        "width": "100px",
                        "justify-content": 'center'
                    }),
                ]),
        ]),
        html.Div(
            style=onboard_section,
            children=[
            html.Div(
                style=onboard_content,
                id="onboard_content"
            )
        ])
    ]
)


@callback(
        Output('onboard_content', 'children'),
        Input('section_tab', 'value'),
        # prevent_initial_call=True   
        )
def navEvent(value):
    if value == "about":
        return about

    if value == "manual":
        return manual

    if value == "report":
        return report

    return welcome