import secrets
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_auth
secret = secrets.token_hex(16)

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

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        print ("tab1")
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab == 'tab-2':
        print ("tab2")
        return html.Div([
            html.H3('Tab content 2')
        ])
    elif tab == 'tab-3':
        print ("tab3")
        return html.Div([
            html.H3('Tab content 3')
        ])
    elif tab == 'tab-4':
        print ("tab4")
        return html.Div([
            html.H3('Tab content 4')
        ])
    elif tab == 'tab-5':
        print ("tab5")
        return html.Div([
            html.H3('Tab content 5')
        ])
    elif tab == 'tab-6':
        print ("tab6")
        return html.Div([
            html.H3('Tab content 6')
        ])

if __name__ == '__main__':
    app.run_server(debug=True)