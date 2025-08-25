import dash_mantine_components as dmc
from ui import footer
from ui.header import header
from ui.controls import controls
from ui.chart import chart
from ui.legend import legend    
from ui.footer import footer
from ui.help import help_section


layout = dmc.Container(
    [
    header(),
    help_section(),
    controls(),
    chart(),
    legend(),
    footer()
    ],
    maw='1400px'

)
    
