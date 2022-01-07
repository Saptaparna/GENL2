# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import dcc
from dash import html
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
import pandas as pd
import requests

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__)
app = dash.Dash(name='multiline', external_stylesheets=external_stylesheets)

base_url = 'https://raw.githubusercontent.com/cms-sw/genproductions/master/bin/MadGraph5_aMCatNLO/cards/production/13TeV/VV/WWTo4Q_4f_amcatnloFxFx/'
proc_url = base_url + 'WWTo4Q_4f_amcatnloFxFx_proc_card.dat'

proc_html_file = requests.get(proc_url).text
print (proc_html_file)

run_url = base_url + 'WWTo4Q_4f_amcatnloFxFx_run_card.dat'
run_html_file = requests.get(run_url).text
print (run_html_file)

madspin_url = base_url + 'WWTo4Q_4f_amcatnloFxFx_madspin_card.dat'
madspin_html_file = requests.get(madspin_url).text
print (madspin_html_file)

#url_samples = 'https://pdmv-pages.web.cern.ch/main_bkg_ul/index.html'

#df = pd.read_html(url_samples, attrs={'class': 'dataframe'},
#                  header=0, flavor='html5lib')[0]

#print (df)

#df_proc = pd.read_html('https://raw.githubusercontent.com/cms-sw/genproductions/master/bin/MadGraph5_aMCatNLO/cards/production/13TeV/VV/WWTo4Q_4f_amcatnloFxFx/WWTo4Q_4f_amcatnloFxFx_proc_card.dat')

#print ('https://raw.githubusercontent.com/cms-sw/genproductions/master/bin/MadGraph5_aMCatNLO/cards/production/13TeV/VV/WWTo4Q_4f_amcatnloFxFx/WWTo4Q_4f_amcatnloFxFx_proc_card.dat')

app.layout = html.Div([
    html.Div(children=[
        html.Label('Process'),
        dcc.Dropdown(
            id='dropdown-process',
            options=[
                {'label': 'WWTo4Q_4f_amcatnloFxFx', 'value': proc_html_file.strip("\n")}, #'value': 'https://github.com/cms-sw/genproductions/blob/master/bin/MadGraph5_aMCatNLO/cards/production/13TeV/VV/WWTo4Q_4f_amcatnloFxFx/WWTo4Q_4f_amcatnloFxFx_proc_card.dat'},
            ],
            value='https://github.com/cms-sw/genproductions/blob/master/bin/MadGraph5_aMCatNLO/cards/production/13TeV/VV/WWTo4Q_4f_amcatnloFxFx/WWTo4Q_4f_amcatnloFxFx_proc_card.dat'
        )#,
        #html.Div(id='dd-output-container')
    ], style={'padding': 10, 'flex': 1}),
    html.Div(children=[
        html.Label('Cards'),
        dcc.Dropdown(
            id='dropdown-cards',
            options=[
                {'label': 'proc_card', 'value': proc_html_file}, #'value': 'https://raw.githubusercontent.com/cms-sw/genproductions/master/bin/MadGraph5_aMCatNLO/cards/production/13TeV/VV/WWTo4Q_4f_amcatnloFxFx/WWTo4Q_4f_amcatnloFxFx_proc_card.dat'}
                {'label': 'run_card', 'value': run_html_file},
                {'label': 'madspin_card', 'value': madspin_html_file},    
                #{'label': 'proc_card', 'value': 'https://raw.githubusercontent.com/cms-sw/genproductions/master/bin/MadGraph5_aMCatNLO/cards/production/13TeV/VV/WWTo4Q_4f_amcatnloFxFx/WWTo4Q_4f_amcatnloFxFx_proc_card.dat'},
                #{'label': 'run_card', 'value': 'https://raw.githubusercontent.com/cms-sw/genproductions/master/bin/MadGraph5_aMCatNLO/cards/production/13TeV/VV/WWTo4Q_4f_amcatnloFxFx/WWTo4Q_4f_amcatnloFxFx_run_card.dat'},
                #{'label': 'madspin_card', 'value': 'https://raw.githubusercontent.com/cms-sw/genproductions/master/bin/MadGraph5_aMCatNLO/cards/production/13TeV/VV/WWTo4Q_4f_amcatnloFxFx/WWTo4Q_4f_amcatnloFxFx_madspin_card.dat'}
            ],
        ),
        html.Div(id='dd-output-container')
], style={'white-space': 'pre', 'overflow-y': 'scroll', 'overflow-x': 'scroll', 'height': '50vh', 'padding': 10, 'flex': 1}) #style={'display': 'flex', 'flex-direction': 'row'}), #style={'white-space': 'pre', 'overflow-y': 'scroll', 'overflow-x': 'scroll', 'height': '50vh', 'width': '170vh', 'padding': 10, 'flex': 1}) #style={'display': 'flex', 'flex-direction': 'row'}),
])

@app.callback(
    Output('dd-output-container', 'children'),
    Input('dropdown-cards', 'value')
)
def update_output(value):
    #print (value)  
    #return 'You have selected "{}"'.format(value) 
    return format(value) 

#def print_output(value):
#    return print ('You have selected "{}"'.format(value))

if __name__ == '__main__':
    app.run_server(debug=True)
