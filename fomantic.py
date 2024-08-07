from fasthtml.common import *
from fastcore.meta import delegates

fui_hdrs = [
    Link(href=f"https://cdn.jsdelivr.net/npm/fomantic-ui@2.9.3/dist/semantic.min.css", rel="stylesheet"),
    # Script(src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.min.js"),
    # Script(src="https://cdn.jsdelivr.net/npm/fomantic-ui@2.9.3/dist/semantic.min.js"),
]

@delegates(Div, keep=True)
def HeroSegment(title, subtitle, *c, **kwargs) -> FT:
    return Div(
        H1(title, cls="ui inverted header"),
        H2(subtitle),
        cls="ui inverted vertical masthead center aligned segment", *c, **kwargs)

@delegates(Div, keep=True)
def Segment(*c, cls="ui segment", **kwargs) -> FT:
    return Div(*c, cls=cls, **kwargs)

@delegates(Div, keep=True)
def VerticalStripeSegment(*c, cls="ui vertical stripe segment", **kwargs) -> FT:
    "A Fomantic UI Vertical Stripe Segment, from the homepage example"
    return Div(*c, cls=cls, **kwargs)


@delegates(Div, keep=True)
def Grid(*c, cls="ui grid container", **kwargs) -> FT:
    "A Fomantic UI Grid"
    return Div(*c, cls=cls, **kwargs)

@delegates(Div, keep=True)
def Column(*c, cls="column", **kwargs) -> FT:
    "A Fomantic UI Column"
    return Div(*c, cls=cls, **kwargs)

