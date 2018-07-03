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
app.scripts.append_script({
    'external_url': 'https://code.jquery.com/jquery-3.3.1.min.js',
    'external_url': '/assets/test.js'
})

app.layout = html.Div(children=[
    html.Link(href='/assets/demo.css', rel='stylesheet'),
    html.Link(href='/assets/style1.css', rel='stylesheet'),
    html.Link(href='/assets/style2.css', rel='stylesheet'),
    html.Link(href='/assets/style3.css', rel='stylesheet'),
    html.Link(href='/assets/test.js', rel='script'),
    dcc.Location(id='url', refresh=False),
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
        style={'float': 'left', 'margin': '25px'},
        children=[
            html.Div(children=[
                html.H3(
                    children='Markets',
                    className='center'
                ),
                html.Hr(style={'border-color': '#ddd'}),
                html.Ul([
                    html.Li(html.A('Exchanges List', href='/markets/exchanges'), className='exchanges'),
                    html.Li(html.A('trading volume', href='/markets/volume', className='chart_link'),
                            className='volume'),
                    html.Li(html.A('rank', href='/markets/rank', className='chart_link'), className='rank'),
                    html.Li(html.A('price', href='/markets/price', className='chart_link'), className='price'),
                    html.Li(html.A('Price + Volume', href='/markets/price_volume', className='chart_link'),
                            className='price_volume'),
                    html.Li(html.A('Market Cap', href='/markets/market_cap', className='chart_link'),
                            className='market_cap'),
                    html.Li(html.A('Trades Per Minute', href='/markets/tradespm', className='chart_link'),
                            className='tradespm'),
                    html.Li(html.A('Volatility', href='/markets/volatility', className='chart_link'),
                            className='volatility'),
                    html.Li(html.A('Arbitrage', href='/markets/arbitrage', className='chart_link'),
                            className='arbitrage'),
                    html.Li(html.A('Combined Order Book', href='/markets/books'), className='books)'),
                    html.Li(html.A('Bid/Ask Spread', href='/markets/spread', className='chart_link'),
                            className='spread'),
                    html.Li(html.A('Bid/Ask Sum', href='/markets/bidask_sum', className='chart_link'),
                            className='bidask_sum'),
                ],
                    className='nav nav-tabs nav-stacked data_type')
            ]),
            html.Div(children=[
                html.H3(
                    children='Blockchain',
                    className='center'
                ),
                html.Hr(style={'border-color': '#ddd'}),
                html.Ul([
                    html.Li(html.A('Hashrate', href='/blockchain/hashrate', className='chart_link'),
                            className='hashrate'),
                    html.Li(html.A('Mining Difficulty', href='/blockchain/difficulty', className='chart_link'),
                            className='difficulty'),
                    html.Li(html.A('Block Size', href='/blockchain/size', className='chart_link'), className='size'),
                    html.Li(html.A('Block Version', href='/blockchain/block_version', className='chart_link'),
                            className='block_version'),
                    html.Li(html.A('Number Of Transactions', href='/blockchain/tx_count', className='chart_link'),
                            className='tx_count'),
                    html.Li(html.A('Time Between Blocks', href='/blockchain/block_time', className='chart_link'),
                            className='block_time'),
                    html.Li(html.A('Block Size Votes', href='/blockchain/block_size_votes', className='chart_link'),
                            className='block_size_votes')
                ],
                    className='nav nav-tabs nav-stacked data_type')
            ])
        ]),
    html.Div(id='plot_type')
])


def create_div(pathname):
    if pathname is None:
        pass
    else:
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
