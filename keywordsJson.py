import dash_html_components as html
import dash_core_components as dcc
ks_list = {
    'market': {
        'exchanges': {
            'path': '/markets/exchanges',
            'title': 'Exchanges List',
            'class': 'exchanges',
            'li': 'Exchanges List'
        },
        'volume': {
            'path': '/markets/volume',
            'title': 'trading volume',
            'class': 'volume',
            'li': 'trading volume'
        },
        'rank': {
            'path': '/markets/rank',
            'title': 'Exchanges ranking',
            'class': 'rank',
            'li': 'rank'
        },
        'price': {
            'path': '/markets/price',
            'title': 'price',
            'class': 'price',
            'li': 'price'
        },
        'price_volume': {
            'path': '/markets/price_volume',
            'title': 'price and volume',
            'class': 'price_volume',
            'li': 'Price + Volume'
        },
        'market_cap': {
            'path': '/markets/market_cap',
            'title': 'market capitalization',
            'class': 'market_cap',
            'li': 'Market Cap'
        },
        'tradespm': {
            'path': '/markets/tradespm',
            'title': 'Number of trades per minute',
            'class': 'tradespm',
            'li': 'Trades Per Minute'
        },
        'volatility': {
            'path': '/markets/volatility',
            'title': 'price volatility',
            'class': 'volatility',
            'li': 'Volatility'
        },
        'arbitrage': {
            'path': '/markets/arbitrage',
            'title': 'markets arbitrage table',
            'class': 'arbitrage',
            'li': 'Arbitrage'
        },
        'books': {
            'path': '/markets/books',
            'title': 'Combined order book',
            'class': 'books',
            'li': 'Combined Order Book'
        },
        'spread': {
            'path': '/markets/spread',
            'title': 'Bid-ask spread',
            'class': 'spread',
            'li': 'Bid/Ask Spread'
        },
        'bidask_sum': {
            'path': '/markets/bidask_sum',
            'title': 'Bid/ask sum within 10% range from the price',
            'class': 'bidask_sum',
            'li': 'Bid/Ask Sum'
        }
    },
    'blockchain': {
        'hashrate': {
            'path': '/blockchain/hashrate',
            'title': 'hashrate',
            'class': 'hashrate',
            'li': 'Hashrate'
        },
        'difficulty': {
            'path': '/blockchain/difficulty',
            'title': 'mining difficulty',
            'class': 'difficulty',
            'li': 'Mining Difficulty'
        },
        'size': {
            'path': '/blockchain/size',
            'title': 'blocks size',
            'class': 'size',
            'li': 'Block Size'
        },
        'block_version': {
            'path': '/blockchain/block_version',
            'title': 'blocks version',
            'class': 'block_version',
            'li': 'Block Version'
        },
        'tx_count': {
            'path': '/blockchain/tx_count',
            'title': 'Number of transactions',
            'class': 'tx_count',
            'li': 'Number Of Transactions'
        },
        'block_time': {
            'path': 'blockchain/block_time',
            'title': 'Average time to mine a block in minutes',
            'class': 'block_time',
            'li': 'Time Between Blocks'
        },
        'block_size_votes': {
            'path': '/blockchain/block_size_votes',
            'title': 'Block size votes',
            'class': 'block_size_votes',
            'li': 'Block Size Votes'
        }
    }
}


def get_kw_value(types='market', kw='exchanges', info='all'):
    if info == 'all':
        return ks_list[types][kw]
    else:
        return ks_list[types][kw][info]


def get_kw(types='market'):
    return ks_list[types].keys()


def gen_html_item(types='market', kw='exchanges'):
    return html.Li(dcc.Link(html.A('{}'.format(ks_list[types][kw]['li'],)), href='{}'.format(ks_list[types][kw]['path']), className='{}'.format(ks_list[types][kw]['class'])))


