import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

# Create a DataFrame from the .csv file:
#df = pd.read_csv('../data/mpg.csv')
df = pd.read_csv('/Users/rah/Desktop/github/DASH/dash-project-2/data/mpg.csv')
#creates a list of column names
features = df.columns

# Create a Dash layout that contains a Graph component:
layout = html.Div([ # app layout has three dcc components > 2 dropdowns and 1 graph > division takes in a list

    html.Div([
        dcc.Dropdown(
            id='xaxis',
            options=[{'label': i.title(), 'value': i} for i in features],
            value='displacement'
        )
    ],
    style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(
            id='yaxis',
            options=[{'label': i.title(), 'value': i} for i in features],
            value='acceleration'
        )
    ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

dcc.Graph(id='feature-graphic')
], style={'padding':30})