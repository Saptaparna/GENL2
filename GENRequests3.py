# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import html
from dash import dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(children=[
        html.Label('Dropdown'),
        dcc.Dropdown(
            options=[
                {'label': 'Leading order', 'value': 'NYC'},
                {'label': 'Next-to-Leading order', 'value': 'MTL'},
                {'label': 'Decay Mode', 'value': 'SF'}
            ],
            value='MTL'
        ),

        html.Br(),
        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(
            options=[
                {'label': 'Leading order', 'value': 'NYC'},
                {'label': 'Next-to-Leading order', 'value': 'MTL'},
                {'label': 'Decay Mode', 'value': 'SF'}
            ],
            value=['MTL', 'SF'],
            multi=True
        ),

        html.Br(),
        html.Label('Items'),
        dcc.RadioItems(
            options=[
                {'label': 'Leading order', 'value': 'NYC'},
                {'label': 'Next-to-Leading order', 'value': 'MTL'},
                {'label': 'Decay Mode', 'value': 'SF'}
            ],
            value='MTL'
        ),
    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        html.Label('Checkboxes'),
        dcc.Checklist(
            options=[
                {'label': 'Leading order', 'value': 'NYC'},
                {'label': 'Next-to-Leading order', 'value': 'MTL'},
                {'label': 'Decay Mode', 'value': 'SF'}
            ],
            value=['MTL', 'SF']
        ),

        html.Br(),
        html.Label('Text Input'),
        dcc.Input(value='MTL', type='text'),

        html.Br(),
        html.Label('Slider'),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
            value=5,
        ),
    ], style={'padding': 10, 'flex': 1})
], style={'display': 'flex', 'flex-direction': 'row'})

if __name__ == '__main__':
    app.run_server(debug=True)
