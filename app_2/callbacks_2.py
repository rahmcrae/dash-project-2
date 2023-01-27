from dash.dependencies import Input, Output, State
from app_2 import app
import plotly.graph_objs as go 
import pandas as pd

# Create a DataFrame from the .csv file:
#df = pd.read_csv('../data/mpg.csv')
df = pd.read_csv('/Users/rah/Desktop/github/DASH/dash-project-2/data/mpg.csv')
#creates a list of column names
features = df.columns


@app.callback(
    Output('feature-graphic', 'figure'),
    [Input('xaxis', 'value'),
     Input('yaxis', 'value')])
def update_graph(xaxis_name, yaxis_name):
    return {
        'data': [go.Scatter(
            x=df[xaxis_name],
            y=df[yaxis_name],
            text=df['name'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            title= yaxis_name.title()+' vs. '+xaxis_name.title(),
            xaxis={'title': xaxis_name.title()},
            yaxis={'title': yaxis_name.title()},
            margin={'l': 40, 'b': 40, 't': 50, 'r': 0}, #adds margin for the graph
            hovermode='closest'
        )
    }
