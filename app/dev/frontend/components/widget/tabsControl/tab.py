from dash import dcc, html, callback, Output, Input, no_update, State, clientside_callback
from dev.frontend.style import tabsStyle, tabChildrenStyle
import time
from dev.backend import FuzzyModel
from dev.frontend.components.controllboard import DisplayGraph
from dash.exceptions import PreventUpdate


"""
Input Variables (Environmental/Management Factors):

1. (Environmental)Temperature (°C): Affects growth rate and flowering.✅
2. (Environmental)Humidity (%): Influences transpiration and disease risk. ✅
3. (Environmental)Soil Moisture (%): Critical for root health and nutrient uptake. ✅
4. (Environmental)Sunlight Exposure (hours/day): Drives photosynthesis. <slider>✅
5. (Management)Soil pH: Affects nutrient availability (optimal range: 6.0–6.8). <range>✅
6. (Management)Pest Incidence (scale 0–10): Impacts crop damage <slider>.✅
7. (Management)Fertilizer Usage (kg/ha): Affects yield and soil health <number> ✅.

"""


PAYLOAD = {
    "Crop Type": None,
    "Crop SubType": None,
    "Crop Size": None,
    "Temperature": None,
    "plant": None,
    "row": None,
    "Humidity": None,
    "Soil Moisture": None,
    "Fertilizer": None,
    "Acidity": None,
    "Sun Light": None,
    "Ethylene": None,
    "Pest Incident": None
}


def scanpayload(payload):
    countOfAssigned = 0
    for param in payload:
        if PAYLOAD[param] is not None:
            countOfAssigned +=1
        elif PAYLOAD[param] is None: pass
    output = True if countOfAssigned >= 12 else False
    # print(countOfAssigned, output)
    return output


LONG_SHELF = ['large', 'medium', "small"]
CHERRIES_AND_COCKTAIL = ["round", "oval"]
SALADETTE = ["cylindrical", "blocky"]


tomatoesVarieties = {
    "Indeterminate fresh": {
        "Long Shelf Life": LONG_SHELF,
        "Red Cherries": CHERRIES_AND_COCKTAIL,
        "Yellow Cherries": CHERRIES_AND_COCKTAIL,
        "Red CockTail": CHERRIES_AND_COCKTAIL,
        "Yellow CockTail": CHERRIES_AND_COCKTAIL,
        "Saladette": SALADETTE

    },
    "Determinate fresh": {
        "Long Shelf Life": LONG_SHELF,
        "Red Cherries": CHERRIES_AND_COCKTAIL,
        "Saladette": SALADETTE
    }
}


