from fasthtml.common import *
from fastcore.meta import delegates

fui_hdrs = [
    Link(href=f"https://cdn.jsdelivr.net/npm/fomantic-ui@2.9.3/dist/semantic.min.css", rel="stylesheet"),
    # Script(src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.min.js"),
    # Script(src="https://cdn.jsdelivr.net/npm/fomantic-ui@2.9.3/dist/semantic.min.js"),
]

@delegates(Div)
def HeroSegment(title, subtitle, *args, **kwargs):
    return Div(
        H1(title, cls="ui inverted header"),
        H2(subtitle),
        cls="ui inverted vertical masthead center aligned segment", *args, **kwargs)
