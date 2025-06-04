from dev.frontend.pages.dashboard import dashboard
from dev.frontend.pages.onboarding import onboarding
from dash import Dash, html, dcc, callback, Input, Output



app = Dash()


app.layout = html.Div([
    dcc.Location(id='url'),
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/dashboard':
        return dashboard
    elif pathname == '/onboarding':
        return onboarding
    else:
        return onboarding

# render first page here
if __name__ == '__main__':
    app.run(
        debug=True, 
        dev_tools_hot_reload=True, 
        dev_tools_hot_reload_interval=True, 
        dev_tools_ui=False
        )
    
