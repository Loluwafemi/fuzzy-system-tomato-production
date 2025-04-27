"""_summary_
    This tab is only active if data is found in the tab space.
    Meaning data is needed to be tuned.

    The data is cloned and the cloned is sent to the fuzzySystem. Which overwrites and enables the tune varaible for other trace and annotation

"""
from dash import dcc, html, callback, Output, Input, no_update, State, clientside_callback
from dash.exceptions import PreventUpdate
from .tab import PAYLOAD, payloadValidator
from dev.frontend.components.controllboard import DisplayGraph

tune_PAYLOAD = {
    "Tune_Temperature": None,
    "Tune_plant": None,
    "Tune_row": None,
    "Tune_Humidity": None,
    "Tune_Soil_Moisture": None,
    "Tune_Fertilizer": None,
    "Tune_Acidity": None,
    "Tune_Sun_Light": None,
    "Tune_Ethylene": None,
    "Tune_Pest_Incident": None,
    "Tune_Nitrogen": None,
    "Tune_Potatium": None,
    "Tune_Magnisium": None,
    "Tune_Phosphorus": None,
    "Tune_Calcium": None,
    "Tune_Sodium": None,
}

tunableparameter = html.Div(
    id="tune_tab",
    children=[
        html.Br(),
        html.Span(children="Status: Pending", id="tune_status"),
        html.Br(),
        html.Div(
        children=[
                html.Label('Temperature (celcius)', id="tune_temperature_output"),
                dcc.RangeSlider(10, 35, value=[0, 0], id='tune_env-temperature-range-slider', 
                tooltip={'always_visible': False},
                className="InputForm"  
                )
            ]
        ),
        html.Div(
        children=[
            html.Label('Humidity(Absolute %): '),
            dcc.Slider(2, 17, value=0, id="tune_soil_humidity_input", 
                       tooltip={'always_visible': False},
                       className="InputForm"
                        )
        ]
        ),
        html.Div(
        children=[
                html.Label('Sunlight Exposure (hour/day)', id="tune_sunlight_range_output"),
                dcc.Slider(0, 12, value=0, id="tune_sunlight_input", 
                tooltip={'always_visible': False},
                className="InputForm"         
                           )
            ]
        ),
        html.Div(
        children=[
            html.Label('Pest Incident per week: '),
            dcc.Slider(0, 7, value=0, id='tune_pest_range_slider', 
                            tooltip={'always_visible': False},
                            className="InputForm"  
                            ),
        ]
        ),
        html.Div(
        children=[
            html.Label('Soil Moisture (% e.g liquid per soil volume)'),
            dcc.Slider(1, 11, value=5, id='tune_my_rain_range_slider', 
                            tooltip={'always_visible': False},
                            className="InputForm"
                            ),
        ]
        ),
        html.Div(
        children=[
            html.Label('Fertilizer Available (kg/ha): ', id="tune_fertilizerLabel"),
            dcc.RadioItems(["True", "False"], "False", id="tune_fertilizerCheckbox", className="InputForm")
        ]
        ),
        html.Div(
        children=[
            html.Label('Sodium Level (kg/Ha): '),
            dcc.Slider(60, 400, value=0, id="tune_soil_fert_sodium_input", 
                       tooltip={'always_visible': False},
                       className="InputForm"
                        ),
            html.Label('Potasium Level (kg/Ha): '),
            dcc.Slider(60, 400, value=0, id="tune_soil_fert_potash_input", 
                       tooltip={'always_visible': False},
                       className="InputForm"
                        ),
            html.Label('Nitrogen Level (kg/Ha): '),
            dcc.Slider(60, 400, value=0, id="tune_soil_fert_nitro_input", 
                       tooltip={'always_visible': False},
                       className="InputForm"
                        ),
            html.Label('Magnisium Level (kg/Ha): '),
            dcc.Slider(60, 400, value=0, id="tune_soil_fert_magnisium_input", 
                       tooltip={'always_visible': False},
                       className="InputForm"
                        ),
            html.Label('Casium Level (kg/Ha): '),
            dcc.Slider(60, 400, value=0, id="tune_soil_fert_calsium_input", 
                       tooltip={'always_visible': False},
                       className="InputForm"
                        ),
            html.Label('Phosphorus Level (kg/Ha): '),
            dcc.Slider(60, 400, value=0, id="tune_soil_fert_phos_input", 
                       tooltip={'always_visible': False},
                       className="InputForm"
                        )
        ]
        ),
        html.Div(
        children=[
            # dcc.
            html.Label('Plant Row : Plant Spacing'),
            html.Div(children=[
            html.Label('Plant Row (cm) '),
            dcc.Slider(150, 250, value=0, id="tune_plant_row_input", 
                       tooltip={'always_visible': False},
                       className="InputForm"
                        ),
            html.Label('Plant Spacing (cm): '),
            dcc.Slider(20, 50, value=0, id="tune_plant_space_input", 
                       tooltip={'always_visible': False},
                       className="InputForm"
                        )
            ])
        ],

        )
    
],
style={
    "display": "grid",
    "gridTemplateColumns": "auto",
    "backgroundColor": "white",
    "borderRadius": '4px',
    "margin": "8px",
    "padding": "10px",
    "gap": "2px",
    # "pointerEvents": "none" if not payloadValidator(PAYLOAD) else "auto",
    # "opacity": "0.3" if not payloadValidator(PAYLOAD) else "1"
}
)

@callback(
    Output("tune_status",'value', allow_duplicate=True),
    Input(component_id="tune_env-temperature-range-slider", component_property='value'),
    prevent_initial_call=True 
)
def tuneParameters(value):
    tune_PAYLOAD['Tune_Temperature'] = value
    return "Temperature Tuned"



