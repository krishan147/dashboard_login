import secrets
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_auth
from dateutil.relativedelta import relativedelta
secret = secrets.token_hex(16)
from transform import data as df

df = (df())

VALID_USERNAME_PASSWORD_PAIRS = [
    ['hello', 'world']
]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Tab one', value='tab-1'),
        dcc.Tab(label='Tab two', value='tab-2'),
        dcc.Tab(label='Tab three', value='tab-3'),
        dcc.Tab(label='Tab four', value='tab-4'),
        dcc.Tab(label='Tab five', value='tab-5'),
        dcc.Tab(label='Tab six', value='tab-6'),
    ]),
    html.Div(id='tabs-content')
])

slider = (dcc.Slider(
    id='date-slider',
    min=df['Date_Num'].min(),
    max=df['Date_Num'].max(),
    value=df['Date_Num'].min(),
    marks={str(year): str(year) for year in df['Date_Num'].unique()},
    step=None
))

# https://dash.plot.ly/getting-started
# https://dash.plot.ly/getting-started-part-2

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        print ("tab1")

        return html.Div(children=[
            html.H1(children='Hello Dash '),slider,

            html.Div(children='''
                Dash: A web application framework for Python.
            '''),

            dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization'
                    }
                }
            )
        ])








    elif tab == 'tab-2':
        print ("tab2")
        return html.Div([
            html.H3('Tab content 2'),slider
        ])
    elif tab == 'tab-3':
        print ("tab3")
        return html.Div([
            html.H3('Tab content 3'),slider
        ])
    elif tab == 'tab-4':
        print ("tab4")
        return html.Div([
            html.H3('Tab content 4'),slider
        ])
    elif tab == 'tab-5':
        print ("tab5")
        return html.Div([
            html.H3('Tab content 5'),slider
        ])
    elif tab == 'tab-6':
        print ("tab6")
        return html.Div([
            html.H3('Tab content 6'),slider
        ])

if __name__ == '__main__':
    app.run_server(debug=True)