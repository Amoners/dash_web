# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
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
            html.A('DASH WEB DEMO', href='/'),
            # children='DASH WEB DEMO',
            style={
                'textAlign': 'left',
                'padding': '25px',
                'color': colors['text']
            }
        )]),
    html.Div(style={'float': 'left'}, children=[
        html.Div(children=[
            html.H1(
                children='Markets',
                style={
                    'textAlign': 'center',
                    'color': colors['background'],
                }
            ),
            html.Hr(),
            dcc.Markdown('''
            * [Exchanges List](/markets/exchanges)
            * [Trading Volume](/markets/volume)
            * [Rank](/markets/rank)
            * [Price](/markets/price)
            * [Price + Volume](/markets/price_volume)
            * [Market Cap](/markets/market_cap)
            * [Trades Per Minute](/markets/tradespm)
            * [Volatility](/markets/volatility)
            * [Arbitrage](/markets/arbitrage)
            * [Combined Order Book](/markets/books)
            * [Bid/Ask Spread](/markets/spread)
            * [Bid/Ask Sum](/markets/bidask_sum)
        '''.replace('    ', '')),

        ]),
        html.Div(children=[
            html.H1(
                children='Blockchain',
                style={
                    'textAlign': 'center',
                    'color': colors['background'],
                }
            ),
            html.Hr(),
            dcc.Markdown('''
            * [Hashrate](/blockchain/hashrate)
            * [Mining Difficulty](/blockchain/difficulty)
            * [Block Size](/blockchain/size)
            * [Block Version](/blockchain/block_version)
            * [Number Of Transactions](/blockchain/tx_count)
            * [Time Between Blocks](/blockchain/block_time)
            * [Block Size Votes](/blockchain/block_size_votes)
       '''.replace('    ', '')),

        ])
    ]),
    html.Div(id='plot_type')
])


def create_div(pathname):
    types = pathname.split('/')[2]
    return html.Div([
        html.H1(
            children=all_types[types],
            style={
                'textAlign': 'center',
                'color': colors['background'],
            }
        )

    ])


@app.callback(dash.dependencies.Output('plot_type', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    return create_div(pathname)


if __name__ == '__main__':
    app.run_server(host='0.0.0.0')
