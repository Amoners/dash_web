# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import apps.keywordsJson as kwj


app = dash.Dash(__name__, static_folder='../assets')

colors = {
    'background': '#000000',
    'text': '#ffffff'
}

app.css.config.serve_locally = True
#app.scripts.config.serve_locally = True
app.scripts.append_script({
    'external_url': '../assets/jquery-3.3.1.min.js',
})
app.scripts.append_script({
     'external_url': '../assets/demo.js'
 })

app.layout = html.Div(children=[
    html.Link(href='../assets/demo.css', rel='stylesheet'),
    html.Link(href='../assets/style1.css', rel='stylesheet'),
    html.Link(href='../assets/style2.css', rel='stylesheet'),
    html.Link(href='../assets/style3.css', rel='stylesheet'),
    #html.Link(href='../assets/jquery-3.3.1.min.js', rel='script'),
    #html.Link(href='../assets/demo.js', rel='script'),
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
                html.Ul(id='markets',
                        key='markets',
                        className='nav nav-tabs nav-stacked data_type')
            ]),
            html.Div(children=[
                html.H3(
                    children='Blockchain',
                    className='center'
                ),
                html.Hr(style={'border-color': '#ddd'}),
                html.Ul(id='blockchain',
                        key='blockchain',
                        className='nav nav-tabs nav-stacked data_type')
            ])
        ]),
    html.Div(id='plot_type')
])


def create_div(pathname):
    if pathname is None or pathname == '/':
        pass
    else:

        types = pathname.split('/')[1]
        kw = pathname.split('/')[2]
        return html.Div([
            html.H1(
                children=kwj.get_kw_value(types, kw, 'title'),
                style={
                    'textAlign': 'center',
                    'color': colors['background'],
                }
            )

        ])


@app.callback(Output("markets", "children"),
              [Input('markets', 'key')])
def get_market_item(word_key):
    kws = kwj.get_kw(word_key)
    template = []
    for key in kws:
        template.append(kwj.gen_html_item(word_key, key))
    return template


@app.callback(Output("blockchain", "children"),
              [Input('blockchain', 'key')])
def get_blockchain_item(word_key):
    kws = kwj.get_kw(word_key)
    template = []
    for key in kws:
        template.append(kwj.gen_html_item(word_key, key))
    return template


@app.callback(Output('plot_type', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    return create_div(pathname)


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
