import dash_html_components as html
import dash_core_components as dcc

layout = html.Div([
    html.H1('My Dash App'),
    dcc.Input(id='input-1', value='initial value', type='text'),
    html.Div(id='output-1')
])