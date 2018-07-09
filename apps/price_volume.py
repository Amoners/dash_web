# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import keywordsJson as kwj
import time
import requests
import plotly.tools as tls
import plotly.graph_objs as go

app = dash.Dash(__name__, static_folder='../assets')

colors = {
    'background': '#000000',
    'text': '#ffffff'
}

app.css.config.serve_locally = True
app.config.supress_callback_exceptions = True
app.scripts.append_script({
    'external_url': '../assets/jquery-3.3.1.min.js',
})
app.scripts.append_script({
    'external_url': '../assets/demo.js'
})
app.scripts.append_script({
    'external_url': '../assets/plotly-1.38.0.min.js'
})

app.layout = html.Div(children=[
    html.Link(href='../assets/demo.css', rel='stylesheet'),
    html.Link(href='../assets/style1.css', rel='stylesheet'),
    html.Link(href='../assets/style2.css', rel='stylesheet'),
    html.Link(href='../assets/style3.css', rel='stylesheet'),
    dcc.Location(id='url', refresh=False),
    html.Ul(id='para', key='para'),
    html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(
            html.A('DASH WEB DEMO', href='/'),
            style={
                'textAlign': 'left',
                'padding': '25px',
                'color': colors['text']
            }
        )]),
    html.Div(
        children=[
            html.Div([
                html.Div(
                    style={'float': 'left'},
                    children=[
                        html.Div(children=[
                            html.H3(children='Markets', className='center'),
                            html.Hr(style={'border-color': '#ddd'}),
                            html.Ul(id='markets', key='markets', className='nav nav-tabs nav-stacked data_type')
                        ])
                        # html.Div(children=[
                        #     html.H3(children='Blockchain', className='center'),
                        #     html.Hr(style={'border-color': '#ddd'}),
                        #     html.Ul(id='blockchain', key='blockchain', className='nav nav-tabs nav-stacked data_type')
                        # ])
                    ]
                ),
                html.Div([
                    html.Div(id='chart'),

                ],
                    className='span10 main_content'
                ),
            ],
                className='row-fluid'
            )],
        className='container-fluid'
    )
])


def create_div(pathname):
    if pathname is None or pathname == '/':
        pass
    else:
        types = pathname.split('/')[1]
        kw = pathname.split('/')[2]
        return html.Div([
                html.Div(
                    html.Div(
                        html.H3(
                            children=kwj.get_kw_value(types, kw, 'title'),
                            className='title'
                        ),
                        className='span12'
                    ),  # title div
                    className='row-fluid'
                ),
                html.Div([
                    html.Div([
                        html.Span([
                            html.A('10m', href='#', className='v_10m btn btn-mini'),
                            html.A('1h', href='#', className='v_1h btn btn-mini'),
                            html.A('6h', href='#', className='v_6h btn btn-mini'),
                            html.A('24h', href='#', className='v_24h btn btn-mini'),
                            html.A('3d', href='#', className='v_3d btn btn-mini'),
                            html.A('7d', href='#', className='v_7d btn btn-mini'),
                            html.A('30d', href='#', className='v_30d btn btn-mini'),
                            html.A('6m', href='#', className='v_6m btn btn-mini'),
                            html.A('2y', href='#', className='v_2y btn btn-mini'),
                            html.A('5y', href='#', className='v_5y btn btn-mini'),
                            html.A('all', href='#', className='v_all btn btn-mini')

                        ],
                            className='timespans btn-group'
                        )

                    ],
                        className='span4'
                    ),  # timespan
                    html.Div([
                        html.Span([
                            html.A('auto', href='#', style={"display": "inline-block"},
                                   className='v_auto btn btn-mini disabled btn-primary'),
                            html.A('hour', href='#', style={"display": "inline-block"},
                                   className='v_hour btn btn-mini'),
                            html.A('day', href='#', style={"display": "inline-block"}, className='v_day btn btn-mini'),
                            html.A('week', href='#', style={"display": "inline-block"}, className='v_week btn btn-mini')

                        ],
                            className='resolutions btn-group'
                        )
                    ],
                        className='span4 offset4 text-right'),
                ],
                    className='row-fluid'
                ),  # escape
                html.Div([
                    dcc.Graph(
                        id='abccc',
                    ),

                ],
                    className='row-fluid chart_data'
                ),  # show chart in this div
                html.Div([

                ],
                    className='row-fluid'
                )  # options for data
            ]
            )


@app.callback(Output("markets", "children"),
              [Input('markets', 'key')])
def get_market_item(word_key):
    kws = kwj.get_kw(word_key)
    template = []
    for key in kws:
        template.append(kwj.gen_html_item(word_key, key))
    return template


@app.callback(Output('abccc', 'figure'),
              [Input('url', 'pathname')])
def gene_chart(key):
    api_url = "https://data.bitcoinity.org/chart_data?data_type=price_volume&currency=USD&exchange=all&compare=no&volume_unit=curr&function=none&timespan=3d&groups_count=10&resolution=day&chart_type=line_bar&smoothing=linear&scale_type=lin&chart_types="
    res = requests.get(api_url)
    if res.status_code == 200:
        a = res.json()
        fig = tls.make_subplots(rows=2, cols=1, shared_xaxes=True),
        stime = [2015, 2016, 2017]
        price = [l[1] for l in a['data'][0]['values']]
        volume = [t[1] for t in a['data'][1]['values']]
        trace1 = go.Bar(
            x=stime,
            y=price,
            x0=3,
            name='price[BTC/USD]'
        )
        trace2 = go.Scatter(
            x=stime,
            x0=3,
            y=volume,
            name='volume[USD]',
            yaxis='y2'
        )
        data = [trace1, trace2]
        layout = go.Layout(
            title='Price and Volume',
            yaxis=dict(title='price'),
            yaxis2=dict(title='volume', overlaying='y', side='right')
        )
        fig = go.Figure(data=data, layout=layout)
        return fig
# @app.callback(Output("blockchain", "children"),
#               [Input('blockchain', 'key')])
# def get_blockchain_item(word_key):
#     kws = kwj.get_kw(word_key)
#     template = []
#     for key in kws:
#         template.append(kwj.gen_html_item(word_key, key))
#     return template


@app.callback(Output('chart', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    return create_div(pathname)


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
