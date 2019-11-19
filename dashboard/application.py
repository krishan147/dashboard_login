# need to split this out also
import secrets
import pandas as pd
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
import base64
import requests
requests.packages.urllib3.disable_warnings()
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

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
        dcc.Tab(label='Heatmap', value='tab-3'),
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
        print (start_date, end_date, audience_dropdown, location_dropdown, site_dropdown, fold_checklist)

        if type(audience_dropdown) is list:
            pass
        else:
            list(audience_dropdown)

        if type(location_dropdown) is list:
            pass
        else:
            list(location_dropdown)

        df_tabone = df.loc[df.Audience.isin(audience_dropdown) & df.Location.isin(location_dropdown)]

        sales = df_tabone['Sales'].sum()

        return html.Div(children=[html.H1(children=str(sales)),
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
            dcc.Graph(
                id='heatmap',
                figure={
                    'data': [{
                        'z': [
                            [1, 2, 3],
                            [4, 5, 6]
                        ],
                        'text': [
                            ['a', 'b', 'c'],
                            ['d', 'e', 'f']
                        ],
                        'customdata': [
                            ['c-a', 'c-b', 'c-c'],
                            ['c-d', 'c-e', 'c-f'],
                        ],
                        'type': 'heatmap'
                    }]
                }
            ),
            html.Div(id='output')
        ])




    elif tab == 'tab-4':
        print ("tab4")
        return html.Div(children=[start_date, end_date, audience_dropdown, location_dropdown, site_dropdown, fold_checklist,

            html.Div(children='''
                    Dash: A web application framework for Python.
                '''),

                                  dcc.Graph(
                                      figure=go.Figure(
                                          data=[
                                              go.Bar(
                                                  x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                                                     2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                                                  y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                                                     350, 430, 474, 526, 488, 537, 500, 439],
                                                  name='Rest of world',
                                                  marker=go.bar.Marker(
                                                      color='rgb(55, 83, 109)'
                                                  )
                                              ),
                                              go.Bar(
                                                  x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                                                     2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                                                  y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                                                     299, 340, 403, 549, 499],
                                                  name='China',
                                                  marker=go.bar.Marker(
                                                      color='rgb(26, 118, 255)'
                                                  )
                                              )
                                          ],
                                          layout=go.Layout(
                                              title='US Export of Plastic Scrap',
                                              showlegend=True,
                                              legend=go.layout.Legend(
                                                  x=0,
                                                  y=1.0
                                              ),
                                              margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                                          )
                                      ),
                                      style={'height': 300},
                                      id='my-graph'
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

            generate_table(df),



        ], style={'columnCount': 2})

if __name__ == '__main__':
    app.run_server(debug=True)