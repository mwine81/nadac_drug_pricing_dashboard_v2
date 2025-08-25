import dash_mantine_components as dmc
from config import PRIMARY_COLOR, SECONDARY_COLOR
from components.section_container import section_container
from components.badges import badge_nadac, badge_analytics

def header():
    return section_container(
        dmc.Group(
                [
                    dmc.Box(dmc.Image(src='./assets/logo.png',h=40)),
                    dmc.Title("46brooklyn", c=PRIMARY_COLOR), # type: ignore
                    dmc.Text("NADAC Drug Pricing Dashboard", c=SECONDARY_COLOR),
                    badge_nadac()
                ],
                h="100%",
            ),
    )