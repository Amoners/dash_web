# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import requests

app = dash.Dash(__name__, static_folder='assets')

app.css.config.serve_locally = True
app.scripts.append_script({
    'external_url': '/assets/demo.js'
})

app.layout = html.Div(children=[
    html.Link(href='assets/index_hk.css', rel='stylesheet'),
    html.Link(href='assets/bootstrap.min.css', rel='stylesheet'),
    dcc.Location(id='url', refresh=False),
    dcc.Interval(
        id='interval-component',
        interval=1 * 1000,  # in milliseconds
        n_intervals=0
    ),
    html.Nav(children=[
        html.A('Calculus', href="#", className='navbar-brand'),
        html.Div(
            id="navbarSupportedContent",
            children=[
                html.Ul(children=[
                    html.Li(
                        html.A("Index", href="#", className="nav-link"),
                        className="nav-item"
                    ),
                    html.Li(
                        html.A("portfolio", href="#", className="nav-link"),
                        className="nav-item"
                    ),
                    html.Li(
                        html.A("asset", href="#", className="nav-link"),
                        className="nav-item"
                    )
                ],
                    className="navbar-nav"),
            ],
            className='collapse navbar-collapse'),
    ],
        className='navbar navbar-expand-lg navbar-light bg-light'),
    html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        style={'width': '200px'},
                        children=[
                            html.A(
                                children='index',
                                href="#",
                                className='list-group-item  list-group-item-action'
                            ),
                            html.A(
                                children='exchange',
                                href="#",
                                className='list-group-item  list-group-item-action'
                            ),
                            html.A(
                                children='coin',
                                href="#",
                                className='list-group-item  list-group-item-action'
                            ),
                        ],
                        className='list-group'
                    ),
                ],
            ),
        ],
        className='plot_div'
    ),
    html.Div(
        dcc.Graph(
            id='cal_chart',

        )
    )
])

@app.callback(Output('cal_chart', 'figure'),
              [Input('interval-component', 'n_intervals')])
def draw_plot(n_intervals):
    req_url = "http://47.75.103.110:5000/dv"
    res = requests.get(req_url)
    dates = []
    price = []
    if res.status_code == 200:
        a = res.json()
        for i, j in a:
            dates.append(i)
            price.append(j)
    fig = {
        'data': [{
            #x=dates,
            #y=price,
            'x': dates,
            'y': price,
            'mode': 'line'
        }],
        'layout': {
            'title': '本征指数'
        }
    }
    return fig


if __name__ == '__main__':
    app.run_server(host='0.0.0.0')
