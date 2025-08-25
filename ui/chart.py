import dash_mantine_components as dmc
from dash import dcc
from components.section_container import section_container


def chart():
    return section_container(
        [
            dmc.Title("Chart Area", order=2),
            dcc.Graph(figure={}, id='chart'),
        ]
    )