@callback(
    Output("tune_status",'value', allow_duplicate=True),
    Input(component_id="tune_soil_humidity_input", component_property='value'),
    prevent_initial_call=True 
)
def tuneParameters(value):
    tune_PAYLOAD['Tune_Humidity'] = value
    return "Humidity Tuned"



@callback(
    Output("tune_status",'value', allow_duplicate=True),
    Input(component_id="tune_sunlight_input", component_property='value'),
    prevent_initial_call=True 
)
def tuneParameters(value):
    tune_PAYLOAD['Tune_Sun_Light'] = value
    return "Sunlight Exposure Tuned"



@callback(
    Output("tune_status",'value', allow_duplicate=True),
    Input(component_id="tune_pest_range_slider", component_property='value'),
    prevent_initial_call=True 
)
def tuneParameters(value):
    tune_PAYLOAD['Tune_Pest_Incident'] = value
    return "Pest Incident Tuned"


@callback(
    Output("tune_status",'value', allow_duplicate=True),
    Input(component_id="tune_my_rain_range_slider", component_property='value'),
    prevent_initial_call=True 
)
def tuneParameters(value):
    tune_PAYLOAD['Tune_Soil_Moisture'] = value
    return "Soil Moisture Tuned"



@callback(
    Output("tune_status",'value', allow_duplicate=True),
    Input(component_id="tune_fertilizerCheckbox", component_property='value'),
    prevent_initial_call=True 
)
def tuneParameters(value):
    tune_PAYLOAD['Tune_Fertilizer'] = value
    return "Fertilizer Toggled"



@callback(
    Output("tune_status",'value', allow_duplicate=True),
    Input(component_id="tune_soil_fert_sodium_input", component_property='value'),
    prevent_initial_call=True 
)
def tuneParameters(value):
    tune_PAYLOAD['Tune_Sodium'] = value
    return "Sodium Level Tuned"






@callback(
    Output("tune_status",'value', allow_duplicate=True),
    Input(component_id="tune_soil_fert_potash_input", component_property='value'),
    prevent_initial_call=True 
)
def tuneParameters(value):
    tune_PAYLOAD['Tune_Potatium'] = value
    return "Soil Potisium Level Tuned"



@callback(
    Output("tune_status",'value', allow_duplicate=True),
    Input(component_id="tune_soil_fert_nitro_input", component_property='value'),
    prevent_initial_call=True 
)
def tuneParameters(value):
    tune_PAYLOAD['Tune_Nitrogen'] = value
    return "Soil Nitrogen Level Tuned"



@callback(
    Output("tune_status",'value', allow_duplicate=True),
    Input(component_id="tune_soil_fert_magnisium_input", component_property='value'),
    prevent_initial_call=True 
)
def tuneParameters(value):
    tune_PAYLOAD['Tune_Magnisium'] = value
    return "Soil Magnisium Level Tuned"



@callback(
    Output("tune_status",'value', allow_duplicate=True),
    Input(component_id="tune_soil_fert_calsium_input", component_property='value'),
    prevent_initial_call=True 
)
def tuneParameters(value):
    tune_PAYLOAD['Tune_Calcium'] = value
    return "Soil Calcium Level Tuned"


@callback(
    Output("tune_status",'value', allow_duplicate=True),
    Input(component_id="tune_soil_fert_phos_input", component_property='value'),
    prevent_initial_call=True 
)
def tuneParameters(value):
    tune_PAYLOAD['Tune_Phosphorus'] = value
    return "Soil Phosphorus Level Tuned"



@callback(
    Output("tune_status",'value', allow_duplicate=True),
    Input(component_id="tune_plant_row_input", component_property='value'),
    prevent_initial_call=True 
)
def tuneParameters(value):
    tune_PAYLOAD['Tune_row'] = value
    return "Plant Row Spacing Tuned"


@callback(
    Output("tune_status",'value', allow_duplicate=True),
    Input(component_id="tune_plant_space_input", component_property='value'),
    prevent_initial_call=True 
)
def tuneParameters(value):
    tune_PAYLOAD['Tune_plant'] = value
    return "Plant-Plant Column Spacing Tuned"

"""
Every change in the tune input triggers the system input.
For this to work, the data from result must be available
1. Add reset button which reset the refine
Before calling, check if payload is set: else print a message
"""

@callback(
    Output("control-section", "children", allow_duplicate=True),
    Input("tune_soil_humidity_input", "value"),
    Input("tune_sunlight_input", "value"),
    Input("tune_pest_range_slider", "value"),
    Input("tune_my_rain_range_slider", "value"),
    Input("tune_fertilizerCheckbox", "value"),
    Input("tune_soil_fert_sodium_input", "value"),
    Input("tune_soil_fert_potash_input", "value"),
    Input("tune_soil_fert_nitro_input", "value"),
    Input("tune_soil_fert_magnisium_input", "value"),
    Input("tune_soil_fert_calsium_input", "value"),
    Input("tune_soil_fert_phos_input", "value"),
    Input("tune_plant_row_input", "value"),
    Input("tune_plant_space_input", "value"),
    Input("tune_env-temperature-range-slider", "value"),
    prevent_initial_call=True 
)
def tunedata(*kwarg):
    # call the tune class which uses result and then inserted data
    if payloadValidator(payload=PAYLOAD):
        return DisplayGraph(PAYLOAD).display(tune=tune_PAYLOAD)
    elif not payloadValidator(payload=PAYLOAD):
        return DisplayGraph().display(message="Important Parameters not set!. Check your Input Data.")
    else:
        return PreventUpdate