parameter = html.Div(children=[
        html.Div(
        children=[
            html.Label('Plant Type'),
            dcc.Dropdown([tomatoTypes for tomatoTypes in list(tomatoesVarieties)], list(tomatoesVarieties)[0], id='type-dropdown', className="InputForm"),
        ]
        ),
        html.Div(
        children=[
            html.Label('Plant Sub-Types'),
            dcc.Dropdown(id='sub-type-dropdown', className="InputForm"),
        ]
        ),
        html.Div(
        children=[
            html.Label('Plant Type Size'),
            dcc.Dropdown(id='type-size', className="InputForm"),
        ]
        ),
        html.Br(),
        html.H3("Environmental Factor"),
        html.Br(),
        html.Div(
        children=[
                html.Label('Sunlight Exposure (hour/day)', id="sunlight_range_output"),
                dcc.Slider(0, 12, value=0, id="sunlight_input", 
                tooltip={'always_visible': False},
                className="InputForm"         
                           )
            ]
        ),
        html.Div(
        children=[
            html.Label('Pest Incident per week: '),
            dcc.Slider(0, 7, value=0, id='pest-range-slider', 
                            tooltip={'always_visible': False},
                            className="InputForm"  
                            ),
        ]
        ),
        # html.Br(),
        # html.Br(),
        html.H3("Management Factor"),
        html.Br(),
        
        html.Div(
        children=[
            html.Label('Soil pH: '),
            dcc.Slider(1.0, 14.0, value=0, id="soil_pH_input", 
                       tooltip={'always_visible': False},
                       className="InputForm"
                        )
        ]
        ),
        html.Div(
        children=[
                html.Label('Temperature (celcius)', id="temperature_output"),
                dcc.RangeSlider(10, 35, value=[0, 0], id='env-temperature-range-slider', 
                tooltip={'always_visible': False},
                className="InputForm"  
                )
            ]
        ),
        html.Div(
        style={
            "width": "220px"
        },
        children=[
            html.Label('Humidity(Absolute %): '),
            dcc.Slider(
                tooltip={'always_visible': False},
                id="humidiy_input",
                min=1,
                max=11,
            )
        ]
        ),
        html.Div(
        children=[
            html.Label('Soil Moisture (% e.g liquid per soil volume)'),
            dcc.Slider(1, 11, id='my-rain-range-slider', 
                            tooltip={'always_visible': False},
                            className="InputForm"
                            ),
        ]
        ),
        html.Div(
        children=[
            # dcc.
            html.Label('Row Spacing'),
            html.Div(children=[
            dcc.Slider(
                150,
                250,
                id="row_spacing",
                tooltip={'always_visible': False},
                className="InputForm"

                ),
            # "x",
            html.Label('Plant Spacing'),
            dcc.Slider(
                20,
                50,
                id="spacing_crop",
                tooltip={'always_visible': False},
                className="InputForm"

            )
            ], style={
                "display": "block"
            })
        ],

        ),

        html.Div(
        children=[
            # html.Label('Fertilizer Available (kg/ha): ', id="fertilizerLabel"),
            # dcc.RadioItems(["True", "False"], "False", id="fertilizerCheckbox", className="InputForm")
            html.Br(),

        ]
        ),
        
        html.Div(children=[
            dcc.Loading(html.Div(id="loading-delay-output"), id="loading-component"),
            html.Progress(hidden=False, disable_n_clicks=False, dir='ltr',id="payload_progress", max=11, value='0', title="Input Progress")
        ]),
        html.Button("Predict", id="submit_payload", disabled= False)
    
],
style={
    "display": "grid",
    "gridTemplateColumns": "auto auto",
    "backgroundColor": "white",
    "borderRadius": '4px',
    "margin": "8px",
    "padding": "10px",
    "gap": "6px",
    
}
)




@callback(
    Output(component_id="sub-type-dropdown", component_property='options'),
    Input(component_id="type-dropdown", component_property='value')
)
def update_output_dropdown(value):
    if (value): 
        PAYLOAD["Crop Type"] = value
    elif (value is None): 
        PAYLOAD["Crop Type"] = None
    return [sub_list for sub_list in tomatoesVarieties[value]]


@callback(
    Output(component_id="type-size", component_property='options'),
    Input(component_id="sub-type-dropdown", component_property='value'),
    Input(component_id="type-dropdown", component_property='value'),
)
def update_sublevel_dropdown(value, sub_value):
    if(value and sub_value):
        PAYLOAD["Crop SubType"] = value
        return [sublevelsize for sublevelsize in tomatoesVarieties[sub_value][value] ]
    elif (not value): 
        PAYLOAD["Crop SubType"] = None
        return []
    else: return []




@callback(
    Output(component_id="type-size", component_property='value'),
    Input(component_id="type-size", component_property='value'),
)
def update_size_dropdown(value):
    if(value):
        PAYLOAD["Crop Size"] = value
        return value
    elif (not value): 
        PAYLOAD["Crop Size"] = None
        return []
    else: return []




@callback(
    Output(component_id="sunlight_input", component_property='value'),
    Input(component_id="sunlight_input", component_property='value'),
)
def update_sunlight_input(value):
    if(value):
        PAYLOAD["Sun Light"] = value
        return value
    elif (not value):
        PAYLOAD["Sun Light"] = None
        return 
    else: return 



@callback(
    Output(component_id="pest-range-slider", component_property='value'),
    Input(component_id="pest-range-slider", component_property='value'),
)
def update_pest_input(value):
    if(value):
        PAYLOAD["Pest Incident"] = value
        return value
    elif (not value):
        PAYLOAD["Pest Incident"] = None
        return 
    else: return 


