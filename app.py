import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, callback, dcc
from typing import Any
from figures.generate_chart import generate_chart
from helpers import filter_chart_data, load_data, update_size_dropdown, render_legend
from ui.layout import layout
import polars as pl
from polars import col as c
import polars.selectors as cs
from config import LEGEND_PALETTE

app = Dash()

# Global Mantine theme for professional, consistent styling
THEME: Any = {
    # Custom brand scale (light -> dark) anchored on our PRIMARY_COLOR (#1a365d)
    "colors": {
        "brand": [
            "#e9eff7",
            "#d7e3f0",
            "#c3d6ea",
            "#a9c4df",
            "#8bb0d3",
            "#6b96c3",
            "#4f80b5",
            "#3c6da7",
            "#2b5b93",
            "#1a365d",
        ]
    },
    "primaryColor": "brand",
    "fontFamily": "Inter, system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif",
    "headings": {
        "fontFamily": "Inter, system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif",
        "sizes": {
            "h1": {"fontSize": "28px", "fontWeight": 700},
            "h2": {"fontSize": "22px", "fontWeight": 700},
            "h3": {"fontSize": "18px", "fontWeight": 700},
        },
    },
    "defaultRadius": "md",
}

app.layout = dmc.MantineProvider(theme=THEME, children=layout)

# Help modal callbacks
@app.callback(
    Output('help-overview-modal', 'opened'),
    Input('help-overview-btn', 'n_clicks'),
    State('help-overview-modal', 'opened'),
    prevent_initial_call=True
)
def toggle_overview_modal(n_clicks, opened):
    return not opened

@app.callback(
    Output('help-data-modal', 'opened'),
    Input('help-data-btn', 'n_clicks'),
    State('help-data-modal', 'opened'),
    prevent_initial_call=True
)
def toggle_data_modal(n_clicks, opened):
    return not opened

@app.callback(
    Output('help-usage-modal', 'opened'),
    Input('help-usage-btn', 'n_clicks'),
    State('help-usage-modal', 'opened'),
    prevent_initial_call=True
)
def toggle_usage_modal(n_clicks, opened):
    return not opened

@app.callback(
    Output('help-technical-modal', 'opened'),
    Input('help-technical-btn', 'n_clicks'),
    State('help-technical-modal', 'opened'),
    prevent_initial_call=True
)
def toggle_technical_modal(n_clicks, opened):
    return not opened

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