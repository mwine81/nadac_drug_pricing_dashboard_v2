import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, callback, dcc
from figures.generate_chart import generate_chart
from helpers import filter_chart_data, load_data, update_size_dropdown, render_legend
from ui.layout import layout
import polars as pl
from polars import col as c
import polars.selectors as cs
from config import LEGEND_PALETTE

app = Dash()

app.layout = dmc.MantineProvider(layout)

@app.callback(
    Output('product-select', 'data'),
    Input('drug-class-select', 'value')
)
def update_product_options(short_name):
    product_options = load_data().filter(c.short_name == short_name)
    return product_options.select(c.product).unique().sort('product').collect(engine='streaming').to_series().to_list()


@app.callback(
    Output('package-size-select', 'data'),
    Input('drug-class-select', 'value'),
    Input('product-select', 'value'),
)
def update_size_options(short_name, product):
    return update_size_dropdown(short_name, product)

@app.callback(
    Output('chart', 'figure'),
    Input('drug-class-select', 'value'),
    Input('product-select', 'value'),
    Input('package-size-select', 'value'),
)
def update_chart(short_name, product, size):
    data = filter_chart_data(short_name, product, size)
    return generate_chart(data, short_name)

@app.callback(
    Output('chart-legend', 'children'),
    Input('drug-class-select', 'value'),
    Input('product-select', 'value'),
    Input('package-size-select', 'value'),
)
def update_legend(short_name, product, size):
    # Get the filtered data to determine which products are in the chart
    legend = render_legend(short_name, product, size)
    return legend

if __name__ == "__main__":
    app.run(debug=True)