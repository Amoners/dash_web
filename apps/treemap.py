import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go
import squarify

app = dash.Dash()
server = app.server
app.config.supress_callback_exceptions = True

app.layout = html.Div([
    dcc.Graph(id='treemap')
])


@app.callback(
    Output('treemap', 'figure'),
    [Input('treemap', 'value')])
def treemap(value):
    x = 0.
    y = 0.
    width = 100.
    height = 100.
    test_data = {
        'BTC': {
            'size': '500',
            'marketcap': -0.34,
        },
        'BCH': {
            'size': '433',
            'marketcap': -0.34,
        },
        'ETH': {
            'size': '78',
            'marketcap': -0.34,
        },
        'XRP': {
            'size': '25',
            'marketcap': 0.34,
        },
        'XLM': {
            'size': '25',
            'marketcap': 0.34,
        },
        'ADA': {
            'size': '25',
            'marketcap': -0.34,
        },

    }
    coin_name_list = test_data.keys()
    coin_name_list2 = []
    for i in coin_name_list:
        coin_name_list2.append(i)

    values = []
    for key in coin_name_list:
        values.append(test_data[key]['size'])
    values = list(map(int, values)) # string to list

    normed = squarify.normalize_sizes(values, width, height)
    rects = squarify.squarify(normed, x, y, width, height)

    # Choose colors from http://colorbrewer2.org/ under "Export"
    color_brewer = ['rgb(255,0,255)', 'rgb(0,255,0)']
    shapes = []
    annotations = []
    counter = 0

    print(test_data['ETH']['marketcap'])
    for r in rects:
        coin_name = coin_name_list2[counter]
        if test_data[coin_name]['marketcap'] > 0:
            color = 0
        else:
            color = 1
        shapes.append(
            dict(
                type='rect',
                x0=r['x'],
                y0=r['y'],
                x1=r['x'] + r['dx'],
                y1=r['y'] + r['dy'],
                line=dict(width=2),
                fillcolor=color_brewer[color]
            )
        )
        annotations.append(
            dict(
                x=r['x'] + (r['dx'] / 2),
                y=r['y'] + (r['dy'] / 2),
                text="<span><a id='a" + str(counter) + "'>" + coin_name_list2[counter] + "</a><br> <b>"+ str(test_data[coin_name_list2[counter]]['marketcap']) +"</b></span>",
                #text=coin_name_list2[counter],
                showarrow=False
            )
        )
        counter = counter + 1

    figure = {
        'data': [go.Scatter(
            x=[r['x'] + (r['dx'] / 2) for r in rects],
            y=[r['y'] + (r['dy'] / 2) for r in rects],
            text=[str(v) for v in values],
            mode='text',
        )
        ],
        'layout': go.Layout(
            height=700,
            width=700,
            xaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False},
            yaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False},
            shapes=shapes,
            annotations=annotations,
            hovermode=False,
        )
    }

    return figure


if __name__ == '__main__':
    app.run_server(debug=True)