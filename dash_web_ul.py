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
    html.Div([
        html.Div(
            className='subtitle'
        ),
        html.H1(
            style={'margin': '25px'},
            children=html.A('DASH WEB DEMO', href='/'),
            className='title'
        ),
     ],
        className='main_title row-fluid'
    ),

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
                    html.Li(dcc.Link(html.A('Exchanges List'),  href='/markets/exchanges'), className='exchanges'),
                    html.Li(dcc.Link(html.A('trading volume', className='chart_link'), href='/markets/volume'), className='volume'),
                    html.Li(dcc.Link(html.A('rank', className='chart_link'), href='/markets/rank'),  className='rank'),
                    html.Li(dcc.Link(html.A('price',  className='chart_link'), href='/markets/price'),className='price'),
                    html.Li(dcc.Link(html.A('Price + Volume', className='chart_link'), href='/markets/price_volume'),
                            className='price_volume'),
                    html.Li(dcc.Link(html.A('Market Cap', className='chart_link'), href='/markets/market_cap'),
                            className='market_cap'),
                    html.Li(dcc.Link(html.A('Trades Per Minute',className='chart_link'),  href='/markets/tradespm'),
                            className='tradespm'),
                    html.Li(dcc.Link(html.A('Volatility', className='chart_link'), href='/markets/volatility'),
                            className='volatility'),
                    html.Li(dcc.Link(html.A('Arbitrage', className='chart_link'), href='/markets/arbitrage'),
                            className='arbitrage'),
                    html.Li(dcc.Link(html.A('Combined Order Book'), href='/markets/books'),  className='books)'),
                    html.Li(dcc.Link(html.A('Bid/Ask Spread', className='chart_link'), href='/markets/spread'),
                            className='spread'),
                    html.Li(dcc.Link(html.A('Bid/Ask Sum',className='chart_link'), href='/markets/bidask_sum'),
                            className='bidask_sum')
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
                    html.Li(dcc.Link(html.A('Hashrate', className='chart_link'), href='/blockchain/hashrate'),
                            className='hashrate'),
                    html.Li(dcc.Link(html.A('Mining Difficulty', className='chart_link'),href='/blockchain/difficulty'),
                            className='difficulty'),
                    html.Li(dcc.Link(html.A('Block Size', className='chart_link'),href='/blockchain/size'),  className='size'),
                    html.Li(dcc.Link(html.A('Block Version',className='chart_link'), href='/blockchain/block_version'),
                            className='block_version'),
                    html.Li(dcc.Link(html.A('Number Of Transactions', className='chart_link'),href='/blockchain/tx_count'),
                            className='tx_count'),
                    html.Li(dcc.Link(html.A('Time Between Blocks', className='chart_link'),href='/blockchain/block_time'),
                            className='block_time'),
                    html.Li(dcc.Link(html.A('Block Size Votes', className='chart_link'),href='/blockchain/block_size_votes'),
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
