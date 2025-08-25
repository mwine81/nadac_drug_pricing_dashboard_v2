import polars as pl
from polars import col as c
import polars.selectors as cs
from config import DATA
import dash_mantine_components as dmc
from config import LEGEND_PALETTE


def load_data() -> pl.LazyFrame:
    return pl.scan_parquet(DATA)

def dropdown_choices(column: str) -> list[str]:
    return load_data().select(pl.col(column)).unique().sort(column).cast(pl.String).collect(engine='streaming').to_series().to_list()

def update_size_dropdown(short_name, product):
    # Start with filtering by short_name
    data = load_data().filter(c.short_name == short_name)
    
    # If products are selected, filter by them as well
    if product and len(product) > 0:
        data = data.filter(c.product.is_in(product))
    
    # Get unique sizes, filter out nulls, and return as list
    size_options = (
        data
        .select(c.size)
        .filter(c.size.is_not_null())
        .unique()
        .sort('size')
        .collect(engine='streaming')
        .to_series()
        .to_list()
    )
    
    # Convert to strings for the dropdown (Dash expects strings)
    size_options = [str(size) for size in size_options if size is not None]
    return size_options

def filter_chart_data(short_name, product, size) -> pl.LazyFrame:
    data = load_data().filter(c.short_name == short_name)
    if product:
        data = data.filter(c.product.is_in(product))
    if size:
        data = data.filter(c.size.is_in([float(x) for x in size]))
    data = (
    data.group_by(c.product,c.effective_date)
    .agg(c.unit_price.mean().round(4))
    .sort(by=['product','effective_date'])
    )
    return data


def render_legend(short_name, product, size):
    data = filter_chart_data(short_name, product, size)
    
    # Check if data is empty
    if data.collect(engine='streaming').is_empty():
        return dmc.Text("No data available for selected filters", size="sm", c="gray")
    
    # Get unique products
    products = data.collect(engine='streaming').select(c.product).unique().to_series().to_list()

    # Create legend items with color indicators
    colors = LEGEND_PALETTE
    
    def legend_item(product_name, color):
        return dmc.Group(
                gap="xs",
                align="center",
                children=[
                    dmc.Box(
                        w=20, h=3, bg=color, bdrs="sm"
                    ),
                    dmc.Text(product_name, size="sm")
                ]
            ) 
    
    legend_items = []
    for i, product_name in enumerate(products):
        color = colors[i % len(colors)]
        legend_items.append(
            legend_item(product_name, color)
        )
    
    # Arrange legend items in a responsive grid
    return dmc.SimpleGrid(
        cols=3,
        spacing="md",
        children=legend_items
    )

