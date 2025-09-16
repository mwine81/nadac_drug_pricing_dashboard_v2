import dash_mantine_components as dmc
from components.section_container import section_container
from components.dropdown import dropdown
from helpers import dropdown_choices
from config import PRIMARY_COLOR

def controls():
    return section_container(
        [
            dmc.Title("Filter Options", order=2, c=PRIMARY_COLOR),
            dmc.Grid([
                dmc.GridCol(
                    span=4,
                    children=[
                        dmc.Select(
                            label="Active Ingredient",
                            data=dropdown_choices("short_name"),
                            value=dropdown_choices("short_name")[0],
                            searchable=True,
                            radius="md",
                            id="drug-class-select",
                        ),
                    ]
                ),
                dmc.GridCol(
                    span=4,
                    children=[
                        dmc.MultiSelect(
                            label="Products",
                            searchable=True,
                            radius="md",
                            placeholder="Select drug class...",
                            clearable=True,
                            id="product-select"
                        ),
                    ]
                ),
                dmc.GridCol(
                    span=4,
                    children=[
                        dmc.MultiSelect(
                            label="Package Sizes",
                            data=dropdown_choices("size"),
                            searchable=True,
                            radius="md",
                            placeholder="Select drug class...",
                            clearable=True,
                            id="package-size-select"
                        )
                    ]
                )
            ])
            #dmc.Text("This is the main content area."),
    ]
)