from dash import html
from .grid import Grid
from .controlpanel import ControlPanel


def Layout(grid=None, controlpanel=None):
    if not controlpanel:
        return html.Div(grid.get_component(), className="dui-layout")
    else:
        return html.Div([
                controlpanel.get_component(),
                grid.get_component()
            ], className="dui-layout")