@callback(
    Output(component_id="soil_pH_input", component_property='value'),
    Input(component_id="soil_pH_input", component_property='value'),
)
def update_acidity_input(value):
    if(value > 1):
        PAYLOAD["Acidity"] = value
        return value
    elif (value <= 1):
        PAYLOAD["Acidity"] = None
        return 
    else: return 



@callback(
    Output(component_id="env-temperature-range-slider", component_property='value'),
    Input(component_id="env-temperature-range-slider", component_property='value'),
)
def update_temperature_input(value):
    if(sum(value) > 20):
        PAYLOAD["Temperature"] = value
        return value
    elif (sum(value) <= 20):
        PAYLOAD["Temperature"] = None
        return 
    else: return 




@callback(
    Output(component_id="humidiy_input", component_property='value'),
    Input(component_id="humidiy_input", component_property='value'),
)
def update_humidity_input(value):
    if(value):
        PAYLOAD["Humidity"] = value
        return value
    elif (not value):
        PAYLOAD["Humidity"] = None
        return 
    else: return 



@callback(
    Output(component_id="my-rain-range-slider", component_property='value'),
    Input(component_id="my-rain-range-slider", component_property='value'),
)
def update_soil_moisture_input(value):
    if(value > 0):
        PAYLOAD["Soil Moisture"] = value
        return value
    elif (value <= 0):
        PAYLOAD["Soil Moisture"] = None
        return 
    else: return 


@callback(
    Output(component_id="spacing_crop", component_property='value'),
    Input(component_id="spacing_crop", component_property='value'),
    prevent_initial_call=True   
)
def update_plant_space_input(value):
    if value:
        PAYLOAD["plant"] = value
        return value
    elif value <= 0:
        # PAYLOAD["plant"] = None
        return  


@callback(
    Output(component_id="row_spacing", component_property='value'),
    Input(component_id="row_spacing", component_property='value'),
    prevent_initial_call=True   
)
def update_row_space_input(value):
    if value:
        PAYLOAD["row"] = value
        return value
    elif value <=0:
        # PAYLOAD["row"] = None
        return  




"""
For every input, if value is added, the payload is updated. 
Constantly check if payload is changed and use its count to change progress value
Returns:
    _type_: _description_
"""

# def callDisplay(param):
#     return DisplayGraph(param).display()


@callback(
    Output("control-section", "children", allow_duplicate=True),
    Input("submit_payload", "n_clicks"),
    prevent_initial_call=True   
)
def load_output(n):
    if payloadValidator(payload=PAYLOAD) and n:
        return DisplayGraph(PAYLOAD).display(tune=False)
    elif not payloadValidator(payload=PAYLOAD):
        return DisplayGraph().display(message="Important Parameters not set!")
    else:
        return PreventUpdate



def payloadValidator(payload:dict) -> bool|dict:
    # check if some important payload is set return payload. else return false
    """
    Important input is all except, 
        fertilizer and ethylene

    """
    stat = True
    output = payload

    for items in PAYLOAD:

        if items == "Fertilizer" or items == "Ethylene":
            pass
        elif PAYLOAD[items] == None:
            stat = False

    return output if stat else stat





@callback(
        Output("payload_progress", "value"),
        Input("payload_progress", "value"),
        Input("type-dropdown", "value"),
        Input("sub-type-dropdown", "value"),
        Input("type-size", "value"),
        Input("sunlight_input", "value"),
        # Input("fertilizerCheckbox", "value"),
        Input("soil_pH_input", "value"),
        Input("env-temperature-range-slider", "value"),
        Input("humidiy_input", "value"),
        Input("pest-range-slider", "value"),
        Input("my-rain-range-slider", "value"),
        Input("spacing_crop", "value"),
        Input("row_spacing", "value"),
)
def progressMonitor(*kwarg):
    if (kwarg):
        # scanpayload(PAYLOAD)
        intProgressValue = 0
        for parameter in PAYLOAD:
            if PAYLOAD[parameter] is not None:
                intProgressValue += 1
        return str(intProgressValue)
        
