import plotly.express as px
import plotly.graph_objects as go

results_by_events = {'phantom': 0, 'Powheg-Openloops': 52059210, 'herwig': 0, 'amcatnlo': 4945503176, 'sherpa': 0, 'evtgen': 437539490, 'pythiaOnly': 3870975276, 'unknown': 629678000, 'powheg': 11686162250, 'pythia': 24345882594, 'madgraph': 3380970251, 'amcatnloFXFX': 4588947176, 'herwigOnly': 0, 'mcfm': 24732151, 'madgraphMLM': 2547392822, 'powhegMiNNLO': 4026908351}

results_by_sample = {'phantom': 0, 'Powheg-Openloops': 36, 'herwig': 0, 'amcatnlo': 304, 'sherpa': 0, 'evtgen': 143, 'pythiaOnly': 554, 'unknown': 64, 'powheg': 317, 'pythia': 4851, 'madgraph': 3496, 'amcatnloFXFX': 120, 'herwigOnly': 0, 'mcfm': 37, 'madgraphMLM': 182, 'powhegMiNNLO': 27}

#results_by_events = {'phantom': 0, 'Powheg-Openloops': 13751647, 'herwig': 0, 'amcatnlo': 1650274627, 'sherpa': 0, 'evtgen': 78948995, 'pythiaOnly': 1047133631, 'unknown': 153132400, 'powheg': 2973963822, 'pythia': 6749059677, 'madgraph': 995739419, 'amcatnloFXFX': 1587714627, 'herwigOnly': 0, 'mcfm': 2999183, 'madgraphMLM': 848950666, 'powhegMiNNLO': 982744850}

#results_by_sample = {'phantom': 0, 'Powheg-Openloops': 9, 'herwig': 0, 'amcatnlo': 63, 'sherpa': 0, 'evtgen': 17, 'pythiaOnly': 123, 'unknown': 17, 'powheg': 71, 'pythia': 925, 'madgraph': 645, 'amcatnloFXFX': 36, 'herwigOnly': 0, 'mcfm': 6, 'madgraphMLM': 47, 'powhegMiNNLO': 7}

df = results_by_events.items() 
print (results_by_events.values())
print (results_by_events.keys())

values = []
keys = []
valueAMC = 0
valueAMCFXFX = 0
valueLO = 0
valueLOMLM = 0
valuePOWHEG = 0
valuePOWHEGNNLO = 0
valueOpenloops = 0
for key, value in results_by_events.items():
  if key=='sherpa':
    value = 2000000000
  if key=='pythia': 
    value = 0
  if key=='herwig':
    value = 200000000
  if key=='amcatnlo':
    valueAMC = value
    print (valueAMC)
  if key=='amcatnloFXFX':
    valueAMCFXFX = value
    print  (valueAMCFXFX)
  if key=='madgraph':
    valueLO = value
  if key=='madgraphMLM':
    valueLOMLM = value
  if key=='powheg':
    valuePOWHEG = value
  if key=='powhegMiNNLO':
    valuePOWHEGNNLO = value
  if key=='Powheg-Openloops':
    valueOpenloops = value
    value = 0
  if key=='evtgen':
    key='evtgen+pythia'
  if key=='unknown':
    key='other generators'
  if value>0:
    values.append(value)
    keys.append(key)
  #if key=='amcatnlo':
valueDiff = valueAMC - valueAMCFXFX #valueNLO[0] - valueNLO[1] 
print ('valueDiff = ', valueDiff)
valueDiffLO = valueLO - valueLOMLM
valueDiffPOWHEG =  valuePOWHEG - valuePOWHEGNNLO 
valueOpenloops = valueOpenloops
total = 0
keys_accuracy = []
values_accuracy = []
for i in range(0, len(values)):
  if keys[i]=='amcatnlo':
    values[i] = valueDiff  
  if keys[i]=='madgraph':
    values[i] = valueDiffLO
  if keys[i]=='powheg':
    values[i] = valueDiffPOWHEG+valueOpenloops
#  if keys[i]==('madgraph' or 'herwig' or 'sherpa' or 'evtgen' or 'pythiaOnly'):
#    keys_accuracy[i] = 'LO'
#    values_accuracy[i] += values[i]
#  else if keys[i]==('madgraphMLM'): 
  total += values[i]
print ('total = ', total)
print (values)
fig = go.Figure(data=[go.Pie(labels=keys, values=values)])
fig.show()
fig.write_image("piechart_UL_events.pdf")
fig.write_image("piechart_UL_events.png")
