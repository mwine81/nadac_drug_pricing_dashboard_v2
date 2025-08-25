import dash_mantine_components as dmc
from components.section_container import section_container
from config import PRIMARY_COLOR

def legend():
    return section_container(
        [
            dmc.Box(
                    className="chart-container",
                    mt='sm',
                    children=[
                        dmc.Stack(
                            gap="sm",
                            children=[
                                dmc.Group(
                                    justify="space-between",
                                    align="center",
                                    children=[
                                        dmc.Title("Products in Chart", order=4, c=PRIMARY_COLOR),
                                    ]
                                ),
                                dmc.Box(id="chart-legend", mih='60px')
                            ]
                        )
                    ]
                )
        ]
    )