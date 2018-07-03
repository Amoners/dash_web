# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
import tushare as ts
import plotly.graph_objs as go
import easyquotation
from dash.dependencies import Input, Output

app = dash.Dash(__name__, static_folder='assets')

colors = {
    'background': '#000000',
    'text': '#ffffff'
}


all_types = {
    'exchanges': 'exchanges',
    'volume': 'trading volume',
    'rank': 'Exchanges ranking',
    'price': 'price',
    'price_volume': 'price and volume',
    'market_cap': 'market capitalization',
    'tradespm': 'Number of trades per minute',
    'volatility': 'price volatility',
    'arbitrage': 'markets arbitrage table',
    'books': 'Combined order book',
    'spread': 'Bid-ask spread',
    'bidask_sum': 'Bid/ask sum within 10% range from the price',
    'hashrate': 'hashrate',
    'difficulty': 'mining difficulty',
    'size': 'blocks size',
    'block_version': 'blocks version',
    'tx_count': 'Number of transactions',
    'block_time': 'Average time to mine a block in minutes',
    'block_size_votes': 'Block size votes'
}

app.css.config.serve_locally = True

app.layout = html.Div(children=[
    html.Link(href='/assets/demo.css', rel='stylesheet'),
    dcc.Location(id='url', refresh=False),
    html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(
            # html.A('DASH WEB DEMO', href='/'),
            children='自选股行情查看',
            style={
                'textAlign': 'left',
                'padding': '25px',
                'color': colors['text']
            }
        )]),
    dcc.Input(id='stock_no', type='text', value='300222', name='请输入自选股股票代号'),
    html.Div(id='price_real'),
    html.Div(id='plot_type'),
    dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
])


@app.callback(dash.dependencies.Output('price_real', 'children'),
                [dash.dependencies.Input('interval-component', 'n_intervals'),
                 dash.dependencies.Input('stock_no', 'value')])
def update_price(n_intervals, value):
    quotation = easyquotation.use('sina')
    stock_info = quotation.real(str(value))
    # {'300222': {'name': '科大智能', 'open': 16.83, 'close': 17.06,
    # 'now': 17.43, 'high': 17.48, 'low': 16.75, 'buy': 17.42, 'sell': 17.43,
    # 'turnover': 3917918, 'volum:67496164.2, 'bid1_volume': 18300, 'bid1': 17.42,
    # 'bid2_volume': 2000, 'bid2': 17.4, 'bid3_volume': 7300, 'bid3': 17.39,
    # 'bid4_volume': 10200, 'bid4': 17.38, 'bid5_volume': 500, 'bid5': 17.37,
    # 'ask1_volume': 3900, 'ask1': 17.43, 'ask2_volume': 45700, 'ask2': 17.44,
    # 'ask3_volume': 42500, 'ask3': 17.45, 'ask4_volume': 10100, 'ask4': 17.46,
    # 'ask5_volume': 15100, 'ask5': 17.47, 'date': '2018-06-26', 'time': '15:05:03'}}
    return html.P(children=stock_info[str(value)]['bid1'])


def create_div(value):
    df = ts.get_tick_data(value, date='2018-06-26').reset_index().sort_values('time')
    xais = df.ix[:, 'time']
    yais = df.ix[:, 'price']
    return html.Div([
        html.H1(
            style={
                'textAlign': 'center',
                'color': colors['background'],
            },
            children=value,
        ),
        dcc.Graph(
            id='price_list',
            figure={
            'data': [
                go.Scatter(
                x=xais,
                y=yais,
                mode='lines'
    )],
            })


    ])


@app.callback(dash.dependencies.Output('plot_type', 'children'),
              [dash.dependencies.Input('stock_no', 'value')])
def display_page(value):
    return create_div(value)


if __name__ == '__main__':
    #app.run_server(host='0.0.0.0')
    # quotation = easyquotation.use('sina')
    # stock_info = quotation.real('300222')
    # print(stock_info['300222'])
    print(ts.get_gem_classified())
