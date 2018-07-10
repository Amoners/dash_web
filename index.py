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
    'external_url': '../assets/jquery-3.3.1.min.js',
})
app.scripts.append_script({
    'external_url': '/assets/demo.js'
})

app.layout = html.Div(children=[
    html.Link(href='assets/index_hk.css', rel='stylesheet'),
    html.Link(href='assets/demo.css', rel='stylesheet'),
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
                style={'width': '120px', 'float': 'left'},
                children=[
                    html.Div(
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
        children=[
            html.Div(
                id='indexChart',
                style={
                    'width': '100%',
                    'margin': '0 auto',
                    'position': 'relative',
                    'height': '550px'
                },
                children=[
                    dcc.Graph(
                        id='cal_chart',
                        config={'displayModeBar': False}
                    ),
                    html.Div(
                        style={
                            'display': 'block',
                            'width': '250px',
                            'position': 'absolute',
                            'left': '8%',
                            'top': '17%',
                        },
                        children=[
                            html.H3('Introducing', className='index__subheader'),
                            html.H1('Calculus指数'),
                            html.Button('5mins', id='5mu', value=5, className='btn btn-primary'),
                        ],
                        className='index__header'
                    ),
                ],
                className='index-chart'
            )]

    )
])


@app.callback(Output('cal_chart', 'figure'),
              [Input('interval-component', 'n_intervals')])
def draw_plot(n_intervals):
    #req_url = "http://47.75.103.110:5000/dv"
    req_url = "http://sb.com/dv"
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
            'x': dates,
            'y': price,
            'mode': 'line',
            'line': dict(width=2,
                      color= ('#009e73')),
            'hoverlabel': {
                'font': {
                    'family': "courier",
                    'size': 20,
                    'color': "#f00"
                },
                'bgcolor': '#f8f9fa',
                 'bordercolor': "#080"

            },
        }],
        'layout': {
            'xaxis': {
                'tickformat': '%Y-%m-%d',
                'showGrid': False,
                'gridcolor': "#ff00",
                 'zeroline': True,
            },
            'yaxis': {
                'tickprefix': "Index\n",
                'showGrid': False,
                'gridcolor': "#ff00",
                'showticklabels': False
            },
            'aaxis': { 'showgrid': False},
            'hovermode': 'closest',
            'bgcolor': '#ff0000',
        }
    }
    return fig


@app.callback(Output('interval-component', 'interval'),
              [Input('5mu', 'value')])
def change_intervals(value):
    intervals = value * 60 * 1000
    return intervals


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
