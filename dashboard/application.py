import secrets
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_auth
from dateutil.relativedelta import relativedelta
secret = secrets.token_hex(16)
from transform import data as df
from datetime import datetime as dt
import plotly.graph_objs as go

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

list_audience = []
for audience in df.Audience.unique():
    temp_dic = {'label': audience, 'value': audience}
    list_audience.append(temp_dic)

list_location = []
for location in df.Location.unique():
    temp_dic = {'label': location, 'value': location}
    list_location.append(temp_dic)

list_site = []
for site in df.Site.unique():
    temp_dic = {'label': site, 'value': site}
    list_site.append(temp_dic)

list_fold = []
for fold in df.Fold_Position.unique():
    temp_dic = {'label': fold, 'value': fold}
    list_fold.append(temp_dic)

app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Overall', value='tab-1'),
        dcc.Tab(label='Over Time', value='tab-2'),
        dcc.Tab(label='Geographic', value='tab-3'),
        dcc.Tab(label='More Charts', value='tab-4'),
    ]),
    html.Div(id='tabs-content'),

    dcc.DatePickerRange(
        id='date_picker',
        min_date_allowed=df['Date'].min(),
        max_date_allowed=df['Date'].max(),
        display_format='Do MMM, YY',
        initial_visible_month=df['Date'].min(),
        start_date=df['Date'].min(),
        end_date=df['Date'].max()
    ),

    dcc.Dropdown(
        id='audience_dropdown',
        placeholder="Select Audience",
        options=list_audience,
        multi=True,
        value='18 - 25',
        style={
            #        'height': '15px',
            #        'width': '50%',
            #        'font-size': "100%",
            #         'min-height': '100%',
            #        'display': 'inline-block',
        }
    ),


    dcc.Dropdown(
        id='location_dropdown',
        placeholder="Select Location",
        options=list_location,
        multi=True,
        value='London',
        style={
            #        'height': '15px',
            #        'width': '50%',
            #        'font-size': "100%",
            #         'min-height': '100%',
            #        'display': 'inline-block',
            }
    ),

    dcc.Dropdown(
        id='site_dropdown',
        placeholder="Select Publisher",
        options=list_site,
        value='Independent',
        multi=True,
        style={
            #        'height': '15px',
            #        'width': '50%',
            #        'font-size': "100%",
            #         'min-height': '100%',
            #        'display': 'inline-block',
            }
    ),

    dcc.Checklist(
        id='fold_checklist',
        options=list_fold,
        labelStyle={'display': 'inline-block'}
    )

])

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value'),
               Input('audience_dropdown', 'value'),
               Input('date_picker', 'start_date'),
               Input('date_picker', 'end_date'),
               Input('location_dropdown', 'value'),
               Input('site_dropdown', 'value'),
               Input('fold_checklist', 'value')])
def render_content(tab, audience_dropdown, start_date, end_date,location_dropdown, site_dropdown, fold_checklist):
    if tab == 'tab-1':
        print ("tab1")

        return html.Div(children=[html.H1(children='Hello Dash1'),
                                  html.H1(children='Hello Dash2'),
                                  html.H1(children='Hello Dash3'),
                                  html.H1(children='Hello Dash4'),
                                  html.H1(children='Hello Dash5'),
                                  html.H1(children='Hello Dash6'),
                                  html.H1(children='Hello Dash7'),
                                  html.H1(children='Hello Dash8'),
                                  html.H1(children='Hello Dash9')

            ,start_date, end_date,audience_dropdown, location_dropdown, site_dropdown, fold_checklist,

        ],style={'columnCount': 3})



    elif tab == 'tab-2':
        print ("tab2")
        print (audience_dropdown)

        return html.Div(children=[start_date, end_date, audience_dropdown, location_dropdown, site_dropdown, fold_checklist,

            html.Div(children='''
                    Dash: A web application framework for Python.
                '''),

            dcc.Graph(
                id='example-graph2',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization'
                    }
                }
            )
        ])



    elif tab == 'tab-3':
        print ("tab3")
        return html.Div([
            html.H3('Tab content 3'),audience_dropdown, location_dropdown, site_dropdown,fold_checklist,
        ])




    elif tab == 'tab-4':
        print ("tab4")
        return html.Div(children=[start_date, end_date, audience_dropdown, location_dropdown, site_dropdown, fold_checklist,

            html.Div(children='''
                    Dash: A web application framework for Python.
                '''),

            dcc.Graph(
                id='example-graph3',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization'
                    }
                }
            ),

              dcc.Graph(
                  id='example-graph4',
                  figure={
                      'data': [
                          {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                          {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
                      ],
                      'layout': {
                          'title': 'Dash Data Visualization'
                      }
                  }
              ),

        ], style={'columnCount': 2})

if __name__ == '__main__':
    app.run_server(debug=True)