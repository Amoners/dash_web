# -*- coding: utf-8 -*-
import tushare as ts
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash(__name__)

colors = {
    'background': '#000000',
    'text': '#ffffff'
}

app.layout = html.Div(children=[
    html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(
            children='DASH WEB DEMO',
            style={
                'textAlign': 'left',
                'padding': '25px',
                'color': colors['text']
            }
        )]),
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
            * Exchanges List
            * Trading Volume
            * Rank
            * Price
            * Price + Volume
            * Market Cap
            * Trades Per Minute
            * Volatility
            * Arbitrage
            * Combined Order Book
            * Bid/Ask Spread
            * Bid/Ask Sum
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
            * [Hashrate](http://www.baidu.com)
            * Mining Difficulty
            * Block Size
            * Block Version
            * Number Of Transactions
            * Time Between Blocks
            * Block Size Votes
       '''.replace('    ', '')),

        ])
])

if __name__ == '__main__':
    app.run_server()
