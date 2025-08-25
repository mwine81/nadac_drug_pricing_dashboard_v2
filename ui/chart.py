import dash_mantine_components as dmc
from dash import dcc
from components.section_container import section_container
from config import PRIMARY_COLOR

def chart():
    return section_container(
        [
            dmc.Title("Price Trends Over Time", order=2, c=PRIMARY_COLOR),
            dcc.Graph(figure={}, id='chart'),
        ]
    )